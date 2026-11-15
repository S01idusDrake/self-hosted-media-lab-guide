# 18. Grafana dashboards, alerting and external status

**Run on:** apps-node and selected notification/monitor account. **Requires:** verified Prometheus labels/targets. **Produces:** useful panels and tested human notification.

1. Install a maintained Grafana release using official instructions, local persistent storage and restricted administration. Change initial credentials, disable anonymous access unless deliberately justified, and set the intended root URL/proxy behavior.
2. Add Prometheus as a datasource using a URL reachable from Grafana's actual host/container. Save/test; then query a known `up` series. A datasource URL using localhost works only if Prometheus is in the same network namespace.
3. Build Overview, Servers/Storage, Network, Services and Public Availability dashboards. Begin with a few panels each: target state, host load/memory, filesystem available bytes/percent, probe success/latency, interface traffic and container state/freshness.
4. Use dashboard variables from current active labels. Avoid stale retired device series defining today's selector. Test every expression in Explore; an empty result is not a healthy result. Display health as a discrete state and avoid averaging incompatible codes.
5. Keep missing/no-healthcheck/starting distinct from healthy. Compare expected target counts with reporting counts. Availability percentages describe recorded samples; they do not cover periods before collection or guarantee playback/downloads.
6. Choose one primary alert owner: Prometheus rules plus Alertmanager, or Grafana-managed alerts. Avoid duplicate notifications from parallel implementations. Set a private contact point (email, chat webhook or supported provider), grouping, quiet hours and sustained-failure thresholds.
7. Add alerts for target down, stale collection, disk capacity, backup freshness, missing expected containers and unhealthy applications. Use `for` delays appropriate to scrape intervals; add no-data alerts separately. Store contact secrets in protected configuration, not exported dashboard JSON.
8. Send an approved test notification. Then cause a harmless staging failure, wait for the real rule to fire, confirm receipt and restore it. Confirm a recovery/resolved message. A saved contact point or firing dashboard state is not proof of delivery.
9. Use an independent outside-the-lab monitor for public HTTPS/DNS/status. Configure only public-safe endpoints, titles and contact information. Check expected content and certificate validity; a public status page should not contain internal topology or live credentials. Keep provider status pages separate from Grafana's private operations data.

Checkpoint: all queries return understood results, absence is visible, real failure and recovery delivery work and external monitoring can notify during a host/Internet outage. Export generic dashboard definitions only after stripping datasource IDs, targets and contact details.

Sources: [Grafana installation](https://grafana.com/docs/grafana/latest/setup-grafana/installation/), [Prometheus alerting overview](https://prometheus.io/docs/alerting/latest/overview/). Example alert expressions are starting points, not a complete tested ruleset.
