#!/usr/bin/env python3
"""Audit publishable text and reachable Git history without printing matched values.

Installation-specific forbidden literals belong in a private external denylist.
This checker is a guardrail, not a proof that arbitrary secrets cannot exist.
"""
import argparse
import ipaddress
from pathlib import Path
import re
import subprocess
import sys

ARTIFACTS = {'.pem', '.key', '.p12', '.pfx', '.cms', '.db', '.sqlite', '.sqlite3',
             '.zip', '.gz', '.tar', '.xlsx', '.png', '.jpg', '.jpeg', '.webp', '.pdf'}
PATTERNS = [
    ('private key', re.compile(r'-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----')),
    ('access token', re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16})\b')),
    ('credential URL', re.compile(r'https?://[^\s/:]+:[^\s/@]+@|https://discord(?:app)?\.com/api/webhooks/\S+')),
    ('private document link', re.compile(r'https?://(?:docs|drive)\.google\.com/(?:document|spreadsheets|drive|file)/')),
    ('inventory identifier', re.compile(r'\b[0-9a-fA-F]{8}-(?:[0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}\b|\b(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}\b')),
    ('personal home path', re.compile(r'(?:/Users/|/home/)[A-Za-z0-9_.-]+/')),
]
MAIL = re.compile(r'\b[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})\b')
IPV4 = re.compile(r'(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])')
IDENTITY_KEYS = ('author ', 'committer ', 'tagger ')


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], stderr=subprocess.DEVNULL)


def inspect(name, data, denied):
    issues = []
    if Path(name).suffix.casefold() in ARTIFACTS:
        issues.append('deployment, media or recovery artifact')
    try:
        body = data.decode('utf-8')
    except UnicodeDecodeError:
        return issues + ['binary content requires separate review']
    if any(term in (name + '\n' + body).casefold() for term in denied):
        issues.append('private denylist match')
    # Checker source contains detection expressions, not deployment values.
    if name not in {'tools/check_privacy.py', 'tools/check_docs.py'}:
        issues.extend(label for label, pattern in PATTERNS if pattern.search(body))
        if any(not domain.endswith(('.invalid', '.example', '.test')) for domain in MAIL.findall(body)):
            issues.append('non-example email address')
        for value in IPV4.findall(body):
            try:
                address = ipaddress.ip_address(value)
            except ValueError:
                continue
            if not address.is_loopback and not address in ipaddress.ip_network('192.0.2.0/24') and not address in ipaddress.ip_network('198.51.100.0/24') and not address in ipaddress.ip_network('203.0.113.0/24'):
                issues.append('non-documentation IP address')
                break
        # Actual IPv6 literals in URL brackets; placeholders and regexes do not match.
        for value in re.findall(r'https?://\[([0-9a-fA-F:]+)\]', body):
            address = ipaddress.ip_address(value)
            if not address.is_loopback and not address in ipaddress.ip_network('2001:db8::/32'):
                issues.append('non-documentation IPv6 address')
        # Secret worksheets should be empty, required-variable references or explicit placeholders.
        for match in re.finditer(r'^[ \t]*(?:[A-Z_]*(?:PASSWORD|API_KEY|TOKEN|SECRET|CREDENTIAL)[A-Z_]*)[ \t]*[=:][ \t]*(.+)$', body, re.M):
            value = match.group(1).strip().strip('\"\'')
            if value and not value.startswith(('$', '<', '#', '/run/secrets/')):
                issues.append('non-placeholder credential assignment')
                break
    return sorted(set(issues))


def audit(root, denied, history=False):
    errors = []
    files = [p for p in root.rglob('*') if p.is_file() and not set(p.relative_to(root).parts) & {'.git', '__pycache__'}]
    for path in sorted(files):
        for issue in inspect(path.relative_to(root).as_posix(), path.read_bytes(), denied):
            errors.append(f'worktree:{path.relative_to(root)}: {issue}')
    counts = {'files': len(files), 'commits': 0, 'historical_blobs': 0, 'tags': 0}
    if history:
        commits = git(root, 'rev-list', '--all').decode().splitlines()
        seen = set()
        for commit in commits:
            counts['commits'] += 1
            message = git(root, 'cat-file', 'commit', commit)
            for issue in inspect('commit metadata', message, denied):
                errors.append(f'commit:{commit[:12]}: {issue}')
            for line in git(root, 'ls-tree', '-rz', commit).split(b'\0'):
                if not line:
                    continue
                metadata, rawname = line.split(b'\t', 1)
                _, kind, oid = metadata.split()
                name = rawname.decode('utf-8')
                if kind != b'blob':
                    errors.append(f'commit:{commit[:12]}: non-text repository entry requires review')
                    continue
                key = (oid, name)
                if key in seen:
                    continue
                seen.add(key)
                counts['historical_blobs'] += 1
                for issue in inspect(name, git(root, 'cat-file', 'blob', oid.decode()), denied):
                    errors.append(f'history:{name}: {issue}')
        for tag in git(root, 'tag').decode().splitlines():
            counts['tags'] += 1
            for issue in inspect('tag', git(root, 'show', '-s', '--format=fuller', tag), denied):
                errors.append(f'tag: {issue}')
    return counts, sorted(set(errors))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--deny-file', type=Path, help='Private file outside this repository, one forbidden literal per line')
    parser.add_argument('--history', action='store_true', help='Also inspect every commit and blob reachable from local refs')
    args = parser.parse_args()
    root = args.root.resolve()
    denied = []
    if args.deny_file:
        denyfile = args.deny_file.resolve()
        if denyfile.is_relative_to(root):
            parser.error('The denylist must stay outside the publishable repository')
        denied = [v.strip().casefold() for v in denyfile.read_text().splitlines() if v.strip() and not v.startswith('#')]
    try:
        counts, errors = audit(root, denied, args.history)
    except (OSError, subprocess.CalledProcessError):
        print('Audit failed: files or Git history could not be read.', file=sys.stderr)
        return 2
    print('Audited ' + ', '.join(f'{value} {key}' for key, value in counts.items()) + f'; {len(errors)} issue(s).')
    for error in errors:
        print(error)
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
