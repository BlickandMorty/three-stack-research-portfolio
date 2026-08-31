# Selected Project Atlas

This page is the public study map for the work I am ready to discuss. I use AI heavily for implementation and documentation. My part is choosing the problem, shaping the constraints, running the work, checking failures, and learning enough to explain what happened and what the result does not prove.

I deliberately keep the public list small. Supporting experiments, theorem notes, abandoned directions, and code I cannot yet explain well remain private.

## 1. Epistemos

**Question:** Can notes, retrieval, evidence, editing, and AI assistance live in one research workspace without giving the model uncontrolled access to everything?

**What exists:** A large macOS development project with visible app surfaces, local retrieval work, evidence and editing workflows, and separate experimental areas.

**My role:** I chose the product direction, shaped the research workflow, ran and inspected the app, and reviewed development. AI assistance is substantial. I am still learning the deeper Swift, Rust, and TypeScript implementation.

**Plain version:** The app is meant to be the desk, filing cabinet, search system, and research assistant in one place. The assistant should only receive the drawer of information needed for the current task.

**Limit:** It is still in development. A design document or screenshot does not prove that every planned feature is complete.

[Open Epistemos](https://github.com/BlickandMorty/Epistemos)

## 2. Instant Recall

**Question:** Can local search combine exact words, titles, and fuzzy text matching while keeping the ranking inspectable?

**What exists:** A Rust search companion using BM25, title and prefix scoring, trigram similarity, and weighted rank fusion.

**Plain version:** Instead of saying “AI understood the meaning,” the program keeps a visible scorecard showing why a note was retrieved.

**Limit:** Trigram similarity and weighted ranking are retrieval tools, not human understanding.

[Open Instant Recall](https://github.com/BlickandMorty/epistemos-instant-recall)

## 3. LivingBrain

**Question:** What happens if an agent memory can weaken, strengthen after use, surface contradictions, and turn successful procedures into reusable skills?

**What exists:** An AI-assisted Rust library exploring decay, reinforcement, contradiction handling, tiered retrieval, and skill records.

**Plain version:** A normal database treats an old note and a new note the same unless somebody changes them. LivingBrain experiments with memory behaving more like a garden: useful paths get reinforced, neglected material fades, and contradictions are shown instead of silently overwritten.

**Limit:** The brain language is an analogy. This is not neuroscience, consciousness, emotion, or a recreation of biological memory.

[Open LivingBrain](https://github.com/BlickandMorty/LivingBrain)

## 4. Scientific Reasoning Audit Loops

**Question:** Does asking a small open-weight model to check its work improve controlled science answers? Does a narrow verifier repair mistakes more safely?

**Method:** Qwen3 1.7B answered deterministic chemistry, physics, and biology multiple-choice problems under three conditions: direct answer, intrinsic self-audit, and verifier-gated feedback. Development cases were used to repair the measurement interface; held-out cases were then run once.

**First held-out result:**

| Condition | Accuracy | Change from direct | Wrong to right | Right to wrong |
| --- | ---: | ---: | ---: | ---: |
| Direct | 44/72 (61.1%) | - | - | - |
| Intrinsic audit | 57/72 (79.2%) | +18.1 points | 16 | 3 |
| Verifier-gated | 55/72 (76.4%) | +15.3 points | 11 | 0 |

A separate label-balanced replication again improved over direct answering, with the verifier-gated condition reaching 81.9% and recording no direct-correct regressions.

**Plain version:** One student checks every answer again. Another only receives a small error label when a calculator-like check finds a mistake. The first catches more mistakes but can second-guess correct work; the second is narrower and safer by design.

**Limit:** The verifier has privileged knowledge of whether the initial choice is wrong. This is controlled inference-time help, not model training or proof of general scientific intelligence.

[Open Scientific Reasoning Audit Loops](https://github.com/BlickandMorty/scientific-reasoning-audit-loops)

## 5. Unified Address Space Reasoning Lab

**Question:** Does giving different kinds of evidence stable typed addresses reduce cross-domain retrieval mistakes compared with mixing everything into one flat text pool?

**Results kept together:**

- A deterministic synthetic retrieval test produced 90/90 wrong-type results for a deliberately confused flat baseline and 90/90 target retrieval for typed UAS.
- A first 24-case Qwen3 4B comparison tied at 24/24 in both conditions. The planned improvement did not appear.
- A different metadata-loss ablation scored 8/24 when type information was removed and 24/24 when typed addresses preserved it; wrong-domain answers fell from 16 to 0.

**Plain version:** A library can put every book in one pile or keep science, security, and evaluation records on labeled shelves. Labels help when the alternative has thrown away the label. They do not automatically make a strong reader smarter.

**Limit:** The positive ablation has a narrow interpretation. It does not establish a general reasoning advantage, factual truth, or a production AI memory architecture.

[Open Unified Address Space Reasoning Lab](https://github.com/BlickandMorty/unified-address-space-reasoning-lab)

## 6. DataSight

**Question:** Can a beginner-friendly tool turn a CSV into a review list instead of silently “cleaning” data?

**What exists:** Python checks for missing values, likely outliers, schema risks, and reviewable explanations, with setup instructions and a small test suite.

**Plain version:** It is a first-pass inspection sheet. It points at cells or columns worth checking; the person still decides whether they are actually wrong.

**Limit:** Statistical unusualness is not the same as an error, and an AI explanation is not proof.

[Open DataSight](https://github.com/BlickandMorty/DataSight-AI)

## 7. Security Operations Lab

**Question:** Can I build entry-level security investigation habits using only systems I own and reports I can explain?

**What exists:** A controlled loopback Wireshark/TShark investigation, an authorized localhost Nmap service review, Windows records, and written reporting templates.

**Plain version:** I captured traffic from my own computer, followed the connection from start to finish, compared a scanner result with Windows, and wrote down what the evidence did and did not show.

**Limit:** These are personal-lab exercises. They are not professional SOC employment, external monitoring, vulnerability confirmation, or penetration testing.

[Open Security Operations Lab](https://github.com/BlickandMorty/security-operations-lab)

## 8. Epistemos Prompt Lab

**Question:** Can prompts make model-assisted work less careless by requiring evidence, alternatives, falsifiers, approval boundaries, and a stopping rule?

**What exists:** Prompt patterns for research, evaluation, software work, careful editing, and tool-using agents.

**Why it belongs here:** Prompting and evaluation are areas where I have paid experience. The repository shows how I structure the work without claiming that a prompt replaces statistics, engineering review, or security authorization.

[Open Epistemos Prompt Lab](https://github.com/BlickandMorty/epistemos-prompt-lab)

## What is not public

I have additional experiments involving model internals, formal math, policy logic, compression, and graph structure. They are now private supporting work. Some contain real runs and useful failures, but publishing each one separately made my profile look broader than my current ability to defend every technical detail. The strongest ideas can return later after consolidation, independent replication, and study.
