# 21. Recovery drills and disaster recovery

**Run on:** isolated spare host/VM or empty private staging location. **Requires:** known complete backup, keys and version inventory. **Produces:** measured proof of recovery without overwriting production.

## Restore drill first

1. Select an explicit completed snapshot ID and record source host/app versions. Confirm you have the password/key through your recovery process. Do not assume `latest` belongs to the intended host or succeeded completely.
2. Choose an empty staging destination on healthy storage with enough capacity. Keep it separate from the original application's live directories, media and backup repository. For restic, a template is:

```sh
restic -r <REPOSITORY> restore <SNAPSHOT_ID> --target <EMPTY_STAGING_DIRECTORY>
```

Replace placeholders before use. Restore into a private path. Inspect the restored directory layout; a source's absolute path may appear nested under the restore target.

3. Verify manifests/checksums, copied SQLite integrity, settings/plugin files and required ownership. Do not expose restored secrets. Restore tool validation is not an application acceptance test.
4. Build an isolated matching-version application instance with outbound integrations disabled or pointed to staging. Do not let a restored downloader/request service submit duplicate jobs or a test server modify production media.
5. Confirm users, watch history, libraries/config, optional plugin data and representative local playback against safe sample content. Measure elapsed restore and time to service readiness separately from the backup pause.

## Real recovery plan

Diagnose first: is this host failure, missing storage, DNS/ingress or app corruption? Healthy application plus missing media usually calls for storage repair/recovery, not overwriting app state.

For an approved application restore, stop all relevant writers, preserve current data/config in a separate timestamped location, install the exact supported version and copy independent restored files with correct ownership. Never hardlink live data to backup inodes. Do not mix stale database sidecars from the old live directory with a restored snapshot. Reconcile host references such as fstab, interface names and tunnel routes with the replacement hardware instead of applying them blindly.

Start local dependencies in order: healthy storage/network/DNS, then apps/integrations, then proxy/remote access. Validate normal users, data, queues and representative workflows before enabling automation. Preserve the previous data and backup until acceptance. Roll back by restoring the preserved prior directories only when that state is safe and version-compatible.

## Caretaker handoff

Maintain private instructions for responsible contacts, console access, vault/recovery-key location, domain renewal, ISP/account ownership and how to identify each disk by serial/UUID. Practice the procedure with a second person. Do not publish those details in this generic repository.

Checkpoint: a real isolated drill passes with documented restore duration, gaps and corrective actions. No production restore is implied by this chapter.

Source: [restic restore](https://restic.readthedocs.io/en/stable/050_restore.html). Application-specific version requirements remain those of each upstream project.
