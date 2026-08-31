# Three-Stack Research Portfolio

This is Jordan Conley's small public portfolio for AI evaluation, data quality, and defensive security. It is deliberately static HTML and CSS: no database, analytics, paid API, environment variable, or build step.

## Public boundary

The homepage lists only projects that are currently public and inspectable. Private/local work, including SYNTH and the Windows Epistemos scaffold, is not represented as a finished public project. Upstream forks are retained for provenance but are not portfolio projects.

## Reading order

1. [PLAIN_LANGUAGE_LAB_GUIDE.md](PLAIN_LANGUAGE_LAB_GUIDE.md) for a no-jargon explanation.
2. [RESEARCH_ATLAS.md](RESEARCH_ATLAS.md) for the public project map, evidence, and limits.
3. [PROJECT_LAYERS.md](PROJECT_LAYERS.md) for how input, comparison, measure, and boundary fit together.

## Ownership and assistance

Jordan defines the research questions, scope, evidence standard, review decisions, and public boundaries. AI assisted some implementation and iteration. Each project README is the source of truth for its specific methods, result files, and limitations.

## Local check

```powershell
python -m http.server 4173
```

Open `http://127.0.0.1:4173/`.

## Vercel Hobby

- Repository: `BlickandMorty/three-stack-research-portfolio`
- Framework preset: `Other`
- Build command: leave blank
- Output directory: `.`
- Environment variables: none

This is intended to remain a free static deployment.
