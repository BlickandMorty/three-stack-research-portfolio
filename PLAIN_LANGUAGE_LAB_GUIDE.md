# What am I actually looking at?

This page is the plain-language companion to the portfolio. It uses everyday comparisons to make the experiments easier to follow, but none of the comparisons mean that an AI model is literally a human brain.

## The shortest version

The research asks one practical question: **when evidence is incomplete, mixed up, or changed, can we measure what happens, make a small controlled repair, and prove that we did not break something else?**

Think of each experiment as a small game level with a score sheet:

1. Give the system a fixed set of evidence cards.
2. Change exactly one thing.
3. Measure the result with a rule written before looking at the score.
4. Compare against a control.
5. Keep the result only if it survives a second safety check.

The same discipline is useful for AI, scientific measurement, and defensive security.

## A simple map of a Transformer experiment

| Technical term | Useful everyday comparison | What it is actually doing |
|---|---|---|
| Tokens | Small cards with pieces of text | The chunks of input a language model processes. |
| Attention | A spotlight choosing which cards to look at | A mathematical weighting operation between tokens. |
| Layers | Repeated update stations | Many sequential transformations of the model state. |
| Residual stream | A shared temporary scratchpad | A vector state carried through the layers. It is not a human memory drawer. |
| Logits | A scoreboard before a move | Numerical scores for possible next tokens. |
| Activation hook / steering | A tiny, temporary nudge at one station | A controlled intervention in an internal vector during one run. It does not permanently retrain the model. |

The portfolio's circle labeled **working state** is therefore a visual aid. It does **not** say the model has a little brain area that stores a thought. It marks the shared numerical state that the experiment measures at a particular layer and time.

## The research ladder

### Level 1 — Does the outward answer change?

This is the most familiar test: give the model a task and score its answer. It is valuable, but it can hide why an answer changed.

The completed 180-cell Qwen3 0.6B baseline makes that limitation easy to see. Direct answering got `15/30` answerable full packets right but fabricated on `30/30` packets after the required fact was removed. A single frozen self-check did the opposite: `30/30` correct abstentions on lossy packets, but `0/30` on answerable full and lossless packets. It is a real result because every cell, fixture receipt, and scorer is public; it is a **failure of both procedures**, not a method to copy. See the [complete behavioral result](https://github.com/BlickandMorty/compression-control-reasoning-lab/blob/main/STAGE1_COMPLETE_RESULT.md).

### Level 2 — Did the internal working state change?

Here the output can be held aside and the residual stream can be measured directly. In the [Compression-Control Reasoning Lab](https://github.com/BlickandMorty/compression-control-reasoning-lab), 30 matched Qwen3 0.6B runs compared two edits:

- Remove an irrelevant fact.
- Remove the decisive assignment fact.

The decisive-fact removal made the final residual state less similar to the full-context state: `0.990804` versus `0.998421`, a preregistered gap of `+0.007617`.

That is evidence that this small model's measured state was more sensitive to the missing decisive fact in this controlled task. It is **not** evidence of recovered memory, better answers, general self-correction, consciousness, emotion, or valence.

### Level 3 — Can a small nudge move the state in a chosen direction?

The next step is like placing a small guide rail at one update station. The experiment copies a chosen difference vector into one residual-stream hook during a single run, then compares it with a random-direction control.

The first residual-repair study is intentionally still public as a failure: it improved the target geometry by `+0.004056`, but its clean-state drop was `0.001357`, worse than the pre-set `0.001` cap. The result did not earn the claim.

An independent v2 used a fresh 48-case fixture. It chose a scale only on development cases, then tested 24 held-out cases. It improved target geometry by `+0.002557`, beat the random control by `+0.002673`, and kept clean-state drop at `0.000441`, under the cap.

This earns one narrow statement: **under this fixture and metric, a development-selected residual nudge moved latent geometry in the intended direction while passing the stated clean-state gate.** The result must still be replicated on new task families before it supports anything broader.

## UAS: the “right folder” experiment

Unified Address Space (UAS) is best understood as a library-card system. Instead of throwing every item into one pile, each item gets a stable address and type: for example, science observation, AI-evaluation note, or safe security trace.

In the [Unified Address Space Reasoning Lab](https://github.com/BlickandMorty/unified-address-space-reasoning-lab), a synthetic type-confusion control asked for a target whose name was easy to confuse with another domain:

- Flat ranker: target retrieval `0 / 90`; contamination `90 / 90`.
- Typed UAS: target retrieval `90 / 90`; contamination `0 / 90`.

That proves a limited retrieval-policy result: preserving the requested type prevents the deliberately created type mix-up. It does not prove that UAS makes a model generally smarter. A separate 24-case local-model follow-up tied at `24 / 24` in both conditions, and that null stays part of the record.

## Answer packets: the “lab report receipt” experiment

An answer packet is a structured receipt attached to an answer: it says what evidence was used, which version produced it, and how to replay the evaluation. The [Answer-Packet Integrity Lab](https://github.com/BlickandMorty/answer-packet-integrity-lab) accepted 90 valid frozen packets and rejected 540 one-rule tamper cases.

This is like checking that a lab report has not lost its sample ID, units, or chain-of-custody line. It checks declared packet integrity—not whether the underlying claim is true and not whether a full production system is secure.

## What the plus, minus, and question marks mean

| Mark | Meaning | It does not mean |
|---|---|---|
| `+` | A measured move in the predeclared desired direction | The model became broadly intelligent, safe, or conscious. |
| `−` | A regression, missing fact, wrong type, or failed safety gate | The whole research program failed. Failures are useful map boundaries. |
| `?` | A question that still needs a better test | A hidden positive result. |

## Three stacks, one habit

- **AI internals:** inspect the working state, then test an intervention instead of trusting a story about it.
- **Science:** freeze controls and quantify uncertainty so a clean-looking curve cannot hide a broken measurement.
- **Defensive security:** require a receipt and an explicit policy test so a later instruction cannot silently claim more authority.

The common habit is: *make the system show its work, then test the part most likely to be misleading.*

## Where to start studying

1. Read this guide while looking at the portfolio's research-map panel.
2. Read the [UAS result and its null follow-up](https://github.com/BlickandMorty/unified-address-space-reasoning-lab).
3. Read the [answer-packet validator](https://github.com/BlickandMorty/answer-packet-integrity-lab).
4. Read the [compression audit and v1/v2 intervention results](https://github.com/BlickandMorty/compression-control-reasoning-lab).
5. Use the [research atlas](RESEARCH_ATLAS.md) for the full project list and boundaries.

Every repository should be read in this order: **question → fixed test → control → result → boundary → next test**. If one of those is missing, treat the headline as an unfinished lead rather than a finished finding.
