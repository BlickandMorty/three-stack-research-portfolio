# Research release audit - v3.2

This is the stopping-point audit for the current three-stack release. A project
is counted as complete only when it has a stated question, frozen or
deterministic inputs, saved artifact, verification path, and boundary. “Done”
here means ready to study and critique, not permanently finished research.

| Requirement | Evidence | Status |
| --- | --- | --- |
| Public AI-internals results | Atlas entries, frozen fixtures, result notes, verifiers, and raw artifacts across the compression, evidence-conflict, transport, probe, and component-edit labs. | Complete for this release |
| Second-model direct replication | SmolLM2 pinned revision and SHA-256, 30 frozen cases, valid float32 artifact, preserved invalid bfloat16 artifact, and structural verifier. | Complete |
| New behavioral generalization gate | 36 frozen science-style cases; baseline, fixed v2 vector, and same-norm random control. Valid run shows universal abstention and no answerable baseline competence. | Complete non-confirmation |
| Science work | Scientific audit-loop replication and dose-response measurement-risk study with disclosed limits. | Complete for this release |
| Defensive-security work | Safe policy/routing evaluations plus authorized localhost packet and service-validation reports. | Complete for this release |
| UAS and answer-packet work | Synthetic retrieval control, local metadata ablation, tied model follow-up, packet integrity validator, and external-corpus preregistration. | Complete narrow results; generalization pending |
| Public explanation | Portfolio, research atlas, plain-language guide, foundation frontier, master study guide, and project READMEs. | Complete |
| Visual and static-site checks | Portfolio charts and research map are published; `verify_site.py` passes. | Complete |

## Completed SmolLM2 gate

The final frozen experiment for this release was a second-model replication of
the activation-compression direction. SmolLM2-1.7B used the original 30
packets and precommitted final-layer cosine statistic. It produced positive
lossless-minus-lossy deltas on 30/30 cases, mean +0.000486662. The result is a
directional replication with a smaller gap than Qwen, not a behavioral or
cross-model effect-size claim. See the linked Compression-Control repository
for the protocol, raw artifacts, verifier, and numerical-repair record.

## Deliberately not run in this release

### UAS external corpus

The next UAS claim requires an independently authored or externally sourced
corpus, separate retrieval implementation, and blind grading. Writing both the
cases and the retrieval system here would violate the point of that test. The
preregistration and contract verifier are complete; no independent result is
claimed.

### Compression behavioral generalization

The preregistered new task has now been run. It failed at task viability:
baseline, candidate, and random control all abstained on every record, leaving
0/72 answerable accuracy. This is not evidence for or against the vector.
Another task may be started only after a new preregistration shows how it will
establish answerable baseline competence before intervention; do not reuse the
geometry cases, tune after outcomes, or search layers for a better number.

### Idea shelf

Eidos evidence admission, SCOPE-Rex routing, functional valence, open-checkpoint
development, and broader canon claims remain hypotheses or study directions.
They are not public results until they have their own falsifier, frozen
protocol, and outcome artifact.

## Resume conditions

Use the continuation queue only when one of these is true:

1. An independent UAS corpus with role separation is available.
2. A new behavioral compression protocol has been explicitly preregistered.
3. A real science-provenance task has identified public sources, an outcome
   measure, and a negative-result plan.
4. A security lab has a safe, authorized scope and an evidence/reporting goal.

Until then, the correct activity is study, presentation, job preparation, and
external review of the current evidence—not unbounded experiment generation.
