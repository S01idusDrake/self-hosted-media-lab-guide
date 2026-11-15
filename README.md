# Self-hosted Media Lab Guide

A beginner's build book for a small Linux home lab: networking, storage, Jellyfin, requests and automation, private DNS, secure access, monitoring, backups and a public website.

**Edition 0.1 — documentation draft, not yet validated by a complete clean-room build.** Start with a private lab and healthy storage. Follow one chapter at a time and pass its acceptance checks before continuing. Commands change only the new systems you explicitly choose to build; never paste them into an existing server without review.

This guide uses invented host roles, reserved example domains and generic paths. It contains no original installation's identities, inventory, addresses, branding, archives or settings. Software/product names identify upstream projects. Some modules use third-party services and require checking their current terms, availability and costs.

## Start here

1. [Choose your build and fill in the worksheet](docs/01-plan.md).
2. [Prepare hardware and Ubuntu](docs/02-ubuntu.md).
3. [Build the network](docs/03-network.md), [admin access](docs/04-admin.md) and [healthy storage](docs/05-storage.md).
4. For two hosts, configure [NFS and permissions](docs/06-nfs.md). For one host, use the same local data tree and skip NFS.
5. Install [Docker](docs/07-docker.md), [DNS](docs/08-dns.md) and [Jellyfin](docs/09-jellyfin.md).
6. Add [VPN/downloads](docs/10-vpn-downloads.md), [media managers](docs/11-managers.md) and [requests](docs/12-requests.md).
7. Add optional [music](docs/13-music.md) and [live TV](docs/14-live-tv.md), then [proxy](docs/15-proxy.md) and [remote access](docs/16-remote-access.md).
8. Configure [metrics](docs/17-monitoring.md), [dashboards/alerts](docs/18-dashboards-alerts.md), [disk health](docs/19-disk-health.md) and [backups](docs/20-backups.md).
9. Test [recovery](docs/21-recovery.md), [media maintenance](docs/22-media-maintenance.md), [branding](docs/23-branding.md) and optional [website/status page](docs/24-website.md).
10. Finish [security and acceptance](docs/25-acceptance.md) and adopt [operations/documentation](docs/26-operations.md).

## What is included

- [Architecture and build order](docs/00-architecture.md).
- [Coverage matrix](COVERAGE.md) for every identified subsystem and optional alternative.
- [Beginner conventions](docs/00-conventions.md), including where to run commands and how to avoid overwriting disks.
- [Example configuration guide](examples/README.md), an illustrative media Compose file and monitoring configuration.
- Blank [inventory](templates/inventory.csv), [build worksheet](templates/build-worksheet.md), [change plan](templates/change-plan.md) and [acceptance record](templates/acceptance-record.md).
- [Validation status](VALIDATION.md), [privacy policy](SECURITY.md), [contributing guide](CONTRIBUTING.md) and [upstream references](REFERENCES.md).

## Limits of this edition

This is a substantial first draft, not a one-click installer or proof of a complete reproducible deployment. Hardware-specific router/switch screens, IPTV provider behavior, GPU support and software releases vary. Example files use deliberate placeholders; they cannot be deployed until you select versions, addresses and storage. Custom historical application shims and private collector/backup scripts are described as design requirements, not shipped as tested generic software. See COVERAGE and VALIDATION for the remaining clean-room work.

The repository starts private for authoring. Any public release requires a separate review of content, Git author metadata, dependencies and license choice. No license is granted by this draft; all third-party software retains its own license. Do not add a real lab inventory or credentials to this repository.
