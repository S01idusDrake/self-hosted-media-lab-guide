# Privacy and safe contribution policy

This repository contains generic instructions only. Keep it free of real hostnames, domains, internal/public addresses, emails, account names, disk serials/UUIDs, tunnel IDs, real inventories, credentials, configuration exports, screenshots or branded assets from any particular installation. Reserved example domains and clearly identified loopback/documentation values are acceptable.

Examples must use required placeholders or locally supplied environment variables. Keep actual `.env`, secret files, databases, backups, raw logs, monitoring targets and rendered private reports outside the repository. Review history as well as current files before any public release. Git author metadata identifies contributors and is a separate privacy consideration from tutorial content.

To report a discovered credential, do not paste it into a public issue. Contact the owner privately through an agreed channel. Revoke/rotate exposed credentials and review history before publishing again. No public reporting address is prescribed in this draft.

Changes to running systems and destructive media operations require an explicit reviewed scope. Never format disks or disable authentication to make a generic example work. All content acquisition/sharing must comply with applicable permissions and service terms.

## Repeatable publication checks

Run `python3 tools/check_privacy.py --history` to inspect the working tree and all commits reachable from local branches/tags. Add `--deny-file /path/outside/repository/denylist.txt` to check names and literals belonging to a private installation. The denylist and full audit report must remain in private documentation, never in this repository or CI output. Findings report categories and file paths without printing matched values.

The GitHub workflow runs generic checks with full reachable history. It cannot see a private external denylist, hosted issues, pull-request discussions, attachments, releases, caches, forks or inaccessible refs. Review those surfaces separately. Do not claim content is anonymous merely because a scanner passes. Hosting account names and repository ownership remain visible independently of file content. Use a neutral approved author and committer identity for anonymous guide commits; never copy a private installation identity into public commit metadata.
