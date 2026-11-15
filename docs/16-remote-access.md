# 16. Remote access and public HTTPS

**Run on:** private gateway/VPN/ingress account and chosen connector host. **Requires:** accepted local apps, backups and an explicit exposure decision. **Produces:** access to selected services only.

## Choose an approach

For administration, prefer a private VPN/overlay with least-privilege access rather than public admin ports. Choose a provider/tool compatible with your clients and read its installation/access-control docs. This edition does not prescribe a tested overlay-vendor configuration. Verify a remote admin can reach only allowed services and that losing the overlay does not remove console recovery.

For public web requests, a tunnel/reverse proxy can avoid an inbound port-forward. It does not remove authentication requirements. Before using a third party for video transport, check its current plan, terms, bandwidth and media-use constraints; do not assume a free web tunnel is suitable for sustained media traffic.

## Cloudflare Tunnel optional web route

1. Use a domain you control and a private account with MFA/recovery details. Select the current supported cloudflared installation method for your OS. Store tokens/credential files privately; do not embed them in this guide, command history or Git.
2. Create a named tunnel through the dashboard or documented CLI workflow and run the connector as a managed service on a host that can reach its origins. Choose either remotely managed or locally managed configuration and document it; do not mix both casually.
3. Publish **only** an intended hostname such as `requests.example.net` to its initialized request-app proxy origin. Use your actual domain and origin. Locally managed ingress needs a final reject/404 rule. Do not route wildcard hostnames to all internal apps.
4. Configure the app's HTTPS URL/trusted proxy behavior and restrict origin access to the connector path. A tunnel on a different host requires a deliberate private origin listener and firewall rule; localhost cannot cross machines.
5. Validate ingress/configuration with the selected management method, start/reload during a setup window and inspect bounded sanitized logs. Verify public DNS and TLS without disabling certificate validation.
6. Test from a genuinely external connection: sign-in, pending request, logout and unauthenticated API denial. Inspect normal-user permissions. Confirm management names and alternate hostnames are not accidentally exposed.
7. Monitor external availability independently from the lab. A probe originating inside the lab cannot prove every outside user's route. Keep origin/edge certificates distinct in expiry monitoring.

Checkpoint: expected outside access works, unexpected hosts fail and an origin cannot be used to bypass intended controls. Roll back by removing only the newly published route/DNS record and restoring prior connector config; do not delete the account or unrelated tunnels.

Source: [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/). Public video ingress needs a separately validated approach under current provider terms.
