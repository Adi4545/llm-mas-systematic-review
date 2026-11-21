# Deliverable B — Topic Selection, Novelty Verification & Research Questions Report

**Phases:** Phase 2 (Focused Topic Discovery & Saturation Audit) & Phase 3 (Research Question Formulation)  
**Compiled by:** Agent 1 (Research Director), synthesizing parallel outputs from **Agent 5 (Research Gap & Novelty Analyst)** ([agent5_topic_novelty_matrix.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/agents/agent5_topic_novelty_matrix.md)), **Agent 3 (Literature Discovery Probe)** ([agent3_topic_feasibility_probe.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/agents/agent3_topic_feasibility_probe.md)), and **Agent 8 (Evaluation Feasibility Challenger)** ([agent8_topic_challenge.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/agents/agent8_topic_challenge.md))  
**Target Venues (from Deliverable A):** #1 **ACM Computing Surveys (CSUR)** | #2 **Transactions on Machine Learning Research (TMLR)** | #3 **Artificial Intelligence Review (AIRE)**  
**Date:** November 20, 2026  

---

## 1. Selected Primary Topic & Working Title

### Final Working Title
> **When Do LLM Multi-Agent Systems Outperform Single Agents? A Systematic Review of Compute-Normalized Evidence, Coordination Topologies, Failure Mechanisms, and Evaluation Validity**

### One-Paragraph Research Problem
Between 2023 and 2026, Large Language Model (LLM)-based multi-agent systems (MAS)—spanning multi-agent debate, role-specialized software/research pipelines, hierarchical orchestrator-worker teams, and dynamic communication graphs—proliferated across reasoning, coding, and interactive tool-use benchmarks. However, a growing wave of controlled empirical audits demonstrates that multi-agent architectures frequently match or underperform well-engineered single-agent systems (`SAS`) once total inference tokens, API expenditure, and wall-clock latency are normalized, and exhibit substantial failure rates (`41%–86.7%` in trace-level audits such as *MAST*) driven by inter-agent error amplification, premature consensus, and specification drift. Although at least 42 surveys published or posted between 2023 and 2026 catalog general MAS architectures, multi-agent debate protocols, communication topologies, security threats, or runtime compression algorithms, **no systematic review conducts an integrated empirical meta-audit comparing LLM-MAS directly against single-agent baselines across compute-matched versus unmatched regimes**, isolating the architectural and task conditions under which collaboration genuinely outperforms single-agent scaling versus when apparent gains stem from methodological confounders.

### Strict Scope & Exclusions
* **Included Primary Scope (2023–November 2026):**
  1. Primary empirical studies directly comparing an LLM-based MAS (at least two distinct LLM agent roles, debating peers, hierarchical orchestrator-worker teams, or multi-agent graph architectures) against one or more LLM single-agent baselines (`CoT`, `Self-Consistency` / `Best-of-N`, `ReAct`/reflexion tool loops, or single-LLM pipelines), evaluated on effectiveness alongside compute, token, call-count, or latency metrics (whether compute-matched or unmatched).
  2. Controlled empirical diagnostic studies quantifying MAS-vs.-SAS scaling regimes, topology-dependent coordination overhead/amortization, inter-agent error propagation/conformity collapse, and agentic benchmark/harness validity confounders that directly govern MAS-vs.-SAS comparisons.
* **Explicit Terminological Exclusion Gate (Addressing NeurIPS 2025 `La Malfa et al.` & Classical MAS Standards):**
  - Classical non-LLM Swarm Intelligence (`ACO`, `PSO`, `Boids`) and classical pre-LLM `MARL`/`BDI`/`FIPA` systems are excluded from primary quantitative pooling and discussed strictly in a bounded **Technical Background & Terminological Hygiene** section distinguishing decentralized biological/numeric swarms from natural-language LLM orchestration graphs.
  - Pure single-query weak-to-strong LLM model routers (`RouteLLM`, `AutoMix`, `Hybrid LLM`) and pure single-agent prompt/RAG tuning without a multi-agent comparator are excluded.
  - Broad security/prompt-injection catalogs (*He et al.* CSUR 2026; *Kim et al.* USENIX Security 2026), standalone trajectory root-cause attribution surveys (*Wang et al.* IEEE TSE 2026), and general agent-harness surveys (*Meng et al.* 2026; *Guo et al.* 2026) are referenced for differentiation rather than duplicated.

---

## 2. Candidate-Topic Evaluation, Saturation Audit & Reasons for Rejection

Agent 5 audited **42 verified 2023–2026 surveys/position papers**, Agent 3 independently probed **84 unique primary/diagnostic studies across 7 thematic clusters**, and Agent 8 challenged every candidate on **metric measurability, baseline fairness, and cross-study comparability**.

### Summary Scoring & Rejection Matrix (100-Point Rubric)

| Rank | ID | Candidate Topic | Novelty (20) | Evidence (15) | Feasibility (15) | Clarity (15) | Journal Fit (15) | Tech Imp. (10) | Review Def. (10) | **Total** | Director Verdict & Rejection/Integration Rationale |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **T1** | **Compute- & Token-Matched Empirical Comparisons of LLM MAS vs. SAS** *(Integrated with topology strata, failure mechanisms & validity audit)* | 18 | 14 | 13 | 15 | 14 | 10 | 9 | **93** | **SELECTED PRIMARY TOPIC.** Clearest CSUR/TMLR white space; highest falsifiability via within-study paired baseline coding; avoids descriptive cataloging. |
| **2** | **T10** | **Inter-Agent Conformity Bias, Sycophancy Cascades & Consensus Collapse** *(Carved behavioral slice)* | 16 | 12 | 13 | 13 | 12 | 9 | 8 | **83** | **SELECTED FALLBACK TOPIC.** Viable orthogonal backup (~18+ studies), though narrower in structural/economic ROI scope for CSUR than T1. |
| **3** | **T7** | Multi-Run Reliability (`pass^k`), Non-Determinism & Reproducibility | 12 | 8 | 10 | 12 | 10 | 8 | 7 | **67** | **REJECTED (Standalone):** 90%+ of `pass^k`/randomness literature (`2406.12045`, `2602.16666`) is single-agent; MAS corpus too sparse. **Repurposed inside T1 (RQ4).** |
| **4** | **T6** | Uncertainty-Aware Delegation & Single-to-Multi Escalation | 13 | 7 | 9 | 12 | 10 | 8 | 7 | **66** | **REJECTED (Standalone):** Only ~7 true MAS escalation studies (`Sparse <12`); single-query routing already surveyed (`TMLR 2026`, `JAIR 2025`); overlaps *Li et al.* "Collaboration Boundary." **Retained as Future Work / Mitigation.** |
| **5** | **T4** | Communication Topology & Coordination Overhead Scaling | 7 | 13 | 10 | 12 | 7 | 8 | 5 | **62** | **REJECTED (Standalone):** Saturated by *Yue et al.* (EMNLP 2026 Findings), *Yan et al.* (`2502.14321`), *Zhu et al.* (*Future Internet* 2026), *Li et al.* (Sept 2026), and CSUR *Geng et al.* (`10.1145/3817113`). **Integrated strictly as moderating topology strata in T1 (RQ2).** |
| **6** | **T8** | LLM Agent Swarms vs. Classical SI & Classical MAS | 8 | 9 | 10 | 11 | 10 | 7 | 6 | **61** | **REJECTED (Standalone):** Saturated conceptually (*Wang et al.* `2604.18133`; *Bădică et al.* `2509.02515`; *Rahman et al.* `2506.14496`; *La Malfa et al.* NeurIPS 2025) + zero shared benchmarks (`SwarmBench` withdrawn). **Used strictly as Section 2 Terminological Gate.** |
| **7** | **T2** | Evaluation Validity, Harness Fragility & Cost-Normalized Benchmarking | 7 | 12 | 9 | 11 | 8 | 8 | 5 | **60** | **REJECTED (Standalone):** Crowded by 3 eval surveys (`ACL 2025`, `KDD 2025`, `2503.22458`) + 3 2026 harness surveys (*Meng et al.*, *Guo et al.*, withdrawn TMLR `3hXEPbG0dh`); primary audits mostly single-agent. **Embedded as Quality-Audit Rubric & RQ4.** |
| **8** | **T3** | Cascading Error Propagation, Conformity & Failure Attribution *(Broad)* | 6 | 13 | 9 | 11 | 8 | 8 | 4 | **59** | **REJECTED (Broad Standalone):** Preempted by *Wang et al.* (IEEE TSE 2026, 55+ trajectory attribution papers), anonymous *ACL ARR 2026* (#2880/#3533), and *Motger et al.* (`2607.26212`, 141 MAD studies). **Error cascades/conformity integrated into T1 (RQ3).** |
| **9** | **T5** | Cross-Agent Prompt-Injection & Trust Boundaries | 4 | 12 | 10 | 13 | 4 | 9 | 3 | **55** | **REJECTED (Standalone):** Severely saturated by 6 surveys incl. CSUR *He et al.* (`10.1145/3773080`), USENIX Security *Kim et al.* (`2603.11088`), *Nguyen et al.* (`2603.09002`), *Chu* (`2604.23338`), *Kong et al.* (`2506.19676`). **Summarized briefly in Threat/Governance section.** |
| **10** | **T9** | Termination, Liveness & Verification Failure Modes | 7 | 7 | 9 | 9 | 9 | 7 | 5 | **53** | **REJECTED (Standalone):** Directly preempted by *Mallampati & Nagoriya* (Oct 2026, 62 papers) and *Dantas et al.* (`arXiv:2608.14590`, PRISMA 38 studies). |

---

## 3. Verified Literature Gap & Explicit Comparison Against Closest Prior Surveys

We do **not** claim absolute novelty. The table below maps precisely what the closest 2024–2026 surveys cover and what the proposed review uniquely contributes.

| Closest Prior Survey | Year / Venue & Status | Exact Scope Covered | What Our Review Uniquely Adds (Verified Gap) |
| :--- | :--- | :--- | :--- |
| **Li et al.** — *Efficiency in LLM Multi-Agent Systems: A Survey* (`10.20944/preprints202609.1639.v1`) | Sept 2026 / Preprints.org (`Preprint`) | Engineering techniques to reduce MAS compute/latency across Topology pruning, Runtime pruning, Offline Optimization, and Collaboration-Boundary routers. | Li et al. asks *how to make MAS faster/cheaper*; our review asks **whether and when MAS actually beats compute-matched SAS**, systematically auditing head-to-head SAS baselines, search-time amortization omissions, and 6 distortion confounders. |
| **Motger et al.** — *Multi-Agent Debate Strategies: Survey, Taxonomy, and Challenges* (`arXiv:2607.26212`) | July 2026 / arXiv (`Preprint`) | Systematic review of 141 primary Multi-Agent Debate (`MAD`) papers by participants, interaction topology, and agreement mechanisms. | Covers only `MAD`; does not synthesize non-debate MAS (`SWE`, tool-use, hierarchical teams, orchestrator-worker) nor systematically stratify outcomes against compute-matched `Self-Consistency`/single-agent baselines. |
| **Zhu et al.** (*Future Internet* `10.3390/fi18060326`) & **Tran et al.** (`arXiv:2501.06322`) | 2025–2026 (`Journal` / `Preprint`) | Taxonomies of MAS collaboration structures, frameworks (LangGraph, CrewAI, AutoGen), and protocols (MCP, A2A). | Descriptive architecture and protocol mappings; neither quantifies SAS-vs.-MAS break-even boundaries nor evaluates benchmark/harness validity confounders. |
| **Wang et al.** (IEEE TSE 2026) & **Anonymous** (ACL ARR 2026 #2880/#3533) | 2026 (`Journal` / `Under Review`) | Trajectory analysis and 5Ws+H root-cause failure attribution over execution traces. | Focuses on post-hoc fault localization in MAS traces; our review links inter-agent error amplification and conformity collapse specifically to *why MAS underperforms compute-matched SAS*. |
| **Ala'anzy et al.** (`10.1007/s10462-026-11731-2`), **Chowa et al.** (`10.1007/s10462-025-11471-9`), **Abou Ali et al.** (`10.1007/s10462-025-11422-4`) | Nov 2025 – Oct 2026 / **AIRE** (`Journal`) | Broad overview reviews of autonomous agents, tool use, and Agentic AI applications/governance. | High-level narrative/PRISMA field surveys; none constructs a falsifiable compute-normalization audit comparing MAS vs. SAS baselines across matched vs. unmatched regimes. |
| **Du et al.** (`10.1145/3789261`), **Zhang et al.** (`10.1145/3794858`), **Geng et al.** (`10.1145/3817113`), **He et al.** (`10.1145/3773080`) | 2025–2026 / **ACM CSUR** (`Journal`) | Single/general agent optimization, generalizability, classical MARL team scaling, and agent security/privacy. | Establishes CSUR's exact white space: no CSUR article evaluates empirical SAS-vs.-MAS effectiveness, coordination overhead, and evaluation confounders in LLM-based MAS. |

### Proposed Original Contribution (Synthesis-Derived)
1. **Four-Tier Baseline-Rigor Coding Framework:** Classifying every primary comparison from Tier 1 (*Compute/Token-Matched Strong SAS*) down to Tier 4 (*Invalid/Absent SAS Baseline*) to isolate genuine coordination gains from hidden inference-compute scaling.
2. **Conditional Regime Matrix:** Stratified within-study synthesis mapping `MAS > SAS`, `MAS ≈ SAS`, and `MAS < SAS` outcomes across **Task Structure** (decomposable/parallelizable/context-overflowing vs. tightly coupled sequential), **Backbone Capability Tier**, **Topology**, and **Model Heterogeneity**.
3. **Six-Class Experimental Confounder & Failure-Linkage Taxonomy:** Connecting measurement distortions (unmatched tokens, API thinking-budget leaks, voting-as-deliberation, asymmetric prompting, strict exact-match/harness drift, unamortized search cost) with mechanistic failure drivers (error amplification, conformity/sycophancy collapse, Data Processing Inequality handoff loss).

---

## 4. Target-Journal Fit Rationale

* **Primary Target — ACM Computing Surveys (CSUR):** Directly fills CSUR's verified thematic gap in its 2025–2026 LLM-agent portfolio; delivers an original multi-dimensional taxonomy and comparative synthesis (explicitly avoiding chronological cataloging); adheres to `acmart` format, CCS concepts, and a tight $\le 100$-word unstructured abstract.
* **Backup Target 1 — Transactions on Machine Learning Research (TMLR):** Ideal match for TMLR Criterion 1 (strict *claims–evidence parity* exposing where primary claims exceed cost-matched evidence) and *Survey Certification*, with zero crowding and $\$0$ Diamond OA.
* **Backup Target 2 — Artificial Intelligence Review (AIRE):** Ready fallback using PRISMA 2020 + Table 1 differentiation, contingent on a pre-submission editorial inquiry explicitly separating this empirical SAS-vs.-MAS meta-audit from AIRE's three broad 2025–2026 reviews.

---

## 5. Precise Research Questions (Phase 3 — RQ1 to RQ4)

Each Research Question avoids presupposing that multi-agent architectures improve or degrade performance, separates independent analytical dimensions without overlap, and specifies verifiable extraction fields and synthesis logic.

### RQ1: Compute-Normalized Effectiveness & Conditional Regimes
* **Question:** *Under what task structures, base-model capability regimes, and compute- or token-budget conditions do LLM-based multi-agent systems outperform, match, or underperform single-agent baselines?*
* **Purpose:** Establish whether observed MAS advantages persist once total inference tokens, sample counts, and prompt quality are controlled, and map the boundary conditions separating positive vs. negative returns.
* **Defined Concepts:** *Single-Agent System (SAS)* (single LLM instance with prompting, CoT, Self-Consistency/Best-of-$N$, or single-agent tool/reflexion loop); *Compute/Token-Matched Regime* (total prompt + reasoning + completion tokens or API cost held equal within tolerance); *Task Structure* (parallelizable/decomposable vs. sequential/state-dependent; context-exceeding vs. single-context).
* **Explicit Evidence Requirements:** Primary empirical studies (peer-reviewed or major verified preprints) reporting head-to-head MAS and SAS accuracy/resolve rates alongside token, sample-count, or dollar-cost accounting (or documenting absence thereof).
* **Relevant Extraction Fields:** `Task/Benchmark`, `Task Structure Type`, `Backbone Model(s) & Heterogeneity`, `SAS Baseline Type & Tier (1–4)`, `Token/Cost Matching Status`, `Reported Effectiveness Delta (Δ_MAS-SAS)`, `Direction Verdict (Win/Tie/Loss)`.
* **Planned Synthesis Approach:** Stratified within-study paired-outcome mapping (strictly forbidding cross-benchmark numerical averaging), contrasting matched (`Tier 1`) vs. unmatched (`Tier 2–4`) distributions across task-structure and model-capability strata.
* **Why Answering It Matters:** Prevents practitioners and researchers from paying $3\times$–$15\times$ token and latency penalties for multi-agent pipelines where an equal-budget single agent matches or beats them.

### RQ2: Coordination Topologies, Scaling & Cost-Amortization Trade-Offs
* **Question:** *How do different multi-agent coordination topologies and communication paradigms relate to task effectiveness, inference token overhead, amortized optimization cost, and end-to-end latency?*
* **Purpose:** Disentangle topology-driven coordination efficiency from hidden search/training costs and naive dense-graph strawman baselines.
* **Defined Concepts:** *Coordination Topology* (Independent/Voting Ensemble, Sequential Chain/SOP, Centralized Star/Orchestrator-Worker, Dense All-to-All Debate, Adaptive Sparse/Learned DAG); *Inference Cost* (test-time tokens/USD); *Amortized Optimization Cost* (upfront MCTS/RL/VGAE/prompt-search compute required to build/prune the topology); *Wall-Clock Latency* (makespan dependent on critical path depth).
* **Explicit Evidence Requirements:** Primary empirical studies evaluating topological variants, communication pruning, or multi-agent scaling curves ($N$ agents) with measured accuracy alongside token, cost, or latency outputs.
* **Relevant Extraction Fields:** `Coordination Topology`, `Agent Count (N)`, `Communication Protocol / Graph Type`, `Inference Token/Cost Delta`, `Amortization/Search Cost Reported?`, `Wall-Clock Latency`, `SAS Comparator Included?`.
* **Planned Synthesis Approach:** Cross-tabulate topology families against task structure, critical-path latency impact, and whether net efficiency holds after accounting for optimization/search costs and strong SAS comparators.
* **Why Answering It Matters:** Clarifies why communication pruning claims (e.g., "-70% tokens vs. complete-graph debate") can still underperform simpler single-agent or sampling baselines when total lifecycle compute is audited.

### RQ3: Mechanisms Explaining Multi-Agent Degradation & Failure
* **Question:** *Which empirically documented mechanisms—including inter-agent error amplification, conformity or sycophancy cascades, information loss across agent handoffs, and specification or verification failures—account for multi-agent underperformance relative to single-agent execution?*
* **Purpose:** Provide the mechanistic explanation linking negative empirical MAS deltas (RQ1/RQ2) to structural, communication, and social-epistemic failure modes.
* **Defined Concepts:** *Error Amplification* (propagation/compounding of upstream mistakes across agents); *Conformity / Sycophancy Collapse* (agents abandoning correct outputs to align with confident majorities, personas, or judges); *Handoff Information Loss* (semantic truncation/compression under Data Processing Inequality bounds); *Specification & Verification Failures* (*MAST*-style role disobedience, premature termination, faulty cross-verification).
* **Explicit Evidence Requirements:** Quantitative trace audits, error-propagation experiments, controlled conformity/debate ablations, and failure-attribution studies documenting failure incidence ($\kappa$-validated where available), amplification multipliers, or degradation drivers.
* **Relevant Extraction Fields:** `Failure Mechanism Category`, `Empirical Incidence / Amplification Metric`, `Inter-Annotator or Attribution Metric`, `Trace Observability Scope`, `Proposed Mitigation & Empirical Recovery Delta`.
* **Planned Synthesis Approach:** Cross-study mechanistic synthesis mapping failure modes onto topology classes (RQ2) while strictly separating intra-agent single-loop faults from genuine inter-agent coordination faults.
* **Why Answering It Matters:** Shifts field guidance from ad-hoc prompt tweaking toward targeted structural controls (centralized verification, anonymization, context provenance, selective escalation).

### RQ4: Evaluation Validity, Harness Sensitivity & Methodological Confounders
* **Question:** *To what extent do experimental confounders—including unmatched compute budgets, asymmetric prompting, evaluation-harness fragility, single-run variance masking (`pass^k` decay), and benchmark leakage—distort reported multi-agent comparisons across the primary literature?*
* **Purpose:** Audit the epistemic reliability of the empirical MAS literature itself, explaining why contradictory performance claims proliferate across studies.
* **Defined Concepts:** *Baseline Asymmetry* (unequal compute, few-shot examples, or tool access between MAS and SAS); *Harness Fragility* (exact-match extraction sensitivity, sparse test suites, grading/reward-hacking bugs); *Multi-Run Reliability (`pass^k`)* (probability that all $k$ independent runs succeed vs. optimistic single-run `pass@1`); *Verification Transport Failure* (evaluator drift across delegation/abstraction boundaries).
* **Explicit Evidence Requirements:** Primary MAS comparative studies audited via our quality/validity checklist, paired with 2024–2026 benchmark/harness diagnostic studies quantifying measurement skew.
* **Relevant Extraction Fields:** `Multi-Run / Seed Reporting (k, Variance/CI)`, `Compute/Prompt/Tool Parity Status`, `Exact-Match / Harness Sensitivity Flag`, `Code & Prompt Reproducibility`, `Publication Status & Verification Level`.
* **Planned Synthesis Approach:** Systematic Risk-of-Bias / Evaluation-Validity Matrix across all included primary studies, paired with verified confounder magnitude bounds from benchmark audit studies.
* **Why Answering It Matters:** Directly satisfies TMLR Criterion 1 and CSUR analytical rigor by equipping readers and reviewers with concrete validity filters before accepting any MAS benchmark claim.
