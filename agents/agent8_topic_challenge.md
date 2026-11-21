# Agent 8 Challenge Report: Topic Comparability, Evaluation Validity & Methodological Feasibility Audit

**Role:** Evaluation and Metrics Specialist (Independent Topic Comparability & Methodological Feasibility Challenger)  
**Target Venues Audited Against:** ACM Computing Surveys (**CSUR**, Primary), Transactions on Machine Learning Research (**TMLR**, Backup 1), Artificial Intelligence Review (**AIRE**, Backup 2) — per [Deliverable_A_Journal_Intelligence_Report.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/deliverables/Deliverable_A_Journal_Intelligence_Report.md)  
**Primary Peer-Review Evidence Reference:** [agent4_openreview_analysis.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/agents/agent4_openreview_analysis.md)  
**Date:** November 20, 2026  

---

## 1. Executive Challenge Summary & Verdict Matrix

From an evaluation-science and statistical-comparability perspective, **most candidate LLM-MAS review topics fail if pursued naively** because primary studies in this literature suffer from severe inference-compute confounding, incompatible backbone tiers, unstandardized harness bugs, non-comparable baselines, and terminological conflation. Any topic that invites cross-study metric averaging ("Paper X got 88% vs. Paper Y got 76%") or descriptive cataloging will violate **TMLR Criterion 1** (claims–evidence parity) and **CSUR** standards against catalog-style surveys.

The table below summarizes the independent challenge verdict across all seven candidate directions `(A)–(G)`:

| Candidate Direction | Available Quantitative Metrics | Dominant Comparability Hazard | Invalid Pooling / Shallow Description Risk | Beginner / M.Tech Defensibility | **Challenge Verdict** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **(A) SAS vs. MAS Compute/Token-Matched Comparisons & When MAS Outperforms SAS** | Accuracy/EM, `pass@1`, Resolve Rate (%), tokens/task, USD cost/task, call count, $\Delta_{\text{MAS-SAS}}$, error-amplification multiplier (`17.2x` vs. `4.4x`) | **Extreme in naive studies:** unmatched `1x` SAS vs. `k×` MAS tokens; zero-shot MAS vs. weak SAS prompts; `gpt-3.5` vs. reasoning models (`o1`/`R1`); tool-access asymmetry | **Low-to-Moderate IF strictly stratified within-setting**; High if pooling raw accuracy across papers | **Very High** — clear economic & compute-parity logic | **NARROW & ACCEPT** *(Core Spine: Within-setting compute-matched comparison + conditional regime mapping)* |
| **(B) Evaluation Validity, Harness Fragility & Multi-Run Reliability (`pass^k`)** | `pass@1` vs. `pass@k` vs. `pass^k`, strict-EM delta (`100%→77.5%`), ABC relative skew (`up to 100%`), `EvalPlus` test-expansion drops, cost-Pareto | Audits inspect disparate benchmarks with different criteria; **most studies reporting `pass^k` or ABC audits target single-agent harnesses**, leaving thin MAS-only corpus | **High scope drift risk** (turns into a general single-agent eval survey already covered by *Kapoor et al.* in TMLR) | **High** for `pass^k` & cost-Pareto; **Moderate** for container/sandbox security exploits | **NARROW & REPURPOSE** *(Reject as standalone MAS review; embed as mandatory quality-appraisal & validity-gate layer)* |
| **(C) Failure Taxonomies, Error Cascades & Failure Attribution** | Failure incidence (`41%–86.7%`, $\kappa=0.88$), agent-level & step-level attribution accuracy (`~53.5%` / `~14.2%`), error amplification, diversity collapse | **Incompatible failure ontologies** (*MAST* 14 inter-agent modes vs. *AgentErrorTaxonomy* 17 intra-agent module modes); LLM-judge self-bias; single- vs. multi-agent dataset mixing | **High taxonomic cataloging risk**; young 2025–2026 standalone corpus (~10–25 core diagnostic studies) | **High** for cascade multipliers; **Low-Moderate** for counterfactual RL / subjective "decisive step" credit assignment | **NARROW & INTEGRATE** *(Weak standalone CSUR survey; indispensable mechanistic explanation layer paired with A/D)* |
| **(D) Communication Topology, Pruning & Coordination Cost/Latency Scaling** | Benchmark accuracy (`GSM8K`, `MMLU`, `HumanEval`), token reduction (`28%–95%`), USD savings, wall-clock latency, agent count $N$ scaling | **Hidden search/training cost** (MCTS/VGAE/RL cost omitted from inference savings); strawman dense-graph baselines; wall-clock vs. token divergence; static benchmarks masking sequential collapse | **High if pooling % token savings** across mismatched reference baselines; **Low** if comparing topology classes within-study | **Moderate** — topology graphs & cost intuitive; VGAE/policy-gradient/MCTS machinery denser | **NARROW & ACCEPT (INTEGRATED)** *(Merge topology axis into A; require amortization accounting & cost-matched SAS baselines)* |
| **(E) Cross-Agent Prompt Injection & Trust Boundaries** | Attack Success Rate (`ASR`), Benign Utility (`U`), Utility Under Attack (`UA`), Defense Success Rate, Collective Danger Rate | **Single-agent tool-use benchmarks** (*AgentDojo*, *InjecAgent*, *ASB*) dominate; true cross-agent setups (*Prompt Infection*, *NetSafe*, *PsySafe*) use non-comparable bespoke ASR rules; safety-alignment drift | **Very High** — risks relabeling single-agent indirect injection as MAS + descriptive attack listing + CSUR security survey overlap | **Moderate** — ASR intuitive, but cryptographic/information-flow trust boundaries require deep security rigor | **REJECT (Standalone)** *(Demote to bounded Threat/Governance sub-section)* |
| **(F) Uncertainty-Aware Delegation / Selective Single-to-Multi Escalation** | Routing cost savings (`17%–52%`), accuracy delta, token entropy/AUROC/ECE, latent escalation thresholds (*LEASH*, *SAUP*) | **Severe conflation:** single-model routers (*RouteLLM*, *FrugalGPT*) & intra-MAS routers (*MasRouter*) dominate; tiny corpus of true SAS$\to$MAS escalation; commercial API logprob opacity | **Extreme** — forces artificial pooling of model-routing, uncertainty calibration, and HITL escalation, or yields <15 genuine primary studies | **Low-Moderate** — requires calibration theory, conformal/entropy math, and bandit routing | **REJECT (Standalone)** *(Retain only as Future Research / Open Challenge)* |
| **(G) LLM Agent Swarms vs. Classical Swarm Intelligence / Classical MAS** | *SwarmBench* 5-task grid scores, PID/TDMI synergy (*Riedl 2026*), sociological counts (*Project Sid*), classical convergence/regret | **Zero shared benchmarks:** classical SI (ACO/PSO/Boids) & FIPA/BDI run in microseconds without NL; "LLM swarms" are mostly centralized NL graphs; *SwarmBench* exposes extreme latency/cost mismatch | **Maximum** — guaranteed non-comparative descriptive essay; *La Malfa et al. (NeurIPS 2025)* already claimed the position-paper space | **Deceptively easy to sound shallow**; vulnerable to classical MAS (*JAAMAS*/CSUR) referee demolition | **REJECT (Standalone)** *(Retain strictly as a 1–2 page Terminological & Scope Exclusion Gate upfront)* |

---

## 2. Cross-Cutting Benchmark & Evaluation Hazard Audit

Before auditing each candidate topic individually, any review team must confront the structural defects documented across the primary benchmarks used in LLM-MAS papers. Pooling headline percentages across these benchmarks without auditing their setup guarantees invalid conclusions:

| Benchmark | Task Domain & Evaluation Mechanism | Documented Methodological / Harness Hazards | Impact on Multi-Agent Comparisons |
| :--- | :--- | :--- | :--- |
| **GSM8K / MATH** | Static single-turn math word & competition problems; Exact Match / final numerical extraction | Heavily contaminated in pre-training corpora; **inference-compute scaling confound** (`AgenticNet` TMLR 7332 showed MATH Level 5 cost-matched performance collapsed to barely above Vanilla CoT, and negative ablation dropped MATH `96.4%→83.2%`). | Multi-agent debate/discussion gains on GSM8K often reflect $k\times$ extra test-time tokens or zero-shot prompt weakness rather than interactive coordination (*Rethinking the Bounds*; *Should We Be Going MAD?*). |
| **MMLU / HotpotQA** | Static 4-way multiple choice (57 subjects) / multi-hop QA; Accuracy / EM | Near-saturation and memorization in frontier models; rigid EM string penalties. In MAS topology papers (*G-Designer*, *ARG-Designer*), multiple-choice MMLU reduces MAS interaction to **single-turn consensus/routing**, hiding long-horizon coordination failures. | Inflates apparent effectiveness of learned DAGs and pruning methods on non-interactive tasks that do not require stateful coordination. |
| **HumanEval / MBPP (+ EvalPlus)** | Single-function Python synthesis; `pass@k` against unit tests | Severe **test-suite sparsity** in original releases; *EvalPlus* (`HumanEval+` / `MBPP+`) expanded tests by **80× / 35×**, exposing brittle edge-case failures. Extreme sensitivity to extraction/eval protocol (`AgenticNet` TMLR 7332 MBPP dropped **`100%→77.5%`** under `"strict exact-match"` rebuttal re-runs). | Cannot pool raw `HumanEval`/`MBPP` scores across papers using different extraction wrappers, test suites (`EvalPlus` vs. base), or retry budgets. |
| **SWE-bench (Lite / Verified)** | Multi-file GitHub issue resolution in repo sandboxes; unit-test Resolve Rate (%) | **Scaffold & tool asymmetry:** non-agentic deterministic pipeline *Agentless* achieves `~50.8%` Verified (`~$0.34–$0.70`/issue) vs. single-agent *OpenHands* `~$1.50–$3.50+` and multi-agent variants adding 2×–3× token cost. **ABC (`arXiv:2507.02825`)** documented insufficient test coverage; **Berkeley RDI** documented lack of isolation (agents able to inspect/tamper with evaluation logs/state in shared environments). | Multi-agent gains (`+5% to +10%`) are easily confounded with AST search access (*AutoCodeRover*), retry sampling, or test-execution loops rather than multi-agent dialogue. |
| **$\tau$-bench** | Multi-turn enterprise dialogue + backend API/DB mutation; final DB state matching + **`pass^k`** | Introduces **`pass^k`** (consistency across all $k$ independent trials), proving single-run `pass^1` overstates production reliability. However, **ABC (`arXiv:2507.02825`)** identified reward-design flaws where empty or non-committal responses could be scored as successes, skewing relative performance up to **100%**, plus reliance on LLM-simulated users. | Exposes fragility of MAS/agent reliability over multi-turn trajectories; requires auditing reward scripts and simulated-user model versions before trusting deltas. |
| **WebArena** | Self-hosted functional websites (e-commerce, forum, GitLab, CMS); end-to-end state/URL/LLM-judge checks | High execution variance from asynchronous DOM timing and site state drift; historical harness security flaws (`eval()` execution on agent strings, unsanitized LLM-judge transcript interpolation). Long horizons magnify coordination bugs between planner/navigator sub-agents. | Small leaderboard differences between single-agent and multi-agent web agents are often indistinguishable from run-to-run variance unless multi-seed variance and latency are reported. |
| **GAIA** | Multi-step generalist assistant tasks (web, files, multimodal); exact-match string answers | **Benchmark leakage** (validation sets hosted publicly on HuggingFace); rigid string/number parsing bugs (e.g., splitting `"1,500"` into list `["1","500"]` vs. scalar `"1500"`); high sensitivity to external web search tool quality and live web drift. | Confounds tool-harness quality (browser/PDF parsers) and memorization with multi-agent planning quality. |
| **ALFWorld** | Embodied household navigation mapped to symbolic text environments (TextWorld / ALFRED) | **Text-to-grounding transfer gap** (*AgentBench* ICLR 2024 `zAdUB0aCTQ` criticized stripping 2D/3D context into simplified text/code setups); text state hides perceptual ambiguity and physical timing errors. | High success rates in text-based ALFWorld cannot be generalized to embodied/multimodal multi-agent coordination. |

---

## 3. Detailed Candidate-by-Candidate Challenge Audit

### Candidate (A): Single-Agent vs. Multi-Agent Compute/Token-Matched Comparisons & When MAS Actually Outperforms SAS

#### 1. Measurable Metrics Available
Primary studies in this thread expose concrete, commensurable metrics when properly extracted:
* **Task Effectiveness:** Exact Match / Accuracy (`GSM8K`, `MATH`, `MMLU`, `ECQA`, `FOLIO-wiki`), `pass@1` / `pass@k` (`HumanEval+`, `MBPP+`), Resolve Rate (`SWE-bench Verified`), and multi-turn Task Success (`Finance-Agent`, `BrowseComp-Plus`, `PlanCraft`, `Workbench`, `Terminal-Bench`).
* **Compute & Economic Cost:** Total prompt + completion tokens per task, tokens per resolved task, USD API cost per resolved issue (e.g., *Agentless* `$0.34–$0.70` vs. *OpenHands* `$1.50–$3.50+` vs. multi-agent `2×–3×`), LLM API call count, and parallel sample count $N$ (where *More Agents Is All You Need* scales tokens linearly with $N$).
* **Conditional Delta & Regime Metrics:** Compute-matched performance delta $\Delta_{\text{MAS}-\text{SAS}}(B)$ at equal token budget $B$; baseline capability threshold (~45% SAS accuracy saturation observed in *Towards a Science of Scaling Agent Systems*, Kim et al., `arXiv:2512.08296`); task-structure splits (e.g., parallelizable *Finance-Agent* gains up to ~80% vs. sequential *PlanCraft* degradation of `39%–70%`).

#### 2. Comparability Hazard
Cross-paper comparisons in raw LLM-MAS literature are severely poisoned by **five recurring confounders**:
1. **The $1\times$ vs. $k\times$ Token-Budget Confound:** Most MAS papers compare multi-agent debate/SOPs consuming $3\times$–$15\times$ tokens against a *single-pass* SAS. When token/call budgets are matched via Self-Consistency or repeated sampling (*Should We Be Going MAD?*, Smit et al.; *TMLR Paper 7332 AgenticNet* MATH Level 5 rebuttal), MAS gains frequently vanish or turn negative.
2. **Prompt-Engineering Asymmetry:** *Rethinking the Bounds of LLM Reasoning* (Wang et al., ACL) demonstrated that multi-agent discussion outperformed SAS **only in zero-shot settings**; once strong few-shot demonstrations were given to the SAS, the advantage disappeared.
3. **Non-Monotonic Backbone Capability Drift:** Results from `gpt-3.5-turbo` (where a weak base model benefits from self-correction/voting) routinely **invert** on frontier/reasoning models (`gpt-4o`, `Claude 3.5 Sonnet`, `o1`/`R1`). Kim et al. (`arXiv:2512.08296`) documented a **capability-saturation threshold (~45% SAS accuracy)** beyond which multi-agent coordination yields diminishing or negative returns under fixed token budgets.
4. **Tool & Execution-Feedback Asymmetry:** Comparing a vanilla single LLM against a multi-agent system where a "Verifier" or "Executor" agent runs Python/bash unit tests conflates **multi-agent role splitting** with **environment execution feedback** (highlighted by *Agentless* and *AutoCodeRover* on SWE-bench).
5. **Strict Evaluation Harness Drift:** As shown in *AgenticNet* (TMLR 7332), tightening evaluation from lenient parsing to `"strict exact-match"` dropped MBPP from `100%→77.5%`, invalidating cross-paper percentage tables.

#### 3. Risk of Invalid Pooling / Shallow Description
* **If pooled naively across papers:** Extreme risk of **Simpson's paradox** and invalid meta-analysis (you cannot average a zero-shot GSM8K delta on `gpt-3.5-turbo` with a tool-use SWE-bench delta on `Claude 3.5 Sonnet`).
* **If designed with within-study stratified comparison:** **Very low risk of shallow description.** Every primary study is coded *relative to its own internal SAS baseline* along explicit stratification axes: *(i) Token-matched vs. unmatched? (ii) Strong SAS baseline (Self-Consistency / Few-Shot CoT / Agentless) vs. weak zero-shot SAS? (iii) Task structure (decomposable/parallelizable vs. sequential state-dependent)? (iv) Backbone tier?* This turns heterogeneous papers into a falsifiable audit of *when* coordination beats compute scaling.

#### 4. Beginner Comprehensibility & Defense
**Very High.** An M.Tech-level researcher can cleanly grasp and defend tokens-per-task, USD cost, compute-matched `Self-Consistency` baselines, and task-decomposability stratification without needing opaque mathematical machinery. The central argument ("most claimed MAS wins are unadjusted test-time compute effects unless tested against compute-matched SAS") is crystal clear to CSUR, TMLR, and AIRE referees.

#### 5. Challenge Verdict: **NARROW & ACCEPT (Strongest Core Spine)**
* **Required Narrowing:** Do **not** ask *"Do multi-agent systems outperform single-agent systems?"* (unanswerable globally). Frame it as: **"When Do LLM Multi-Agent Systems Outperform Compute-Matched Single-Agent Baselines? A Stratified Synthesis of Cost, Task Structure, and Evaluation Confounders."**
* **Epistemic Guardrail:** Explicitly reject calling empirical thresholds (such as Kim et al.'s ~45% saturation or 17.2×/4.4× amplification across 5 canonical architectures and 6 benchmarks) universal "causal laws." Report them strictly as **conditional empirical associations** bounded by tested model families, harnesses, and task structures.

---

### Candidate (B): Evaluation Validity, Harness Fragility & Multi-Run Reliability (`pass^k`) in Agentic/MAS Benchmarks

#### 1. Measurable Metrics Available
* **Multi-Run Consistency:** `pass@1`, `pass@k` (at least 1 success in $k$), and **`pass^k`** (all $k$ independent trials succeed, introduced in $\tau$-bench, exposing steep reliability collapse as $k$ increases).
* **Harness & Scoring Distortion Bounds:** Performance swing from strict vs. lenient matching (e.g., `100%→77.5%` in *AgenticNet*), *EvalPlus* test-expansion drop (`80×`/`35×` tests on `HumanEval+`/`MBPP+`), and **Agentic Benchmark Checklist (ABC, `arXiv:2507.02825`)** error bounds showing task/outcome-validity flaws skew relative scores by **up to 100%** (and cut overestimation by ~33% on `CVE-Bench`).
* **Joint Cost-Accuracy Frontiers:** Pareto dominance plots mapping USD API cost and token budgets against task resolution (*AI Agents That Matter*, Kapoor et al., TMLR).

#### 2. Comparability Hazard
* **Meta-Audit Heterogeneity:** Benchmark-validity studies audit different targets (`SWE-bench Verified`, $\tau$-bench, `WebArena`, `OSWorld`, `GAIA`, `CVE-Bench`, `CAR-bench`) using non-standardized failure probes (unit-test coverage analysis vs. `eval()`/LLM-judge injection vs. HuggingFace leakage checks vs. multi-seed variance).
* **Severe Single-Agent Dominance in Corpus:** Critically, the landmark evaluation-critique literature (*Kapoor et al.* TMLR, *Zhu et al.* ABC, *EvalPlus*, *SWE-bench* audits, $\tau$-bench `pass^k`) primarily evaluates **single-agent tool-use harnesses**. Very few primary *multi-agent* architecture papers report `pass^k` across $k \ge 3$ independent seeds, confidence intervals, or ABC-audited outcome validity checks.

#### 3. Risk of Invalid Pooling / Shallow Description
* **High risk of scope drift and redundancy if pitched standalone:** A standalone review of Topic B would either (a) drift into reviewing *general/single-agent* benchmark flaws—directly colliding with *Kapoor et al.* (already published in **TMLR**) and *Zhu et al. (2025)*—or (b) lack enough MAS-specific `pass^k` and harness-fragility primary studies to fill a CSUR/AIRE systematic corpus.
* **Zero risk if used as an Appraisal Rubric:** Turning Topic B into the **methodological quality-assessment tool** (analogous to Cochrane Risk-of-Bias in medical systematic reviews) used to score all included MAS studies solves the corpus problem while maximizing rigor.

#### 4. Beginner Comprehensibility & Defense
**High** for `pass@k` vs. `pass^k`, exact-match fragility, and cost-accuracy Pareto frontiers; **Moderate** for low-level systems exploits (sandbox state tampering, Python `eval()` injection, judge prompt injection).

#### 5. Challenge Verdict: **NARROW & REPURPOSE (Mandatory Methodological Quality-Audit Pillar; REJECT as Standalone MAS Survey)**
* **Actionable Guidance:** Embed Topic B's metrics (`pass^k` reporting rate, ABC task/outcome-validity checks, cost-reporting compliance, prompt-sensitivity testing) as the **Risk-of-Bias / Evaluation Validity Audit** inside a compute-matched MAS synthesis (Topic A+D), rather than attempting a standalone MAS benchmark-critique survey.

---

### Candidate (C): Failure Taxonomies, Error Cascades & Failure Attribution in LLM-MAS

#### 1. Measurable Metrics Available
* **Structural Failure Prevalence:** Annotated failure rates (`41%–86.7%` across 7 MAS frameworks and 1,600+ traces in **MAST**, NeurIPS 2025, `arXiv:2503.13657`) with human inter-annotator agreement ($\kappa = 0.88$) across 3 macro-categories: *System Design/Specification* (`~44.2%`), *Inter-Agent Misalignment* (`~32.35%`), and *Task Verification/Termination* (`~23.5%`).
* **Root-Cause Localization Metrics:** *Agent-Level Attribution Accuracy* and *Step-Level (Decisive Error Step) Accuracy* on **Who&When** (127 MAS failure logs across `GAIA` and `AssistantBench`; frontier reasoning models achieve `~53.5%` agent-level and `~14.2%` step-level precision; **AgenTracer**, ICLR 2026, reports `<10%` baseline attribution in some regimes and improves attribution up to `~18%` via counterfactual replay RL, yielding `4.8%–14.2%` downstream task gains); **AgentDebug** (`arXiv:2509.25370`) reports `step-level` and `all-correct` accuracy on *AgentErrorBench*.
* **Cascade & Conformity Metrics:** Error amplification ratios (`17.2×` independent vs. `4.4×` centralized in Kim et al.); inter-agent correlation collapse ("diversity collapse", *When Consensus Is Not Correctness*, TMLR 9844 / KDD Workshop); disagreement vs. outcome dissociation (TMLR 7253).

#### 2. Comparability Hazard
1. **Incompatible Taxonomies:** *MAST* (14 modes in 3 MAS-centric buckets), *AgentErrorTaxonomy* in *AgentDebug* (17 modes in 5 *single-agent cognitive modules*: Memory, Reflection, Planning, Action, System), and *Who&When* (`(Agent, Step)` pairs) do **not** map cleanly 1-to-1. Simply summing category counts across papers without shared trace re-coding is invalid.
2. **Intra-Agent vs. Inter-Agent Dataset Mixing:** *AgentErrorBench* derives trajectories from `ALFWorld`, `GAIA`, and `WebShop` (primarily single-agent agentic loops), whereas *MAST* and *Who&When* inspect multi-agent frameworks (*MetaGPT, ChatDev, OpenManus, Magentic-One*). Pooling them conflates single-agent planning bugs with multi-agent handoff/misalignment failures.
3. **LLM-as-a-Judge & Counterfactual Replay Circularity:** Scaling annotation via LLM judges (*MAST*) or fault injection (*AgenTracer* `TracerTraj`) introduces judge sensitivity and synthetic-vs-organic error mismatch.
4. **Root-Cause Epistemic Ambiguity:** In cyclic multi-agent dialogues, defining a single "decisive step" is often ill-posed when failure is jointly produced by an ambiguous spec (upstream) + premature termination (downstream).

#### 3. Risk of Invalid Pooling / Shallow Description
* **Moderate-to-High as a standalone survey:** The dedicated automated MAS failure-attribution literature is heavily concentrated in **2025–2026** (~10–25 focused primary studies) and risks reading like a list comparing one author's 14-category box against another author's 17-category box.
* **High analytical value as a diagnostic layer:** When linked directly to Topic A/D, Topic C explains the *mechanisms* behind compute-matched MAS failure (e.g., why independent agents amplify errors `17.2×` while centralized verification reduces it to `4.4×`, and why consensus without verification manufactures overconfidence).

#### 4. Beginner Comprehensibility & Defense
**High** for structural failure modes (`Spec`, `Misalignment`, `Verification`) and cascade amplification; **Low-to-Moderate** for counterfactual replay RL (`AgenTracer-8B`), Cohen's $\kappa$ validation protocols, and causal credit-assignment edge cases where beginners easily overclaim single-step causality.

#### 5. Challenge Verdict: **NARROW & INTEGRATE (Essential Mechanistic Sub-Pillar; Reject Standalone Full Survey)**
* **Actionable Guidance:** Narrow to **Inter-Agent Error Propagation, Conformity Collapse, and Root-Cause Attribution** as the mechanistic explanation layer supporting Topic A+D, strictly separating *intra-agent module faults* (*AgentDebug*) from *inter-agent coordination faults* (*MAST*, *Who&When*).

---

### Candidate (D): Communication Topology, Pruning & Coordination Cost/Latency Scaling

#### 1. Measurable Metrics Available
* **Task Accuracy:** Scores on `GSM8K`, `MATH`, `MMLU`, `HumanEval`, `MBPP`, `GAIA`, `Mini Crosswords` (e.g., *G-Designer* `84.50%` MMLU; *ARG-Designer* `~89.5%` MMLU, `~94.4%` GSM8K; *GPTSwarm* `0.800` Mini Crosswords, `~76%→88%` HumanEval; *MaAS* `+0.54% to +11.82%` across 6 benchmarks).
* **Token & Cost Savings:** Inference token reduction vs. static dense graphs (*AgentPrune* `28.1%–72.8%` tokens, cost `~$43→~$5.6`; *G-Designer* up to `95.33%` token drop on HumanEval; *MaAS* consuming `6%–45%` of static MAS inference cost), pruned edge density.
* **Scaling & Latency:** Wall-clock makespan (seconds), API round count, agent scale $N$ curves (*MacNet* ICLR 2025 scaling to `1,000+` agents showing accuracy plateauing alongside context accumulation and token bloat).

#### 2. Comparability Hazard
1. **Unamortized Search / Training Cost Confound (Critical!):** Automated topology frameworks (*AFlow* MCTS search, *GPTSwarm* RL edge optimization, *AgentPrune* low-rank mask training, *G-Designer* VGAE training, *MaAS* supernet controller training) routinely headline **inference-time** savings (`6%–45%` cost or `95%` token drop) while omitting or separating the **upfront search/training API cost** needed to discover/train the topology. Without break-even query counts ($Q_{\text{break-even}}$), inference savings are incomparable to zero-shot prompting baselines.
2. **Dense-Graph Strawman Baselines:** Showing `70%–95%` token savings over a naive all-to-all complete-graph debate obscures whether the pruned topology beats a **cost-matched SAS** (`Self-Consistency` / CoT) at the same final token expenditure (precisely the failure caught in *AgenticNet* TMLR 7332).
3. **Wall-Clock Latency vs. Token Count Divergence:** Parallel topologies (*More Agents*, *MoA* layers, *MacNet* parallel DAG branches) keep latency bounded by graph depth $D$ while inflating total tokens/rate-limit contention, whereas sequential SOP chains (*MetaGPT*, multi-round debate) multiply wall-clock latency linearly with turns. Many primary papers report *tokens* or *rounds* while omitting *wall-clock runtime*.
4. **Static Single-Turn Benchmarks Hide Coordination Collapse:** Testing graph pruning on `MMLU` or `GSM8K` treats communication as static ensembling/routing, masking the `39%–70%` degradation observed on sequential stateful tasks (*PlanCraft* in Kim et al.).

#### 3. Risk of Invalid Pooling / Shallow Description
* **High if pooling "% token reduction" across papers:** Because reference baselines (`Complete Graph` vs. `Chain` vs. `AutoGen` vs. `MetaGPT`), benchmarks, and backbones (`gpt-3.5-turbo-0125` vs. `gpt-4-1106-preview` vs. `gpt-4o`) vary across every study, averaging `% savings` is meaningless.
* **Low if structured around Topology Classes × Task Structure × Cost Amortization:** Comparing *Independent/Parallel*, *Sequential Chain*, *Centralized Star/Hub*, *Dense Debate*, and *Adaptive Sparse DAG* within-study—and auditing whether search cost and SAS baselines were disclosed—produces a sharp, falsifiable engineering taxonomy.

#### 4. Beginner Comprehensibility & Defense
**Moderate.** Graph topologies (Chain, Star, Tree, Complete, Sparse DAG) and token vs. wall-clock trade-offs are intuitive; however, an M.Tech researcher must carefully avoid mischaracterizing VGAE topology decoding, low-rank policy-gradient masks, or MCTS search operators, and must explicitly track *amortized vs. inference-only cost*.

#### 5. Challenge Verdict: **NARROW & ACCEPT (Best Integrated with Topic A)**
* **Actionable Guidance:** Integrate Topic D with Topic A so the review tests **both** *whether* MAS beats compute-matched SAS **and** *which communication topology/pruning regime* avoids the coordination tax—strictly separating **inference cost vs. search/training amortization cost** and **static QA/code vs. stateful sequential environments**.

---

### Candidate (E): Cross-Agent Prompt Injection & Trust Boundaries

#### 1. Measurable Metrics Available
* **Compromise / Propagation Metrics:** Attack Success Rate (`ASR`, e.g., *AgentDojo* undefended GPT-4o `~28%–42%` overall, `76%–80%` on Slack suite; `0%` under strict tool firewalls; *Prompt Infection* viral payload spread; *NetSafe* topological compromise; *Flooding Spread of Manipulated Knowledge* belief-flip ASR); *Agent Security Bench (ASB)* 7–8 metrics including *Utility-Security Balance*; *PsySafe* dark-trait scores and *Collective Dangerous Behavior Rate*.
* **Utility Trade-Off Metrics:** Benign Utility (`U`) and Utility Under Attack (`UA`).

#### 2. Comparability Hazard
1. **Single-Agent Tool-Use Disguised as Multi-Agent Trust:** The largest, cleanest benchmarks (*AgentDojo* NeurIPS 2024, *InjecAgent* ACL 2024, *WASP*, *ASB*) overwhelmingly evaluate **single-agent indirect prompt injection** (poisoned tool outputs/emails/Slack messages hijacking one agent). Genuine *inter-agent* trust-boundary studies (*Prompt Infection*, *NetSafe*, *Flooding Spread*, *PsySafe*) rely on fragmented, bespoke simulated graphs with incompatible threat models.
2. **Incommensurable ASR Definitions:** `ASR` denotes unauthorized state-mutating API calls in *AgentDojo*, QA accuracy degradation under poisoned peer beliefs in *Flooding Spread*, viral instruction replication in *Prompt Infection*, and psychological/roleplay harm scores in *PsySafe*. Pooling ASR across these studies is invalid.
3. **Model Safety-Training Confound:** Base-model alignment (`gpt-4-0613` vs. `gpt-4o` vs. instruction-hierarchy models vs. `Llama-3`) radically alters refusal and injection susceptibility independent of MAS topology (echoing the guardrail confound flagged in `ICLR 2024 LLM-Deliberation`).

#### 3. Risk of Invalid Pooling / Shallow Description
**Very High.** A systematic review centered on Topic E will either (a) pad its primary corpus with *single-agent* indirect injection papers to gain standardized metrics, violating MAS scope integrity, or (b) become a qualitative taxonomy of attack styles across incompatible toy simulations. Furthermore, **CSUR** already has recent LLM-agent security survey coverage (threat origin $\times$ layer $\times$ impact noted in Deliverable A).

#### 4. Beginner Comprehensibility & Defense
**Moderate.** Prompt injection and utility-security trade-offs are intuitive, but rigorous evaluation of trust boundaries requires systems-security concepts (data/control-plane separation, capability tokens, adaptive red-teaming against LLM judges/firewalls) that frequently collapse into superficial "add an LLM guard agent" advice.

#### 5. Challenge Verdict: **REJECT as Standalone Review Topic**
* **Actionable Guidance:** Do not select (E) as the primary systematic review topic. Include cross-agent propagation/trust boundaries strictly as a **scoped Risk & Governance sub-section** (satisfying TMLR's Broader Impact and CSUR's threat considerations) without pretending standardized cross-agent ASR meta-comparisons exist yet.

---

### Candidate (F): Uncertainty-Aware Delegation / Selective Single-to-Multi Escalation

#### 1. Measurable Metrics Available
* **Cost-Normalized Routing Metrics:** Accuracy vs. token/cost reduction (`MasRouter`: up to `52.07%` token savings on HumanEval, `+1.8%–8.2%` MBPP, `+3.51 pp` over single-model routers, `17.21%–28.17%` plug-and-play savings; `MaAS`: `6%–45%` inference cost; `EcoAssistant`: resolve rate across weak-to-strong escalation).
* **Uncertainty Estimation & Escalation Signals:** Token-level entropy/probabilities, trajectory uncertainty propagation (`SAUP`, `arXiv:2412.01033`), latent hidden-state probes (`LEASH` weak-to-strong computer-use escalation), confidence attenuation across handoffs (*Lost in Communication* "vanishing uncertainty").

#### 2. Comparability Hazard
1. **Severe Scope Conflation (`Single-Model Routing ≠ SAS→MAS Escalation`):** The visible benchmarked corpus is dominated by **single-agent model routing** (*RouteLLM*, *RouterBench*, *FrugalGPT*, *AutoMix*—choosing cheap vs. expensive model for one agent) and **intra-MAS model assignment** (*MasRouter*—picking LLM backbones for preset MAS roles). Genuine **uncertainty-aware SAS-to-MAS escalation** (invoking a single agent first, detecting epistemic/aleatoric failure signals mid-trajectory, and dynamically spawning MAS verification/collaboration *only when needed*) remains a sparse, mostly preprint-stage niche (`LEASH`, `SAUP`, `MaAS` variants).
2. **Closed-API Logprob Opacity:** Entropy/logprob-based uncertainty estimators and hidden-state probes (`LEASH`) are impossible to reproduce or benchmark consistently across closed reasoning APIs that hide logprobs or internal activations.
3. **Missing Compute-Matched Adaptive SAS Baselines:** Routing/escalation works commonly benchmark against "always run static MAS" or "always run GPT-4", rarely testing against **adaptive single-agent self-consistency** (escalating sample count $N$ on uncertain queries) at matched cost.

#### 3. Risk of Invalid Pooling / Shallow Description
**Extreme.** Building a systematic review on Topic F forces an author either into invalid pooling across incompatible literatures (single-model routers + intra-MAS routers + ReAct UQ + HITL safety escalation) or into an underpowered, premature synthesis of <15 unstandardized 2025–2026 preprints.

#### 4. Beginner Comprehensibility & Defense
**Low-to-Moderate.** Defending ECE/AUROC calibration, split-conformal bounds (compare TMLR Paper 9844 rejection context), hidden-state probes, and contextual bandit routing alongside MAS orchestration invites formal errors for a beginner researcher.

#### 5. Challenge Verdict: **REJECT as Standalone Review Topic**
* **Actionable Guidance:** Treat selective SAS$\to$MAS escalation strictly as a **High-Value Future Research Direction** emerging from Topic A+D's compute-matching synthesis, rather than an established primary literature ready for systematic review.

---

### Candidate (G): LLM Agent Swarms vs. Classical Swarm Intelligence / Classical MAS

#### 1. Measurable Metrics Available
* **Decentralized Grid / Swarm Metrics (*SwarmBench*, Ruan et al. `arXiv:2505.04364`):** Performance on 5 spatial tasks (*Pursuit, Synchronization, Foraging, Flocking, Transport*) under restricted $k \times k$ local perception and anonymous local messaging; spatial congestion and information-silo rates.
* **Complex-Systems / Information-Theoretic Coupling (*Emergent Coordination*, Riedl, ICLR 2026, `arXiv:2510.05174`):** Partial Information Decomposition (`PID`) of Time-Delayed Mutual Information (`TDMI`) isolating cross-agent synergy from temporal correlation.
* **Macro-Simulation Observations (*Project Sid*, Altera `arXiv:2411.00114`):** Role specialization, rule generation, and cultural spread across 10–1,000+ Minecraft agents (primarily descriptive/qualitative event logs).
* **Classical SI / Classical MAS Metrics:** Convergence iterations, global optimum gap, communication bit-rate, formal protocol liveness/deadlock freedom (ACO, PSO, Boids, BDI, FIPA ACL, Contract Net).

#### 2. Comparability Hazard
1. **Total Benchmark Disjointness:** Classical SI algorithms optimize continuous spaces, graphs, or decentralized spatial physics in **microseconds per iteration with zero token cost**, whereas commercial/open-source "LLM swarms" (`OpenAI Swarm`, `Swarms`, `GPTSwarm`, `AgentVerse`) are **centralized or graph-routed natural-language orchestration pipelines** (*La Malfa et al.*, NeurIPS 2025, `FfsxgSZW0c`). There is virtually zero shared benchmark suite where classical ACO/PSO/Contract-Net and modern LLM-MAS compete meaningfully.
2. **Artificial Compression into Tokenized Grids:** Even where *SwarmBench* enforces genuine decentralized local-perception constraints on LLMs, the result exposes a massive hardware/cost mismatch (LLMs struggling at spatial planning at orders-of-magnitude higher latency and cost than simple reactive heuristics, and coordinating mainly via visual observation rather than text broadcasts).
3. **Severe Terminological Pollution:** Co-opting "swarm," "emergent," and "protocol" for sequential prompt chains (*La Malfa et al.* NeurIPS 2025) makes keyword-based literature screening hazardous unless strict exclusion definitions are enforced.

#### 3. Risk of Invalid Pooling / Shallow Description
**Maximum.** A review centered on (G) cannot deliver a falsifiable quantitative comparison across primary systems—it inevitably degrades into a philosophical/historical compare-and-contrast essay. Worse, *La Malfa et al. (NeurIPS 2025)* has already published the definitive position critique on classical MAS vs. LLM-MAS misappropriation, and **CSUR** explicitly rejects broad descriptive essays lacking either unified empirical rigor or deep formal synthesis.

#### 4. Beginner Comprehensibility & Defense
**Deceptively Easy to Sound Superficial; Very Hard to Defend.** Beginners are easily tempted by anthropomorphic analogies ("ants vs. LLM agents") that trigger immediate pushback from traditional MAS referees (classical BDI/Contract-Net/game-theory rigor) and complex-systems reviewers (`PID`/`TDMI` emergence rigor).

#### 5. Challenge Verdict: **REJECT as Primary Review Topic**
* **Actionable Guidance:** Demote (G) to a **1–2 page Definitional & Terminological Exclusion Gate** in Section 2 of the review: formally distinguish *true decentralized swarm intelligence* (*SwarmBench*) and *classical autonomous MAS* (*La Malfa et al.*) from *LLM multi-agent orchestration graphs*, excluding non-interactive prompt chains and pure classical SI from the empirical synthesis.

---

## 4. Strategic Synthesis Decision: Constructing the Most Falsifiable & Publishable Framing

### Why an Integrated Framing (`A + D` Anchored by `B` & `C`) Beats Every Single Topic Alone

Evaluating the seven directions strictly on **measurability, falsifiability, non-overlapping CSUR/TMLR/AIRE positioning, and M.Tech-level defensibility** yields a decisive structural conclusion:

* **Do NOT pick E, F, or G** as the review's backbone (each suffers from single-agent contamination, tiny/fragmented corpora, or zero benchmark commensurability).
* **Do NOT run A purely in isolation from D, B, and C:**
  1. Pure **(A)** tells you *whether* a token-matched MAS won or lost, but cannot explain *why* unless paired with **(D) Topology & Pruning** (e.g., Independent vs. Centralized vs. Sparse Learned DAGs) and **(C) Failure Attribution & Error Cascades** (inter-agent misalignment, `17.2×` vs. `4.4×` amplification, conformity collapse).
  2. Pure **(A)** or **(D)** without **(B) Evaluation-Validity Auditing** (`pass^k`, strict exact-match checks, ABC outcome/task validity, search-cost amortization) will accidentally treat flawed, overfitted, or compute-inflated primary papers as valid evidence—violating **TMLR Criterion 1**.

### Recommended Master Framing (Optimized for CSUR Primary / TMLR Backup 1 / AIRE Backup 2)

> **Working Thesis Scope:**  
> ***When and How Multi-Agent LLM Systems Outperform Single-Agent Baselines: A Systematic Review of Compute-Matched Baselines, Coordination Topologies, Failure Attribution, and Evaluation Validity***

#### Why This Framing Wins at All Three Venues:
1. **Verified CSUR White Space:** Directly fills the gap identified in [Deliverable_A_Journal_Intelligence_Report.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/deliverables/Deliverable_A_Journal_Intelligence_Report.md#L52) via an original **4-Axis Taxonomy** (`Orchestration Topology × Compute/Cost Control × Task Structure × Failure/Validity Regime`) rather than a paper-by-paper catalog.
2. **TMLR Criterion 1 & Survey Certification Fit:** Every quantitative table audits claims against evidence (compute-matched vs. unmatched SAS baselines, inference vs. amortized search cost, single-run `pass@1` vs. `pass^k`), avoiding synthetic cross-paper score averages.
3. **AIRE Differentiation Shield:** Completely separates itself from AIRE's crowded 2025–2026 "architectures + applications + governance" general surveys (*Ala'anzy et al.*, *Chowa et al.*, *Abou Ali et al.*) via PRISMA screening paired with a falsifiable **within-setting confounder audit**.

---

## 5. Mandatory Anti-Overclaiming & Within-Setting Comparison Protocol

To prevent the review from falling into invalid meta-analytic pooling or claiming universal causal laws where primary literature only demonstrates conditional associations, the synthesis must enforce **five hard methodological rules**:

1. **Zero Unstratified Cross-Paper Pooling:** Never average accuracy percentages or "% token savings" across studies with different backbones, different reference baselines (`All-to-All` vs. `Chain` vs. `CoT`), or different benchmark harnesses (`EvalPlus` vs. base `HumanEval`; `SWE-bench Lite` vs. `Verified`). Use **within-study paired deltas** ($\Delta_{\text{MAS-SAS}}$) stratified by baseline rigor.
2. **Four-Tier Baseline Rigor Coding:** Code every primary empirical comparison into one of four falsifiable baseline tiers:
   * *Tier 1 (Gold):* Compute/token-matched strong SAS (`Self-Consistency`, `Few-Shot CoT`, or tool-equivalent pipeline like `Agentless`) on the same backbone and eval harness.
   * *Tier 2 (Partial):* Strong SAS baseline included, but unmatched in total token/API call budget or search-time amortization omitted.
   * *Tier 3 (Weak):* Single-pass zero-shot SAS only (highly vulnerable to the *Rethinking the Bounds* zero-shot confound).
   * *Tier 4 (Invalid Comparator):* No SAS LLM baseline (e.g., comparing only against unpruned dense MAS, classical RL like PPO/PBT, or human annotation without cost accounting).
3. **Separate Inference Cost from Search/Training Amortization:** For automated graph/topology learners (*AFlow*, *GPTSwarm*, *AgentPrune*, *G-Designer*, *MaAS*), report test-time token reduction **only alongside** upfront optimization/search token budgets (or mark `Amortization Cost: Unreported`).
4. **Enforce Conditional Association Language (No Fake "Universal Laws"):** Even flagship controlled studies like *Towards a Science of Scaling Agent Systems* (`arXiv:2512.08296`) establish **conditional empirical associations** across specific architectures, benchmarks, and 2025 frontier models—not invariant physical laws. Frame findings explicitly as *observed conditional regimes* (e.g., *"Within tested benchmarks and model tiers, centralized coordination improved parallelizable tasks while sequential state-dependent planning suffered under fixed token budgets"*).
5. **Apply Upfront Terminological & Validity Gates:**
   * *Scope Exclusion Gate (from Topic G + NeurIPS 2025 `FfsxgSZW0c`):* Distinguish genuine interactive/stateful multi-agent LLM coordination from static prompt chaining, isolated parallel voting (*TMLR 7253*), and classical SI/BDI protocols.
   * *Evaluation Validity Gate (from Topic B + ABC `arXiv:2507.02825`):* Tag every included study for multi-run reporting (`pass^k` / variance vs. single-run `k=1`), strict exact-match / `EvalPlus` sensitivity, and harness/leakage caveats.
   * *Status Integrity Gate (from Agent 4 OpenReview Audit):* Tag every reference strictly as `Peer-Reviewed Journal`, `Peer-Reviewed Conference`, `Workshop`, `Preprint`, `Withdrawn` (never relabeled rejected), or `Rejected` (cited solely as documented methodological failure cases when public).
