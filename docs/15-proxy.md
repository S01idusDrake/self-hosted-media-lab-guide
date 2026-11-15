# 15. Nginx and private service names

**Run on:** apps-node. **Requires:** secured local app UIs and working private DNS. **Produces:** controlled hostname routes with predictable authentication.

1. Deploy a maintained Nginx image or distribution package and choose one method consistently. Keep config on local disk, back it up and restrict listeners to intended interfaces. A containerized proxy must share an explicitly named network with its upstream containers; a host proxy can use loopback published ports.
2. Create one server block per service; do not use a catch-all that publishes every management app. For a **host-installed** proxy and loopback Radarr mapping, an internal-only starting route is:

```nginx
server {
    listen <APPS_IP>:80;
    server_name radarr.lab.test;
    allow <ADMIN_SUBNET_CIDR>;
    deny all;
    location / {
        proxy_pass http://127.0.0.1:7878;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

This template is not executable until placeholders are replaced. It is internal HTTP, not encrypted public access. App authentication still applies. A container proxy cannot use this localhost upstream for a different container; choose service names on a shared network and account for Docker DNS resolution/recreation.

3. Add a DNS rewrite for the internal name and verify it resolves to the proxy from an allowed client. Validate Nginx with `nginx -t` using the appropriate host/container invocation, then reload only after it passes.
4. Test the correct Host header, expected login/redirect behavior, API authentication and disallowed source access. HTTP 401/403 may be healthy if that route is protected; specify the check's expectation rather than treating every non-200 as down.
5. For Jellyfin, follow its supported Nginx reverse-proxy example for WebSockets, buffering/timeouts and paths. Test live playback, seeking and subtitles through the proxy. Do not assume a generic HTML proxy block is adequate for video.
6. For request apps behind HTTPS ingress, configure app URL, secure cookies, CSRF and supported proxy trust. Accept client-IP/protocol headers only from your actual trusted proxy/tunnel path and overwrite untrusted values. Do not trust arbitrary LAN requests with forged HTTPS headers.

Checkpoint: each route reaches only its intended app, unauthorized clients are denied, and sign-in plus a state-changing request succeed securely. Back up/restore the specific changed server block for rollback. Avoid disabling certificate or CSRF validation as a fix.

Sources: [Nginx proxy module](https://nginx.org/en/docs/http/ngx_http_proxy_module.html), [Jellyfin proxy documentation](https://jellyfin.org/docs/general/post-install/networking/reverse-proxy/).
