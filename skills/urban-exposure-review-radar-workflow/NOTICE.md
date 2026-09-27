# Notice

This package contains original workflow material for urban exposure, sports geography, urban health, geospatial review, bibliometric review, and frontier radar tasks.

It also vendors a third-party Codex-native academic research package:

- Source package: `Imbad0202/academic-research-skills-codex`
- Upstream suite: `Imbad0202/academic-research-skills`
- Vendored path: `subskills/academic-research-suite`
- Codex adapter version: 3.22.0
- Codex package commit used: `3c37ef8`
- Upstream ARS commit recorded in manifest: `3c546bc08c56f79e0068f1ea4f0acedf5bf69b5e`
- License: Creative Commons Attribution-NonCommercial 4.0 International

The upstream license text is preserved at:

```text
subskills/academic-research-suite/LICENSE
```

The upstream manifest, notice, license, README files, changelog, and traceability material are preserved under:

```text
subskills/academic-research-suite/manifest.json
subskills/academic-research-suite/NOTICE.md
subskills/academic-research-suite/LICENSE
subskills/academic-research-suite/ars/
```

Modification note:

- The upstream Codex package is vendored as an isolated subskill.
- The parent skill adds an urban-exposure and sports-geography routing layer before calling the ARS subskill.
- The parent skill instructs agents to load only the ARS router and one relevant workflow instead of loading the whole vendored suite.
- The parent skill preserves domain-specific constraints for exposure validity, accessibility, use, causality, formal review corpus rules, and frontier radar handoff.

Do not remove attribution, upstream license files, or the non-commercial restriction when copying, publishing, or adapting this package.
