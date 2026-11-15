# 9. Jellyfin media server

**Run on:** media-node. **Requires:** accepted media mount, read/traverse permissions and local network access. **Produces:** a secured local library and a tested playback path.

## Install and initialize

1. Choose the native Debian/Ubuntu package route for this build. Follow Jellyfin's current official Linux repository instructions; inspect any downloaded installer before running it. Record the installed server/web/FFmpeg package versions. This guide does not assume a historical version number.
2. Check `systemctl status jellyfin` and a bounded `curl --max-time 5 http://127.0.0.1:8096/health`. Restrict LAN access to trusted clients while initializing. If the service fails, read a bounded journal excerpt privately before reinstalling.
3. Open `http://<MEDIA_IP>:8096` from a trusted client. Create your own administrator; do not use it for ordinary family playback. Complete language/preferences, and keep remote exposure off until local setup and backups are accepted.
4. Add Movies, TV and Music libraries using the media-host paths under `/srv/media-data/media/`. Configure library type and preferred language. Kids/anime may use distinct directories and libraries; create them deliberately and document mappings.
5. Grant the Jellyfin service account read/traverse access through each parent and read access to content; optional artwork/subtitle writes need explicit policy. Verify effective access as the service user. Do not grant world-write or recursively rewrite existing ownership to fix one path.
6. Add one small, authorized sample of each media type to healthy storage. Run a targeted library scan. Inspect title matching, season/episode ordering, music album/artist grouping, artwork and subtitles before importing a large library.

## Playback and acceleration

Start with direct play. In the playback dashboard, record Direct Play, remux or transcode and the reason. Test your intended browser/TV/mobile client with subtitles and audio formats. For supported Intel/AMD hardware, follow Jellyfin's acceleration guide, confirm `/dev/dri` device/group access, enable the matching backend and test one forced transcode. Do not assume an old CPU can decode/encode every codec. Keep the working software-transcode setting for rollback.

Create a restricted normal user and verify it cannot administer the server or access excluded libraries. Test an actual minute of video/audio; `/health` only confirms application response. Back up `/etc/jellyfin` and the actual data/plugin directories using chapter 20 before extensions or public access.

## Optional extensions

Use the server's supported plugin catalog and match plugin/server versions. Playback-reporting and intro-detection plugins are optional, can consume resources and may add SQLite databases to backup scope. Install one at a time, preserve app state first and verify startup/playback. Do not assume plugin cache files are disposable until scope is understood.

Checkpoint: library scan, normal login, representative playback and intended transcode pass; data/config/version and optional plugin databases are inventoried. Roll back a plugin or acceleration setting selectively. Do not restore the database to fix missing storage.

Sources: [Linux installation](https://jellyfin.org/docs/general/installation/linux/), [acceleration](https://jellyfin.org/docs/general/post-install/transcoding/hardware-acceleration/).
