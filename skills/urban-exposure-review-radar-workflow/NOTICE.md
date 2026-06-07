# Notice

This package contains original workflow material for urban exposure, sports geography, urban health, geospatial review, bibliometric review, and frontier radar tasks.

It also vendors a third-party Codex-native academic research package:

- Source package: `Imbad0202/academic-research-skills-codex`
- Upstream suite: `Imbad0202/academic-research-skills`
- Vendored path: `subskills/academic-research-suite`
- Codex adapter version: 0.1.11
- Upstream ARS commit recorded in manifest: `2560a072386d4b1a035e5a40ed24ce1edbc0a356`
- License: Creative Commons Attribution-NonCommercial 4.0 International

The upstream license text is preserved at:

```text
subskills/academic-research-suite/LICENSE
```

The upstream README, changelog, security note, and version file are preserved as:

```text
subskills/academic-research-suite/README.upstream.md
subskills/academic-research-suite/CHANGELOG.upstream.md
subskills/academic-research-suite/SECURITY.upstream.md
subskills/academic-research-suite/VERSION
```

Modification note:

- The upstream Codex package is vendored as an isolated subskill.
- The parent skill adds an urban-exposure and sports-geography routing layer before calling the ARS subskill.
- The parent skill instructs agents to load only the ARS router and one relevant workflow instead of loading the whole vendored suite.
- The parent skill preserves domain-specific constraints for exposure validity, accessibility, use, causality, formal review corpus rules, and frontier radar handoff.

Do not remove attribution, upstream license files, or the non-commercial restriction when copying, publishing, or adapting this package.
