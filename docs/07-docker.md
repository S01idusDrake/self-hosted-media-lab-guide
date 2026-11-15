# 7. Docker and Compose foundations

**Run on:** apps-node. **Requires:** working OS/network, local SSD configuration directory and accepted storage. **Produces:** a documented container lifecycle.

## Install and verify

Use Docker's official Ubuntu repository instructions for your release; do not mix Docker packages from multiple repositories or remove an existing engine without a migration plan. Install Engine, CLI and Compose plugin. Check `docker version` and `docker compose version`. Decide whether to use `sudo docker` or grant an operator Docker access; Docker socket access is effectively administrative access, not a harmless convenience.

Create `/opt/media-lab` with private config/secrets directories and reviewed ownership. Copy example files from this repository into a **private deployment directory**, never add real settings back to this guide. Record all selected image tags/digests in the private version inventory.

## Compose workflow

Read [examples/README](../examples/README.md). Fill in the `.env.example` worksheet as a private `.env`, and create local secret files only if using the VPN example. Do not put secrets on a command line or paste `docker compose config` output into chat. Validate privately with:

```sh
docker compose --env-file .env -f media.compose.yaml config --quiet
```

The supplied file deliberately refuses missing variables. Use the same file and project directory for all later Compose commands. Start only the service you are configuring: `docker compose -f media.compose.yaml up -d prowlarr`, for example, after prerequisites are met. `docker compose ps` reports state. Read bounded logs privately and redact credentials before sharing. Never publish an uninitialized app publicly.

## Persistence and health

Each app needs persistent configuration, an explicit startup policy, log limits, selected network and suitable health check. Bind app databases to local SSD; bind media through one `/data` root. Images differ in UID/GID handling and available health tools; verify the chosen version rather than imposing environment variables universally. The example probes assume LinuxServer images with curl, and Seerr with wget; confirm those tools before deployment.

An image digest makes a reference reproducible but does not make it secure or compatible. Save the old digest and consistent app backup before updates. Recreate containers from the intended definition, verify health and settings, then accept. An unhealthy container is not automatically restarted by an ordinary restart policy. A dependency's health at startup is not a continuing workflow guarantee.

Docker-published ports can bypass expected host-firewall paths. Prefer loopback bindings plus controlled proxy/private networking; explicitly test access from an unauthorized client. Do not expose the Docker TCP API. Do not mount the Docker socket into arbitrary dashboards/apps.

Checkpoint: config validation succeeds, required directories preexist, each new app persists a harmless test setting through recreation, and unauthorized LAN clients cannot reach management UIs. Do not run `down -v` or prune as rollback; preserve volumes and restore selected config/image versions.

Sources: [Engine installation](https://docs.docker.com/engine/install/ubuntu/), [Compose plugin](https://docs.docker.com/compose/install/linux/).
