# Project Layers: How the Work Is Put Together

This is a map of the main projects behind the portfolio. A layer is a distinct job inside a project—not a claim that every layer is finished, production-ready, or independently hand-coded. I used AI substantially across much of this work for scaffolding, implementation help, and learning. I chose the questions, reviewed the evidence, ran or checked the experiments, and keep the limits visible.

The common pattern is:

```text
input -> mechanism -> check -> saved result -> boundary
```

## Epistemos and Instant Recall

```text
notes/files -> prose editor -> local index/retrieval -> link graph -> reliability checks
```

- **Prose editor:** text/Markdown surfaces, debounced saves, selection/scroll state, and visible conflict handling.
- **Controlled edits:** a historically tested note-edit core and a structured vault patch direction.
- **Search:** index wiring, a focused regression test, and a recorded runtime bug finding.
- **Graph:** note links can become graph data through separate builder/store/engine surfaces.
- **Vault context and provenance:** historical vault work exposed selected note context, followed outbound links, used a bounded atomic note-edit path, and recorded edit mutation envelopes. This is an evidence-carrying direction, not unrestricted agent access to notes.
- **Reliability:** atomic-write fixes and focused tests address interruption/corruption risk; they do not guarantee every path is finished.

[Epistemos](https://github.com/BlickandMorty/Epistemos) is the workspace direction. [Instant Recall](https://github.com/BlickandMorty/epistemos-instant-recall) is the separately inspectable local search companion: title/prefix scoring, BM25, deterministic trigram similarity, and weighted rank fusion. The default trigram channel is not a neural semantic model.

Inside Instant Recall, a note is split into title, heading, and paragraph chunks with content/revision identities before ranking. Search-channel results are vault-bound and fused with explicit receipts; ambient recall removes the note already open. The contract tests also reject cross-vault publication and forged chunk identity, use a local lexical fallback when a semantic asset is unavailable, and redact note/query content from diagnostics. Those are reliability and privacy constraints around retrieval, not claims that search is perfect.

The prose-editor path is also its own stack: a SwiftUI editor container and TextKit coordinator; Markdown storage, projection, and command surfaces; disk-backed body loading with debounced persistence; wikilink/title/block interaction; a provenance store plus the bounded note-edit direction; and focused editor, Markdown, provenance, layout, and benchmark tests. Historic work logged content-process crashes, while automatic recovery was explicitly left as a deferred gap. That distinction is intentional: an editor can have substantial tested machinery without being described as complete.

## Unified Address Space Reasoning Lab

```text
source records -> typed address/digest -> retrieval condition -> verifier -> ablation/result table
```

The key distinction is between keeping a record's type/identity and flattening it into loose text. A frozen flat-vs-UAS model comparison tied; a metadata-loss ablation favored the typed records only when the flat baseline had deleted the needed discriminator. That is a narrow metadata-preservation result, not a general intelligence result.

[Study repository](https://github.com/BlickandMorty/unified-address-space-reasoning-lab)

## Evidence Conflict and Scientific State Transport

```text
evidence packet -> four-state label -> activation measurement/patch -> matched controls -> held-out outcome
```

Evidence Conflict asks whether a model treats support, refutation, conflict, and unknown evidence differently. Scientific State Transport asks whether a small internal effect carries across science formats. Both preserve failures: a sparse edit did not reproduce the whole-state effect, and a longer transport replication failed after a shorter signal.

[Evidence Conflict](https://github.com/BlickandMorty/evidence-conflict-circuits) · [State Transport](https://github.com/BlickandMorty/scientific-evidence-state-transport)

## Compression-Control Reasoning

```text
full context -> lossless/lossy fixture -> control condition -> score accuracy/abstention -> fabrication and clean-context checks
```

This project does not claim to recover deleted information. The intended behavior is: check more carefully when facts remain, and correctly say “insufficient” when a necessary fact is gone. Internal-control work requires random-vector, random-layer, and clean-context controls.

[Study repository](https://github.com/BlickandMorty/compression-control-reasoning-lab)

## Dose-Response Audit

```text
synthetic curve -> ordinary/robust fit -> outlier or missing-plateau stress -> error score -> failure-mode report
```

The useful scientific lesson is that a fit can converge while its IC50 is still untrustworthy because the experiment never captured enough of the curve. Robust loss can reduce one sort of outlier damage; it cannot recreate a missing plateau.

[Study repository](https://github.com/BlickandMorty/dose-response-audit-lab)

## Proof-Carrying Policy and Interrupt Routing

```text
policy packet -> deterministic oracle or escalation rule -> model response -> receipt/replay -> dangerous-error check
```

These are synthetic defensive evaluations. The important metric is not just average accuracy: a condition that improves the average but raises unauthorized ALLOW decisions fails its safety gate. The interrupt router is the more modest idea of escalating uncertain cases rather than confidently guessing.

[Policy Evals](https://github.com/BlickandMorty/proof-carrying-policy-evals) · [Interrupt Router](https://github.com/BlickandMorty/interrupt-router-calibration-lab)

## Answer-Packet Integrity and ETHOS Eval

```text
versioned answer/prompt -> explicit validator or weighted rule -> deterministic report -> replay/diff
```

Answer-Packet Integrity checks whether receipt metadata was altered; it does not check whether a conclusion is true. ETHOS Eval makes simple behavior rules replayable from saved responses; it does not replace expert review or prove model safety.

[Answer-Packet Integrity](https://github.com/BlickandMorty/answer-packet-integrity-lab) · [ETHOS Eval](https://github.com/BlickandMorty/ethos-eval)

## Sheaf Connectome Sanity Lab

```text
planted graph -> sheaf restriction map -> Laplacian/metric -> shuffle and rewire controls -> preregistered directional test
```

The algebraic identity checked in the defined setting. The proposed positive spectral-gap/modularity direction did not: the synthetic confirmation found the opposite sign. Inverse gap was a useful diagnostic, not a retroactive rescue. This is a toy graph experiment, not a result about real brains or transformer connectomes.

[Study repository](https://github.com/BlickandMorty/sheaf-connectome-sanity-lab)

## EML-star Epistemos

```text
expression -> immutable representation -> canonical digest -> numerical/branch witness -> theorem ledger and falsifier
```

This is an attributed derivative and public learning project, not authorship of the original EML-star operator or paper. It separates executable checks, numerical evidence, analytic arguments, formal-structural statements, and open obligations. One closed grammar claim was falsified because the grammar had no input variable and could not separate points.

[Study repository](https://github.com/BlickandMorty/eml-star-epistemos)

## What I would show first

1. Epistemos plus Instant Recall, using a safe workspace visual and the search companion card.
2. UAS, showing both the model tie and the metadata-loss ablation.
3. Dose-Response, with the missing-plateau lesson.
4. State Transport, with first signal and failed confirmation together.

The rest remains public because it carries useful controls and failures. A long list of projects is not the point; a small number that can be explained, rerun, and limited honestly is.
