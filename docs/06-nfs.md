# 6. NFS between the two hosts

**Run on:** media-node (server) and apps-node (client). **Skip:** one-host build. **Requires:** chapter 5 accepted, stable IPs and numeric UID/GID plan.

1. Install `nfs-kernel-server` on media-node and `nfs-common` on apps-node using `sudo apt install <PACKAGE>`, replacing the placeholder with the appropriate package on each host. The actual filesystem must already be mounted and healthy.
2. Save existing exports privately. Create an export file under `/etc/exports.d/` containing your reviewed values:

```exports
/srv/media-data <APPS_IP>(rw,sync,no_subtree_check,root_squash,mountpoint=/srv/media-data)
```

This is a template; replace the address. Limit the export to the client IP. `root_squash` prevents remote root becoming server root. The mountpoint guard avoids exporting the empty underlying directory if the media filesystem is missing; verify support on your installed NFS server. NFS AUTH_SYS trusts client numeric identities, so use only on a trusted restricted network.

3. Apply with `sudo exportfs -ra`, inspect `sudo exportfs -v` privately and confirm the intended single export. Restrict NFSv4 TCP 2049 to apps-node at host and network firewalls. Verify your negotiated NFS version; older protocols can need additional ports. Do not open broad port ranges blindly.
4. On apps-node create an empty `/srv/media-data` mountpoint. Preserve any files already there instead of hiding them. Save fstab, then add your client line:

```fstab
<MEDIA_IP>:/srv/media-data /srv/media-data nfs4 rw,hard,_netdev,nofail,x-systemd.automount 0 0
```

This is a starting pattern; confirm export-path visibility and options for your server. `hard` favors data consistency but an inaccessible server can block callers. Automount helps ordering; it is not a storage-health monitor. During an active storage incident do not probe/traverse a stale mount to test it.

5. Reload systemd after fstab editing and mount the selected new entry in your setup window. Verify server/export/source, not just directory existence. Never place SQLite app config on NFS.
6. On healthy storage, create a unique scratch file as the actual container UID, hardlink it within the same tree, compare device/inode/link count using `stat`, then remove only both scratch paths. This confirms permissions and hardlink behavior without touching the library. Do not assume separate Docker bind mounts preserve a single filesystem view; use `/data` as one common bind.

## Startup and outage gate

Docker `create_host_path: false` catches an absent directory, not a missing filesystem beneath an existing directory. Before starting media profiles, require the intended NFS source and a ready server. Enforce reviewed startup dependencies and a continuing storage guard; a boot check alone cannot handle later disconnects. Simulate a missing mount only in an isolated test lab, never by unplugging a working production disk.

Checkpoint: one writer/read test and hardlink test passes, reboot ordering is documented, and apps fail safely without storage. Roll back by stopping dependent apps, unmounting in a planned window and restoring the saved export/fstab; never force an unmount over active writes.

Source: [Ubuntu NFS](https://ubuntu.com/server/docs/how-to/networking/install-nfs/).
