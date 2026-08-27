# Three-Stack Research Portfolio

This is my lightweight public research portfolio for the three parts of my work:
AI internals, science, and defensive security. It is deliberately plain static
HTML and CSS. There is no database, analytics script, paid API, serverless
function, or build step.

## Why this is the Vercel project

The larger private Epistemos site contains application logic and local research
features. It is the wrong artifact to use as a zero-cost public portfolio. This
repository is smaller, auditable, and safe to host as static files.

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
