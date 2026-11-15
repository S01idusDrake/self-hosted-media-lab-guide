#!/usr/bin/env python3
"""Check local links, obvious credential artifacts and an optional private denylist.

This scans text files, not Git history. It is not a complete secret scanner.
Keep denylist files OUTSIDE this repository; error output never prints their terms.
"""
import argparse
import pathlib
import re
import sys
from urllib.parse import unquote


def check(root, denied=()):
    errors = []
    count = 0
    for path in sorted(root.rglob('*')):
        if not path.is_file() or '.git' in path.relative_to(root).parts:
            continue
        relative = path.relative_to(root)
        if '__pycache__' in relative.parts:
            continue
        if path.suffix.lower() in {'.pem', '.key', '.db', '.sqlite', '.zip', '.xlsx'}:
            errors.append(f'{relative}: forbidden artifact type')
        try:
            body = path.read_text(encoding='utf-8')
        except (UnicodeDecodeError, OSError):
            errors.append(f'{relative}: unreadable or binary artifact')
            continue
        if any(term.casefold() in (str(relative) + '\n' + body).casefold() for term in denied):
            errors.append(f'{relative}: private denylist match')
        # Avoid scanning this checker's own literal patterns as leaked content.
        if path.name != 'check_docs.py':
            if re.search(r'-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----', body):
                errors.append(f'{relative}: private key material')
            if re.search(r'https://(?:discord(?:app)?\.com)/api/webhooks/\S+', body):
                errors.append(f'{relative}: webhook credential URL')
            if re.search(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b', body):
                errors.append(f'{relative}: possible access token')
        if path.suffix == '.md':
            count += 1
            for target in re.findall(r'\]\(([^)]+)\)', body):
                if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                    continue
                local = unquote(target.split('#', 1)[0].strip('<>'))
                if not local or not (path.parent / local).exists():
                    errors.append(f'{relative}: broken local link')
    required = [f'{n:02d}-' for n in range(1, 27)]
    names = [p.name for p in (root / 'docs').glob('*.md')]
    for prefix in required:
        if not any(name.startswith(prefix) for name in names):
            errors.append(f'docs: missing chapter {prefix[:2]}')
    return count, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[1])
    parser.add_argument('--deny-file', type=pathlib.Path, help='Private external UTF-8 file: one forbidden literal per line')
    args = parser.parse_args()
    denied = []
    if args.deny_file:
        denied = [line.strip() for line in args.deny_file.read_text().splitlines() if line.strip()]
    count, errors = check(args.root.resolve(), denied)
    print(f'Checked {count} Markdown files; {len(errors)} issue(s).')
    for error in errors:
        print(error)
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
