# Validation status

## What has been checked in this edition

- Documentation was newly written around generic roles and placeholders, rather than exporting private configuration.
- Upstream primary references were consulted for core software; version-sensitive details are linked to their owners.
- Local relative Markdown links, text privacy rules and template structure are checked by `python3 tools/check_docs.py`.
- The publication guard `python3 tools/check_privacy.py --history` checks publishable text and reachable Git metadata/blobs; a private external denylist adds installation-specific checks.
- YAML syntax can be checked separately; actual Docker Compose schema/runtime validation requires Docker on a staging system.

## What has not been proved

No new server was installed; no application container was started; no actual DNS/VLAN/firewall/tunnel configuration was applied. No complete request/download/import/playback, VPN isolation, IPTV, notification or restore test was run for this generic version. Image variables have no tested pinned version set. Hardware/provider-specific steps remain open in COVERAGE.md.

Examples are illustrative starting configurations and may need changes for upstream releases. The documentation checker is not a secret scanner, security certification or infrastructure test. Do not describe this draft as production-ready or fully reproducible.

## Release qualification checklist

- [ ] Select and record supported OS/hardware/image versions in a private acceptance record, then publish a generic version matrix.
- [ ] Parse all YAML with a real YAML parser; run Compose config validation using dummy non-secret values.
- [ ] Deploy one-host path on clean equipment/VMs with authorized test content.
- [ ] Deploy two-host NFS path and verify numeric identities, hardlinks and boot ordering.
- [ ] Test missing mount/disconnect behavior safely in staging; no fallback writes.
- [ ] Complete request, music and selected IPTV workflows.
- [ ] Test local/proxy/remote authentication and denied exposure.
- [ ] Prove VPN fail-closed and recovery behavior.
- [ ] Implement/test custom registry, heartbeat and storage guards or choose maintained alternatives.
- [ ] Verify backup consistency, encrypted offsite copy, retention and isolated restore.
- [ ] Test notification failure and recovery delivery.
- [ ] Review content and Git author metadata before a public release; choose an explicit license.

Use the blank acceptance template for each module. Mark skipped modules honestly and report every deviation.
