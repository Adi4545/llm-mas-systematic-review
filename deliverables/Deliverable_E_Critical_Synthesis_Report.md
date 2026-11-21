# Deliverable E — Critical Synthesis Report (`Protocol v1.4`, Cleaned Corpus `N = 59`, `k = 87` Comparisons)

**Updated:** 2026-11-20 (`Protocol v1.4`: Wilson & Cluster-Bootstrap CIs, Tier 2A/2B Split, Agent Forest `C3` Boundary Enforcement, 3-Model CAIS '26 Binomial Variance Audit, GRADE Calibration)  
**Data Backing:** [verified_stats.json](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/verified_stats.json) | [tuple_cleanup_log.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/reviews/tuple_cleanup_log.md)

---

## 1. Executive Synthesis Headlines (RQ1–RQ4)

1. **`RQ1` Compute-Parity Attenuation (Tuple & Study-Weighted, Observational Moderate GRADE Certainty):** Across **`34` comparative studies** and **`87` verified `MAS vs. SAS` comparisons**, `MAS > SAS` win rates decline as solo controls equalize:
   - **`Tier 3` (Weak Single-Pass SAS Only, `n=6, k=10`):** `8/10` (`80.0%`) tuple wins (`95%` boot CI `[55.6, 100.0]`; Wilson CI `[49.0, 94.3]`); `79.2%` study-weighted fractional wins (`5/6` [`83.3%`] study majority wins).
   - **`Tier 2A` (Strong SAS, Unmatched Inference Budget, Zero Search, `n=12, k=29`):** `14/29` (`48.3%`) tuple wins (boot CI `[14.8, 73.2]`; Wilson CI `[31.4, 65.6]`), `30.6%` study-weighted.
   - **`Tier 2B` (Strong SAS, Unamortized Training/Search `C6`, `n=9, k=33`):** `28/33` (`84.8%`) tuple wins (boot CI `[64.0, 100.0]`; Wilson CI `[69.1, 93.3]`), `81.5%` study-weighted.
   - **`Tier 2 (All)` (`n=21, k=62`):** `42/62` (`67.7%`) tuple wins (Wilson CI `[55.4, 78.0]`); `52.4%` study-weighted (`10/21` [`47.6%`] majority).
   - **`Tier 1` (Strictly Equal-Compute Strong SAS, `n=7, k=15`):** `3/15` (`20.0%`) tuple wins (boot CI `[0.0, 33.3]`; Wilson CI `[7.0, 45.2]`) vs. `7/15` (`46.7%`) outright losses; `12.9%` study-weighted (`0/7` strict majority; `1/7` [`14.3%`] `>=50%`).
   - **Attenuation & Sensitivity Slices:** `Tier 2+3 -> Tier 1` win rate drops by **`-49.4 pp`** (tuple-level, `95%` boot CI `[-75.3, -25.8]`), **`-45.4 pp`** (study-weighted, exact two-sided permutation **$p = 0.0154$**), and **`-55.6 pp`** (majority Fisher **$p = 0.0106$**; `>=50%` Fisher **$p = 0.0282$**). Archival-Only (`n=4` vs `21`): `22.2%` vs. `69.0%` (`-46.8 pp`; study-weighted `10.0%` vs `62.3%`, permutation **$p = 0.0353$**, Fisher `p = 0.0957`). Wave 1 `Tier 2+3 = 71.0%` (Fisher `p = 0.0075`) vs. Wave 2 `Tier 2+3 = 68.3%`; Interactive-Only `Tier 1 = 23.1%` vs. `70.1%` (Fisher `p = 0.0209`); Zero-Search Static `Tier 2A+3 = 51.4%`; Optimistic Nguyen Table 17 `Tier 1 = 26.7%`.
2. **`RQ2` Topology & Amortization Asymmetry:** Interactive `MAD` accounts for `4/7` `Tier 1` studies (`6` comparisons) vs. `3/7` non-debate multi-topology/voting studies (`9` comparisons). Zero learned sparse DAG studies (`0/10`) satisfy `Tier 1` parity due to unamortized upfront search/training compute (`C6`: **`12/12` = 100%** comparative optimizers unamortized vs. `22/34` static zero-search papers).
3. **`RQ3` Mechanistic Failures (`12/14` Dense Debate Conformity):** Error amplification (`34/59`), verification/termination failure (`21/59`), conformity collapse (`17/59`, `12/14` [`85.7%`] Dense Debate papers), `DPI` handoff tax (`11/59`), and topological security exposure (`8/59`, up to `3.8x` higher ASR in MAS vs. SAS).
4. **`RQ4` Validity & Sensitivity:** **`0/34` (`0%`)** comparative studies (`0` `NV`) and only `3/59` (`5.1%`) studies overall report multi-trial `pass^k`; `79.7%` (`47/59`) omit direct wall-clock seconds and `88.1%` (`52/59`) omit numeric USD spend/ratios. `RQ3` rests on `13/16` archival studies; `RQ4` rests on `6/10` archival studies (including *Agent Forest* `[51]` as `C3` boundary audit).

---

## 2. Reconciled Quantitative Synthesis Tables

### Table E1 — Stratified `RQ1` Synthesis, Wilson/Bootstrap CIs & Sensitivity Slices

| Baseline Quality Tier / Sensitivity Slice | Studies (n) | Comparisons (k) | MAS Wins [95% Boot CI; 95% Wilson CI] | Ties (%) | MAS Losses (%) | Mixed (%) | Study-Weighted Win % [Boot CI] | Study Maj (>50%) | Study >=50% |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Tier 1: Equal-Compute Strong Single Agent | 7 | 15 | 3/15 (20.0%) [Boot 0.0–33.3%; Wilson 7.0–45.2%] | 0 (0.0%) | 7 (46.7%) | 5 (33.3%) | 12.9% [0.0–28.6%] | 0/7 (0.0%) | 1/7 (14.3%) |
| Tier 2A: Strong Solo, Unmatched Inference Budget (Zero Search) | 12 | 29 | 14/29 (48.3%) [Boot 14.8–73.2%; Wilson 31.4–65.6%] | 3 (10.3%) | 7 (24.1%) | 5 (17.2%) | 30.6% [8.3–52.8%] | 3/12 (25.0%) | 5/12 (41.7%) |
| Tier 2B: Strong Solo, Unamortized Training/Search (C6) | 9 | 33 | 28/33 (84.8%) [Boot 64.0–100.0%; Wilson 69.1–93.3%] | 2 (6.1%) | 3 (9.1%) | 0 (0.0%) | 81.5% [57.4–100.0%] | 7/9 (77.8%) | 8/9 (88.9%) |
| Tier 2 (All): Strong Solo, Unmatched Cost or Search | 21 | 62 | 42/62 (67.7%) [Boot 45.8–83.0%; Wilson 55.4–78.0%] | 5 (8.1%) | 10 (16.1%) | 5 (8.1%) | 52.4% [33.3–70.6%] | 10/21 (47.6%) | 13/21 (61.9%) |
| Tier 3: Weak Single-Pass Single Agent Only | 6 | 10 | 8/10 (80.0%) [Boot 55.6–100.0%; Wilson 49.0–94.3%] | 0 (0.0%) | 0 (0.0%) | 2 (20.0%) | 79.2% [45.8–100.0%] | 5/6 (83.3%) | 5/6 (83.3%) |
| Tier 2+3 Combined: All Non-Parity Controls | 27 | 72 | 50/72 (69.4%) [Boot 50.9–83.2%; Wilson 58.0–78.9%] | 5 (6.9%) | 10 (13.9%) | 7 (9.7%) | 58.3% [41.0–74.4%] | 15/27 (55.6%) | 18/27 (66.7%) |
| Parity Gap (Tier 2+3 to Tier 1, Full Corpus) | 34 total | 87 | -49.4 pp [Boot -75.3 to -25.8 pp] | — | +32.8 pp | — | -45.4 pp (perm p=0.0154) | -55.6 pp (Fisher p=0.0106) | Fisher p=0.0282 |
| Sensitivity A: Archival-Only Tier 1 (No Preprints/Wkshps) | 4 | 9 | 2/9 (22.2%) [Boot 0.0–37.5%; Wilson 6.3–54.7%] | 0 (0.0%) | 4 (44.4%) | 3 (33.3%) | 10.0% [0.0–30.0%] | 0/4 (0.0%) | 0/4 (0.0%) |
| Sensitivity A: Archival-Only Tier 2+3 (Fisher p=0.0957) | 21 | 58 | 40/58 (69.0%) [Boot 48.8–84.4%; Wilson 56.2–79.4%] | 4 (6.9%) | 9 (15.5%) | 5 (8.6%) | 62.3% [42.9–80.2%] | 12/21 (57.1%) | 15/21 (71.4%) |
| Sensitivity B: Wave 1 Baseline Tier 2+3 (S01-S11, Fisher p=0.0075) | 16 | 31 | 22/31 (71.0%) [Boot 54.5–84.4%; Wilson 53.4–83.9%] | 4 (12.9%) | 1 (3.2%) | 4 (12.9%) | 66.1% [45.3–85.4%] | 10/16 (62.5%) | 12/16 (75.0%) |
| Sensitivity B: Wave 2 Gap Imports Tier 2+3 Only (S12-S13) | 11 | 41 | 28/41 (68.3%) [Boot 33.3–88.7%; Wilson 53.0–80.4%] | 1 (2.4%) | 9 (22.0%) | 3 (7.3%) | 47.0% [21.2–74.2%] | 5/11 (45.5%) | 6/11 (54.5%) |
| Sensitivity C: Interactive Teams Only Tier 1 (Excl. Ensembles) | 6 | 13 | 3/13 (23.1%) [Boot 0.0–37.5%; Wilson 8.2–50.3%] | 0 (0.0%) | 5 (38.5%) | 5 (38.5%) | 15.0% [0.0–31.7%] | 0/6 (0.0%) | 1/6 (16.7%) |
| Sensitivity C: Interactive Teams Only Tier 2+3 (Fisher p=0.0209) | 25 | 67 | 47/67 (70.1%) [Boot 50.0–84.4%; Wilson 58.3–79.8%] | 4 (6.0%) | 10 (14.9%) | 6 (9.0%) | 60.0% [42.7–76.0%] | 14/25 (56.0%) | 17/25 (68.0%) |
| Sensitivity D: Practical ±1.0 pp Tie Margin Tier 1 | 7 | 15 | 3/15 (20.0%) [Boot 0.0–33.3%; Wilson 7.0–45.2%] | 1 (6.7%) | 7 (46.7%) | 4 (26.7%) | 12.9% [0.0–28.6%] | 0/7 (0.0%) | 1/7 (14.3%) |
| Sensitivity D: Practical ±1.0 pp Tie Margin Tier 2+3 | 27 | 72 | 49/72 (68.1%) [Boot 50.7–81.5%; Wilson 56.6–77.7%] | 6 (8.3%) | 10 (13.9%) | 7 (9.7%) | 57.8% [40.7–73.8%] | 15/27 (55.6%) | 18/27 (66.7%) |
| Sensitivity E: Zero-Search Static Only Tier 2A+3 (No C6) | 15 | 35 | 18/35 (51.4%) [Boot 23.3–73.0%; Wilson 35.6–67.0%] | 3 (8.6%) | 7 (20.0%) | 7 (20.0%) | 36.1% [16.1–57.2%] | 5/15 (33.3%) | 7/15 (46.7%) |
| Sensitivity F: Optimistic Tier 1 (Nguyen Table 17 as Win) | 7 | 15 | 4/15 (26.7%) [Boot 7.7–40.0%; Wilson 10.9–52.0%] | 0 (0.0%) | 7 (46.7%) | 4 (26.7%) | 20.0% [5.7–35.7%] | 0/7 (0.0%) | 2/7 (28.6%) |

### Table E2 — Flagship `Tier 1` Compute-Parity Corpus (`n = 7` Studies, `15` Cleaned Comparisons)

| Study | Status | Benchmark & Model Family | Comparison Pair | Accuracy Difference (MAS minus SAS) | Compute Ratio | Verdict |
| :--- | :---: | :--- | :--- | :--- | :--- | :---: |
| Kim et al. (2026) [46] | Archival | Finance-Agent (Decomposable financial analysis; OpenAI/Anthropic/Google models) | Centralized MAS (Orchestrator-Subagents) vs. Compute-matched SAS (normalized reasoning budget) | Up to +80.8% / +80.9% relative improvement | 1.0x normalized reasoning budget (+285% unconstrained orchestration overhead in turn-sweep runs) | **MAS > SAS** |
| Kim et al. (2026) [46] | Archival | BrowseComp-Plus (Decomposable web browsing; frontier models) | Decentralized / Structured MAS vs. Compute-matched SAS (normalized reasoning budget) | +9.2% relative improvement | 1.0x normalized reasoning token budget | **MAS > SAS** |
| Kim et al. (2026) [46] | Archival | PlanCraft (Sequential stateful crafting across all 4 MAS topologies) | Independent / Centralized / Decentralized / Hybrid MAS (all 4 topologies) vs. Compute-matched SAS | -39% to -70% relative degradation | 1.0x normalized reasoning token budget | **MAS < SAS** |
| Kim et al. (2026) [46] | Archival | WorkBench (Workplace tool-execution environment; NMI core suite) | Independent / Centralized / Decentralized / Hybrid MAS vs. Compute-matched SAS | Mixed tool-coordination trade-off under fixed token budgets | 1.0x normalized reasoning token budget (+58% to +285% unconstrained overhead) | **Mixed across budgets/subtasks** |
| Kim et al. (2026) [46] | Archival | SWE-bench Verified & Terminal-Bench (NMI held-out coding/CLI validation suite) | Canonical MAS architectures vs. predictive scaling model vs. Compute-matched SAS | Mixed across capability levels (~45% saturation cutoff predicts declines at high SAS) | 1.0x normalized reasoning token budget | **Mixed across budgets/subtasks** |
| Tran & Kiela (2026) [78] | Preprint | FRAMES & MuSiQue 4-hop (500 to 10,000 thinking-token budgets across 5 MAS topologies & 4 LLMs) | Sequential / Subtask-parallel / Parallel-roles / Debate / Ensemble MAS vs. Equal-thinking-token SAS / SAS-L | -3.9 pp at 1k tok (0.379 vs 0.418); -4.1 pp at 5k tok (0.386 vs 0.427); SAS beats MAS across all >=500-token budgets | 1.0 | **MAS < SAS** |
| Tran & Kiela (2026) [78] | Preprint | FRAMES & MuSiQue (100-token floor & injected context-fragmentation stress test) | 5 MAS topologies under 100-tok budget or severe SAS context rot vs. Equal-thinking-token SAS | Parity at 100 tokens; MAS helps selectively under severe context-rot stress | 1.0 | **Mixed across budgets/subtasks** |
| Nguyen et al. (2026) [61] | Preprint | GSM8K, MATH500, MMLU-Pro, CSQA (980 shared-window settings: MAD vs. Self-Consistency) | Multi-Agent Debate (reading peer outputs inside shared window W) vs. Self-Consistency (k-sample single-model parallel voting, zero reading tax) | SC >= MAD in 93% of 980 matched settings (ties/losses across tight-to-moderate windows) | 1.0 | **MAS < SAS** |
| Nguyen et al. (2026) [61] | Preprint | Shared-Context Generous-Window Regime (Table 17: MAD vs. 1-pass Long-CoT) | Multi-Agent Debate (generative peer reading) vs. 1-pass Long-CoT single agent (without multi-sample voting) | MAD beats single-pass Long-CoT in generous-window Table 17 slices despite losing to parallel SC overall | 1.0 | **Mixed across budgets/subtasks** |
| Smit et al. (2024) [74] | Archival | MedQA, PubMedQA, MMLU, CosmosQA, CIAR, GPQA, Chess (GPT-3.5-turbo & GPT-4) | Default/out-of-the-box MAD vs. Agreement-Modulated MAD vs. Compute-matched Self-Consistency & Medprompt | Default MAD fails to reliably outperform SC/Medprompt while incurring higher token/USD/time cost; tuned agreement modulation narrows or reverses gap on specific splits | Pareto frontier sweeps across matched USD/token budgets (Figs 1-13) | **Mixed across budgets/subtasks** |
| Zhang et al. (2025) [110] | Archival | 9 benchmarks x 4 models (36 scenarios) | 5 homogeneous MAD frameworks vs. Compute-matched Self-Consistency (SC) | Homogeneous MAD fails to beat CoT/SC in >80% of scenarios despite higher token/call cost | 1.0 (compute-matched against Self-Consistency; separate >1x vs 1-pass CoT analyzed in Within-Study Contrasts) | **MAS < SAS** |
| Li et al. (2026) [53] | Archival | AlpacaEval 2.0 (matched proposer sample budget) | Mixed-MoA (heterogeneous LLM mixture) vs. Self-MoA (single best LLM k-sample voting/synthesis ensemble; non-interactive boundary benchmark) | -6.6 pp (-10.0% relative; Mixed-MoA 59.1% vs. Self-MoA 65.7%) | 1.0 | **MAS < SAS** |
| Li et al. (2026) [53] | Archival | MMLU, CRUX, MATH average (matched sample budget) | Mixed-MoA (heterogeneous) vs. Self-MoA (single best LLM k-sample voting/synthesis ensemble) | -3.8% average (Mixed-MoA trails single-LLM Self-MoA) | 1.0 | **MAS < SAS** |
| Chen et al. (2026) [15] | Workshop | Error detection & reasoning tasks (matched compute) | CopMAD (Competitive MAD) vs. Single-Agent (SA) baseline | -15% to -19% degradation due to competitive cheap-talk hacking | 1.0 | **MAS < SAS** |
| Chen et al. (2026) [15] | Workshop | Error detection & reasoning tasks (equal token/compute budgets) | ColMAD (Collaborative Non-Zero-Sum MAD) vs. Compute-matched Single-Agent (SA) & CopMAD/CosMAD | Up to +10 pp over prior MAD protocols; outperforms compute-matched SA | 1.0 | **MAS > SAS** |

### Table E3 — Within-Study Paired Contrasts Holding Author Team & Benchmarks Fixed

| Study | Benchmarks Held Constant | Result vs. Weak or Unmatched Baseline | Result vs. Strong or Equal-Compute Baseline (Same Authors/Tasks) |
| :--- | :--- | :--- | :--- |
| Smit et al. [74] | MedQA, PubMedQA, MMLU, CosmosQA, GPQA, Chess | Untuned multi-round MAD vs. single-pass baselines (outperforms 1x on specific configs) | Same MAD vs. equal-budget Self-Consistency / Medprompt (out-of-the-box gains disappear; tuned agreement needed) |
| Wang et al. [84] | ECQA, GSM8K, FOLIO-wiki | MAD / ReConcile / CMD vs. Zero-Shot CoT (no demonstrations -> MAS wins) | Same MAS vs. Strong Few-Shot CoT (same-model prompt parity collapses gap to near tie) |
| Zhang et al. [110] | 9 benchmarks x 4 models (36 scenarios) | Standard homogeneous MAD benchmarks in prior papers at >1x calls | Same 5 MAD methods vs. CoT & compute-matched Self-Consistency (<20% win rate; >80% tie or lose) |
| Choi et al. [16] | 7 benchmarks incl. GSM8K (Qwen2.5-7B) | Decentralized MAD (T=2, N=5) vs. Single-Agent (0.7377 vs. 0.7205 macro avg; drops below SAS by T=3/5) | Same MAD vs. T=0 Majority Voting (N=5: 0.8867 MAD vs. 0.9400 MV = -5.33 pp loss on GSM8K) |
| Chen et al. (Optima) [14] | HotpotQA, GSM8K, MATH (Llama-3-8B) | Unoptimized MAD appears competitive when tested only against 1-pass CoT (33.8% SC omitted) | Unoptimized MAD loses vs. SC(n=8) (-5.4, -7.8, -5.9 pp); OPTIMA beats SC only after RL/DPO (<12h on 8x A100 for HotpotQA/GSM8K, ~24h for MATH) |
| Gao et al. [30] | HumanEval, MBPP, GSM8K | MetaGPT / SelfCol / MathDebate vs. older GPT-3.5-era SAS (+8.0 to +20.7 pp gains) | Exact same MAS vs. stronger Gemini-2.0-Flash SAS (margins compress to +0.8 to +3.0 pp) |

### Table E4 — Continuous Accuracy Effect Sizes (`Δ pp`: Unweighted Study-Level Panel A + CAIS '26 Variance Audit Panel B)

Panel A — Unweighted Study-Level Descriptive Accuracy Differences (Percentage Points: MAS minus Solo Agent; Strictly Single Aggregation Level)

| Control Regime (Numeric 0–100% Scale Pairs Only) | Studies (n) | Comparisons (k) | Unweighted Study Mean (pp) | Study Median [IQR] (pp) | Full Study Range [Min to Max] (pp) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Tier 1 Equal-Compute Numeric Subset ([78], [53]) | 2 | 2 | -5.25 | -5.25 [-6.60 to -3.90] | -6.60 to -3.90 |
| Strong Voting or Self-Correction Controls — All 3 CAIS '26 Models ([78], [53], [16], [14], [6]) | 5 | 9 | -6.54 | -6.37 [-6.60 to -5.33] | -10.50 to -3.90 |
| Strong Controls — Main Large-N Model Only for CAIS '26 (Qwen2.5-7B, n=1,017, -2.2 pp) | 5 | 7 | -4.88 | -5.33 [-6.37 to -3.90] | -6.60 to -2.20 |
| Weak Single-Pass Solo Controls (Untrained MAS vs. 1x Solo) | 8 | 34 | +7.06 | +7.61 [+6.70 to +12.50] | -5.40 to +13.33 |
| Post-Trained (RL/DPO) or Selective Escalation Systems | 4 | 6 | +13.05 | +13.83 [+9.43 to +22.52] | +2.00 to +22.52 |

Panel B — Binomial Variance & Inverse-Variance Reweighting Across Bertalanič & Fortuna (CAIS '26) [6] GSM-Hard Splits (Why One Small-N Model Split Inflates Unweighted Averages)

| Model Split in CAIS '26 [6] | Test Items (N) | Debate vs. Isolated Self (%) | Gap (pp) | Binomial SE (pp) | Variance | Inverse-Variance Weight (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Qwen2.5-7B (Primary split, n=1,017) | 1017 | 58.8% vs. 61.0% | -2.2 | 2.17 | 4.72 | 82.5% |
| Llama-3.1-8B (Secondary split, n=100) | 100 | 39.3% vs. 41.0% | -1.7 | 6.93 | 48.05 | 8.1% |
| Ministral-3-8B (Secondary split, n=100) | 100 | 20.7% vs. 48.3% | -27.6 | 6.43 | 41.39 | 9.4% |
| Summary Across All 3 CAIS '26 Models | 1,217 total | Unweighted study mean = -10.50 pp | Item-weighted = -4.25 pp | IV-weighted = -4.55 pp | — | Exact DerSimonian-Laird cross-study pooling omitted because 4/5 studies lack complete per-item SEs |

### Table E5 — Multi-Agent Win Rates Stratified by Task Family

| Task Family | Studies Testing Family (n) | Comparisons (k) | All-Corpus Wins / k (%) [Wilson 95% CI] | Tier 1 Wins / k (%) [Wilson 95% CI] | Pattern Summary |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Decomposable / Multi-Source & Info-Split | 5 | 8 | 6/8 (75.0%) [40.9–92.9%] | 2/2 (100.0%) [34.2–100.0%] | Partitioned information & splittable sub-tasks; Tier 1 wins (2/2) come solely from Kim et al. [46] (Finance-Agent, BrowseComp-Plus). |
| General QA, Truthfulness & Instruction Following | 20 | 40 | 26/40 (65.0%) [49.5–77.9%] | 1/7 (14.3%) [2.6–51.3%] | Most Tier 1 debate/polling studies tie or lose once sampling/prompt quality is matched. |
| Math & Symbolic Logic | 16 | 27 | 14/27 (51.9%) [34.0–69.3%] | 0/2 (0.0%) [0.0–65.8%] | Majority voting (Self-Consistency) matches or beats iterative debate at equal token budgets. |
| Sequential Planning, Embodied & Tool/SWE | 6 | 12 | 7/12 (58.3%) [32.0–80.7%] | 0/4 (0.0%) [0.0–49.0%] | Tightly coupled step dependencies incur up to -39% to -70% degradation (PlanCraft) and coordination deadlocks. |

### Table E6 — Compact Orthogonal Topology Synthesis (`RQ2`)

| Coordination Structure | Single-Topology Studies (n) | Evaluated in Multi-Topo Suites | Citations | How It Works | Key Parity Finding |
| :--- | :---: | :---: | :--- | :--- | :--- |
| Non-Interactive Multi-LLM Ensemble | 3 | +3 suites | [22], [53], [82] | Parallel independent candidates aggregated by majority vote or final synthesizer across models (single-LLM voting treated as solo baseline per Sec. 3.4). | Single-best repetition (Self-MoA) beat mixed-model ensembles by +6.6 pp (+10.0% rel.) on AlpacaEval 2.0 under equal sampling. |
| Sequential Pipeline / SOP | 0 | +3 suites | Tested inside Multi-Topo Suites: [78], [67], [101] | Fixed ordered steps passing text summaries downstream without revisiting raw context. | Findings derive from multi-topology suites: step-by-step handoffs lose information in closed-book reasoning and multiply latency. |
| Centralized Orchestrator-Worker | 0 | +4 suites | Tested inside Multi-Topo Suites: [46], [67], [34], [101] | One central coordinator assigns sub-tasks to isolated workers and checks final output. | Findings derive from multi-topology suites: wins on splittable multi-source tasks (+80.8% rel. on Finance-Agent, +285% overhead) while capping error growth at 4.4x vs. 17.2x. |
| Dense All-to-All Debate | 14 | +6 suites | [61], [74], [110], [92], [15], [25], [17], [63], [42], [65], [19], [118], [27], [6] | Every agent reads peers' answers across multiple critique rounds on shared prompts. | 12/14 (85.7%) document peer conformity collapse (up to 85.5% modal adoption); loses to Self-Consistency and isolated self-correction at strong controls. |
| Adaptive / Learned Sparse Graph | 10 | — | [124], [106], [107], [112], [105], [103], [55], [89], [102], [85] | Pruning, MCTS, RL, or evolutionary search shapes agent workflows automatically. | 0/10 learned-graph comparative studies pass Tier 1 parity because headline test-time tables omit hours of upfront search or RL training. |
| Selective Escalation & Multi-Topology Suites | 13 | — | Hybrid: [10], [30]; Multi-Topo: [46], [78], [96], [84], [67], [120], [16], [119], [14], [34], [101] | Try a fast single agent first, calling a team only on uncertain items; plus factorial sweeps across topologies. | Selective escalation cuts deployment cost ~20% vs. always-on MAS while avoiding needless sequential penalties. |
| Non-Topological Diagnostic & Validity Studies | 19 | — | 19 trace, conformity, embodied, security, & C3 boundary studies (incl. [51]) | Trace localization, sycophancy probes, embodied partner checks, benchmark audits, and solo-voting boundary checks. | No comparative MAS-vs-SAS arm; unique primary study assignments = 40 + 19 = 59. |

### Table E7 — Compact Mechanistic Failure-Pathway Synthesis (`RQ3`)

| Failure Pathway | Studies (n / 59) | Citations | Observed Quantitative Evidence & Remedies |
| :--- | :---: | :--- | :--- |
| Error Amplification & Cascading Mistakes | 34 | [46], [61], [74], [84], [110], [92], [22], [53], [82], [25], [124], [106], [107], [9], [116], [108], [95], [13], [86], [23], [63], [42], [57], [120], [76], [19], [30], [16], [27], [6], [119], [68], [101], [85] | Multiplies initial mistakes 4.4x (Centralized) to 5.1x (Hybrid), 7.8x (Decentralized), and 17.2x (Independent) without central checks. |
| Conformity, Sycophancy & Debate Hacking | 17 | [46], [74], [84], [110], [92], [15], [9], [17], [63], [42], [65], [19], [118], [16], [27], [6], [101] | Agents cave to a loud majority (12/14 [85.7%] Debate studies, up to 85.5% modal adoption); competitive debate cheap-talk drops -15% to -19% below single agents before collaborative ColMAD recovers up to +10 pp. |
| Information Loss Across Text Summaries | 11 | [78], [61], [9], [116], [13], [73], [30], [119], [103], [14], [34] | Passing compressed summaries along sequential closed-book chains discards subtle details (0.379 vs 0.418 at 1k tokens); peer reading also steals context window room in 93% of 980 settings. |
| Role Confusion & Fault Attribution Gaps | 14 | [46], [15], [105], [9], [108], [95], [13], [23], [99], [76], [118], [102], [68], [34] | Persona prompts offer little real specialization; human single-step bug labels show 59.3% LLM-council disagreement in TRIAGE [86] and 14.2% step-level accuracy ceiling (53.5% agent-level) in Who&When [116], alongside 41%–86.7% trace failure in MAST [9]. |
| Verification & Stopping Breakdowns | 21 | [46], [22], [15], [124], [112], [10], [9], [116], [108], [23], [99], [69], [88], [123], [80], [26], [73], [120], [19], [103], [68] | Verifier summary abstraction drops 30.9% of initially correct answers (85.5% recoverable via full trace links); weak stopping rules cause 18%–47% calibration miscoverage. |
| Inter-Agent Attack Spread | 8 | [124], [106], [107], [17], [120], [34], [101], [85] | Multi-agent tool wiring shows up to 3.8x higher attack success than single agents (Hagag et al.); CORBA recursive blocking disables ~92%–100% of broadcast agents in 1.6–1.9 turns unless pruned. |

### Table E8 — Quality Appraisal, `12`-Point Sensitivity & Confounders (`RQ4`)

Panel A — Quality Scores (QA1–QA7 Raw Scale vs. 12-Pt Scale Across QA2–QA7; N = 59)

| Subgroup | Studies (n) | Raw Mean (%) | 12-Pt Normalized Mean (%) | Key Score Drivers (0–2 Scale) |
| :--- | :---: | :---: | :---: | :--- |
| Full Corpus | 59 | 73.4% (Med 75.0%) | 74.2% | Single-agent rigor = 1.21 (n=34); Cost/latency = 1.05; Amortization = 1.8; Stats = 1.12; Reproducibility = 1.73 |
| Comparative Track (RQ1/RQ2) | 33 | 68.2% | 69.4% | Pulled down by single-run tables, omitted latency, and unamortized search costs. |
| Mechanistic & Security Track (RQ3) | 16 | 76.9% | 77.1% | 15/16 studies use the 12-pt diagnostic scale; CONSENSAGENT carries QA1=1 on 14-pt scale, explaining the minor raw-vs-12pt difference. |
| Evaluation Validity Track (RQ4) | 10 | 85.0% | 85.0% | All 10/10 use 12-pt diagnostic scale (0.0 pp difference); includes [51] as C3 boundary audit alongside harness studies. |
| Archival vs. Preprints | 43 vs. 12 | 71.9% vs. 75.9% | 72.7% vs. 77.1% | Preprints passed a strict >=6/14 (12) quality screen before admission (QA7 = 2.0 vs. 1.65). |

Panel B — Confounder Prevalence & Missing Reporting (N = 59; Comparative Studies = 34)

| Methodological Confounder or Reporting Gap | All 59 Studies (%) | Comparative 34 Studies (%) | Practical Effect on Claims |
| :--- | :---: | :---: | :--- |
| Unequal Compute / Token Budgets (C1) | 27/59 (45.8%) | 26/34 (76.5%) | Multi-agent pipelines spend 2x to 25x more tokens or API calls without equal-token Self-Consistency or Best-of-N single-agent controls. |
| Hidden Reasoning Token Leaks (C2) | 1/59 (1.7%) | 1/34 (2.9%) | Hidden thinking tokens inside reasoning APIs distort nominal token matching unless internal reasoning tokens are explicitly metered. |
| Voting Labeled as Deliberation (C3) | 8/59 (13.6%) | 5/34 (14.7%) | Parallel independent candidate voting/polling attributed to interactive multi-agent communication or persuasion (incl. [51]). |
| Prompt or Tool Asymmetry (C4) | 10/59 (16.9%) | 10/34 (29.4%) | Extra system hints, code execution loops, or human/tool feedback given to teams while withheld from the single-agent baseline. |
| Fragile / Leaky Test Harnesses (C5) | 44/59 (74.6%) | 29/34 (85.3%) | Weak unit tests (PatchDiff 6.2–6.4 pp inflation) or buggy substring checks (WebArena 11.3 pp false negatives) dwarf typical MAS deltas. |
| Omitted Upfront Search/Training Costs (C6) | 12/59 (20.3%) | 12/34 (35.3%) | All 12/12 comparative systems using upfront graph search, prompt search, or RL/DPO training (0% amortized; vs. 22/34 static zero-search comparative papers) omit training GPU/token costs from headline efficiency tables. |
| Clean of Flagged Confounders (None Observed) | 10/59 (16.9%) | 2/34 (5.9%) | Controlled multi-topology/debate parity studies and clean diagnostic/benchmark audits. |
| Missing Multi-Trial Consistency (pass^k) | 56/59 (94.9%) | 34/34 (100.0%) | Only 3/59 studies overall ([99], [69], [57]) measure whether systems pass consistently across k runs. |
| Missing Direct Wall-Clock Latency | 47/59 (79.7%) | — | Only 9 studies ([10], [26], [57], [61], [74], [95], [96], [107], [119]) report direct seconds/minutes (+3 proxy step/TFLOP studies). |
| Missing Dollar (USD) Cost Totals/Ratios | 52/59 (88.1%) | — | Only 7/59 (11.9%) report exact USD spend ([41], [95], [106]) or numeric USD ratios ([30], [57], [82], [112]). |

### Table E9 — Populated 2D `Topology × Task Structure` Evidence-Gap Heatmap (`40` Topological + `19` Diagnostic = `59`)

| Primary Topology Row | Decomposable / Parallel (Tot / Tier 1) | Sequential / State-Dep. (Tot / Tier 1) | Long-Context / Sandbox (Tot / Tier 1) | Static Single-Turn / Mixed (Tot / Tier 1) | Unique Studies in Row (Tot / Tier 1) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Independent / Voting | 0 / 0 (Gap) | 0 / 0 (Gap) | 1 / 0 | 3 / 1 | 3 / 1 |
| Sequential Chain / SOP | 0 / 0 (Gap) | 0 / 0 (Gap) | 0 / 0 (Gap) | 0 / 0 (Gap) | 0 / 0 |
| Centralized Star | 0 / 0 (Gap) | 0 / 0 (Gap) | 0 / 0 (Gap) | 0 / 0 (Gap) | 0 / 0 |
| Dense All-to-All Debate | 0 / 0 (Gap) | 4 / 1 | 2 / 0 | 10 / 4 | 14 / 4 |
| Adaptive Sparse / Learned DAG | 2 / 0 | 3 / 0 | 1 / 0 | 10 / 0 | 10 / 0 |
| Hybrid / Selective Escalation | 0 / 0 (Gap) | 0 / 0 (Gap) | 0 / 0 (Gap) | 2 / 0 | 2 / 0 |
| Multi-Topology Suites | 3 / 1 | 3 / 2 | 4 / 1 | 7 / 0 | 11 / 2 |
| Non-Topological Diagnostic / Validity Studies (N/A) | — | — | — | — | 19 / 0 |
| Total Corpus Studies | Multi-label coverage above | Multi-label coverage above | Multi-label coverage above | Multi-label coverage above | 59 / 7 |
