# Hermes — Hermes Cornerstone

Public policy and support pages for the **Hermes** Discord application, used privately by the operator and explicitly approved Hermes Cornerstone team members. Bot identity supplied by the operator: **HermesBot#9321**. Operated by GitHub account **susheel009**, not Discord or Nous Research.

## Discord Developer Portal links

| Field | Public URL |
| --- | --- |
| Terms of Service URL | https://susheel009.github.io/Discord/terms.html |
| Privacy Policy URL | https://susheel009.github.io/Discord/privacy.html |
| Website / overview, if requested | https://susheel009.github.io/Discord/ |
| Support website, if requested | https://susheel009.github.io/Discord/support.html |
| Data-deletion instructions | https://susheel009.github.io/Discord/data-deletion.html |

The support website is **not** a Discord Support Server invite. This deployment has no public install link. The policy pages do not provide an OAuth callback, Interactions Endpoint, or Linked Roles endpoint.

## Publishing

GitHub Pages serves the repository root from `main`. The site is static HTML and CSS with no build step, third-party scripts, analytics, forms, or frontend dependencies. `.nojekyll` disables Jekyll processing. Do not commit credentials, transcripts, user data, or runtime configuration.

## Testing

```sh
python -m unittest discover -s tests -v
```

Tests validate required pages, semantic landmarks, navigation, relative links and fragments, duplicate IDs, obvious placeholders, and the absence of executable scripts, forms, or iframes. A browser and live HTTP check are also needed after deployment.

## Operator responsibilities

Read [SETUP.md](SETUP.md) before using the links for any review. The policies describe data flows and limitations; they do not turn on privacy controls or certify legal compliance. They are a practical starting point, not legal advice. Review them against your actual use and applicable law.

The initial local Hermes configuration inspected during setup uses the `openai-codex` provider and has persistent memory enabled. No Discord bot token or Discord user allowlist was configured in the inspected profile's `.env` at the time of setup. No token was read into or committed to this repository. Future provider or functionality changes must be reflected in the policy and disclosed to authorized users.

Private requests are routed through the existing Hermes Cornerstone administrator because no public email or administrator Discord username was supplied. GitHub Issues are only a public fallback for non-sensitive support or a request for a private contact route. The operator must monitor that route and respond privately before requesting personal details.
