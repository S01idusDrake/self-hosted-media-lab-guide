# 25. Security review and final acceptance

**Run on:** admin workstation, test clients and selected app UIs. **Requires:** each selected module's checkpoint. **Produces:** a private signed-off build record.

## Test by layer

| Layer | Expected evidence |
| --- | --- |
| Host | Supported OS, updates, correct time, second SSH login and console recovery |
| Network | Intended DHCP/DNS/routes, management restrictions, IPv4/IPv6 exposure checked |
| Storage | Physical identity matches mount, reader/writer access, safe startup and reserves |
| Containers | Correct image/mount/network/startup policy; app health persisted across recreation |
| Media | Representative movie/episode/album playback and intended transcode |
| Requests | Normal user pending request; admin approval; correct destination; no accidental auto-approve |
| VPN | Intended egress and fail-closed test with recovery |
| IPTV | Fresh guide/channel mapping and real playback, if selected |
| Remote | Valid TLS/login, anonymous denial where expected, no management exposure |
| Monitoring | Understood queries, missing/stale states and actual failure/recovery notification |
| Backup | Encrypted independent snapshot, integrity evidence and isolated restore |
| Website | Public-safe build, navigation/assets, HTTPS and current external status link |

Use `templates/acceptance-record.md` for actual results. Do not mark skipped modules as passed. Distinguish UI/health checks from full workflow tests. Record versions and deviations so another person can reproduce the result.

## Review exposure and privileges

Inspect explicit listening addresses and firewall rules privately. Test from a permitted client, a denied network and a truly external connection if publishing. No unauthenticated Docker API, exporters, app management UIs, DNS resolver open to the Internet or broad admin access should be assumed acceptable. Verify application users/imported permissions, distinct recovery administrators and account recovery/MFA for external services.

Review secret files, directory ownership, encrypted backup scope and decryption-key access. A config export can contain credentials even if its filename says backup/report. Inspect Git history as well as working files before public publication. Rotate any exposed credential; deletion from a current file does not erase history.

## Failure handling

A failed check is a documented open issue, not a reason to disable TLS/authentication/firewalls. Stop the affected rollout, keep prior working data/config and use the scoped rollback. Approve substantial changes separately from read-only diagnosis. Never intentionally crash or unplug production storage to prove monitoring.

Checkpoint: every required item passes with evidence; remaining gaps have an owner and the build stays private until exposure is accepted. This guide's own end-to-end acceptance is still pending in VALIDATION.md.
