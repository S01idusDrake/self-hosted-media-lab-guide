# 24. Public website and independent status page

**Run on:** admin workstation and your own GitHub/static-hosting account. **Requires:** original public-safe content and a chosen domain. **Produces:** a public site separate from private infrastructure documentation.

1. Create a separate website repository. Decide whether it is a user/organization site or a project site; its URL/base path differs. Keep infrastructure inventory, private docs, configs and diagnostic screenshots out of it.
2. Install a supported Node.js version using an official distribution/version manager and the current Astro prerequisites. Create a new Astro project using its official starter, then commit the dependency lockfile. Record the runtime/package-manager versions in the website repository.
3. Build a simple home/about/projects/services/status/contact structure. Write original text and use properly licensed assets. Link to public service endpoints only after explicitly deciding to advertise them; an internal service list is not public website content.
4. Set Astro `site` to the intended public URL. For a project URL set `base` to its repository path; for a domain root use the correct root base. Test asset links under that exact base, not just the development root.
5. Run the local development server bound to loopback, inspect phone/tablet/desktop layouts, then run the project's production build/preview. Check local links/fragments, image alt text, unique IDs, page descriptions, headings, keyboard focus and color contrast. Keep development-only theme/test switches out of production output.
6. For GitHub Pages, select GitHub Actions as the source and use Astro's current documented workflow. Limit workflow permissions, use a lockfile/frozen install and review third-party actions. Build and deploy the reviewed commit; verify the completed deployment URL.
7. If using a custom domain, verify ownership in your hosting account and add only the currently documented DNS records for that host. Wait for DNS/certificate readiness and enable HTTPS. Do not copy arbitrary IP records from an old tutorial or alter unrelated service DNS.
8. Create an independent external monitor/status page for selected public services using your chosen provider. Configure alerts privately, set a public-safe status name and optional custom status domain. Link to the provider's live status page rather than hard-coding stale uptime into the site. Do not place webhook/API credentials in client JavaScript.

Checkpoint: successful production build/deployment, verified HTTPS, working navigation/assets/status link and no private values in generated files. Roll back by redeploying a known working website commit; keep domain/ingress changes separate from content changes.

Source: [Astro deployment to GitHub Pages](https://docs.astro.build/en/guides/deploy/github/). The static website is an optional module; no pre-existing branded content is supplied.
