# 5. Storage, mounts and permissions

**Run on:** media-node console/SSH. **Requires:** healthy disks and an explicit target plan. **Produces:** verified persistent media mount without modifying pre-existing content.

## Identify before changing

```sh
lsblk -o NAME,SIZE,MODEL,SERIAL,FSTYPE,UUID,MOUNTPOINTS
cat /proc/self/mountinfo
```

Map each physical serial to its intended role and existing filesystem. `/dev/sdb` can change after reboot. UUID identifies a filesystem; serial identifies a device. Do not format an unfamiliar disk. New filesystem creation is a separate deliberate action following filesystem/vendor instructions; no automated erase command is provided.

1. Inspect existing SMART/log evidence and connection stability as in chapter 19. If there are I/O errors, clicking, disconnects or an aborted journal, stop setup and preserve data first.
2. Choose a stable mount root such as `/srv/media-data`. Before mounting, confirm it is empty and not already covering local files. Create only the directory needed with `sudo install -d -m 0755 /srv/media-data` on a known new host.
3. Save `/etc/fstab` privately before editing. Add a reviewed entry for your actual UUID/filesystem. An **illustrative, non-executable** ext4 entry is:

```fstab
UUID=<MEDIA_FILESYSTEM_UUID> /srv/media-data ext4 defaults,nofail 0 2
```

`nofail` can allow the OS to boot without media; it does not make applications safe to start without it. Use separate application mount checks. XFS and other filesystems need their own options/check behavior; do not copy this ext4 line unchanged.

4. Validate the edited table using available `findmnt --verify` support, then mount only the intended new entry during your setup window. Do not run broad `mount -a` as an incident repair. Verify exact source, UUID, filesystem/options and underlying device presence. A mount-table match alone does not establish usable storage.
5. Create new directories only after mount identity is confirmed:

```sh
sudo mkdir -p /srv/media-data/downloads/incomplete
sudo mkdir -p /srv/media-data/downloads/movies /srv/media-data/downloads/tv
sudo mkdir -p /srv/media-data/downloads/music
sudo mkdir -p /srv/media-data/media/movies /srv/media-data/media/tv /srv/media-data/media/music
```

## Ownership model

Create a dedicated media-writer account/group on the apps host, record numeric UID/GID and map permissions intentionally on the server. Use matching numeric IDs or explicit ACLs; matching account names alone is insufficient for NFS AUTH_SYS. Give import/download writers write access to new directories and Jellyfin read/traverse access. Do not recursively take ownership of an existing library. Apply setgid/default ACLs only to reviewed new roots and test newly created files.

Use `namei -l <PATH>` and `getfacl <PATH>` to inspect each parent. Parent directories require execute/traverse permission. A narrowly configured group/ACL is preferable to world-write access. Keep app config databases on local SSD with their image-specific ownership, separate from this media tree.

## Checkpoint

On healthy new storage only, create a uniquely named scratch file as the intended writer, read it as the reader and remove only that scratch file. Record free-space reserve and expected behavior on a missing mount. Test reboot/mount ordering before filling the library. Do not perform scratch writes on a suspected failing disk.
