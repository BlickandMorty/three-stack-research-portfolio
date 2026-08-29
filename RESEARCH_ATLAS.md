# Jordan Conley Research Atlas

This is my study map for the three-stack program: AI internals, science, and
defensive security. I keep the wins, ties, failures, and limits together. A
result is useful when another person can rerun it and see exactly what it does
not prove.

## Where to start

For a first pass, start with eight core projects: **Unified Address Space**,
**Compression-Control**, **Scientific Reasoning Audit Loops**,
**Answer-Packet Integrity**, **Dose-Response Audit**, **Proof-Carrying Policy
Evals**, **Security Operations Lab**, and **EML-star Epistemos**. The remaining
studies are still public because they carry useful controls, failed
generalizations, or technical bounds. They are supporting evidence, not extra
headline claims.

## At a glance: what each experiment actually is

| Project | Stack | Plain-language task | Current status |
| --- | --- | --- | --- |
| Scientific Reasoning Audit Loops | AI × science | Make a student check a numerical answer, then compare correction paths. | Bounded replication; verifier help is not learning. |
| Compression-Control Reasoning Lab | Direct Transformer internals | Remove one evidence card and photograph the model's shared scratchpad. | Geometry result plus behavioral tradeoff; next task family pending. |
| Evidence-Conflict Circuits | Direct Transformer internals | Copy a whole internal signal, then see whether proposed parts reproduce it. | Whole-state effect; sparse explanation failed. |
| Scientific Evidence-State Transport | AI × science | Try carrying a short-form signal through a longer problem. | Short result; longer replication failed. |
| Representation-Causality Gap | AI internals | Read a state versus prove it controls an action. | Readout generalizes partly; causality remains separate. |
| Component-Edit Bound | AI safety | Nudge one component and inspect collateral effects. | Narrow locality envelope passed. |
| Dose-Response Audit | Science | Fit a curve with missing ends or a biased control. | Synthetic measurement-risk map. |
| Proof-Carrying Policy Evals | Security | Ask a guard to attach a checkable receipt to a door decision. | Dangerous ALLOWs rose; failed safety gate. |
| Lattice State Consistency | Formal security | Merge checklists and test which rules remain valid. | Exact finite result. |
| Interrupt Router Calibration | AI × security | Let a junior analyst escalate uncertain cases. | Fewer dangerous ALLOWs; weak base classifier. |
| Security Operations Lab | Defensive security operations | Trace one self-owned localhost transaction, then validate one local service scan. | Two sanitized, authorized lab reports. |
| EML-star Epistemos | Math | Check whether an old map even has coordinates. | Broad density claim falsified. |
| UAS Reasoning Lab | AI systems × science × security | Keep every evidence page in the right labeled folder. | Narrow results; independent-corpus study preregistered. |
| Answer-Packet Integrity Lab | Provenance | Check whether a receipt silently lost a required field. | Exact integrity result, not truth. |

## First, the human-brain translation

These are analogies, not claims that a transformer is a literal human brain.

- **Tokens** are the words or sensory fragments currently on a workbench.
- **Residual stream** is like a shared scratchpad passing through many brain
  areas; every layer can add or revise a note.
- **Attention** is a moving spotlight deciding which earlier notes matter now.
- **Activation patching** is like temporarily copying a signal from one brain
  scan into another trial to test whether it caused a choice.
- **Sparse feature / SAE** is like a tentative detector channel: perhaps a
  pattern such as “conflicting evidence” rather than a single named neuron.
- **Logit** is a model’s pre-decision score: a contestant’s scorecard before
  the final answer is chosen.
- **Retrieval** is opening the right folder from memory; UAS asks that every
  folder keep its identity tag instead of becoming loose pages in one pile.

## How to read any result

1. What was frozen before the result?
2. What changed, and what stayed matched?
3. Which comparison or control could have killed the claim?
4. What number moved?
5. What does that number still not prove?

## AI internals and AI × science

### Scientific Reasoning Audit Loops

- **Question:** Can an inference-time audit improve a model’s short numerical
  science answers without breaking answers that were already right?
- **Experiment:** Qwen3 answered frozen chemistry, physics, and biology cases
  directly, with an intrinsic self-audit, and with a ground-truth-gated
  verifier.
- **Result:** The public balanced replication went 62.5% direct → 75.0%
  intrinsic → 81.9% verifier-gated; the verifier made 14 repairs and preserved
  all initially correct cases by design.
- **Brain analogy:** Ask a student for an answer, then make them check their
  work. The verifier is a teacher with the answer key, so it is safer but not
  proof the student learned the subject.
- **Limit:** It is inference scaffolding, not model training or independent
  scientific discovery.
- **Study:** [repo](https://github.com/BlickandMorty/scientific-reasoning-audit-loops)

### Compression-Control Reasoning Lab

- **Question:** When a packet loses one fact, does a direct Transformer state
  react differently when that fact is decisive rather than irrelevant?
- **Experiment:** Qwen3 0.6B was run locally through Transformers with thinking
  disabled in the chat template. On 30 matched full/lossless/lossy packets, I
  compared final residual-stream cosine similarity to the matched full state;
  no answer was generated for this activation audit.
- **Result:** The precommitted final-layer comparison was 0.998421 after an
  irrelevant deletion and 0.990804 after a decisive deletion, a +0.007617
  lossless-minus-lossy gap. A fresh held-out residual hook then shifted lossy
  states toward full-context geometry by +0.004056 and beat a same-norm random
  vector by +0.004792, but failed its clean-context safety gate (0.001357 drop;
  cap 0.001). A separate 48-case independent v2 fixture then selected scale on
  development cases only and passed the 24-case held-out geometry gate:
  +0.002557 over baseline, +0.002673 over random, and 0.000441 clean drop.
  The completed 180-cell frozen behavioral baseline made that early tradeoff
  unambiguous: direct answers fabricated on 30/30 lossy packets, while the
  frozen self-check abstained correctly on 30/30 lossy packets but answered
  0/30 full and 0/30 lossless answerable packets.
- **Brain analogy:** Compare a person's shared mental scratchpad after crossing
  out a footer detail versus the actual rule needed to solve a problem. The
  second change moves the scratchpad more, even if the person still answers
  badly.
- **Limit:** The state-sensitivity and v2 hook result are not accuracy, memory
  recovery, answer improvement, a permanent parameter update, general causal
  control, valence, or consciousness. v1 failed its overall gate; v2 passes
  only a narrow latent-geometry gate.
- **Study:** [repo](https://github.com/BlickandMorty/compression-control-reasoning-lab)

### Evidence-Conflict Circuits

- **Question:** Is there a causal internal state related to support,
  refutation, conflict, and unknown evidence?
- **Experiment:** I used a four-valued evidence task, residual-stream patching,
  and sparse-feature interventions on open Qwen models.
- **Result:** A 48-pair residual patch shifted the conflict logit, but a sparse
  eight-feature edit failed to reproduce the full-state effect. A later
  32-packet prompt ledger tied direct classification at 15/32.
- **Brain analogy:** A whole-area stimulation changes a choice, but picking a
  few individual cells does not reproduce it. That means the first effect is
  real enough to investigate, not that those few cells are “the conflict
  circuit.”
- **Limit:** Causal state effect ≠ identified sparse circuit.
- **Study:** [repo](https://github.com/BlickandMorty/evidence-conflict-circuits)

### Scientific Evidence-State Transport

- **Question:** Does a layer-20 internal patch carry evidence state across
  science reasoning formats?
- **Experiment:** A frozen short numeric-pair patch was tested, then a longer
  chain preregistered replication was run separately.
- **Result:** The short patch kept its sign on 31/36 pairs; the longer-chain
  replication failed.
- **Brain analogy:** A signal transfer works for short flashcards but breaks
  when the person must carry the idea through a longer proof.
- **Limit:** Do not call it robust, layer-specific, or general transport.
- **Study:** [repo](https://github.com/BlickandMorty/scientific-evidence-state-transport)

### Representation–Causality Gap Audit

- **Question:** Does being able to read a concept from an activation mean that
  activation causes the behavior?
- **Experiment:** Linear probes were trained across source, Quill, and Mosaic
  formats and compared with model-head behavior.
- **Result:** A multiformat probe reached 79.2% on held-out Mosaic, while the
  model head reached 49.2%; the REFUTED class stayed only 50% accurate.
- **Brain analogy:** A brain scan can tell which picture someone saw without
  proving that the scanned spot made them choose it.
- **Limit:** Readability (decodability) ≠ control (causality).
- **Study:** [repo](https://github.com/BlickandMorty/representation-causality-gap-audit)

### Component-Edit Bound Audit

- **Question:** Can a bounded model-component edit stay local instead of
  damaging unrelated behavior?
- **Experiment:** A frozen transcoder-hook locality envelope was evaluated on
  87 held-out prompts with random and development controls retained.
- **Result:** Two violations; no eligible perplexity drift above 1.0.
- **Brain analogy:** A careful local stimulation mostly leaves the rest of the
  person’s abilities unchanged; “mostly” is a measured bound, not a guarantee.
- **Limit:** It is not a universal parameter-edit theorem.
- **Study:** [repo](https://github.com/BlickandMorty/component-edit-bound-audit)

### Sheaf Connectome Sanity Lab

- **Question:** Does a graph pattern claimed in the canon survive an exact
  synthetic sanity check?
- **Experiment:** I tested 360 held-out planted graphs, then compared the
  observed relationship with label shuffles and degree-preserving rewires.
- **Result:** The identity check passed, but the claimed positive
  spectral-gap/modularity relationship reversed to rho = -0.972; controls
  collapsed close to zero.
- **Brain analogy:** Before claiming a brain-network rule applies in nature,
  build a small toy nervous system where you know the wiring and see whether
  the claimed rule even points in the right direction.
- **Limit:** A planted synthetic graph is not a transformer, a biological
  connectome, or a production network.
- **Study:** [repo](https://github.com/BlickandMorty/sheaf-connectome-sanity-lab)

## Science and measurement

### Dose-Response Audit Lab

- **Question:** How much can an incomplete curve or wrong fixed control corrupt
  an IC50 estimate?
- **Experiment:** Frozen Monte Carlo curve sweeps separate robust fitting from
  structural identifiability.
- **Result:** Missing plateaus produced 69–74% twofold error; a 40-unit fixed
  control bias produced about 54% twofold error across 400 curves/condition.
- **Brain analogy:** It is like trying to judge someone’s sprint speed after
  seeing only their warm-up and not their full run.
- **Limit:** Synthetic curve maps are not laboratory biology.
- **Study:** [repo](https://github.com/BlickandMorty/dose-response-audit-lab)

## Security and formal safety

### Proof-Carrying Policy Evals

- **Question:** Can an answer carry a checkable reason for ALLOW, DENY, or
  ESCALATE?
- **Experiment:** A deterministic policy oracle and canonical receipts were
  evaluated under paraphrase and surface changes.
- **Result:** A certificate condition improved accuracy 40.3%→59.7% but
  increased unauthorized ALLOWs from 3 to 6, failing the safety gate.
- **Brain analogy:** A guard writes down why they opened a door. More correct
  decisions overall still fail if the dangerous doors become easier to open.
- **Limit:** Average accuracy cannot hide a dangerous error class.
- **Study:** [repo](https://github.com/BlickandMorty/proof-carrying-policy-evals)

### Security Operations Lab

- **Question:** Can I collect and report simple network evidence without
  overstating what a lab capture or scanner proves?
- **Experiment:** In a self-owned localhost-only scope, I captured one TCP and
  HTTP transaction with Wireshark/TShark, then ran an authorized Nmap service
  check and compared it with native Windows listener and service data.
- **Result:** The capture contains 13 frames showing the expected TCP
  handshake, HTTP `GET` / `200`, and orderly FIN/ACK close. Nmap's localhost
  observations were manually checked against Windows data instead of being
  treated as a vulnerability finding.
- **Human analogy:** Check a door's hinge and latch in your own house, then
  write down exactly what moved. It does not tell you that every door in the
  neighborhood is secure or insecure.
- **Limit:** Two authorized personal-lab reports are not enterprise SOC
  monitoring, forensic investigation, incident response, or penetration
  testing.
- **Study:** [repo](https://github.com/BlickandMorty/security-operations-lab)

### Lattice State Consistency Lab

- **Question:** Which rule grammars stay stable when authorization state is
  merged or intersected?
- **Experiment:** Exhaustive finite lattice and migration checks, then an
  84-rule atlas.
- **Result:** All-of rules were closed under both operations; any-of was
  join-only, at-most-one was meet-only, and exactly-one was neither.
- **Brain analogy:** Combining two checklists is safe only for certain kinds of
  checklist rules; “exactly one key” is fragile when lists are merged.
- **Limit:** Exact finite grammar result, not arbitrary production policy.
- **Study:** [repo](https://github.com/BlickandMorty/lattice-state-consistency-lab)

### Interrupt Router Calibration Lab

- **Question:** Can a model output router ask for escalation when uncertain and
  lower dangerous ALLOWs?
- **Experiment:** A frozen logit-margin fallback was tested on 108 prompts.
- **Result:** Unauthorized ALLOWs fell 4→1 at a 24.1% interrupt rate; accuracy
  stayed 38.9%.
- **Brain analogy:** A junior analyst learns to ask a supervisor rather than
  confidently guess in some hard cases.
- **Limit:** The base classifier is weak and this is not an attention change.
- **Study:** [repo](https://github.com/BlickandMorty/interrupt-router-calibration-lab)

## Math, structure, and the Unified Address Space

### EML-star Epistemos

- **Question:** Did an older elementary-math grammar actually satisfy the
  assumptions needed for its density claim?
- **Experiment:** Structural proof plus an executable 677-term audit.
- **Result:** The closed grammar had no input variable, so its terms were
  constant and could not separate points; the broad density claim was falsified.
- **Brain analogy:** You cannot claim a map describes a city if the map has no
  coordinate for where anything is.
- **Limit:** Adding a variable repairs one issue, not every theorem condition.
- **Study:** [repo](https://github.com/BlickandMorty/eml-star-epistemos)

### Unified Address Space Reasoning Lab

- **Question:** Does preserving identity and type prevent evidence from being
  mixed up across science, security, and evaluation work?
- **Experiment 1:** A 90-query synthetic retrieval type-confusion control.
- **Result 1:** Flat lexical ranking returned the wrong type 90/90; typed UAS
  retrieval found the target 90/90.
- **Experiment 2:** Qwen3 4B saw flat versus UAS evidence on 24 cases.
- **Result 2:** A tie: 24/24 in both conditions. This is a real
  non-confirmation.
- **Experiment 3:** A metadata-loss ablation removed record type in flat text
  but retained it in UAS addresses.
- **Result 3:** Flat 8/24 with 16 wrong-domain answers; UAS 24/24 with 0.
- **Brain analogy:** UAS is a hospital records system where every page keeps a
  patient ID, department, revision, and chain of custody. A flat text pile can
  contain the right page but lose whose chart it belongs to.
- **Limit:** The ablation proves that keeping needed type metadata matters when
  the baseline erases it; it is not general intelligence.
- **Next:** An [independent-corpus preregistration](https://github.com/BlickandMorty/unified-address-space-reasoning-lab/blob/main/EXTERNAL_CORPUS_PREREGISTRATION.md)
  now requires public third-party source receipts, a frozen retrieval hash,
  separate case-author and blind-grader roles, and no result until that
  contract is met.
- **Study:** [repo](https://github.com/BlickandMorty/unified-address-space-reasoning-lab)

### Answer-Packet Integrity Lab

- **Question:** Can an answer expose a receipt that detects altered schema,
  type, evidence link, fallback label, or replay material?
- **Experiment:** 90 valid synthetic packets and 540 one-rule tamper cases.
- **Result:** The validator accepted all valid packets and rejected all
  tampered packets.
- **Brain analogy:** A lab report has a sample ID, method, chain of custody,
  and checksum. It can be internally intact yet still contain a wrong scientific
  conclusion.
- **Limit:** Integrity is not factual truth or deployed-system security.
- **Study:** [repo](https://github.com/BlickandMorty/answer-packet-integrity-lab)

## The one-sentence program

I am building an evidence discipline across model internals, scientific
measurement, and defensive security: preserve the object, test the claim,
record the failure, and do not let a clean story outrun the evidence.

## Where this pass stops

Read [Research Status and Stopping Rule](STATUS_AND_STOPPING_RULE.md). The
short version: the current public experiments are ready to study and discuss;
the next UAS study should wait for an independent corpus and grader rather than
chasing another synthetic percentage.
