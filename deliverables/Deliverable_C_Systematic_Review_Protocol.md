# Deliverable C — Systematic Review Protocol (`v1.0`)

**Working Title:** *When Do LLM Multi-Agent Systems Outperform Single Agents? A Systematic Review of Compute-Normalized Evidence, Coordination Topologies, Failure Mechanisms, and Evaluation Validity*  
**Protocol Version:** `v1.0` *(Pre-Search & Pre-Screening Freeze)*  
**Protocol Date:** `November 20, 2026`  
**Phase:** Phase 4 (Methodological Design & Extraction Architecture)  
**Author:** Agent 6 (Systematic Review Methodologist)  
**Target Venues (from [Deliverable_A_Journal_Intelligence_Report.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/deliverables/Deliverable_A_Journal_Intelligence_Report.md)):**  
- **#1 Primary Target:** *ACM Computing Surveys (CSUR)*  
- **#2 Backup Target 1:** *Transactions on Machine Learning Research (TMLR — Survey Certification)*  
- **#3 Backup Target 2:** *Artificial Intelligence Review (AIRE — Springer)*  
**Companion Extraction Schema:** [extraction_schema.json](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/extraction_schema.json)  
**Upstream Scope & Research Questions:** [Deliverable_B_Topic_and_Novelty_Report.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/deliverables/Deliverable_B_Topic_and_Novelty_Report.md)

> [!IMPORTANT]
> **Pre-Execution Zero-Fabrication & Access-Honesty Covenant:** This protocol is frozen prior to Phase 5 search execution and dual screening. Zero literature searches have been executed inside this deliverable, and all PRISMA 2020 flow counts remain explicitly unpopulated (`[Pending Phase 5 Execution]`). Every retrieval source, database boundary, and paywall limitation reflects our actual operational environment (`search_web` over open academic indexing, preprint servers, proceedings archives, OpenReview, and publisher metadata; **no** direct Scopus or Clarivate Web of Science bulk API/export access).

---

## 1. Review Design Selection & Justification

### 1.1 Selected Methodology
This review adopts a **PRISMA 2020 and Kitchenham–Charters-guided Systematic Literature Review (SLR) with Transparent Open-Web Retrieval Boundaries**, paired with a **Within-Study Stratified Paired-Delta Synthesis** and an **Evaluation-Validity / Risk-of-Bias Audit**.

Specifically, the methodology integrates:
1. **Kitchenham & Charters (2007) Software Engineering SLR Engineering:** Formal linkage between research questions (`RQ1`–`RQ4`), Boolean search queries (`Q1`–`Q6`), two-stage dual screening, snowballing, and structured 7-item quality appraisal tailored to empirical computing systems.
2. **PRISMA 2020 Reporting Standards:** Explicit eligibility gates (`I1`–`I6`, `E1`–`E8`), transparent duplicate resolution, itemized study provenance (`access_level` and `supporting_evidence_locations`), risk-of-bias/publication-bias evaluation, and mandatory sensitivity analyses contrasting peer-reviewed archival literature against qualified preprints.
3. **Transparent Open-Web Retrieval Boundaries:** Honest disclosure that candidate discovery relies on structured open-web academic search (`arXiv`, `OpenReview`, `ACL Anthology`, `NeurIPS/ICLR/ICML/PMLR`, `ACM DL`, `SpringerLink`, `IEEE Xplore`, `ScienceDirect`, `Nature`, and `Semantic Scholar / Google Scholar` web indexing) rather than subscription bulk exports from **Scopus** or **Web of Science**, preventing false claims of exhaustive closed-database coverage.

### 1.2 Alignment with RQ1–RQ4 and Target Journal Standards

| Alignment Dimension | Why PRISMA 2020 + Kitchenham–Charters + Open-Web Boundaries Fits |
| :--- | :--- |
| **Fit to `RQ1`–`RQ4`** | Primary LLM-MAS studies span heterogeneous LLM backbones, unequal token budgets, disparate evaluation harnesses, and non-peer-reviewed preprints. Standard meta-analytic cross-paper averaging would induce severe Simpson's paradox. Pairing PRISMA's rigorous bias/status controls with within-study paired delta extraction ($\Delta_{\text{MAS-SAS}}$) and explicit baseline-rigor tiering (`Tier 1`–`Tier 4`) isolates true coordination regimes (`RQ1`/`RQ2`) from failure dynamics (`RQ3`) and measurement artifacts (`RQ4`). |
| **Fit to #1 ACM CSUR** | CSUR rejects chronological paper catalogs and demands an original multi-axis analytical taxonomy plus explicit *Methods*-section disclosure of AI/tooling methodology. Our protocol enforces a falsifiable **4-Axis Taxonomy** (`Coordination Topology × Baseline/Compute Rigor × Task Structure × Failure/Validity Regime`) while keeping empirical counts cleanly separated from paywalled uncertainty. |
| **Fit to #2 TMLR** | TMLR Criterion 1 audits strict *claims–evidence parity*, and *Survey Certification* rewards non-overlapping operational vocabularies and candid limitation framing. Embedding `QA1`–`QA7`, explicit `Tier 1`–`Tier 4` baseline controls, upfront terminological gating, and separate OpenReview rejection-case auditing directly operationalizes TMLR's review standards. |
| **Fit to #3 AIRE** | AIRE explicitly favors PRISMA 2020 checklists, numbered RQs, corpus flow diagrams, and Table 1 prior-survey comparison matrices. This protocol natively yields all PRISMA audit artifacts while establishing sharp analytical differentiation from AIRE's three recent general agentic surveys (*Ala'anzy et al. 2026*; *Chowa et al. 2026*; *Abou Ali et al. 2025/2026*). |

### 1.3 PRISMA 2020 Flow Tracking Template *(Pre-Execution State)*

```text
+-----------------------------------------------------------------------------+
| PRISMA 2020 IDENTIFICATION & SCREENING FLOW (TO BE POPULATED IN PHASE 5)    |
+-----------------------------------------------------------------------------+
| Identification:                                                             |
|   - Records retrieved via Boolean Queries Q1-Q6:      [Pending Phase 5]     |
|   - Records added via backward/forward snowballing:   [Pending Phase 5]     |
|   - Duplicate / preprint-to-archival records merged:  [Pending Phase 5]     |
|   = Unique candidate records entering Stage 1:        [Pending Phase 5]     |
+-----------------------------------------------------------------------------+
| Screening Stage 1 (Title, Abstract & Venue Metadata):                       |
|   - Records screened independently (Agent 3 & Agent 6): [Pending Phase 5]   |
|   - Stage 1 exclusions logged by E1-E8 codes:           [Pending Phase 5]   |
|   - Pre-arbitration Stage 1 inter-rater kappa:          [Pending Phase 5]   |
+-----------------------------------------------------------------------------+
| Eligibility Stage 2 (Full Text / Verified Open Summary):                    |
|   - Records assessed for full eligibility:              [Pending Phase 5]   |
|   - Stage 2 exclusions logged by E1-E8 (incl. E5):      [Pending Phase 5]   |
|   - Pre-arbitration Stage 2 inter-rater kappa:          [Pending Phase 5]   |
+-----------------------------------------------------------------------------+
| Included Studies (Stratified Synthesis Corpus):                             |
|   - Primary Comparative Effectiveness & Topology (RQ1/RQ2): [Pending Ph. 5] |
|   - Mechanistic Failure & Conformity Studies (RQ3):         [Pending Ph. 5] |
|   - Evaluation-Validity & Reliability Audits (RQ4):         [Pending Ph. 5] |
|   - Separate Status-Bounded Audit Records (Rejected/Withdrawn): [Pending]   |
|   * Sensitivity Breakdown: Peer-Reviewed Archival vs. +Qualified Preprints  |
+-----------------------------------------------------------------------------+
```

---

## 2. Objectives, RQ1–RQ4 Operational Mapping & Conceptual Definitions

### 2.1 Review Objectives
1. **O1 (Compute-Normalized Effectiveness):** Determine under which task structures, backbone capability regimes, and inference-budget controls LLM-based multi-agent systems outperform, match, or underperform strong single-agent baselines (`RQ1`).
2. **O2 (Topology, Scaling & Amortization):** Map how coordination topologies, communication pruning, and agent scaling affect effectiveness, inference token overhead, upfront search/training amortization cost, and end-to-end wall-clock latency (`RQ2`).
3. **O3 (Mechanistic Failure Explanation):** Synthesize quantitative empirical mechanisms—inter-agent error amplification, conformity/sycophancy collapse, handoff information loss, and specification/verification failures—accounting for MAS degradation (`RQ3`).
4. **O4 (Evaluation-Validity Audit):** Quantify how experimental confounders (`C1`–`C6`), harness fragility, benchmark leakage, and multi-run reliability decay (`pass^k`) distort published MAS-vs.-SAS claims (`RQ4`).

### 2.2 Operational Mapping of RQ1–RQ4 to Extraction Schema, Comparators & Synthesis Strata

| RQ | Core Analytical Question | Mapped Extraction Fields (`data/extraction_schema.json`) | Required Comparator Standard | Synthesis Strata & Analytical Outputs |
| :--- | :--- | :--- | :--- | :--- |
| **RQ1** | Under what task structures, base-model capability regimes, and compute- or token-budget conditions do LLM-MAS outperform, match, or underperform single-agent baselines? | `F03` (`year`), `F04` (`publication_status`), `F05` (`rq_mapping`), `F07` (`architecture_and_agent_count`), `F10` (`datasets_and_benchmarks`), `F11` (`experimental_setup`), `F12` (`baselines_and_rigor_tier`), `F14` (`reported_numerical_outcomes`), `F16` (`cost_and_latency`) | **Tier 1–4 SAS Baseline Rigor Framework** (comparing MAS against `Self-Consistency` / `Best-of-N`, `Few-Shot CoT`, `Agentless`/`ReAct`, or flagging weak/absent SAS). | Within-study paired $\Delta_{\text{MAS-SAS}}$ & direction verdicts (`MAS > SAS`, `MAS ≈ SAS`, `MAS < SAS`) stratified by: (a) Baseline Rigor Tier (`1` vs. `2–4`), (b) Task Structure (`Decomposable` vs. `Sequential`), (c) Backbone Tier & Heterogeneity, (d) Publication Status. |
| **RQ2** | How do coordination topologies and communication paradigms relate to effectiveness, inference token overhead, amortized optimization cost, and latency? | `F07` (`topology_class`, `agent_count_n`), `F08` (`coordination_and_communication_method`), `F09` (`role_specialization`), `F10` (`task_structure_type`), `F12` (`baselines_and_rigor_tier`), `F14` (`paired_comparisons`, `diagnostic_or_topology_outcomes`), `F16` (`cost_and_latency`) | Strong SAS comparator (`Tier 1`/`Tier 2`) **AND/OR** explicit within-study multi-topology comparators (`Independent` vs. `Centralized` vs. `Dense Debate` vs. `Sparse Learned DAG`), auditing search-cost inclusion. | Topology × Task-Structure × Amortization Cross-Tabulation; separation of test-time inference cost vs. upfront MCTS/RL/VGAE search cost ($Q_{\text{break-even}}$ transparency); critical-path latency vs. token volume analysis. |
| **RQ3** | Which empirically documented mechanisms—error amplification, conformity/sycophancy cascades, handoff loss, and specification/verification failures—account for MAS degradation? | `F07` (`topology_class`), `F08` (`interaction_paradigm`), `F10` (`verifier_availability`), `F13` (`diagnostic_or_validity_metrics`), `F14` (`diagnostic_or_topology_outcomes`), `F15` (`significance_tests_and_p_values`), `F17` (`reported_successes_and_failures`) | Within-study MAS-vs.-SAS error-amplification comparators, controlled conformity/debate ablations, or multi-agent trajectory attribution benchmarks (`MAST`, `Who&When`, `TRAIL`, `TraceElephant`). | Mechanistic Failure-Linkage Matrix mapping failure modes onto topology classes; strict separation of **inter-agent coordination faults** (*MAST*, *Who&When*) from **intra-agent single-loop module faults** (*AgentDebug*). |
| **RQ4** | To what extent do experimental confounders—unmatched compute, asymmetric prompting, harness fragility, `pass^k` decay, and leakage—distort reported MAS comparisons? | `F04` (`publication_status`), `F11` (`prompt_parity_status`, `tool_execution_parity_status`), `F12` (`sas_baseline_rigor_tier`), `F13` (`process_proxy_metrics`), `F15` (`variance_cis_and_stats`), `F18` (`limitations_and_validity_threats`), `F19` (`quality_appraisal_and_evidence_provenance`) | Audit metrics (`pass@1` vs. `pass^k`, strict-EM deltas, `EvalPlus`/`PatchDiff` inflation, ABC skew, VTFR) + compliance scoring across all included `RQ1`–`RQ3` studies + bounded OpenReview rejection audits. | `QA1`–`QA7` Quality & Risk-of-Bias Matrix across corpus; incidence rates of **Six-Class Confounders (`C1`–`C6`)**; benchmark hazard table; separate *Documented Peer-Review Failure / Rejection-Case Audit*. |

### 2.3 Four-Tier SAS Baseline Rigor Framework (Comparator Coding Standard)
Every comparative primary experiment coded under `F12` (`sas_baseline_rigor_tier`) is classified strictly into one mutually exclusive tier:
* **Tier 1 (Gold — Compute/Token-Matched Strong SAS):** Evaluates MAS and a strong single-agent baseline (`Self-Consistency` / `Best-of-N`, `Few-Shot CoT`, or tool-equivalent single-agent/deterministic scaffold such as `Agentless`) on the **identical LLM backbone(s) and evaluation harness**, holding total inference tokens (prompt + reasoning + completion), sample calls, or API USD expenditure equivalent within an explicit parity protocol (e.g., $\pm 10\%$ tolerance or matched iso-cost Pareto sweeps).
* **Tier 2 (Partial — Strong SAS, Unmatched Compute or Unamortized Search):** Includes a competitive SAS baseline on the same backbone and harness, **but** allows unmatched total token/call budgets favoring MAS (e.g., $3\times$–$15\times$ extra inference tokens without matched SAS sampling) OR omits upfront search/training compute (MCTS/RL/VGAE/prompt optimization) from cost parity.
* **Tier 3 (Weak — Single-Pass Zero-Shot SAS Only):** Benchmarks MAS solely against a single greedy ($N=1$) zero-shot single-LLM pass, leaving outcomes exposed to $1\times$-vs.-$k\times$ sample scaling and zero-shot prompt weakness (*Wang et al.*, ACL 2024).
* **Tier 4 (Invalid or Absent LLM SAS Comparator):** Provides no contemporary LLM single-agent comparator on the same benchmark/harness (e.g., evaluates MAS solely against unpruned dense MAS, classical RL baselines such as PPO/PBT, or human annotators without LLM cost parity).
* **N/A (Non-Comparative Diagnostic/Validity Study):** Reserved strictly for `RQ3` trace-attribution datasets/audits (e.g., *MAST*, *Who&When*, *TRAIL*) and `RQ4` benchmark-harness audits (e.g., *PatchDiff*, *ABC*, *BenchJack*) that do not assert MAS-over-SAS architectural superiority.

### 2.4 Core Conceptual Definitions & Terminological Hygiene
To prevent the conceptual blurring penalized in recent OpenReview evaluations (e.g., *La Malfa et al.*, NeurIPS 2025 `FfsxgSZW0c`; TMLR `CTr3bovS5F` and Desk-Rejects documented in [Deliverable_A_Journal_Intelligence_Report.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/deliverables/Deliverable_A_Journal_Intelligence_Report.md#L70)), this protocol standardizes four core concepts:
1. **Single-Agent System (`SAS`):** A single LLM execution locus (including single-pass zero/few-shot `CoT`, multi-sample `Self-Consistency` / `Best-of-N` voting from one model/prompt distribution, `Self-Refine`, or a single-agent `ReAct`/tool-execution loop) operating without inter-agent role splitting or distinct interacting peer/subordinate LLM instances.
2. **LLM-Based Multi-Agent System (`LLM-MAS`):** A system comprising $N \ge 2$ logically distinct LLM agent instances—differentiated by explicit role personas, isolated context windows/states, specialized tool privileges, or heterogeneous model backbones—coordinating on a shared task. Within `LLM-MAS`, extraction strictly distinguishes:
   * **Interactive / Stateful LLM-MAS:** Multi-turn peer debate, sequential SOP handoffs, centralized orchestrator-worker delegation, or adaptive DAG execution where agents condition subsequent reasoning/actions on intermediate peer messages or shared state.
   * **Parallel / Voting LLM Collectives (`Independent / Voting Ensemble`):** $N \ge 2$ parallel LLM instances/personas generating independent proposals merged via voting, ranking, or synthesis layers (e.g., *Agent Forest*, *MoA* layers). Included explicitly as a boundary baseline stratum to test whether multi-agent interaction adds value over single-agent `Self-Consistency` (`Self-MoA`), and **never** conflated with stateful interactive deliberation.
3. **Inference Compute vs. Amortized Optimization Cost:** *Inference Compute* covers all prompt, hidden reasoning/thinking, and completion tokens (plus USD API spend and API call counts) incurred during test-time task execution. *Amortized Optimization Cost* covers all upfront tokens, GPU-hours, and USD API spend incurred to search, train, or evolve workflows, communication masks, GNN/VGAE decoders, or router policies prior to test-time deployment.
4. **Conditional Empirical Association vs. Universal Law:** Observed scaling thresholds (such as capability-saturation cutoffs or amplification multipliers across tested architectures and benchmarks) are strictly synthesized as **conditional empirical associations** bounded by tested LLM generations, task types, and harnesses—never generalized as invariant physical laws.

### 2.5 Terminological & Scope Exclusion Gate

| Candidate System / Study Type | Gate Decision | Precise Operational Boundary Rule |
| :--- | :--- | :--- |
| **Interactive/Stateful LLM-MAS** (`MetaGPT`, `AutoGen`, `MAD`, `AFlow`, `G-Designer`, `MacNet`, `Orchestrator-Worker`) | **ADMIT** | $N \ge 2$ distinct LLM instances exchanging state, critiques, artifacts, or sub-tasks across sequential, centralized, decentralized, or learned graph topologies. |
| **Parallel / Voting LLM Collectives** (`Agent Forest`, `MoA`, `Self-MoA`) | **ADMIT (Boundary Stratum)** | Tagged strictly as `Independent/Voting Ensemble` under `F07`/`F08`; used to isolate pure sampling/heterogeneity effects vs. interactive coordination. |
| **Single-LLM Prompt Chains / Hard-Coded Single-Model Pipelines** | **EXCLUDE (`E3` / `I4`)** | Sequential prompt chaining within one logical model/context lacking distinct agent roles, independent state boundaries, or inter-agent interaction (*La Malfa et al.*, NeurIPS 2025). *(Note: Deliberate single-LLM simulation baselines like `OneFlow` tested *against* MAS qualify as the `SAS` comparator inside a comparative study.)* |
| **Single-Query Weak-to-Strong Model Routers** (`RouteLLM`, `AutoMix`, `Hybrid LLM`, `RouterBench`) | **EXCLUDE (`E3`)** | Per-query selection among single models without multi-agent collaboration or `SAS→MAS` escalation. *(Exception: Studies explicitly modeling `SAS→MAS` escalation or intra-MAS routing against MAS/SAS baselines, e.g., `CascadeDebate`, `MasRouter`, `Gao et al. 2025`, are admitted.)* |
| **Classical Non-LLM Swarm Intelligence & Classical MAS** (`ACO`, `PSO`, `Boids`, `BDI`, `FIPA`, `PPO/QMIX MARL`, checkpoint weight-space PSO) | **EXCLUDE from Primary Pooling (`E2`)** | Excluded from empirical quantitative synthesis due to benchmark and compute-modality disjointness; cited solely in Section 2 *Technical Background & Terminological Hygiene*. |
| **Standalone Single-Agent Security / Prompt Tuning Without MAS Analysis** | **EXCLUDE (`E3` / `E7`)** | Single-agent indirect prompt-injection benchmarks (`AgentDojo`, `InjecAgent`, `ASB`) or standalone single-agent RAG/prompt tuning lacking MAS comparators are excluded from primary synthesis. |

---

## 3. Search Strategy, Sources, Date Bounds & Reproducible Query Strings

### 3.1 Temporal Window & Search Date
* **Planned Formal Search Date:** `November 20, 2026` (Phase 5 execution timestamp).
* **Primary Empirical & Diagnostic Inclusion Window:** `January 1, 2023 – November 20, 2026` (capturing the modern post-GPT-4/ChatGPT LLM-MAS empirical wave through November 2026 proceedings and preprints).
* **Pre-2023 Foundational Works:** Classical MAS (`BDI`, `FIPA`, `Contract Net`), Swarm Intelligence (`ACO`, `PSO`, `Boids`), and SLR methodology references (`PRISMA 2020`, `Kitchenham & Charters 2007`) may be cited exclusively as conceptual/methodological background and are never counted as primary included studies.

### 3.2 Sources Accessed & Explicit Database / Paywall Boundaries

#### A. Open-Web Sources Accessed (via `search_web` & Verified Public Endpoints)
1. **Preprint & Open Archive Servers:** `arXiv` (`arxiv.org`: `cs.CL`, `cs.AI`, `cs.MA`, `cs.SE`, `cs.LG`), `Preprints.org` (admitted only when complete empirical full text and verification metadata resolve).
2. **Open Peer-Review & Archival Proceedings Portals:** `OpenReview` (`openreview.net` — TMLR, ICLR, NeurIPS, ICML accepted papers, active submissions, and public rejection/withdrawal logs), `ACL Anthology` (`aclanthology.org` — ACL, EMNLP, NAACL, EACL, AACL, Findings), `NeurIPS Proceedings` (`proceedings.neurips.cc`), `PMLR` (`proceedings.mlr.press` — ICML, etc.), and `JMLR / TMLR` (`jmlr.org/tmlr`).
3. **Publisher Metadata & Open-Access Mirrors:** `ACM Digital Library` (`dl.acm.org` — noting CSUR transitioned to 100% Open Access on Jan 1, 2026), `SpringerLink` (`link.springer.com` — AIRE, JAAMAS metadata and OA articles), `IEEE Xplore` (`ieeexplore.ieee.org` — IEEE TSE/conference metadata and OA articles), `ScienceDirect` (`sciencedirect.com`), and `Nature Portfolio` (`nature.com` — *Nature Machine Intelligence* metadata/OA).
4. **Academic Web Discovery Indexes:** `Semantic Scholar` (`semanticscholar.org`) and `Google Scholar` web indexing (`scholar.google.com` search snippets) for cross-venue resolution and one-hop forward citation snowballing.

#### B. Explicitly Documented Inaccessible Databases & Access Limitations
* **No Scopus or Web of Science Bulk Exports:** Direct subscription API access or bulk CSV/BibTeX exports from **Scopus** and **Clarivate Web of Science (WoS)** are **unavailable** in our execution environment. This protocol explicitly refrains from claiming comprehensive Scopus/WoS indexing coverage.
* **Paywalled Non-Open-Access Full Texts:** Closed-access full-text PDFs behind publisher paywalls (`SpringerLink`, `IEEE Xplore`, `ScienceDirect`, `Nature`, or pre-2026 `ACM DL`) that lack an author self-archived PDF, institutional OA mirror, or verified `arXiv`/`OpenReview` preprint cannot be parsed beyond publicly indexed titles, abstracts, and search snippets.
* **Operational Rule for Paywalled Records:** Any paywalled study lacking an accessible open full-text version that leaves methodology or primary numerical outcomes unverifiable is excluded at Stage 2 under code `E5`. Where a peer-reviewed paywalled paper is matched to a verified open `arXiv` preprint, any field confirmed only in the preprint vs. missing from publisher snippets is transparently recorded via `access_level` (`F02`) and `"not verifiable from accessible open summary"`.

### 3.3 Reproducible Boolean Search Strings (`Q1`–`Q6`)
All six Boolean queries are executed on `November 20, 2026` with temporal filtering constrained to `2023–2026` (`2023-01-01` to `2026-11-20`). Platform syntax operators (`site:`, parentheses, quotation marks) are adapted minimally per repository search interface while preserving identical logical terms and logged verbatim in Phase 5 search logs.

* **`Q1` — SAS-vs.-MAS Compute/Token-Matched Empirical Benchmarks (`RQ1`):**
  ```text
  ("multi-agent" OR "multiagent" OR "multi-agent debate" OR "agent collaboration")
  AND ("LLM" OR "large language model" OR "language agent")
  AND ("single-agent" OR "single agent" OR "self-consistency" OR "chain-of-thought" OR "vanilla CoT")
  AND ("token budget" OR "compute-matched" OR "equal compute" OR "inference cost" OR "cost-accuracy" OR "outperform" OR "underperform")
  ```
* **`Q2` — Coordination Topologies, Pruning, Scaling & Amortization (`RQ2`):**
  ```text
  ("multi-agent" OR "LLM-MAS" OR "agentic workflow")
  AND ("LLM" OR "large language model")
  AND ("topology" OR "communication graph" OR "pruning" OR "orchestration" OR "decentralized" OR "centralized" OR "hierarchical")
  AND ("token reduction" OR "token overhead" OR "latency" OR "scaling" OR "MCTS" OR "GNN" OR "amortized" OR "search cost")
  ```
* **`Q3` — Inter-Agent Error Propagation, Conformity, Cascades & Attribution (`RQ3`):**
  ```text
  ("multi-agent" OR "multi-agent debate" OR "LLM agents")
  AND ("LLM" OR "large language model")
  AND ("error propagation" OR "error amplification" OR "cascading failure" OR "conformity" OR "sycophancy" OR "consensus collapse" OR "diversity collapse" OR "failure attribution" OR "root cause" OR "trajectory")
  ```
* **`Q4` — Evaluation Validity, `pass^k`, Harness Fragility & Reliability Audits (`RQ4`):**
  ```text
  ("LLM agent" OR "multi-agent" OR "agentic benchmark")
  AND ("pass^k" OR "pass@k" OR "multi-run" OR "reliability" OR "harness" OR "reward hacking" OR "benchmark leakage" OR "exact match" OR "SWE-bench" OR "tau-bench" OR "WebArena" OR "verification transport")
  ```
* **`Q5` — Terminological Boundary & Selective SAS-to-MAS Escalation (`Gate / Mitigation`):**
  ```text
  ("LLM" OR "large language model")
  AND (("swarm intelligence" OR "classical MAS" OR "prompt chaining" OR "emergent coordination")
       OR ("selective escalation" OR "uncertainty-aware delegation" OR "single-to-multi" OR "masrouter" OR "cascadedebate"))
  ```
* **`Q6` — Venue-Targeted & Public Peer-Review / OpenReview Audit Query (`RQ4 & Status Verification`):**
  ```text
  (site:openreview.net OR site:aclanthology.org OR site:proceedings.neurips.cc OR site:proceedings.mlr.press OR site:dl.acm.org)
  AND ("multi-agent" OR "multiagent")
  AND ("large language model" OR "LLM")
  AND ("single-agent" OR "failure" OR "debate" OR "topology" OR "benchmark")
  AND ("2023" OR "2024" OR "2025" OR "2026")
  ```

### 3.4 Backward and Forward Citation Snowballing Protocol
In addition to queries `Q1`–`Q6`, Phase 5 executes **one-hop backward snowballing** (screening reference lists) and **one-hop forward snowballing** (screening Semantic Scholar / Google Scholar citing records through `November 20, 2026`) anchored on the verified Phase 2 seed papers and prior overlapping surveys:
* **Compute-Matched SAS-vs.-MAS Anchors:** *Kim et al.* (`arXiv:2512.08296`, *Nature Machine Intelligence* 2026); *Tran & Kiela* (`arXiv:2604.02460`); *Xu et al.* (`OneFlow`, `arXiv:2601.12307`); *Smit et al.* (ICML 2024, `arXiv:2311.17371`); *Wang et al.* (ACL 2024, `arXiv:2402.18272`); *Kapoor et al.* (TMLR 2024, `arXiv:2407.01502`); *Li et al.* (`Self-MoA`, TMLR 2026, `arXiv:2502.00674`).
* **Topology & Amortization Anchors:** *Qian et al.* (`MacNet`, ICLR 2025, `arXiv:2406.07155`); *Zhuge et al.* (`GPTSwarm`, ICML 2024); *Zhang et al.* (`AgentPrune`, ICLR 2025, `arXiv:2410.02506`); *Zhang et al.* (`G-Designer`, ICML 2025); *Zhang et al.* (`AFlow`, ICLR 2025, `arXiv:2410.10762`).
* **Failure, Conformity & Attribution Anchors:** *Cemri et al.* (`MAST`, NeurIPS 2025, `arXiv:2503.13657`); *Zhang et al.* (`Who&When`, ICML 2025, `arXiv:2505.00212`); *Zhang et al.* (`AgenTracer`, ICLR 2026, `arXiv:2509.03312`); *Zhu et al.* (`AgentDebug`, ICML FAGEN Workshop, `arXiv:2509.25370`); *Choi et al.* (ACL 2025, `arXiv:2506.01332`); *Pitre et al.* (`CONSENSAGENT`, ACL Findings 2025).
* **Evaluation Validity & Terminological Anchors:** *Yao et al.* ($\tau$-bench, ICLR 2025, `arXiv:2406.12045`); *Rabanser et al.* (ICML 2026, `arXiv:2602.16666`); *Zhu et al.* (ABC, `arXiv:2507.02825`); *Wang et al.* (`PatchDiff`, ICSE 2026, `arXiv:2503.15223`); *Sheshanarayana & Goli* (VTFR, NeurIPS 2026 Workshop, `arXiv:2611.18471`); *La Malfa et al.* (NeurIPS 2025, `FfsxgSZW0c`).
* **Prior Overlapping Surveys (Backward Snowballing + Table 1 Differentiation Only):** *Li et al.* (`10.20944/preprints202609.1639.v1`), *Motger et al.* (`arXiv:2607.26212`), *Yue et al.* (`arXiv:2603.22386`), *Wang et al.* (IEEE TSE 2026), *Yehudai et al.* (`arXiv:2503.16416`), plus CSUR/AIRE surveys cataloged in Deliverables A and B.

---

## 4. Eligibility Criteria (`I1`–`I6`, `E1`–`E8`) & Publication-Status Stratification

### 4.1 Inclusion Criteria (`I1`–`I6`)
A study is admitted to the primary synthesis corpus **only if** it satisfies `I1`, `I3`, `I4`, `I5`, `I6`, and at least one empirical pathway in `I2`:

| Code | Criterion Name | Operational Requirement |
| :--- | :--- | :--- |
| **`I1`** | **Temporal & Language Window** | Publicly posted, accepted, or published between `January 1, 2023` and `November 20, 2026`, in English. |
| **`I2`** | **LLM-MAS Subject & Analytical Pathway** | Evaluates an LLM-based MAS ($N \ge 2$ LLM instances) and fulfills at least one pathway: **(a) Comparative Effectiveness (`RQ1`/`RQ2`):** head-to-head quantitative comparison of `LLM-MAS` vs. `SAS` or across `LLM-MAS` coordination topologies/scales; **(b) Failure Diagnosis (`RQ3`):** quantitative analysis of inter-agent error propagation, conformity/sycophancy collapse, handoff loss, or MAS trajectory attribution; OR **(c) Evaluation-Validity Audit (`RQ4`):** empirical harness, `pass^k`, leakage, or verification-transport audit directly governing agentic/MAS evaluation (coded strictly under the Diagnostic/Validity track). |
| **`I3`** | **Primary Quantitative Evidence** | Reports empirical experimental methodology and concrete quantitative metrics (accuracy, EM, `pass@1`/`pass^k`, resolve rate, failure incidence/attribution accuracy, propagation probability, ASR, or token/USD/latency measurements). |
| **`I4`** | **Terminological Integrity Gate** | Passes Section 2.5's exclusion gate (genuine interactive/stateful LLM-MAS or explicitly tagged parallel voting collective, not a single-LLM prompt chain or non-LLM heuristic). |
| **`I5`** | **Accessible Empirical Verification** | Open-access full text (`arXiv`, `OpenReview`, `ACL Anthology`, `PMLR`, `JMLR/TMLR`, OA publisher page) OR verified open empirical summary/rebuttal record sufficient to extract methodology, comparators, and outcomes without fabricating missing numbers. |
| **`I6`** | **Eligible Publication Status** | Holds an eligible status under Section 4.3 (`Peer-reviewed journal`, `Peer-reviewed conference`, `Workshop`, or `Preprint` passing `QA1`–`QA7` verification). |

### 4.2 Exclusion Criteria (`E1`–`E8`)
Any single condition below triggers immediate exclusion (with exact `E`-code logged in Stage 1 or Stage 2 screening ledgers):

| Code | Exclusion Criterion | Operational Rule |
| :--- | :--- | :--- |
| **`E1`** | **Out of Date / Language Scope** | Published/posted before `January 1, 2023` (except background terminology) or lacking an English full text/verified English record. |
| **`E2`** | **Classical / Non-LLM Systems Only** | Classical Swarm Intelligence (`ACO`, `PSO`, `Boids`), classical symbolic `BDI`/`FIPA` MAS, pre-LLM `MARL` (`PPO`/`QMIX`), or weight-space checkpoint PSO without communicating inference-time agents. |
| **`E3`** | **Single-Agent Only / Prompt Chain / Pure Single-Query Router** | Evaluates solely single-LLM prompting/RAG, sequential single-LLM prompt chains, or single-query model selectors (`RouteLLM`, `AutoMix`) without an MAS comparator or `SAS→MAS` escalation (unless admitted strictly as an `RQ4` harness/reliability audit under `I2(c)`). |
| **`E4`** | **Non-Empirical / Secondary Survey / Unbenchmarked Position** | Surveys, opinion/position essays without quantitative experiments, or qualitative system proposals lacking empirical metrics (retained strictly for background/differentiation and backward snowballing). |
| **`E5`** | **Inaccessible Full Text or Unverified Identifier** | Paywalled publisher records lacking any open-access mirror/preprint where methodology or numerical outcomes cannot be verified, OR non-resolving/broken candidate identifiers (e.g., unresolvable arXiv IDs or unverified forum hashes). |
| **`E6`** | **Duplicate / Superseded Version** | Duplicate index hit or earlier `arXiv` preprint superseded by an included peer-reviewed archival publication of the same study (excluded as a duplicate record and linked to the primary archival ID). |
| **`E7`** | **Ungrounded Proxy Metric Only / Out-of-Scope Security Niche** | Reports solely process proxies (e.g., disagreement counts) divorced from downstream task outcomes, or standalone single-agent indirect prompt-injection benchmarks lacking MAS topology/coordination analysis. |
| **`E8`** | **Disqualified Status (`Withdrawn` / `Publicly rejected` / `Retracted`)** | Excluded from all primary architectural effectiveness synthesis (`RQ1`–`RQ3`), subject only to the strictly bounded `RQ4` audit exceptions defined in Section 4.3. |

### 4.3 Publication-Status Stratification & Synthesis Rules
Every candidate record is coded (`F04`) under one of eight exact status labels and never upgraded or conflated across tiers:

| Publication Status (`F04`) | Verification Requirement | Synthesis Inclusion & Stratification Rule |
| :--- | :--- | :--- |
| **1. `Peer-reviewed journal`** | Verified acceptance/publication in a refereed archival journal (e.g., *Nature Machine Intelligence*, *TMLR*, *ACM CSUR*, *IEEE TSE*, *JAIR*, *AIRE*). | **Tier A Archival Core.** Included in primary synthesis and in the **Peer-Reviewed Archival Only** baseline stratum. |
| **2. `Peer-reviewed conference`** | Verified acceptance in refereed conference proceedings or official *Findings* (*NeurIPS*, *ICML*, *ICLR*, *ACL*, *EMNLP*, *NAACL*, *AACL*, *COLM*, *ICSE*). Must not rely on unverified submission links. | **Tier A Archival Core.** Included in primary synthesis and in the **Peer-Reviewed Archival Only** baseline stratum. |
| **3. `Workshop`** | Verified workshop acceptance (e.g., *ICML FAGEN*, *ICML UQ Workshop*, *NeurIPS Scaling Environments / Who Verifies the Agents?*, *KDD Agentic AI Eval*). | **Tier B Non-Archival Peer-Reviewed.** Eligible for `RQ3`/`RQ4` diagnostic evidence and sensitivity-tested separately from Tier A archival proceedings. |
| **4. `Preprint (arXiv / Preprints.org)`** | Unrefereed public preprint verified against active repository metadata (including papers whose OpenReview submission status is unverified/pending). | **Tier C Non-Peer-Reviewed.** Admitted to primary synthesis **ONLY** if verified full-text/open methodology passes `QA1`–`QA7` appraisal (`>= 6/14` or `>= 6/12` diagnostic; and passes `QA7 >= 1`) and no withdrawal/rejection overrides it. **Always reported distinctly from Tier A** via mandatory dual sensitivity analysis (*Peer-Reviewed Only* vs. *Peer-Reviewed + Qualified Preprints*). |
| **5. `Under review`** | Active double-blind OpenReview / ACL ARR submission without final public decision (e.g., TMLR `SMe5HYmSff`, TMLR Paper `10674`). | **Tracked Separately (Hold / Watchlist).** Excluded from peer-reviewed claims; admitted under `Preprint` rules only if an open de-anonymized empirical preprint independently passes `QA1`–`QA7`. **Never** mislabeled accepted. |
| **6. `Withdrawn`** | Verified author withdrawal on OpenReview/venue portal (e.g., TMLR `3hXEPbG0dh`, *SwarmBench* ICLR 2026 withdrawal, `ICLR 2026 Sub #8079`). | **Excluded from ordinary primary effectiveness claims (`E8`).** Never labeled "rejected." If an open `arXiv` text remains public, it may be cited transparently only as methodological/status-boundary evidence (noting explicit withdrawal date). |
| **7. `Publicly rejected`** | Verified public rejection record (e.g., OpenReview TMLR Paper `7332` *AgenticNet*, TMLR Sub `7253` *Inducing Disagreement*, TMLR Paper `9844`). | **Excluded from positive architectural evidence (`E8`).** Eligible **strictly** inside a separate **Documented Peer-Review Failure / Rejection-Case Audit** under `RQ4` (e.g., exposing exact-match drops or proxy-metric dissociation), explicitly labeled `[Rejected]`. |
| **8. `Retracted`** | Formally retracted by publisher or repository. | **Excluded from all scientific support (`E8`).** Flagged solely if the retraction notice itself documents methodological or benchmark fabrication relevant to `RQ4`. |

---

## 5. Deduplication, Two-Stage Dual Screening & Conflict Resolution

### 5.1 Deduplication & Preprint-to-Archival Linkage Rules
1. **Canonical Key Generation:** Normalize every retrieved candidate by `arXiv ID` (stripping version suffixes `v1`, `v2`, etc.), `DOI`, `OpenReview forum/submission ID`, `ACL Anthology ID`, and lowercased `title + first author surname`.
2. **Preprint-to-Archival Resolution Rule:** When an `arXiv` preprint matches a subsequent peer-reviewed publication (*NeurIPS*, *ICLR*, *ICML*, *ACL*, *TMLR*, *Nature Machine Intelligence*), collapse both into **one unique study record**:
   * **Always retain the peer-reviewed archival publication as the primary record** (`F01`/`F04`).
   * Cross-link the matched `arXiv ID` inside `linked_preprint_or_prior_version_ids` (`F01`).
   * If the publisher proceedings version is paywalled (`SpringerLink`/`IEEE`/`Nature`) while the linked `arXiv` preprint is open access, extract full-text tables from the open preprint only after verifying title/method correspondence, set `access_level = "open_preprint_mirror"`, and record any final-version uncertainty as `"not verifiable from accessible open summary"`.
3. **Longitudinal Resubmission Tracking:** If an OpenReview record was previously rejected or withdrawn at one venue and subsequently accepted at a later archival venue (e.g., ICLR 2024 Reject → NeurIPS 2024 Accept; ICLR 2024 Withdrawn → NAACL Findings Accept), count the study **once** under its final accepted venue and record the prior submission ID in `linked_preprint_or_prior_version_ids`.

### 5.2 Two-Stage Dual Screening Workflow
* **Stage 1 — Title, Abstract & Venue Metadata Screening:**
  * *Inputs:* Title, abstract, publication year, venue/repository metadata, OpenReview decision tag.
  * *Gates Evaluated:* `I1`, initial `I2`, initial `I4` (Terminological Exclusion Gate), `E1`–`E4`, `E6`, `E8`.
  * *Rule:* Any record that is ambiguously relevant or where baseline details are omitted from the abstract advances conservatively to Stage 2.
* **Stage 2 — Full-Text / Verified Open-Summary Eligibility Assessment:**
  * *Inputs:* Open-access full text (or verified OpenReview manuscript/rebuttal record when publisher PDF is inaccessible).
  * *Gates Evaluated:* Full `I1`–`I6` and `E1`–`E8`, `access_level` coding (`F02`), `Publication Status` verification (`F04`), and preliminary `RQ1`–`RQ4` assignment (`F05`).
  * *Audit Trail:* Every excluded Stage-2 record receives a specific `E1`–`E8` code plus a one-sentence verifiable justification referencing the inspected source URL.

### 5.3 Independent Dual Screening & Arbitration Governance
* **Primary Screener:** **Agent 3** (Literature Discovery Specialist) independently screens 100% of deduplicated records at Stage 1 and Stage 2.
* **Independent Second Screener:** **Agent 6** (Systematic Review Methodologist) independently screens 100% of deduplicated records at Stage 1 and Stage 2 without viewing Agent 3's votes prior to lock-in.
* **Inter-Rater Reliability Metrics:** Compute raw percent agreement and Cohen's $\kappa$ separately at Stage 1 and Stage 2 prior to reconciliation, and report both values in Phase 5/final manuscript Methods.
* **Conflict Resolution:** All Stage 1 and Stage 2 discrepancies (eligibility, `I4` terminological gate boundaries, `Publication Status` labels, or `E5` paywall determinations) are compiled into a conflict log and adjudicated by **Agent 1 (Research Director)** strictly against Section 2.5 and Section 4 criteria. Unresolvable paywall ambiguities default conservatively to `E5`.

---

## 6. Quality Appraisal Rubric (`QA1`–`QA7`)

Every study admitted at Stage 2 undergoes independent methodological appraisal across **seven criteria (`QA1`–`QA7`)**, scored on a 3-point ordinal scale: **`2 = Fully Met`**, **`1 = Partially Met`**, **`0 = Not Met / Unreported`** (maximum comparative score = **14**).

> [!NOTE]
> **Handling Non-Comparative Diagnostic Studies (`RQ3`/`RQ4`):** Pure trajectory failure-attribution benchmarks (e.g., *MAST*, *Who&When*, *TRAIL*) and benchmark-validity audits (e.g., *PatchDiff*, *ABC*, *BenchJack*) do not evaluate a candidate MAS against an SAS baseline. For such non-comparative studies, `QA1` is coded `"N/A-Diagnostic"` (with `applicable_max_score = 12` across `QA2`–`QA7`) rather than artificially assigning `QA1 = 0`. Both raw scores and normalized percentages (`total_raw_score / applicable_max_score`) are reported.

| ID | Quality Criterion | Score `2` (Fully Met) | Score `1` (Partially Met) | Score `0` (Not Met / Unreported) |
| :--- | :--- | :--- | :--- | :--- |
| **`QA1`** | **Single-Agent Baseline Rigor** *(Paired with `Tier 1`–`Tier 4` code)* | Includes a **Tier 1** strong SAS baseline (`Self-Consistency`/`Best-of-N`, `Few-Shot CoT`, or tool-equivalent single-agent/deterministic pipeline) on identical backbone(s) and harness with compute/token/USD parity. | Includes a **Tier 2** strong SAS baseline with unmatched tokens or omitted search amortization, OR a **Tier 3** single-pass zero-shot SAS baseline only. | **Tier 4:** No LLM SAS baseline included (compares only against unpruned MAS, classical RL, or human annotation). *(`N/A-Diagnostic` if non-comparative.)* |
| **`QA2`** | **Token / Dollar Cost & Latency Accounting** | Reports both test-time compute/economic cost (total prompt + reasoning + completion tokens OR USD/task) **AND** wall-clock latency / critical-path execution rounds. | Reports only one cost axis (e.g., tokens or API calls without latency, relative `%` savings without absolute totals, or latency without tokens). | Omits both token/USD expenditure and wall-clock latency across compared systems. |
| **`QA3`** | **Amortization Transparency** | Uses zero upfront search/training (explicitly static zero/few-shot) **OR** uses MCTS/RL/VGAE/prompt optimization and explicitly reports upfront search/training token/USD cost and break-even analysis alongside inference cost. | Uses learned/searched topologies or routers and describes training qualitatively, but omits quantitative upfront search/training compute budgets from comparative cost tables. | Uses upfront optimization/search while presenting inference-only savings with zero disclosure or separation of search/training costs. |
| **`QA4`** | **Multi-Run Stochastic Reliability** | Reports outcomes across $k \ge 3$ independent seeds/runs with dispersion/uncertainty stats (SD, SE, 95% CI, IQR, or statistical tests) **OR** explicitly evaluates multi-trial consistency (`pass^k`). | Reports $k = 2$ runs, partial multi-seed subsets without dispersion metrics, or statistical tests only on secondary tables. | Single-run (`k = 1`) reporting with zero variance, CI, or `pass^k` measurement. |
| **`QA5`** | **Benchmark & Harness Integrity** | Enforces prompt and tool/execution-feedback parity between MAS and SAS, utilizes verified/hardened evaluation harnesses (`EvalPlus`, strict exact-match parsing, `SWE-bench Verified`/isolated sandboxes), and evaluates leakage or verifier validity. | Uses standard benchmarks without documented prompt/tool asymmetry, but lacks strict-parsing checks, prompt-sensitivity ablations, or contamination/leakage caveats. | Asymmetric tool/execution feedback favoring MAS, brittle/lenient string extraction, unmitigated harness/reward exploits, or unexamined benchmark leakage. |
| **`QA6`** | **Architectural & Prompt/Code Reproducibility** | Publicly releases runnable code, exact agent/system prompts, exact model snapshots/checkpoints, decoding hyperparameters, and communication graph specifications. | Releases partial code or prompt templates, or specifies architecture/model versions clearly while withholding full prompts/code/hyperparameters. | Closed/unspecified prompts, proprietary code, and ambiguous model versions preventing independent replication. |
| **`QA7`** | **Claims–Evidence Parity** *(TMLR Criterion 1)* | Abstract, introduction, and conclusions faithfully match reported tables, ablations, negative findings, and boundary constraints without overclaiming. | Minor framing over-generalization (e.g., broad "outperforms" wording from bounded zero-shot subsets) without direct table contradiction. | Direct claims–table contradiction, omitted negative ablations, or presenting process proxies (e.g., disagreement rate) as task effectiveness. |

### 6.1 Composite Rigor Bands & Risk-of-Bias Mapping
* **High Methodological Rigor / Low Risk of Bias:** `11–14 / 14` (`10–12 / 12` diagnostic; $\ge 78.0\%$).
* **Moderate Rigor / Moderate Risk of Bias:** `6–10 / 14` (`6–9 / 12` diagnostic; $42.5\%–77.9\%$).
* **Low Rigor / High Risk of Bias:** `0–5 / 14` (`0–5 / 12` diagnostic; $< 42.5\%$). Studies in this band are **never** cited as conclusive evidence of MAS effectiveness and are highlighted explicitly in `RQ4` validity audits.

---

## 7. 19-Field Data Extraction Schema, Missing Data, Synthesis Plan & Bias Assessment

### 7.1 19-Field Data Extraction Codebook (`F01`–`F19`)
The formal machine-validated JSON Schema (`Draft 2020-12`) governing all Phase 5/6 extraction records is saved at [extraction_schema.json](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/extraction_schema.json). Every extracted study record must populate all **19 top-level schema fields**:

| Field | JSON Key (`extraction_schema.json`) | Captured Information & Validation Constraints |
| :--- | :--- | :--- |
| **`F01`** | `bibliographic_and_identifiers` | `study_id`, `title`, `authors`, `venue`, `doi`, `arxiv_id`, `openreview_id`, `acl_anthology_id`, and `linked_preprint_or_prior_version_ids` (for deduplicated preprint-to-archival links). |
| **`F02`** | `source_provenance` | `verified_url` (URI), `access_level` (`open_full_text_pdf`, `open_html_proceedings`, `open_preprint_mirror`, `open_summary_and_metadata_only`, `paywalled_abstract_only_excluded`), and ISO `retrieval_date`. |
| **`F03`** | `year` | Integer year (`2023`–`2026`). |
| **`F04`** | `publication_status` | Exact 8-class enum (`Peer-reviewed journal`, `Peer-reviewed conference`, `Workshop`, `Preprint (arXiv / Preprints.org)`, `Under review`, `Withdrawn`, `Publicly rejected`, `Retracted`). |
| **`F05`** | `rq_mapping` | `rqs_addressed` (`RQ1`–`RQ4`) and `corpus_track` (`Primary Comparative`, `Mechanistic Failure`, `Validity Audit`, or `Rejection-Case Audit Only`). |
| **`F06`** | `objective` | Concise statement of primary research objective and empirical hypothesis/claim. |
| **`F07`** | `architecture_and_agent_count` | `system_names`, `topology_class` (`Independent/Voting`, `Sequential Chain/SOP`, `Centralized Star`, `Dense Debate`, `Adaptive Sparse/Learned DAG`, `Hybrid/Escalation`, `Multiple`, `Diagnostic N/A`), `agent_count_n`, `backbone_models`, `model_heterogeneity`. |
| **`F08`** | `coordination_and_communication_method` | `interaction_paradigm` (separating stateful multi-turn vs. parallel voting), `communication_protocol`, `topology_optimization_or_pruning_method`, `termination_mechanism`. |
| **`F09`** | `role_specialization` | `has_role_specialization` (boolean or missingness sentinel), `defined_roles`, `asymmetric_tool_or_privilege_split`. |
| **`F10`** | `datasets_and_benchmarks` | Array per benchmark: `benchmark_name`, `domain`, `task_structure_type` (`Decomposable/Parallelizable`, `Sequential/State-Dependent`, `Context-Overflowing`, `Static Single-Turn`, `Multi-Turn Interactive`), `verifier_availability`, `harness_version_or_variant`. |
| **`F11`** | `experimental_setup` | `sample_or_trace_count`, `prompt_parity_status`, `tool_execution_parity_status`, `decoding_and_hyperparameters`. |
| **`F12`** | `baselines_and_rigor_tier` | `sas_baselines_included`, `mas_baselines_included`, `sas_baseline_rigor_tier` (`Tier 1`–`Tier 4` or `N/A`), `compute_matching_status`. |
| **`F13`** | `evaluation_metrics` | Strictly disaggregated `effectiveness_metrics`, `diagnostic_or_validity_metrics`, and `process_proxy_metrics`. |
| **`F14`** | `reported_numerical_outcomes` | Within-study `paired_comparisons` (`benchmark_and_backbone`, `mas_configuration`, `sas_comparator`, `mas_score`, `sas_score`, `delta_mas_minus_sas`, `compute_ratio_mas_over_sas`, `direction_verdict`) plus `diagnostic_or_topology_outcomes` for `RQ2`–`RQ4`. |
| **`F15`** | `variance_cis_and_stats` | `num_runs_or_seeds_k`, `pass_power_k_reported`, `dispersion_metrics_reported` (SD/SE/CI/IQR), `significance_tests_and_p_values`. |
| **`F16`** | `cost_and_latency` | `token_accounting`, `usd_cost_accounting`, `api_call_count`, `amortization_search_or_training_cost`, `wall_clock_latency`. |
| **`F17`** | `reported_successes_and_failures` | `regimes_where_mas_succeeded`, `regimes_where_mas_degraded_or_failed`, `failure_mechanisms_documented` (9-class enum), `mitigation_and_recovery_delta`. |
| **`F18`** | `limitations_and_validity_threats` | `author_stated_limitations`, `threats_to_validity`, `six_class_confounder_flags` (`C1`–`C6`), `publication_bias_or_status_caveats`. |
| **`F19`** | `quality_appraisal_and_evidence_provenance` | `qa1`–`qa7` item scores, `total_raw_score`, `applicable_max_score`, `rigor_band`, and `supporting_evidence_locations` (exact section, table, figure, or page citations). |

### 7.2 Missing-Data Handling & Zero-Imputation Protocol
All missing fields in extracted study records must strictly use one of two explicit sentinels validated by `extraction_schema.json`:
1. **`"not reported"`:** Applied when the full open-access text (or complete open repository/OpenReview manuscript) was inspected and the authors omitted the measurement or methodological detail.
2. **`"not verifiable from accessible open summary"`:** Applied when a detail may reside inside a paywalled full-text PDF or restricted attachment outside our open-web retrieval boundary.

**Zero-Imputation / Zero-Extrapolation Rule:** Reviewers shall **never** estimate missing token counts from API pricing heuristics, never derive missing `SD`/`CI` or `pass^k` rates from `pass@1`, never infer unstated baseline configurations, and never interpolate unreported amortization costs. Missingness proportions across `QA1`–`QA7` and `F15`–`F16` are quantified directly as empirical reporting-gap findings under `RQ4`.

### 7.3 Stratified Synthesis Plan & Anti-Pooling Rules
1. **Strict Prohibition on Cross-Benchmark Numerical Pooling:** Averaging raw accuracy scores, resolve rates, or `% token savings` across studies spanning different LLM backbones, reference baselines (`All-to-All` vs. `Chain` vs. `Self-Consistency`), or benchmark harnesses (`EvalPlus` vs. base `HumanEval`; `SWE-bench Lite` vs. `Verified`) is **strictly forbidden**.
2. **Primary Synthesis Unit — Within-Study Paired Comparison (`Δ_MAS-SAS`):** Every quantitative effectiveness claim is anchored to within-study paired tuples `(Study × Benchmark × Backbone × SAS_Comparator)` recording exact `Δ_MAS-SAS = Score_MAS − Score_SAS`, compute ratio (`Compute_MAS / Compute_SAS`), and direction (`MAS > SAS`, `MAS ≈ SAS` [within $\pm 1.0\text{ pp}$ or reported statistical equivalence], `MAS < SAS`).
3. **Five Mandatory Stratification Axes:**
   * **Stratum 1 — SAS Baseline Rigor Tier:** Separately summarize direction distributions (`MAS > SAS`, `MAS ≈ SAS`, `MAS < SAS`) across `Tier 1` (compute-matched strong SAS) vs. `Tier 2` vs. `Tier 3` vs. `Tier 4` comparisons to test whether MAS superiority attenuates under matched compute.
   * **Stratum 2 — Task Structure & Verifier Regime:** Cross-tabulate outcomes across `Decomposable/Parallelizable` vs. `Sequential/State-Dependent` vs. `Context-Overflowing` tasks, and `Deterministic/Unit-Test Verified` vs. `Unverified/Open-Ended` domains.
   * **Stratum 3 — Coordination Topology & Role Paradigm:** Compare `Independent/Voting`, `Sequential Chain/SOP`, `Centralized Star`, `Dense Debate`, `Adaptive Sparse/Learned DAG`, and `Hybrid/Selective Escalation` on net accuracy, token multiplier, upfront amortization disclosure, and critical-path latency.
   * **Stratum 4 — Backbone Capability & Heterogeneity Regime:** Contrast older/weaker model generations against frontier/reasoning models, and `Homogeneous` vs. `Heterogeneous` ensembles (`Self-MoA` effects).
   * **Stratum 5 — Publication-Status Sensitivity Analysis:** Present every headline synthesis stratified side-by-side as **(a) Peer-Reviewed Archival Only (`Peer-reviewed journal` + `Peer-reviewed conference`)** vs. **(b) Peer-Reviewed Archival + Workshop** vs. **(c) Peer-Reviewed + Qualified Preprints**, explicitly testing whether conclusions shift when non-refereed preprints are excluded.
4. **Mechanistic & Confounder Cross-Linkage (`RQ3` & `RQ4`):**
   * Map `RQ3` failure modes (*Error Amplification*, *Conformity/Sycophancy Collapse*, *Handoff Information Loss*, *Specification/Verification Failure*) onto `RQ2` topology strata while strictly separating **inter-agent coordination faults** (*MAST*, *Who&When*) from **intra-agent module faults** (*AgentDebug*).
   * Map `RQ4` experimental confounders (`C1`: Unmatched Inference Compute/Tokens; `C2`: API Thinking-Budget Leaks; `C3`: Voting-as-Deliberation / Proxy Conflation; `C4`: Asymmetric Prompting/Tool Feedback; `C5`: Exact-Match/Harness Fragility/Leakage; `C6`: Unamortized Search Cost) alongside verified benchmark distortion bounds (`pass^k`, `PatchDiff`, `ABC`, `VTFR`) and the bounded OpenReview Rejection-Case Audit.

### 7.4 Risk-of-Bias & Publication-Bias Assessment Plan
Both study-level risk of bias (from `QA1`–`QA7` scores and `C1`–`C6` flags) and corpus-level publication/visibility biases will be formally evaluated and reported:

| Bias Source | Mechanism Distorting LLM-MAS Evidence | Operational Audit & Mitigation in Phase 5–6 |
| :--- | :--- | :--- |
| **Positive-Result & Framework-Advocacy Bias** | Novel MAS architecture papers disproportionately compare against weak `Tier 3/4` baselines, highlight peak benchmarks, and omit negative ablations. | Contrast `MAS > SAS` rates in `Tier 1` vs. `Tier 3/4` strata; audit claims–table parity (`QA7`); include documented public OpenReview rejection cases (`TMLR 7332`, `TMLR 7253`) strictly inside the `RQ4` rejection audit. |
| **Preprint Recency & Velocity Bias** | Fast-moving 2025–2026 MAS findings circulate heavily on `arXiv` prior to peer review, risking inclusion of unvetted or subsequently withdrawn methods. | Enforce strict `QA` entry bar for preprints; stratify all results via dual **Peer-Reviewed Only vs. +Preprints** sensitivity tables; verify OpenReview withdrawal/rejection history for every candidate preprint. |
| **Benchmark Saturation & Leakage Bias** | Pretraining contamination and sparse unit tests on `GSM8K`, `MATH`, `MMLU`, `HumanEval`, and base `SWE-bench` skew small deltas. | Record `harness_version_or_variant` (`F10`), flag contamination-prone benchmarks (`QA5`), and interpret unhardened deltas against `EvalPlus`/`PatchDiff`/`BenchJack` error bounds. |
| **Open-Access Visibility & Database-Access Bias** | Absence of bulk Scopus/WoS exports and paywalled non-OA Springer/IEEE/Elsevier full-text access concentrates discovery in open ML/NLP repositories (`arXiv`, `OpenReview`, `ACL Anthology`, `PMLR`, 2026 OA `CSUR`). | Explicitly document coverage limits (`Section 3.2B`), execute forward/backward snowballing across engineering venues, and code paywalled metadata-only hits transparently (`E5` / `"not verifiable from accessible open summary"`). |

---

## 8. Protocol Amendment Log

All methodological modifications occurring after this `v1.0` freeze (e.g., query syntax adaptations across interfaces, date extensions, or schema field refinements during Phase 5–6 execution) must be appended chronologically below with rationale and Director approval. No silent retroactive edits are permitted.

| Version | Date | Author / Approver | Section(s) Affected | Amendment Description & Justification |
| :--- | :--- | :--- | :--- | :--- |
| **`v1.0`** | `2026-11-20` | Agent 6 (Author) / Agent 1 (Approved Gate 4) | All Sections (`1`–`8`) & `data/extraction_schema.json` | Initial pre-search protocol freeze establishing PRISMA 2020 + Kitchenham–Charters design, open-web boundaries, `Q1`–`Q6`, `I1`–`I6`/`E1`–`E8`, 8-tier status stratification, `QA1`–`QA7` rubric, and 19-field extraction schema prior to Phase 5 literature screening. |
| **`v1.1`** | `2026-11-20` | Agent 1 (Research Director) / Cross-checked Agents 3, 6, 7, 8, 9 | Sec. 1.3, Sec. 4.1–4.3, Sec. 6 (`QA1`), Sec. 7.1 (`data/evidence_matrix.json`) | Post-screening & post-audit reconciliation (see [phase_5_gate.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/phase_logs/phase_5_gate.md)): (1) Recorded exact executed PRISMA counts (`126` raw -> `-42` duplicates -> `84` screened -> `54` Stage 2 -> `44` included, `40` excluded; Stage 1 $\kappa=0.9489$, Stage 2 mutual $\kappa=0.7699$); (2) Strictly enforced `I2`/`E3` to exclude `SR024` (*AgentDebug*, single-agent intra-loop faults) from the $N \ge 2$ MAS corpus while admitting `SR069` (*CORBA*, multi-agent topology blocking under `I2(b)`), de-anonymized open preprints `SR075`/`SR076` under Sec. 4.3 Rule 5, Tier B Workshop `SR079` under Sec. 4.3 Rule 3, and `ACL 2025` archival `SR082` under Sec. 5.1 Rule 3; (3) Upgraded `SR007` and `SR037` from `Preprint` to verified `Peer-reviewed conference` (NeurIPS 2025), corrected 4 bogus/conflated identifiers (`SR011`, `SR012`, `SR027`, `SR033`), and harmonized `SR001` (`180` v1 -> `260` NMI 2026 configurations); (4) Enforced `SR032` (*AI Agents That Matter*) strictly under `N/A-Diagnostic` (`QA1 = N/A-Diagnostic`, removing single-agent `LATS`/`Reflexion`/`LDB` scaffolds from comparative MAS-vs-SAS tuple denominators) and set `SR020` (*CascadeDebate*) to `Tier 2` (`QA1=1`). |
| **`v1.2`** | `2026-11-20` | Agent 1 (Research Director) / Adjudicated Phase 9 Referee Audit (Reviewers A–D) | Sec. 3.2–3.3, Sec. 4.1–4.2, Sec. 6, Sec. 7.1–7.2 | Post-peer-review remediation amendment (see [phase_9_review_gate.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/phase_logs/phase_9_review_gate.md)): **(1) Transparent Search Framing & Query-Specialization Disclosure:** Retroactively discloses targeted system/paper terms injected during Phase 5 searches `S02` (`Mixture-of-Agents`, `Self-MoA`, `ColMAD`, `Self-Refine`, `Reflexion`), `S05` (`CONSENSAGENT`, `CORBA`), and `S09` (`SwarmBench`, `SCALE`) outside baseline `Q1`–`Q6`; formally characterizes retrieval as a **PRISMA-governed, open-web query- and snowball-seeded systematic review** (explicitly non-exhaustive relative to proprietary Scopus/WoS exports, logging surfaced distinct candidates per search). **(2) Honest Stage 2 Labeling & Dual-Review Completion:** Renames Stage 2 from `"Full-Text Eligibility"` to **"Open Full-Text & Structured Open-Summary Eligibility"** (distinguishing verified open PDF/HTML extractions from open summary bounds and paywalled non-OA sources such as `SR001` NMI and `SR036` ICSE) and completes independent first-reviewer Stage 2 screening on `SR079` and `SR082` while disclosing Stage 2 `n = 52` mutual vs. `N = 54` union $\kappa$. **(3) Explicit Eligibility Carve-Outs:** Formalizes the `I2(c)` single-agent audit rule distinguishing admitted `RQ4` benchmark/validity/harness audits (`SR032`–`SR039`) from single-agent intra-loop failure taxonomies outside `I2(b)`/`I2(c)` (`SR024` *AgentDebug*, `E3`), and documents `SR082` (*SCALE*, ACL 2025) inclusion under `I2(a)` (multi-agent role-collaborative pipeline vs. single-agent prompt baseline). **(4) Remediation Wave `S12`–`S13`:** Imports `16` verified Phase-2 and referee-identified primary candidates (`SR085`–`SR100`, including Protocol `v1.0` anchors `Agent Forest` and `Gao et al.`, plus `Debate or Vote`, `Estornell & Liu`, `Cost of Consensus`, `Zhao et al.`, `Yuan et al.`, `DyLAN`, `AgentDropout`, `Optima`, `Router-R1`, `EvoAgent`, `VerifyMAS`, `Hagag et al.`, `NetSafe`, `G-Safeguard`) for blinded dual screening and QA scoring alongside open-HTML/PDF `NV` resolution and non-`MAS-vs.-SAS`/nested tuple cleaning (`reviews/tuple_cleanup_log.md`). |
| **`v1.3`** | `2026-11-20` | External Referee Remediation & Verification Pass | Sec. 4.3, Sec. 6, Sec. 7.1, Sec. 7.3, `data/evidence_matrix.json`, `data/bibliography.bib` | External Referee Report (`20 Nov 2026`, Major `#1`–`#10`, Minor `#1`–`#16`) full reconciliation: **(1) Strict Tier 1 Compute Parity Cleanup:** Moved `SR003` (*OneFlow*, KV-cache state-sharing / MCTS `C6` asymmetries, 3-run SDs recorded) and `SR009` (*Denisov-Blanch et al.*, `25x` polling calls vs. `1x` query) from `Tier 1` to `Tier 2`, leaving `n = 7` strictly compute-matched studies (`15` clean comparisons, `0` `C6` omissions). **(2) Comparison Granularity & Comparator Splits:** Expanded `SR001` across all 6 benchmarks (`WorkBench`, `SWE-bench Verified & Terminal-Bench`), split `SR002` into `>=500-token` (`MAS < SAS`) vs. `100-token/context-rot` (`Mixed`), and split `SR004` into `MAD vs. Self-Consistency` (`MAS < SAS`, `93%` of `980` settings) vs. `MAD vs. 1-pass Long-CoT` (`Mixed`), yielding **`101` cleaned comparisons across `35` comparative studies** (`SR075` *PARTNR* aligned to `N/A-Diagnostic`, `12`-pt scale). **(3) Bibliographic & Venue Fixes:** Reclassified `SR012` (*ColMAD*) from `Peer-reviewed conference` to `Workshop` (`ICML 2026 Workshop on Failure Modes of Agentic AI`), giving `43` Archival (`72.9%`), `4` Workshop (`6.8%`), `12` Preprint (`20.3%`); fixed `SR027` (*TRIAGE*) to `2026.aacl-short.27` (`59.3%` council disagreement); removed unsubstantiated conformity flag from `SR013` (*Du et al.*, yielding `12/14 = 85.7%` dense debate conformity); excluded `SR032` from `C6` optimizer count (`16/16` learned/optimized frameworks = `0%` amortized); cleaned `124` BibTeX entries (`0` internal notes, `14` foundational citations added, `Anonymous2026_ACL_ARR_FailureAttribution` removed). **(4) Statistical & Readability Upgrade:** Computed 10,000-replicate cluster-bootstrap CIs (`-55.6 pp`), exact 20,000-shuffle study-weighted permutation tests (`p = 0.0113`), within-study 6-paper contrasts, continuous `%` effect-size pooling (`I^2`), plain-English Class-12-accessible prose with zero backticks and self-contained Section 12 Appendix. |
| **`v1.4`** | `2026-11-20` | Round-2 Reconciled Referee Report Remediation (`v2`) | Sec. 3.2–3.4, Sec. 4.1, Sec. 5.1–5.4, Sec. 6.1–6.2, Sec. 11–12, `data/evidence_matrix.json`, `data/bibliography.bib` | Round-2 Reconciled Referee Report (`21 Nov 2026`, `M1`–`M10`, `m1`–`m16`, `N1`–`N13`, `Second Reviewer #1`–`#19`) complete resolution: **(1) Consistency of Section 3.4 Solo-Voting Definition (`M2`/`N4`):** Re-coded `SR085` (*More Agents Is All You Need* / *Agent Forest*) from `Tier 3` MAS (`15` comparisons) to `RQ4` `C3` validity benchmark (`N/A-Diagnostic`), leaving `34` comparative studies across `87` paired comparisons (`25` diagnostic/validity studies). **(2) Expanded `SR089` & Exact Effect Sizes (`N3`):** Replaced 1-model `-27.6 pp` *Bertalanič & Fortuna* summary with all 3 GSM-Hard Table 1 models (`Qwen2.5-7B` `n=1,017` `-2.2 pp`; `Llama-3.1-8B` `n=100` `-1.7 pp`; `Ministral-3-8B` `n=100` `-27.6 pp`), rebuilt Table 11 strictly at study level without missing-variance RE pooling, and computed exact binomial SE/IV weights across `[6]` splits; fixed *Optima* MATH training time (`~24h`, `<12h` other tasks). **(3) `Tier 2A` vs. `Tier 2B` & Non-Circular `C6`:** Split `Tier 2` into unmatched inference budget (`Tier 2A`, `n=12`) vs. unamortized training/search (`Tier 2B`, `n=9`); removed `C6` from 4 diagnostic tools (`SR023, SR025, SR097, SR100`) so `12/12` (`100%`) reflects comparative MAS optimizers strictly vs. `22/34` static comparators. **(4) Uncertainty Intervals, GRADE & Full Self-Contained Reproducibility:** Added Wilson 95% CIs alongside cluster-bootstrap CIs, Wave 1 vs. Wave 2 side-by-side results, Interactive-Only `Tier 2+3` sensitivity (`p = 0.0209`), true `±1.0 pp` tie re-coding (`Sensitivity D` + optimistic `Nguyen` `Sensitivity F`), downgraded GRADE headline parity certainty to **Moderate** (`Table 16`), removed *Kim et al.* paywall & *MAST* `25.8%` claims, fixed `163/170 (95.9%)` pooled judgment agreement alongside `95/100 (95.0%)` record agreement, fixed BibTeX (`[12]` title, `[6]/[86]` pages, removed `ARR #1068`), embedded populated multi-node Mermaid figures + PNGs, and embedded full **Appendix A (`Q1–Q6` strings + Log)**, **Appendix B (`59`-study ledger)**, **Appendix C (`87`-comparison dataset + `34`-study shares)**, **Appendix D (Cleaning log)**, and **Appendix E (`41`-record exclusion ledger)** directly in Section 12 of `Deliverable_F`. |
