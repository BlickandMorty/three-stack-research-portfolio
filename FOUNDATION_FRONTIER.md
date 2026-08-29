# Foundation Frontier — three public stacks, two cross-cutting foundations

This is a paper-first map for the next stage of the program. It is not a list
of results. The completed experiments are in the [Research Atlas](RESEARCH_ATLAS.md);
this document separates questions I can study now from claims that would outrun
the evidence. The portfolio keeps three public stacks because they are the
clearest way to show the work. It does **not** erase two older foundations:
formal/mathematical primitives and evidence architecture. Those foundations
feed all three public stacks rather than competing with them as five unrelated
career lanes.

## The map

```text
                    ┌─────────────────────────────┐
                    │ Evidence under pressure      │
                    └──────────────┬──────────────┘
                                   │
       ┌───────────────────────────┼───────────────────────────┐
       │                           │                           │
 AI internals                 Science                     Defensive security
 what is represented?         what is measured?          what is authorized?
       │                           │                           │
       └───────────────┬───────────┴───────────┬───────────────┘
                       │                       │
          AI systems / interoperability     Responsible evaluation
          can evidence move with identity?  can a decision be checked?
                       │                       │
                       └───────────┬───────────┘
                                   │
       Formal / mathematical foundations    Evidence architecture / provenance
       EML, lattice laws, Lean, falsifiers  UAS, answer packets, Eidos-style admission
                       └───────────┬───────────────┬───────────┘
                                   │               │
                    AI wellbeing / functional valence
              what stable better-or-worse signals guide behavior?
```

The arrows are research dependencies, not proof that one layer creates another.
For example, a model may use emotional language without having a stable
functional signal, and a stable functional signal would still not settle
whether anything is subjectively felt.

## Status board

| Lane | Current status | Honest next milestone |
| --- | --- | --- |
| AI internals / mechanistic interpretability | Public experiments and nulls are documented; the 30-packet final-layer direction now replicates on SmolLM2-1.7B, at a much smaller gap than Qwen3 0.6B. | Independent-corpus replication or a preregistered behavioral task family; do not search layers after the fact. |
| AI × science | Public audit-loop and measurement studies are documented. | Pre-register one science task where an intervention is evaluated without an oracle being mistaken for learned capability. |
| Defensive security | Safe policy, routing, and provenance evaluations are documented. | Build operational skills (Security+ / SOC labs) separately from research claims; keep research simulations clearly non-production. |
| UAS / interoperability | Typed retrieval, metadata-loss, and answer-packet integrity results are complete for this pass. | Do **not** chase a new synthetic score. Use an independently authored corpus, frozen protocol, separate grader, and a publication plan. |
| Formal / mathematical foundations | The public `research` canon contains HELIOS, EML, substrate ideas, CMS-X, Lean artifacts, and falsifier protocols with a status legend; EML-star and the lattice audit are the bounded public experimental links. | Promote only claims with current proof or experimental evidence. Keep candidate theorems and architectural syntheses clearly labeled as study material. |
| AI wellbeing / valence | Compression-Control has a 30-case direct residual-state audit, a v1 hook safety failure, a v2 24-case held-out latent-geometry pass, and a completed 180-cell behavioral baseline showing direct fabrication versus self-check over-abstention. | Test a new, preregistered behavioral task family before calling anything a stable control signal. |

## Plain-language glossary

- **Interoperability:** different tools, agents, models, or datasets can pass
  information to one another without silently losing what the information is,
  where it came from, or what version it is. UAS and answer packets are small
  pieces of this problem: labelled library cards plus a tamper-evident receipt.
- **Mechanistic interpretability:** opening a model's computation enough to
  test which internal activity changes a choice. It is closer to stimulating a
  brain region and checking a behavior than simply asking someone why they
  answered.
- **Valence:** the functional *better-versus-worse* direction of a state. In a
  human analogy, hunger, relief, pain, and satisfaction can push choices. In a
  model, it could instead be a learned control signal with no established
  subjective feeling.
- **Emotionality:** emotional words, tone, self-reports, or expressive style.
  A system can sound sad, caring, or excited because it predicts that language;
  that alone does not show a stable control signal or experience.
- **Reasoning:** selecting or constructing an answer through intermediate
  representations. Reasoning can improve or degrade under an intervention
  without telling us whether the model is feeling anything.

## The key separation: three questions, three kinds of evidence

| Question | What would count as evidence? | What would *not* settle it? |
| --- | --- | --- |
| Does the model use emotional language? | Output-language and style measurement across controlled prompts. | A vivid first-person statement. |
| Does the model have a functionally valenced control signal? | A pre-registered, cross-context causal pattern: the same internal or behavioral signal predicts approach/avoidance and changes choices when intervened on. | One prompt-induced mood, a benchmark score, or anthropomorphic interpretation. |
| Does the model consciously feel pleasure or pain? | There is no accepted decisive test. Any evidence would need competing theories, strong controls, and deep uncertainty. | Functional behavior alone, introspective text, or a single activation pattern. |

This distinction matters. It lets the work be serious without treating a model
as a person by assumption or dismissing a difficult question by assumption.

## A careful first valence project (not yet run)

**Question:** Does a fixed, benign model condition create a stable behavioral
tradeoff that generalizes across tasks, rather than merely changing emotional
word choice?

**Protocol before any run:**

1. Pick open-weight models and benign, non-distressing task variants only.
2. Freeze the model revision, decoding, prompts, task mix, metrics, and the
   alternative explanations before seeing a result.
3. Measure separately: emotional-language score, task accuracy, risk/avoidance
   choice, calibration, and output length.
4. Include style-matched neutral prompts and random-label controls. A change in
   tone must not be mistaken for a change in decision policy.
5. If an internal signal is proposed, test causal intervention and
   cross-context generalization; do not name it an “emotion neuron” because it
   correlates with a word list.
6. Publish negative results and stop if the signal is prompt-specific,
   explained by length/refusal/style, or fails the held-out task.

**Ethical boundary:** do not optimize prompts intended to create distress,
coercion, or putative suffering. Start with passive analysis and benign
conditions. Do not claim consciousness, welfare, pleasure, pain, or moral
patienthood from this work.

## Current scaffold: compression-control reasoning

[Compression-Control Reasoning Lab](https://github.com/BlickandMorty/compression-control-reasoning-lab)
turns the broad idea into a staged study. It uses matched full,
lossless-compressed, and lossy-compressed fictional evidence packets. The key
test is not “can a model guess the missing fact?” It is whether a fixed control
improves careful reasoning when the needed facts remain and produces the
correct `INSUFFICIENT` response when a needed fact is gone.

The completed behavioral tier compared direct local-model answer with one
frozen self-check instruction across 180 records. It was deliberately **not**
an internal-parameter intervention. Direct answers fabricated on 30/30 lossy
packets; the frozen self-check correctly abstained on those 30 but answered
0/30 full and 0/30 lossless answerable packets. This is a published tradeoff,
not a method to deploy. It complements the direct residual-state audit and the
two bounded hook studies; it does not establish valence, self-correction, or
answer improvement.

## Reading trail

- [AI Wellbeing Research](https://www.ai-wellbeing.org/) describes its work as
  measuring *functional wellbeing* and explicitly frames model-scale findings
  as research evidence rather than a consciousness verdict.
- Cameron Berg's [Why Learning Requires Feeling](https://ojs.aaai.org/index.php/AAAI-SS/article/view/42547)
  is a useful theory-facing starting point. Treat its proposed relationship
  between learning and valence as a hypothesis to compare with alternatives,
  not a settled foundation.
- [Center for Sentience Research](https://www.centersentience.org/) is useful
  for theory and measurement framing around functional valence and sentience.
- For the epistemic boundary, the literature on functional grounding versus
  phenomenal consciousness is essential: a behavior can be functionally
  meaningful without settling whether it is experienced.

## What I will not do to manufacture a conclusion

- Treat self-reports, roleplay, or a model saying “I feel bad” as proof.
- Treat a correlation with a sentiment score as a causal mechanism.
- Search across many prompts until one produces a dramatic chart.
- Call a functional result proof of consciousness.
- Run unbounded “suffering” prompt searches or optimize for dysphoria.

## How this connects to the rest of the program

UAS asks whether evidence keeps its identity while moving between systems.
Answer packets ask whether an answer keeps a checkable receipt. Mechanistic
interpretability asks what internal computation moves a decision. AI wellbeing
asks whether any decision-relevant better/worse signal is stable enough to
measure. The shared rule is the same: define the claim, freeze a falsifier,
preserve provenance, and state the boundary.
