# Three-Stack Research Portfolio

This is my lightweight public research portfolio for the three parts of my work:
AI internals, science, and defensive security. It is deliberately plain static
HTML and CSS. There is no database, analytics script, paid API, serverless
function, or build step.

## Design

The site uses a deliberately minimal off-white pixel-art system and bundles the
SIL Open Font License 1.1 `Press Start 2P` font in `assets/fonts/`. The font
license is preserved alongside the asset. Hosting remains a free static Vercel
deployment with no environment variables.

## Why this is the Vercel project

The larger private Epistemos site contains application logic and local research
features. It is the wrong artifact to use as a zero-cost public portfolio. This
repository is smaller, auditable, and safe to host as static files.

## Study map

Start with [RESEARCH_ATLAS.md](RESEARCH_ATLAS.md) for the complete project
index, exact results, and limits. [PLAIN_LANGUAGE_LAB_GUIDE.md](PLAIN_LANGUAGE_LAB_GUIDE.md)
explains the same work without assuming research or engineering background.
The homepage highlights the core projects; the atlas keeps supporting tests,
failed generalizations, and technical bounds visible without turning each into
a separate headline claim.

[RELEASE_AUDIT_v3_2.md](RELEASE_AUDIT_v3_2.md) records what is complete for the
current release, what is deliberately pending, and the conditions required to
resume research without reopening closed experiments.

For a Vercel Hobby import:

- repository: `BlickandMorty/three-stack-research-portfolio`
- framework preset: `Other`
- build command: leave blank
- output directory: `.`
- environment variables: none

Do not accept a Pro trial or enter payment details for this project. The site
does not need them.

## Local check

```powershell
python -m http.server 4173
```

Then open `http://127.0.0.1:4173/`.

The public page links to the source artifacts rather than embedding private
notes, contact details, résumé data, API keys, or research credentials.
