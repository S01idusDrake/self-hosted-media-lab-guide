# 12. Seerr requests and approvals

**Run on:** apps-node and trusted browser. **Requires:** working Jellyfin, managers, healthy storage and a normal-user account. **Produces:** requests with deliberate approval and category routing.

1. Select a maintained Seerr release and follow its current image instructions. Bind its persistent configuration directory to the image's documented path and expose setup on loopback only. The example uses `/app/config` and port 5055; confirm them for your chosen release.
2. Reach the UI through a temporary SSH tunnel. Connect Jellyfin by a host-reachable LAN URL such as `http://<MEDIA_IP>:8096`; inside Seerr, localhost is not media-node. Authenticate with the intended admin integration and sync only the users/libraries you mean to support.
3. Connect Radarr at `http://radarr:7878` and Sonarr at `http://sonarr:8989` on their shared network, using private API keys. Choose default profile, language/quality and root folder. Run each connection test and inspect returned roots rather than typing a stale path.
4. Require manual approvals for ordinary users. Check imported permissions, request limits and auto-approve settings individually; an imported user must not become an administrator by accident.
5. Add category rules only after verifying your release supports them. Define Kids/Anime/normal roots consistently across request UI, manager and Jellyfin. Metadata-based routing is a convenience, not parental control or an age-rating guarantee. An approver must review ambiguous matches.
6. Test as a non-admin: search an allowed title, submit one request and confirm it remains pending with no downloader activity. Approve as admin, inspect chosen root/profile and verify the accepted sample all the way to playback. Keep a record of what test data you created before cleanup.
7. For external access set the intended application URL to HTTPS and configure the current supported proxy/trust/CSRF behavior. Trust only the actual proxy path. Test sign-in in a fresh browser and authenticated request submission; an anonymous status endpoint returning 200 proves only that endpoint.

Checkpoint: approval separation, duplicate/availability matching, manager integration, login and a complete authorized request work. Leave it private if any integration fails. Removing public ingress is a safer rollback than deleting the persistent request database.

Source: [Seerr upstream](https://github.com/seerr-team/seerr). Naming, variables and proxy options are version-sensitive; this chapter's generic workflow has not been clean-installed as a single supported version set.
