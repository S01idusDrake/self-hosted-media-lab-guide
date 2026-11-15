# 26. Maintenance, documentation and assisted operations

**Run on:** admin workstation and authorized host sessions. **Requires:** an accepted build and private operational repository. **Produces:** a maintainable system rather than an undocumented one-off installation.

## Maintain your own private inventory

Create a private repository containing README, CURRENT_STATE, NETWORK, SERVERS, STORAGE, SERVICES, MEDIA, BACKUPS, MONITORING, CHANGELOG, ROADMAP and RECOVERY. Record facts with observation time, evidence and confidence. Keep raw secrets/config backups out of Git and use vault references. Use a separate private inventory workbook/CSV with retained source data when that is your preferred access register; never maintain contradictory copies silently.

For every container record name, image digest, host/purpose, internal/published endpoints, dependencies, persistent mounts, startup policy, health check and actual deployment-definition path. Discovery labels/runtime metadata help identify live configuration; old local Compose files are not proof of what runs.

## Change cycle

1. Read current deployment and dependencies; create private rollback copies.
2. Describe the requested change, user impact, backup needs and rollback. Obtain approval for changes on shared/live systems.
3. Capture consistent backups and verify them before migrations.
4. Apply one bounded change, validate local health and the affected workflow, then check dashboards/metrics/alerts.
5. Update inventory/source data, current-state summary and changelog. Refresh encrypted configuration backup and verify destination UUID/checksums/access before copying.
6. Retire components deliberately: remove actual app references, preserve data, stop/remove only approved resources and update expected-service registry so real accidental disappearance still shows Missing.

## Suggested cadence

Daily: inspect alerts, backup last success and storage capacity. Weekly: review failed queues, new disk errors and dependency health without initiating bulk jobs. Monthly: review updates/security notices and perform a small restore drill on a rotating app. After any change: verify and document. Set cadence for your actual risk/usage; do not schedule intensive diagnostics on deteriorating media.

## Safe assisted-audit prompt

> Read this lab's private instructions and current-state/source documents. Inspect only the authorized hosts using existing access. Start with bounded cached logs, service state and mount tables; avoid media/NFS traversal and disk stress. Do not stop/start/reload anything, install tools, run backups, change configuration, mount/repair disks, delete/move media or expose secrets. Select safe Docker fields only, never full environment/inspect/config dumps. Report observation times, host/container/storage/backup/network facts, unknowns, discrepancies and proposed next steps. If storage has I/O errors, stop broad inspection and prioritize preservation. Separate current observation from cached history. Return a sanitized report; obtain separate approval for all changes.

Review generated commands and results as you would another operator's work. A tool reporting success does not establish playback, import, persistence or recovery. Give helpers only needed access, and never put live credentials into a general tutorial.

Checkpoint: a second operator can locate current definitions, identify disks, obtain approved access and follow the recovery drill without private knowledge held by one person.
