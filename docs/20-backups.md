# 20. Configuration, application and media backups

**Run on:** each source host and independent backup destination. **Requires:** healthy storage, private key/password custody and selected retention. **Produces:** a checked recoverable snapshot, not just a copied folder.

## Define protection before choosing a tool

| Data | Capture method | Typical exclusions |
| --- | --- | --- |
| Compose/YAML, proxy/DNS/monitor configs and required secrets | Encrypted versioned backup from private deployment directory | Image layers, unrelated logs |
| Arr/request/downloader state | App-supported backup or consistent local SQLite snapshot plus settings/state | Regenerable artwork/cache only after checking scope |
| Jellyfin | Matching-version supported backup or stopped consistent complete data/config capture including plugins | Transcodes, disposable caches/logs; media is separate |
| Personal media | Independent file backup according to importance and capacity | Only consciously excluded replaceable content |
| OS/network references | Version, package, mount/service/port inventory and private config exports | Credentials must remain encrypted |

App backups do not protect movie/audio files unless those paths are explicitly included. RAID and hardlinks are not independent backups. Document what you cannot replace.

## Capture consistency

Use application-supported backup/export where it protects the full required scope. For SQLite, use the database's backup API to a new local staging file or stop all writers and copy the complete consistent data set. Do not casually copy a changing main database and omit its WAL. A valid SQLite file alone does not ensure matching settings/plugin data across the application.

For a beginner's first full Jellyfin capture, choose a maintenance window, record whether it was already stopped, stop the service, copy the complete actual data/config and required plugin/host-reference files into a **new empty private staging directory**, then restore its prior running state even on failure. Validate copies and measured downtime. This draft does not ship an automatic stop/copy/restart wrapper; implement error handling and recovery before scheduling it. Do not point recursive copies at nested backup/cache/media trees unintentionally.

Run integrity checks on copied SQLite snapshots in staging and record exact app versions, capture time, expected files, checksums and ownership. Mark a point complete only after checks pass. Do not replace/prune prior complete points if capture fails.

## Encrypted storage: generic restic option

Use a maintained restic package and its documented repository setup. First verify the **actual mount and expected UUID** of the backup disk at `/mnt/backup`. Abort if absent, wrong, full or unhealthy. The commands below assume that guard has already passed and the path is a new intended destination:

```sh
restic -r /mnt/backup/media-lab-restic init
restic -r /mnt/backup/media-lab-restic backup /path/to/verified/private/staging
restic -r /mnt/backup/media-lab-restic snapshots
restic -r /mnt/backup/media-lab-restic check
```

Replace the staging path; supply a repository password privately. Init creates a new repository; do not reinitialize an existing one. Keep recovery credentials separate from the repository and test a second authorized operator can retrieve them. Encryption does not help if the only password is lost.

Store an additional encrypted offsite copy using a restic-supported destination or verified complete encrypted archive upload. For a cloud Drive archive workflow, create a complete encrypted immutable archive locally, generate a checksum, upload to your private chosen folder and read back name/size/checksum where supported; retain a local verified copy. Do not copy an actively changing restic repository with an arbitrary file-sync tool or assume Drive is a native restic backend. No cloud upload automation is shipped in this edition.

## Optional complete encrypted archive format

If you need portable immutable files instead of a backup repository, define a consistent private staging tree and manifest first, then archive it and encrypt using a maintained authenticated format with separate recovery keys. An OpenSSL CMS certificate-based workflow is possible, but requires an explicitly reviewed cipher/recipient policy, a tested decrypt path and supported OpenSSL versions; do not reuse someone else's certificate or private key. This edition deliberately does not supply an unvalidated encryption command. Prefer the documented restic path until this alternative is implemented and tested.

For archives exceeding an uploader limit, split the already-encrypted file into numbered parts, record a checksum for every part and the full encrypted file, and retain an exact ordered reconstruction procedure. Download/reassemble and verify the complete hash before attempting decryption into empty private staging. Partial cloud uploads are not complete recovery points. Keep decryption keys and passwords separate from cloud objects.

## Schedule and retention

Only automate after a restore test. Choose distinct windows for app capture and transfer, explicit timezone, persistent failure logging, maximum pause/time budget and recovery behavior. Add mount/UUID/source identity/free-space guards and a last-success metric. A timer can fail while its service is enabled; monitor result/completeness/freshness.

Example policy: seven successful daily points plus three earlier weekly checkpoints. This is a design choice, not a guaranteed storage budget. Review retention in dry-run/list mode before any forget/prune/delete action. Date/name/manifest time is safer than directory mtime when copy tools preserve timestamps. Keep legacy points until replacements verify.

Checkpoint: one complete snapshot, checked databases/manifests, independent destination, separate keys and isolated restore. Record real pause, logical size, physical growth and restore time separately.

Sources: [Jellyfin backup/restore](https://jellyfin.org/docs/general/administration/backup-and-restore/), [SQLite backup API](https://www.sqlite.org/backup.html), [restic setup](https://restic.readthedocs.io/en/stable/030_preparing_a_new_repo.html), [backup](https://restic.readthedocs.io/en/stable/040_backup.html).
