# Contributing

Write for a beginner who has no access to the original installation. Each chapter needs purpose, prerequisites, location, step order, explained settings/commands, expected result, acceptance evidence and rollback. Mark alternatives, provider/version dependence and untested code clearly.

Use fictional role names, reserved domains and generic paths. Do not copy screenshots, raw configs or logs from a real lab. Link primary upstream documentation for version-sensitive details and paraphrase; do not reproduce entire vendor manuals.

For new configurations, supply placeholders, persistence, deliberate listeners/networks, startup policy, meaningful health behavior and backup scope. For custom scripts, require safe failure behavior and meaningful fixture/staging tests before declaring the feature implemented. Prefer maintained components where that reduces untested custom machinery.

Run `python3 tools/check_docs.py` and `python3 tools/check_privacy.py --history`; inspect the staged diff and Git history for private values, binary files and secret material. Validate YAML/Compose on staging; do not deploy examples to a live host merely to test docs. Record supported versions and actual acceptance results. Update COVERAGE and VALIDATION whenever scope/status changes.

This draft has no redistribution license selected. Obtain the repository owner's license decision before a public collaborative release.
