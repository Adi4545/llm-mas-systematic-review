# Agent 8 — Evaluation Metrics Extraction & Metric-Validity Analysis (Phase 5 Wave 4B)

**Role:** Evaluation and Metrics Specialist (Agent 8)  
**Extraction Output:** [agent8_metrics_extraction.json](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/agents/agent8_metrics_extraction.json) (`N = 44` included studies, schema-validated via `jsonschema.Draft202012Validator` with `0` errors against [extraction_schema.json](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/extraction_schema.json))  
**Protocol Anchor:** [Deliverable_C_Systematic_Review_Protocol.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/deliverables/Deliverable_C_Systematic_Review_Protocol.md) (Sections 2.3, 6, 7.1–7.4)  
**Date:** `November 20, 2026`  

---

## 1. Metric Dependency & Validity Guide (`RQ1`–`RQ4`)

Cross-study synthesis in LLM Multi-Agent Systems (`LLM-MAS`) frequently fails because researchers compare raw percentages across incompatible benchmarks, unverified harnesses, unmatched token budgets, and single-run trials. The six-part guide below defines the operational semantics, empirical measurement practices, confounding mechanisms (`C1`–`C6`), and strict validity boundaries for every core metric class used across `RQ1`–`RQ4` in our 44-study corpus.

---

### 1.1 Task Effectiveness Metrics (`Accuracy`, `Exact Match`, `F1`, `pass@1`, `Resolve Rate`)

1. **What It Measures:**  
   Point-in-time task completion quality on a static problem set or interactive sandbox: multiple-choice/exact-match accuracy (`MMLU`, `GSM8K`, `MATH`, `ARC`, `MedQA`, `ECQA`, `FOLIO-wiki`), token-overlap `F1` (`HotpotQA`, `DROP`), unit-test single-sample code generation (`pass@1` on `HumanEval`/`MBPP`), or repository-level patch pass rates (`Resolve Rate` on `SWE-bench Verified`).
2. **Why It Matters:**  
   Serves as the primary outcome yardstick (`RQ1`/`RQ2`) determining whether multi-agent coordination delivers net task-solving utility beyond a single-agent system (`SAS`) baseline.
3. **How Studies in Corpus Measure It:**  
   * *Static Exact-Match / Multiple-Choice:* Used across topology and debate studies (`SR004`, `SR005`, `SR006`, `SR007`, `SR013`, `SR014`, `SR016`, `SR017`, `SR018`, `SR019`, `SR020`, `SR030`, `SR076`).
   * *Deterministic Unit-Test / State Verifiers:* Code execution `pass@1` (`SR003`, `SR014`, `SR015`, `SR016`, `SR017`, `SR018`, `SR019`, `SR032`), database/policy state verification (`SR001` `WorkBench`/`PlanCraft`, `SR033` $\tau$-bench), and GitHub test suites (`SR036` `SWE-bench Verified`).
   * *LLM-as-a-Judge Grading:* Semantic equivalence rubrics (`SR002` `FRAMES`/`MuSiQue`) and pairwise preference win rates (`SR010`, `SR011` `AlpacaEval 2.0 LC` and `MT-Bench`).
4. **What Confounds Its Interpretation (`C1`–`C5`):**  
   * **Unmatched Compute (`C1`):** Multi-agent pipelines using $3\times$–$15\times$ tokens outperform $1\times$ single-pass SAS due to extra test-time sampling rather than interaction (`SR002`, `SR005`, `SR007`).
   * **Prompt & Tool Asymmetry (`C4`):** Zero-shot SAS vs. role-prompted MAS (`SR006`), or single-LLM prompt without execution tools vs. multi-agent code-test loops (`SR015`, `SR018`, `SR082`).
   * **Harness Fragility, Sparse Tests & Reward Hacking (`C5`):** `SR036` (*PatchDiff*, ICSE 2026) proves `29.6%` of plausible `SWE-bench Verified` patches diverge behaviorally from human oracles and test-restriction flaws inflate resolve rates by **`6.2–6.4 pp`**; `SR037` (*ABC*) shows reward-oracle flaws skew relative scores **up to `100%`** (cutting `CVE-Bench` overestimation by `33%`); `SR039` (*WebArena Verified*) proves brittle substring matchers inflate false negatives by **`11.3 pp`** across `812` tasks; `SR038` (*BenchJack*) uncovers **`219` exploit flaws** across `10` major benchmarks yielding near-`100%` scores without solving tasks.
   * **Verifier Absence (`SR009`):** Without an external verifier (`TruthfulQA`, `SimpleQA`, `FreshQA`), extra compute amplifies shared misconceptions rather than accuracy.
5. **When Cross-Study Comparisons Are Valid vs. Invalid:**  
   * **Valid:** Comparing **within-study paired deltas** ($\Delta_{\text{MAS-SAS}} = \text{Score}_{\text{MAS}} - \text{Score}_{\text{SAS}}$) anchored on identical backbones, identical prompt/tool parity, identical harness versions, and stratified by `Tier 1` vs. `Tier 2–4` baseline rigor.
   * **Invalid:** Pooling or averaging raw accuracies across studies using different model snapshots (`gpt-3.5-turbo-0613` vs. `GPT-5`/`Gemini 2.5`), different harnesses (`base HumanEval` vs. `EvalPlus`, `WebArena` vs. `WebArena Verified`), or mismatched compute budgets (`Tier 1` vs. `Tier 2/3`).

---

### 1.2 Multi-Run Stochastic Reliability Metrics (`pass^k`, `Consistency`, `Dispersion`, `Significance Tests`)

1. **What It Measures:**  
   Reliability across $k$ independent stochastic trials (`pass^k`: probability that **all $k$** consecutive runs of a task succeed), outcome/trajectory/resource dispersion (`SD`, `SE`, `95% CI`, `Bernoulli-normalized variance`), and inferential hypothesis tests (`Welch's t-test`, `ANOVA`, `Chi-square`, `mixed-effects regression`).
2. **Why It Matters:**  
   Single-run `pass@1` hides production tail instability. A system scoring `60%` on a single run can collapse below `25%` across `8` consecutive executions (`SR033`, `SR035`). In multi-agent workflows, stochastic variance compounds across $N$ interacting agents and $T$ handoffs.
3. **How Studies in Corpus Measure It:**  
   * **`pass^k` & Multi-Dimensional Reliability (`RQ4`):** `SR033` ($\tau$-bench) introduces `pass^k` ($k=1\dots8$), observing `~60.4%–61%` `pass^1` dropping to `<25%` `pass^8` on Retail; `SR035` (*CLEAR*) measures `8`-run decay (`60% -> 25%`) and `50x` cost variance; `SR034` (*Science of AI Agent Reliability*, ICML 2026) decomposes `12` metrics across Consistency ($R_{\text{Con}}^{\text{Out}}, R_{\text{Con}}^{\text{Traj-D}}, R_{\text{Con}}^{\text{Traj-S}}, R_{\text{Con}}^{\text{Res}}$), Robustness, Predictability (`AUROC`, `Brier`), and Safety across `K` runs.
   * **Comparative `RQ1`/`RQ2` Variance & Tests:** `SR001` runs multi-seed evaluations with mixed-effects regression ($p < 0.001$); `SR032` runs $k=5$ independent HumanEval passes; `SR076` applies Welch's $t$-test ($p < 0.001$); `SR029` uses Chi-square and Two-Way ANOVA across $>2,500$ debates; `SR039` reports `95%` CIs.
4. **What Confounds Its Interpretation:**  
   * **Single-Run Reporting Dominance (`k = 1`):** `0 / 25` comparative MAS-vs-SAS studies report `pass^k`, and only `7 / 44` (`15.9%`) verify $k \ge 2$ multi-run stochastic trials across tasks, leaving small `1–3 pp` MAS improvements indistinguishable from sampling noise.
   * **`pass@k` vs. `pass^k` Conflation:** Reporting `pass@k` (best of $k$ attempts) rewards variance, whereas `pass^k` (all $k$ succeed) penalizes unreliability.
   * **Prompt & Environment Drift (`SR034`):** Even at fixed decoding hyperparameters, minor prompt paraphrases and asynchronous web DOM timing induce non-trivial run-to-run trajectory divergence.
5. **When Cross-Study Comparisons Are Valid vs. Invalid:**  
   * **Valid:** Comparing `pass^k` curves only at matched $k$, identical task-set difficulty, and identical simulated-user/environment randomness.
   * **Invalid:** Equating `pass@1` (single run) or `pass@k` (at least one success) with `pass^k` (consistency across all $k$ runs), or inferring statistical superiority from unseeded single-run point deltas (`<3 pp`) lacking dispersion metrics.

---

### 1.3 Inference Compute, Economic Cost & Amortized Optimization Cost (`Tokens`, `USD`, $Q_{\text{break-even}}$)

1. **What It Measures:**  
   Test-time resource consumption (prompt + hidden reasoning/thinking + completion tokens, API call counts, and USD API spend per task/resolved issue) **separately** from upfront optimization/search/training compute (MCTS search iterations, RL rollouts, VGAE/GNN training, or prompt evolution).
2. **Why It Matters:**  
   Determines whether an MAS architecture sits on a genuinely superior **cost-accuracy Pareto frontier** (`SR032`, `SR035`) or merely buys accuracy via unbudgeted inference compute (`C1`) or hidden upfront search (`C6`).
3. **How Studies in Corpus Measure It:**  
   * **Strict Token/Budget Matching (`Tier 1`):** `SR002` sweeps matched thinking-token budgets (`100` to `10,000`); `SR004` matches shared context window $W$ across `980` configs; `SR001` tracks normalized tokens, success per `1,000` tokens, and `+58%` to `+285%` overhead; `SR009` scales inference compute up to `25x`; `SR010` matches proposer sample count $N$.
   * **Pareto & Dollar Accounting:** `SR032` records exact `164`-problem HumanEval USD totals (`$0.27` Escalation, `$1.93` Direct, `$2.45` Warming vs. `$134.50` LATS); `SR016` reports `$43.7 -> $5.6` and `28.1%–72.8%` token drops; `SR018` reports `4.55%` of GPT-4o inference cost; `SR019` reports up to `52.07%` token/cost reduction on HumanEval and training cost separately in Table 12; `SR003` models KV-cache prefix reuse USD savings.
4. **What Confounds Its Interpretation (`C1`, `C2`, `C6`):**  
   * **API Thinking-Budget Leaks (`C2`, `SR002`):** Commercial reasoning APIs (observed in Gemini 2.5) can misallocate or under-deliver declared thinking budgets across MAS vs. SAS invocations, breaking nominal token parity.
   * **Unamortized Search / Training Cost (`C6`):** `9 / 10` (`90%`) search/RL/VGAE/fine-tuning methods (`SR003`, `SR015`, `SR016`, `SR017`, `SR018`, `SR019`, `SR023`, `SR025`, `SR076`) omit upfront MCTS (`20` iterations of Claude-3.5-Sonnet in `SR018`), RL edge/router training (`SR015`, `SR019`, `SR023`, `SR076`), or mask/VGAE training (`SR016`, `SR017`) from headline test-time cost ratios without computing break-even query volume $Q_{\text{break-even}}$.
   * **Dense-Graph Strawman Denominators:** Claiming `72.8%–95.33%` token savings (`SR016`, `SR017`) relative to an unpruned all-to-all complete graph obscures whether the pruned MAS beats a compute-matched `Self-Consistency` SAS at the same final token expenditure.
   * **Provider Pricing & KV-Cache Asymmetry (`SR003`, `SR011`):** Comparing open-weights Together AI USD pricing against proprietary GPT-4o API rates (`SR011`), or assuming ideal provider KV-cache prefix discounts (`SR003`), conflates pricing arbitrage with algorithmic efficiency.
5. **When Cross-Study Comparisons Are Valid vs. Invalid:**  
   * **Valid:** Comparing **total tokens** (prompt + hidden reasoning + completion) within a single model snapshot and reporting test-time inference cost alongside upfront optimization cost (`Q_break-even` or explicit amortization status).
   * **Invalid:** Averaging `% token savings` across papers with different reference denominators (`Complete Graph` vs. `DyLAN` vs. `AutoGen` vs. `SAS`), comparing historical 2023–2026 USD prices across snapshots, or comparing inference-only cost of searched workflows against zero-shot prompting (`C6`).

---

### 1.4 Critical-Path Wall-Clock Latency vs. Aggregate Token Volume

1. **What It Measures:**  
   End-to-end wall-clock completion time (seconds/minutes or sequential graph depth $D$ / execution steps) from query arrival to final verified output, distinct from total cumulative tokens summed across concurrent branches.
2. **Why It Matters:**  
   Sequential MAS topologies (`MetaGPT`, multi-round `MAD`, `Chain` DAGs) incur latency proportional to sequential critical-path depth $\sum_{d=1}^{D} t_d$, whereas parallel topologies (`Self-Consistency`, `MoA` within-layer proposers, `MacNet` parallel branches) bound latency near $\max_i t_i$ while multiplying token spend—creating an acute deployment trade-off (`RQ2`) missed by token-only reporting.
3. **How Studies in Corpus Measure It:**  
   * Only `5 / 44` (`11.4%`) report or evaluate actual wall-clock latency/runtime: `SR003` (end-to-end latency & throughput gains from single-context KV-cache reuse vs. multi-agent API hops), `SR005` (wall-clock runtime Pareto plots in Appendix Figs 1–13), `SR017` (wall-clock completion speedups vs. dense graphs), `SR035` (`L` Latency pillar in CLEAR), and `SR039` (`68%–83%` runtime reduction on WebArena Verified Hard).
   * `3 / 44` report structural proxies: `SR011` (cumulative TFLOPs latency proxy), `SR069` (blocking turn number `PTN = 1.60–1.90`), and `SR075` (Habitat simulation steps, `-25%` via Knowledge Exchange).
4. **What Confounds Its Interpretation:**  
   * **Rate-Limit & Network Serialization (`SR003`, `SR028`):** Parallel branches (`N = 10` to `1,000+` agents in `SR014`) face API rate-limit queueing (`HTTP 429` documented in `SR028`) that invalidates idealized zero-contention parallel latency assumptions.
   * **Omission Bias (`81.8%` Unreported):** `36 / 44` studies omit wall-clock timing, masking multi-round sequential slowdowns (`MAD` taking $4\times$–$10\times$ longer than parallel `Self-Consistency`).
5. **When Cross-Study Comparisons Are Valid vs. Invalid:**  
   * **Valid:** Within-study wall-clock benchmarks on identical API endpoints/hardware concurrency comparing parallel SAS (`Self-Consistency`) vs. sequential/parallel MAS topologies.
   * **Invalid:** Comparing raw wall-clock seconds across different hardware, years, or API tiers, or treating aggregate token counts as a proxy for end-to-end latency.

---

### 1.5 Failure Incidence & Root-Cause Attribution Metrics (`MAST`, `Who&When`, `Top-K Triage`)

1. **What It Measures:**  
   Prevalence and structural distribution of MAS execution failures (`SR021` *MAST* 14-mode taxonomy), automated root-cause localization accuracy (`Who` agent caused the failure and `When` at the decisive error step), severity-ranked `Top-K` intervention hit rates (`SR027`), and downstream self-correction recovery deltas (`SR023`).
2. **Why It Matters:**  
   Explains *mechanistically* why MAS underperforms compute-matched SAS (`RQ3`), separating inter-agent coordination breakdowns (`~32.35%` misalignment + `~44.2%` specification + `~23.5%` verification in `SR021`) from raw base-model reasoning errors.
3. **How Studies in Corpus Measure It:**  
   * **Taxonomy Incidence (`SR021`):** `1,642+` traces across `7` MAS frameworks (`41%–86.7%` failure rates), verified at human $\kappa = 0.88$ and LLM-judge `94%` accuracy ($\kappa = 0.77$).
   * **Agent- & Step-Level Attribution (`SR022`, `SR023`, `SR025`, `SR026`, `SR028`):** `Who&When` (`127` logs: `53.5%` best agent-level, `14.2%` best step-level); `AgenTracer` (`+18.18%` over Gemini-2.5-Pro/Claude-4-Sonnet, `+4.8%–14.2%` MetaGPT/MaAS recovery); `AgentLocate` (`76.19%` agent-level on Qwen-3.6-27B); `TraceElephant` (`220` traces: full trace raises step attribution `+76%` to `76.5%`); `TRAIL` (`148` traces `>200k` avg tokens up to `6M`: `11%` best joint localization).
   * **Severity-Ranked Triage (`SR027`):** `Top-5` (`73.9%` Who&When) and `Top-10` (`93.2%` TRAIL) hit rates plus `326`-trace patch plausibility.
4. **What Confounds Its Interpretation:**  
   * **Incompatible Ontologies:** `MAST` (14 inter-agent modes) vs. `TRAIL` (3 reasoning/planning/system pillars) vs. single-agent module debuggers (`AgentDebug`, excluded under `E3`) do not map 1-to-1; category sums cannot be merged across papers.
   * **Single "Decisive Step" Ambiguity (`SR027`):** An LLM council selected a completely different repair step from ground-truth decisive-step labels in **`59.3%`** of `Who&When` traces, demonstrating that causal attribution in cyclic MAS dialogues is frequently non-unique.
   * **Partial Observability & Context Overflow (`SR026`, `SR028`):** Attributing failures from output-only logs loses up to `76%` step precision (`SR026`), while full traces averaging `>200k` tokens truncate frontier context windows (`SR028`).
   * **Unamortized Attribution Training (`C6`):** `SR023` (*AgenTracer*) and `SR025` (*AgentLocate*) fine-tune/RL-train specialized tracers using synthetic counterfactual replay (`TracerTraj`) without amortizing generation/training costs.
5. **When Cross-Study Comparisons Are Valid vs. Invalid:**  
   * **Valid:** Benchmarking multiple attribution algorithms on the *same* public trace corpus (`Who&When` or `TRAIL`) under matched Top-1 vs. Top-$K$ and full-vs.-partial trace observability protocols.
   * **Invalid:** Mixing Top-1 step accuracy with Top-5/Top-10 triage accuracy, comparing intra-agent single-loop module accuracy against inter-agent attribution, or summing failure-category counts across incompatible taxonomies.

---

### 1.6 Conformity, Sycophancy Collapse & Verification Transport Failure Rate (`CR`, `Miscoverage`, `VTFR`, `P-ASR`)

1. **What It Measures:**  
   Social/epistemic distortion and evaluation loss across agent communication boundaries: `Conformity Rate` (`SR029`), `Miscoverage Rate` under consensus stopping (`SR079`), `Sycophancy-Prior Recovery` (`SR031`), `Error Amplification Multiplier` (`SR001`), `Verification Transport Failure Rate` (`VTFR`, `SR040`), and topology-dependent paralysis (`P-ASR`, `PTN`, `SR069`).
2. **Why It Matters:**  
   Proves that process proxies—such as **inter-agent agreement/consensus** (`C3`)—frequently signify **diversity collapse and manufactured overconfidence** (`SR079`, `R^2 = 0.96` between calibration gap and residual error) rather than truth verification (`SR009`). Simultaneously, `VTFR` (`SR040`) shows that even correct verifiers break **`30.9%`** of the time across multi-agent delegation boundaries.
3. **How Studies in Corpus Measure It:**  
   * `SR029`: Conformity Rate across `>2,500` debates via Chi-square, Two-Way ANOVA, and regression.
   * `SR079`: Miscoverage (`18%–47%`) under agreement-based stopping across `15` tasks $\times$ `5` model families (`R^2 = 0.96`).
   * `SR031`: Majority-opinion accuracy recovery (`+10.5 pp`) using static/dynamic sycophancy priors (`BSS/DBSS/DSS`).
   * `SR040`: `VTFR` holding task, outcome, ground truth, and verifier model constant across native vs. abstracted views (`31.0%` macro-tool, `30.9%` multi-agent delegation, `20.3%` history compaction; `85.5%` provenance recovery).
   * `SR069`: Contagious recursive blocking `P-ASR` (`~92%–100%`) and `PTN` (`1.60–1.90` turns) on `AutoGen`/`CAMEL`.
4. **What Confounds Its Interpretation (`C3`):**  
   * **Process-Proxy Conflation (`C3`):** Treating consensus, disagreement rate, or message convergence as a proxy for correctness (`SR009`, `SR079`, and TMLR 7253 audit) without external ground-truth verification.
   * **Open-Ended Unverified Tasks (`SR029`):** Stance-shift rates on contentious social topics measure persuasion/conformity dynamics rather than objective problem-solving accuracy.
5. **When Cross-Study Comparisons Are Valid vs. Invalid:**  
   * **Valid:** Reporting within-study causal interventions holding task and backbone fixed (e.g., `VTFR` view-invariance holding ground truth constant in `SR040`; `BSS` priors vs. random/accuracy priors in `SR031`).
   * **Invalid:** Comparing `P-ASR` (denial-of-collaboration paralysis) with prompt-injection `ASR`, or equating lower disagreement/higher consensus with higher truthfulness (`SR079`).

---

## 2. Corpus Baseline Rigor & Confounder Distribution Summary (`N = 44`)

All statistics below were computed programmatically from [agent8_metrics_extraction.json](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/agents/agent8_metrics_extraction.json) and [included_studies.csv](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/included_studies.csv).

### 2.1 Corpus Composition & Publication-Status Stratification

| Publication Status (`F04`) | Stratum | Study Count (`n / 44`) | Share (%) | Record IDs |
| :--- | :--- | :---: | :---: | :--- |
| **`Peer-reviewed journal`** | Tier A Archival | **3** | `6.8%` | `SR001`, `SR010`, `SR032` |
| **`Peer-reviewed conference`** | Tier A Archival | **27** | `61.4%` | `SR005`, `SR006`, `SR009`, `SR011`–`SR023`, `SR025`–`SR027`, `SR029`–`SR031`, `SR033`, `SR034`, `SR036`, `SR069`, `SR082` |
| **`Workshop`** | Tier B Peer-Reviewed | **3** | `6.8%` | `SR039`, `SR040`, `SR079` |
| **`Preprint (arXiv / Preprints.org)`** | Tier C Non-Refereed | **11** | `25.0%` | `SR002`–`SR004`, `SR007`, `SR008`, `SR028`, `SR035`, `SR037`, `SR038`, `SR075`, `SR076` |
| **Total Corpus** | **All Included** | **44** | **100.0%** | **Peer-Reviewed Archival Core = `30 / 44` (`68.2%`); +Workshop = `33 / 44` (`75.0%`)** |

---

### 2.2 Four-Tier SAS Baseline Rigor Breakdown (`F12`) & Paired-Delta Attenuation (`F14`)

#### A. Study-Level Distribution by Publication Status

| SAS Baseline Rigor Tier (`F12`) | Total (`N = 44`) | % of Corpus | % of Comparative (`n = 25`) | Peer-Reviewed Journal (`3`) | Peer-Reviewed Conf (`27`) | Workshop (`3`) | Preprint (`11`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`Tier 1` (Compute/Token-Matched Strong SAS)** | **10** | `22.7%` | `40.0%` | `3` (`SR001, SR010, SR032`) | `3` (`SR005, SR009, SR012`) | `0` | `4` (`SR002, SR003, SR004, SR007`) |
| **`Tier 2` (Strong SAS, Unmatched Compute / Unamortized Search)** | **13** | `29.5%` | `52.0%` | `0` | `11` (`SR006, SR011, SR013–SR020, SR030`) | `0` | `2` (`SR008, SR076`) |
| **`Tier 3` (Weak Zero-Shot Single-Pass SAS Only)** | **1** | `2.3%` | `4.0%` | `0` | `1` (`SR082`) | `0` | `0` |
| **`Tier 4` (Invalid or Absent LLM SAS Baseline)** | **1** | `2.3%` | `4.0%` | `0` | `0` | `0` | `1` (`SR075`) |
| **`N/A` (Non-Comparative Diagnostic/Validity Study)** | **19** | `43.2%` | `—` | `0` | `12` (`SR021–SR023, SR025–SR027, SR029, SR031, SR033, SR034, SR036, SR069`) | `3` (`SR039, SR040, SR079`) | `4` (`SR028, SR035, SR037, SR038`) |

#### B. Within-Study Paired Comparison Verdicts (`52` Extracted Tuples) Stratified by Rigor Tier

| Baseline Rigor Tier | Paired Tuples (`n`) | `MAS > SAS` | `MAS ≈ SAS` | `MAS < SAS` | `Mixed across budgets/subtasks` | Empirical Signal |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **`Tier 1` (Gold Compute-Matched)** | **19** | **3 (`15.8%`)** | **2 (`10.5%`)** | **10 (`52.6%`)** | **4 (`21.1%`)** | **`63.2%` (`12/19`) show MAS fails to beat SAS** (`MAS < SAS` or `MAS ≈ SAS`); MAS wins only on decomposable retrieval (`SR001`) & non-zero-sum `ColMAD` (`SR012`). |
| **`Tier 2` (Unmatched / Unamortized)** | **32** | **25 (`78.1%`)** | **2 (`6.3%`)** | **1 (`3.1%`)** | **4 (`12.5%`)** | **`78.1%` apparent MAS win rate**, heavily inflated by $3\times$–$15\times$ unmatched tokens (`C1`) and omitted MCTS/RL/VGAE search costs (`C6`). |
| **`Tier 3` (Zero-Shot Weak SAS)** | **1** | `0` | `0` | `0` | **1 (`100%`)** | `SR082` (`ACL 2025 SCALE`, missing cost parity; `ICLR 2025` predecessor withdrawn). |
| **Total Comparative Tuples** | **52** | **28 (`53.8%`)** | **4 (`7.7%`)** | **11 (`21.2%`)** | **9 (`17.3%`)** | **Tier 1 vs. Tier 2 MAS-win drop: `78.1% -> 15.8%` (`-62.3 pp`).** |

> [!IMPORTANT]
> **Peer-Reviewed Archival vs. Preprint Sensitivity Check:** Separating **Tier A Peer-Reviewed Archival studies (`n = 30`)** from **Tier C Preprints (`n = 11`)** shows that `Tier 1` representation is proportionally lower in archival venues (`6 / 30 = 20.0%`, or `6 / 18 = 33.3%` of comparative archival studies) than in recent 2025–2026 preprints (`4 / 11 = 36.4%`, or `4 / 7 = 57.1%` of comparative preprints), because `11` major 2024–2026 conference MAS topology/debate papers (`SR006, SR011, SR013–SR020, SR030`) sit in `Tier 2`. Crucially, **restricting strictly to Peer-Reviewed Archival Tier 1 studies (`SR001, SR005, SR009, SR010, SR012, SR032`) preserves the exact same directional conclusion**: MAS only surpasses matched SAS in decomposable/retrieval regimes (`SR001` Finance-Agent, BrowseComp-Plus) or non-zero-sum collaborative debate (`SR012`), while failing on sequential state-dependent planning (`SR001` PlanCraft `-39% to -70%`), unverified truthfulness polling (`SR009` `25x`), heterogeneous mixing (`SR010` Self-MoA), default MAD (`SR005`), and expensive agent scaffolds (`SR032` LATS/Reflexion).

---

### 2.3 Six-Class Confounder (`C1`–`C6`) Prevalence (`F18`)

| Confounder Flag (`extraction_schema.json`) | Studies Flagged (`n / 44`) | % of Full Corpus (`44`) | % of Comparative (`25`) | Representative Record IDs |
| :--- | :---: | :---: | :---: | :--- |
| **`C5: Exact-Match / Harness Fragility / Benchmark Leakage`** | **26** | `59.1%` | `84.0%` (`21/25`) | `SR002–SR007, SR010, SR011, SR013–SR020, SR030, SR032–SR034, SR036–SR040, SR076` |
| **`C1: Unmatched Inference Compute/Tokens`** | **15** | `34.1%` | `60.0%` (`15/25`) | `SR006, SR008, SR011, SR013–SR020, SR030, SR075, SR076, SR082` |
| **`C6: Unamortized Search/Training Cost Omission`** | **9** | `20.5%` | `28.0%` (`7/25`) | `SR003, SR015–SR019, SR023, SR025, SR076` *(Note: `SR023, SR025` are `RQ3` diagnostic tracers)* |
| **`C3: Process Proxy / Voting-as-Deliberation Conflation`** | **4** | `9.1%` | `12.0%` (`3/25`) | `SR009, SR010, SR011, SR079` |
| **`C4: Asymmetric Prompting or Tool/Execution Feedback`** | **4** | `9.1%` | `16.0%` (`4/25`) | `SR015, SR018, SR030, SR082` |
| **`C2: API Thinking-Budget / Hidden Reasoning Leak`** | **1** | `2.3%` | `4.0%` (`1/25`) | `SR002` *(Explicitly diagnoses & measures Gemini 2.5 thinking-budget leak)* |
| **`None Observed`** | **11** | `25.0%` | `8.0%` (`2/25`) | `SR001, SR012, SR021, SR022, SR026–SR029, SR031, SR035, SR069` |
| **`not verifiable from accessible open summary`** | **2** | `4.5%` | `8.0%` (`2/25`) | `SR008, SR075` *(Paired alongside `C1` where full token parity tables were absent in snippets)* |

*(Note: Multi-label flagging applies because individual studies can exhibit multiple confounders simultaneously, e.g., `C1 + C4 + C5 + C6` in `SR015` and `SR018`.)*

---

### 2.4 Stochastic Reliability, Amortization, Cost & Latency Reporting Gaps (`F15`, `F16`)

| Reporting Integrity Dimension | Observed Count (`n / 44`) | Share (%) | Key Empirical Finding |
| :--- | :---: | :---: | :--- |
| **`pass^k` Multi-Trial Consistency Reported** | **3 / 44** *(0 / 25 comparative MAS)* | `6.8%` | Only `RQ4` reliability benchmarks (`SR033`, `SR034`, `SR035`) report `pass^k` (`SR001` NMI supplement `"not verifiable"`). Zero comparative `RQ1`/`RQ2` MAS studies report `pass^k`. |
| **Verified Multi-Seed / Multi-Run Stochastic Evaluation ($k \ge 2$ runs/task)** | **7 / 44** | `15.9%` | Verified multi-run/seed execution in `SR001, SR002, SR003, SR032 (k=5), SR033 (k=8), SR034 (K runs), SR035 (k=8)` (`SR009` uses up to `25x` polling samples; `SR005` & `SR076` run sweeps/multi-benchmark evaluations). Remaining `RQ1`/`RQ2` studies either omit seeds or leave them `"not verifiable from accessible open summary"`. |
| **Dispersion / Reliability / Agreement Interval Metrics** | **16 / 44** | `36.4%` | Includes `SR001, SR003, SR005, SR021 (kappa), SR027, SR029, SR032, SR033, SR034, SR035, SR036, SR038, SR039 (95% CI), SR069, SR076, SR079`; explicit per-cell `SD`/`95% CI` in primary comparative `RQ1`/`RQ2` tables remains rare. |
| **Statistical Significance Tests / Regressions / Correlations** | **8 / 44** | `18.2%` | `SR001 (p<0.001), SR004, SR021 (kappa=0.88/0.77), SR029 (Chi-sq/ANOVA), SR035 (rho=0.83), SR039 (95% CI), SR076 (Welch t-test p<0.001), SR079 (R^2=0.96)`. |
| **Unamortized Search/Training Cost (`C6` among `10` searched/trained MAS & tracers)** | **9 / 10** (`90.0%`) | `20.5%` of corpus | `9` of `10` learned/searched workflows, routers, or RL tracers (`SR003, SR015, SR016, SR017, SR018, SR019, SR023, SR025, SR076`) fail to amortize upfront MCTS/RL/VGAE search or training tokens into headline comparative cost tables (`SR019` isolates training cost in Table 12; `SR032` DSPy Optuna is the lone comparative cost-optimized exception). |
| **Concrete USD Cost Figures or Cost Ratios Reported** | **7 / 44** *(+4 relative mentions)* | `15.9%` *(25.0% w/ relative)* | Concrete dollar metrics/ratios appear in `SR003, SR005, SR011, SR016 ($43.7->$5.6), SR018 (4.55% GPT-4o), SR032 ($0.27–$134.50), SR035 (4.4x–10.8x)`; `SR019, SR020, SR034, SR039` note relative USD tracking. |
| **Actual Wall-Clock Latency / Runtime Reported** | **5 / 44** *(+3 step/TFLOP proxies)* | `11.4%` *(18.2% w/ proxies)* | Only `SR003, SR005, SR017, SR035, SR039` evaluate actual runtime/wall-clock latency (`SR011` uses TFLOPs; `SR069` uses turns; `SR075` uses simulation steps); `36 / 44` (`81.8%`) omit wall-clock timing or leave it unverifiable. |
