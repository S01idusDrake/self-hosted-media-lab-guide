# 17. Prometheus and exporters

**Run on:** apps-node; node exporter on each Linux host. **Requires:** stable management access and local SSD space for metrics. **Produces:** private metrics with known meanings.

## Collect host and application availability

1. Choose a maintained package/binary/container method for Prometheus; record versions and storage retention. Use its official instructions, a dedicated service identity and a local persistent data directory. Bind the UI/API to loopback or management-only access. Do not expose unauthenticated metrics publicly.
2. Install node exporter on each host using a maintained release/service. Restrict port 9100 to Prometheus. Confirm its local metrics endpoint and then remote scrape from Prometheus. If containerizing, use its documented host mounts/namespaces; ordinary container filesystem metrics are not automatically host metrics.
3. Add one static job per host with role labels; see the schematic `examples/prometheus.yml.example`. Run `promtool check config <PRIVATE_CONFIG_PATH>` before reload. A successful reload and `up == 1` establish scrape success, not application health.
4. Deploy blackbox exporter privately (commonly port 9115). Configure a small HTTP module, one intended target and the standard `__param_target`/`instance` relabel pattern. Validate the application status code/content and TLS expectations for each endpoint. Add DNS/TCP/ICMP modules only when needed and tested.
5. Start with Jellyfin `/health`, manager `/ping`, request app public-settings endpoint and proxy health. A protected endpoint may correctly return 401; choose a safe health endpoint rather than embedding admin credentials in URLs.
6. For a managed switch/router, prefer restricted SNMPv3 where supported. If you deliberately choose v2c, use a unique read-only community restricted to the collector address, keep it private and understand it is unencrypted. Generate version-compatible snmp_exporter modules/config. Test interface counters and operational states. An unused port can correctly be Down.
7. If the gateway does not support SNMP, monitor reachability, DNS and selected TCP service instead of leaving a knowingly broken scrape job. ICMP privileges should be limited to the actual service identity; do not give broad network capabilities to every container.

## Optional application metrics

Jellyfin/plugin-specific exporters can add playback/session data, but require a maintained exporter compatible with your server API. Select one deliberately, create the narrowest supported dedicated API credential, store it privately, restrict its metrics listener to Prometheus and verify metric meanings against one controlled playback session. User/session labels may reveal viewing habits; minimize them. No particular exporter image/schema was verified for this draft, so this is an optional implementation gap rather than a ready recipe.

## Docker discovery and missing services

A generic collector must discover containers, keep an expected-name registry on persistent local storage and emit running/health/restart metrics atomically through node exporter's textfile directory. It must export no environment/credentials. Define health states separately: Healthy, Unhealthy, Starting, No health check and Missing. Keep a stopped state visible; absent metrics must not become healthy.

Discovery alone cannot remember removed containers. Retain registry entries until deliberate retirement; exclude disposable setup/backup containers through a chosen generic ignore label such as `lab.monitoring=ignore`. Record last success separately from last attempt and alert on stale/failed collection. Docker API access is privileged; run the collector as a narrowly managed local task, never expose the socket over TCP.

**Implementation status:** this edition supplies the metric contract and acceptance requirements, not a tested generic Docker discovery daemon. You can use a maintained exporter for basic state, but missing-expected-service behavior still needs the registry implementation and fixture tests before claiming parity. Do not import private collectors into this repository.

Checkpoint: each host scrape works, endpoint probes report actual expectations, a test failure remains visible and registry/collector freshness behavior is tested in staging. Back up configs/registry and monitor the collector itself.

Sources: [Prometheus getting started](https://prometheus.io/docs/prometheus/latest/getting_started/), [node exporter](https://github.com/prometheus/node_exporter), [blackbox exporter](https://github.com/prometheus/blackbox_exporter), [SNMP exporter](https://github.com/prometheus/snmp_exporter).
