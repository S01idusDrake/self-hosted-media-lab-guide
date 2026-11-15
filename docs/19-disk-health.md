# 19. Disk health, capacity and preservation

**Run on:** relevant host; use existing logs first. **Requires:** serial/UUID inventory. **Produces:** an evidence-based health policy and a safe incident sequence.

## Normal monitoring on healthy equipment

Install your distribution's smartmontools package and read its supported device/USB-bridge instructions. Identify each drive by model and serial. Capture baseline SMART attributes/error/self-test logs privately; use model-specific interpretation. A global PASSED flag does not override pending/uncorrectable sectors or kernel I/O errors. USB adapters may hide information; missing data is unknown, not zero.

Configure smartd or a suitable supported collector for scheduled attribute collection and alerts. Schedule self-tests only on known healthy drives during low load, with current backups and an understood performance impact. Do not run extended tests on a drive you are trying to recover. Store error history so changes are visible.

Monitor both percent free and absolute available bytes, with reserves for OS, downloads, database growth and backup retention. A manager's import threshold is not a downloader stop. A SMART metric does not detect every cable/power/disconnect problem; correlate kernel USB resets, aborted filesystem journals and missing devices.

## Incident sequence

1. Record symptoms/times and existing bounded kernel/app logs. Determine whether the device is present; a stale rw mount or successful app health endpoint proves neither storage access nor integrity.
2. Stop routine setup and propose a scoped pause of downloads/imports/renames/scans/NFS clients that touch the affected disk. Approval is needed on shared systems. Preserve databases/watch history; no automatic library cleanup.
3. Identify irreplaceable content and choose a healthy destination. A file recovery needs capacity for selected content plus reserve; a full device image needs the whole device byte size plus overhead, not only used space. No destination is implicitly approved for overwrite.
4. If the disk clicks or repeatedly disconnects and data matters, consider professional recovery before further reads. Avoid reconnect loops, write tests, rw automount, fsck and surface scans.
5. For an approved DIY recovery, use an appropriate tool such as GNU ddrescue with an unmounted identified source and persistent mapfile on healthy storage. Validate source/target serials and capacities before constructing a command. Minimal initial retries protect time on a deteriorating source.
6. Retain source and mapfile; validate important recovered files and unreadable ranges. Repair a separate working copy, not the only original. Replace the failing component, reconcile paths and verify small representative workflows before targeted refresh.

## Backup-disk connection failures

A backup disk with clean sector counters can still have unstable cabling/power or a damaged journal. Safely unmount before relocating healthy equipment. Verify the expected UUID is truly mounted before every write. Never let a job fill the server's empty mount directory. Preserve earlier recovery points until new ones are verified.

Checkpoint: serial-based inventory, alert route, capacity thresholds and preservation decision template exist. Recovery commands are intentionally not universal: an incorrect source/target can destroy the only copy. Exact recovery execution requires its own reviewed plan.
