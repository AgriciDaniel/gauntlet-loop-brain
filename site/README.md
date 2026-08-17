# Gauntlet Loop Brain Site

`site/` is a reviewed configuration overlay for a sanitized Quartz publish
surface. It is not a standalone Quartz checkout.

Content should be built from the reviewed wiki only. Do not publish `.raw/`, source captures, internal ledgers, credentials, local paths, or private client data.

Public exclusions: .raw, .obsidian, hot.md, log.md, references/source-ledger.json, references/claim-ledger.md, runs, private.

Quartz is distributed as a repository template, not as a public npm package.
Use the official Quartz repository, pin the reviewed release or commit, apply
`quartz.config.ts`, and build the reviewed public content there. Copy the build
output to `site/public/`, then run:

```bash
node site/scripts/sanitize-public.mjs
```

Review `PUBLISHING_NOTICE.md` before publishing.
