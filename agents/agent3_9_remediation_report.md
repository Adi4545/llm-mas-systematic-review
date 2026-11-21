# Agent 3 + Agent 9 Remediation Wave Report (`S12`–`S13`, Protocol `v1.2`)

**Roles:** Agent 3 (Literature Discovery Specialist) + Agent 9 (Evidence & Citation Auditor)  
**Date:** 2026-11-20  
**Protocol Anchor:** [Deliverable_C_Systematic_Review_Protocol.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/deliverables/Deliverable_C_Systematic_Review_Protocol.md) (`v1.2`)  
**Machine-Validated Data Artifact:** [agent3_9_remediation_wave.json](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/agents/agent3_9_remediation_wave.json) (`16/16` `INCLUDE` records verified against [extraction_schema.json](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/extraction_schema.json) via `Draft202012Validator` with `0` schema errors)  
**Independence Attestation:** Executed strictly independently of Agent 6 (zero inspection of any `agent6_remediation_*` outputs). Every numeric cell, author list, venue, DOI, OpenReview forum ID, and exclusion check was verified via live `search_web` queries or direct inspection of repository ground truth.

---

## Executive Summary

| Wave Workstream | Scope Checked | Key Outcomes |
| :--- | :--- | :--- |
| **Task 1 (`SR085`–`SR100`)** | 16 candidate primary/boundary papers | **16/16 `INCLUDE`** (`0` excluded; none publicly rejected/withdrawn under `E8`; `SR097` *VerifyMAS* confirmed accepted at NeurIPS 2026; `64` pure non-nested `MAS vs. SAS` `paired_comparisons` tuples extracted; `0` schema validation errors) |
| **Task 2 (`SR079`, `SR082`)** | Retroactive Stage 2 Agent-3 audit under `v1.2` | Both **`INCLUDE`** under Amendment `v1.2` dual-track rules (`SR079` KDD 2026 Workshop + TMLR `9844/11271` rejection audit -> `8/12` Moderate, `QA2` adjusted `1->0`; `SR082` ACL 2025 archival + withdrawn ICLR 2025 `#6097` audit -> `7/14` Moderate) |
| **Task 3 (`NV` Reduction & Disputes)** | `SR001–SR005, SR007, SR008, SR010, SR012, SR017, SR020, SR025, SR032, SR034, SR039` | Resolved **4 major factual disputes** (`SR005` keep `C1`; `SR007` `+6.4%/+8.2%` strictly vs Homog-MAD; `SR010` `65.7%` vs `59.1%`; `SR012` verbatim `+10 pp` abstract) and **10-study `QA2` latency audit** (`3` upgrades to `QA2=2`: `SR004, SR017, SR039`; `3` confirmed `QA2=2`: `SR003, SR020, SR025`; `3` downgrades to `QA2=1`: `SR002, SR032, SR034`; `1` NV/paywall caveat: `SR001`) |
| **Task 4 (BibTeX & Venue Audit)** | Restored `Kim2026`, `10` missed surveys, `12` broken/incomplete existing entries + `16` new `SR085–SR100` entries | **39 complete BibTeX entries** verified with full author lists (`0` `"et al."`, exact DOIs/volumes/articles/pages/OpenReview IDs, `0` brace mismatches) |

---

## 1. Task 1: Verification, Stage 1+2 Screening, and Schema Extraction (`SR085`–`SR100`)

All 16 candidates passed Stage 1 and were confirmed real, publicly accessible, and free of `E8` public rejection/withdrawal flags. Every `paired_comparisons` array contains strictly pure, non-nested `MAS vs. SAS` tuples; `MAS vs. MAS` ablations (`SR087` macro-averages, `SR093` Table 2 Llama-3-8B, `SR097`/`SR099`/`SR100` diagnostics) are isolated cleanly in `diagnostic_or_topology_outcomes`.

| Study ID | Short Title | Venue & Year | Verified Identifiers / URL | Stage 2 Verdict & Rule | Rigor Tier / QA (`Score/Max`, Band) | Pure `MAS vs. SAS` Tuples |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| `SR085` | *More Agents Is All You Need* (`Agent Forest`) | *TMLR* 2024 | [OpenReview:bgzUSZ8aeg](https://openreview.net/forum?id=bgzUSZ8aeg), `arXiv:2402.05120` | **INCLUDE** (`I1–I6`; Sec. 2.5 Boundary Stratum: `Independent/Voting Ensemble`) | Tier 3 / `8/14` (`Moderate`) | 15 (`Llama2-13B/70B`, `GPT-3.5` x 5 tasks) |
| `SR086` | *Single-agent or Multi-agent Systems? Why Not Both?* | Preprint (May 2025) | [arXiv:2505.18286](https://arxiv.org/abs/2505.18286) | **INCLUDE** (`I1–I6`; Sec. 2.5 `SAS->MAS` cascading exception) | Tier 2 / `6/14` (`Moderate`) | 7 (`MetaGPT`, `SelfCol`, `MathDebate`, `Cascading`) |
| `SR087` | *Debate or Vote: Which Yields Better Decisions?* | *NeurIPS 2025* (Spotlight) | [OpenReview:nfKfAzkiez](https://openreview.net/forum?id=nfKfAzkiez), `arXiv:2508.17536` | **INCLUDE** (`I1–I6`; `N=5` MAD `T=2..5` + Majority Vote vs `N=1`) | Tier 2 / `11/14` (`High`) | 8 (7 `Qwen2.5-7B` tasks + GSM8K `MV N=5`) |
| `SR088` | *Multi-LLM Debate: Framework, Principals, and Interventions* | *NeurIPS 2024* | [OpenReview:OkHC30LLpO](https://openreview.net/forum?id=OkHC30LLpO), `10.52202/079017-0911` | **INCLUDE** (`I1–I6`; `N=6, T=10` SoM & Interventions vs `Solo`) | Tier 3 / `7/14` (`Moderate`) | 1 (`BoolQ/MMLU/MathQA/TruthfulQA` summary) |
| `SR089` | *The Cost of Consensus: Isolated Self-Correction Prevails...* | Preprint (May 2026) | [arXiv:2605.00914](https://arxiv.org/abs/2605.00914) | **INCLUDE** (`I1–I6`; `N=10, R=3` unguided MAD vs `N=1` Self-Correction) | Tier 2 / `9/14` (`Moderate`) | 2 (`Ministral-3-8B` `20.7% vs 48.3%`, `Qwen/Llama`) |
| `SR090` | *When Does Multi-Agent Collaboration Help? An Entropy Perspective* | Preprint (Feb 2026; ACL ARR `#1068`) | [arXiv:2602.04234](https://arxiv.org/abs/2602.04234) | **INCLUDE** (`I1–I6`; 245 features, `SAS > MAS` in `~43.3%`; ARR `#1068` active/not rejected) | Tier 2 / `7/14` (`Moderate`) | 1 (6 reasoning + 2 agentic tasks) |
| `SR091` | *Rethinking Multi-Agent Collaboration: When More Is Less* (`SAIGE`) | Preprint (Sept 2026) | [arXiv:2609.19759](https://arxiv.org/abs/2609.19759) | **INCLUDE** (`I1–I6`; `SAIGE` & 3 MAS vs `N=1` Single-Agent across 4 tasks) | Tier 2 / `7/14` (`Moderate`) | 3 (`Terminal-Bench 2.1`, `AgentIF-OneDay`, etc.) |
| `SR092` | *DyLAN: Dynamic LLM-Powered Agent Network* | *COLM 2024* | [arXiv:2310.02170](https://arxiv.org/abs/2310.02170) | **INCLUDE** (`I1–I6`; `DyLAN` vs `N=1` `Single Execution`) | Tier 3 / `7/14` (`Moderate`) | 4 (`HumanEval GPT-3.5/4`, `MATH`, `MMLU`) |
| `SR093` | *AgentDropout: Dynamic Agent Elimination...* | *ACL 2025* (Main) | [2025.acl-long.1170](https://aclanthology.org/2025.acl-long.1170/), `arXiv:2503.18891` | **INCLUDE** (`I1–I6`; Table 1 includes `Vanilla`/`CoT` `N=1`; Table 2 MAS-vs-MAS kept in diagnostics) | Tier 3 / `6/14` (`Moderate`) | 1 (Table 1 `GPT-4o-mini` suite) |
| `SR094` | *Optima: Optimizing Effectiveness and Efficiency...* | *Findings of ACL 2025* | [2025.findings-acl.601](https://aclanthology.org/2025.findings-acl.601/), `arXiv:2410.08115` | **INCLUDE** (`I1–I6`; `OPTIMA` & `MAD` vs `N=1` `CoT` & `SC(n=8)`) | Tier 1 / `11/14` (`High`) | 8 (`HotpotQA`, `GSM8K`, `MATH` Table 1) |
| `SR095` | *Router-R1: Teaching LLMs Multi-Round Routing & Aggregation...* | *NeurIPS 2025* | [OpenReview:DWf4vroKWJ](https://openreview.net/forum?id=DWf4vroKWJ), `arXiv:2506.09033` | **INCLUDE** (`I1–I6`; Sec. 2.5 multi-round multi-LLM routing/aggregation exception vs `Direct/CoT/RAG/Search-R1` & `MoA`) | Tier 2 / `8/14` (`Moderate`) | 2 (`Router-R1-Qwen 0.416`, `Router-R1-Llama 0.409`) |
| `SR096` | *EvoAgent: Towards Automatic Multi-Agent Generation...* | *NAACL 2025* (Main) | [2025.naacl-long.315](https://aclanthology.org/2025.naacl-long.315/), `arXiv:2406.14228` | **INCLUDE** (`I1–I6`; evolved MAS vs `Direct/CoT/SPP/Self-Refine3` & `Single`) | Tier 2 / `6/14` (`Moderate`) | 11 (Table 1 NLP x 3 models + Table 2 `ScienceWorld`) |
| `SR097` | *VerifyMAS: Hypothesis Verification for Failure Attribution...* | *NeurIPS 2026* (Accepted) | [arXiv:2605.17467](https://arxiv.org/abs/2605.17467) | **INCLUDE (`I2b`)** (Verified real & accepted at NeurIPS 2026; `RQ3` attribution on `Aegis-Bench` & `Who&When`) | `N/A-Diagnostic` / `9/12` (`Moderate`) | 0 (Diagnostic attribution `muF1/MF1`) |
| `SR098` | *Architecture Matters for Multi-Agent Security* | *ICML 2026* (*PMLR 306*) | [v306/hagag26a](https://proceedings.mlr.press/v306/hagag26a.html), `arXiv:2604.23459` | **INCLUDE** (`I1–I6`; 13 configs incl. `single_agent` vs `star_specialist`, `mesh_*`, up to `3.8x` ASR spread) | Tier 2 / `9/14` (`Moderate`) | 1 (`13` configs on `BrowserART/OS-Harm/RedCode`) |
| `SR099` | *NetSafe: Exploring the Topological Safety of MAS* | *Findings of ACL 2025* | [2025.findings-acl.150](https://aclanthology.org/2025.findings-acl.150/), `arXiv:2410.15686` | **INCLUDE (`I2b`)** (`RQ3` misinformation propagation across 5 topologies; no `N=1` accuracy arm in Table 1) | `N/A-Diagnostic` / `10/12` (`High`) | 0 (`Table 1` Fact `Chain 93.46->85.10`, `Star 92.81->66.80`) |
| `SR100` | *G-Safeguard: Topology-Guided Security Lens & Treatment...* | *ACL 2025* (Main) | [2025.acl-long.359](https://aclanthology.org/2025.acl-long.359/), `arXiv:2502.11127` | **INCLUDE (`I2b`)** (`RQ3` PI/TA/MA defense across 8..80 agents; `3.49%–35.97%` ASR cut, `>40%` recovery; contrasts `Self-Check`) | `N/A-Diagnostic` / `9/12` (`Moderate`) | 0 (Topological ASR & utility recovery diagnostics) |

### Key Boundary Notes on `SR085`, `SR090`, `SR091`, `SR093`, `SR095`, `SR097`
- **`SR085` (*More Agents Is All You Need*):** Explicitly admitted as a boundary stratum (`Independent/Voting Ensemble`) under `Deliverable_C` Sec. 2.5 (`C1`, `C3`, `C5` active; `N` up to 40 vs `N=1` single-pass).
- **`SR090` (*Entropy Perspective*, `arXiv:2602.04234`):** OpenReview search located ACL ARR submission `#1068` (*"Understanding Large Language Models-based Multi-Agent Collaboration Through Entropy Dynamics"*); review cycle completed without a public rejection or withdrawal under `E8`, so it remains eligible as an active preprint.
- **`SR091` (*SAIGE*, `arXiv:2609.19759`):** Direct verification resolved an apparent `76.71` vs `51.76` discrepancy: `76.71` is Single-Agent on **Terminal-Bench 2.1** (outperforming `TDAG`, `DynTaskMAS`, `GoA`, and `SAIGE` on tightly coupled sequential steps), whereas `51.76` is the Single-Agent **Content** subscore on **AgentIF-OneDay** (where total Single-Agent score `53.57` trails `SAIGE` `71.80`).
- **`SR093` (*AgentDropout*, `2025.acl-long.1170`):** Verified Table 1 includes Single-Agent `Vanilla` and `CoT` alongside MAS pruning (`AgentPrune`, `AgentDropout`), satisfying `I2(a)`. Table 2 (`Llama-3-8B` `Vanilla MAS 57.52/71.72/52.89` vs `AgentPrune 59.48/71.09/56.20` vs `AgentDropout 61.44/72.27/57.02`) is strictly `MAS vs MAS` and placed in `diagnostic_or_topology_outcomes`.
- **`SR095` (*Router-R1*, `OpenReview:DWf4vroKWJ`):** Unlike excluded single-query weak-to-strong routers (`RouteLLM`, `AutoMix`), `Router-R1` executes multi-round `<think>` + `<route>` aggregation over a 6-model heterogeneous pool and benchmarks against Single-LLM (`Direct`, `CoT`, `RAG`, `Search-R1`), single-turn routers (`RouterDC`, `GraphRouter`), and `MoA` baselines. Admitted under the Sec. 2.5 router exception with an explicit boundary caveat (`C3`/`C6`).
- **`SR097` (*VerifyMAS*, `arXiv:2605.17467`):** Confirmed real and **accepted at NeurIPS 2026** (https://github.com/mala-lab/VerifyMAS), evaluating `Aegis-Bench` and `Who&When` (`I2b`, `RQ3`).

---

## 2. Task 2: Retroactive Stage 2 Agent-3 Screening (`SR079` and `SR082`)

| Study ID | Archival / Prior Version Status | Agent 3 Stage 2 Decision (`v1.2`) | `QA1`–`QA7` Verification | Protocol `v1.2` Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **`SR079`** (*CMAD*, Chengxiao Dai) | **Primary:** [KDD 2026 Workshop on Evaluation and Trustworthiness of Agentic AI](https://openreview.net/group?id=KDD.org/2026/Workshop/Agentic_AI) (`Workshop`)<br>**Rejected Prior Versions:** TMLR Paper `9844` (AE Peng Li) & TMLR Paper `11271` ([OpenReview:TMLR](https://openreview.net/group?id=TMLR)) | **INCLUDE** (`Workshop` / `RQ3–RQ4` Mechanistic & Rejection Audit) | `QA1=N/A-Diagnostic`, **`QA2=0`** (downgrade from `1`: tokens, USD, & latency are all `NR` in open text), `QA3=1`, `QA4=2` (15 tasks, 5 model families, slope `0.82`, `R^2=0.96`), `QA5=2`, `QA6=1`, `QA7=2` -> **`8/12` (`Moderate`)** | Under `Deliverable_C` `v1.2`: publicly rejected `TMLR 9844/11271` manuscripts are excluded from archival primary claims under `E8` (tracked in `RQ4` Rejection Audit), while the accepted **KDD 2026 Workshop** paper meets Workshop eligibility and contributes direct `I2(b)` mechanistic evidence on diversity collapse ($\rho \to 1$, `18–47%` agreement-stopping miscoverage). Workshop sensitivity flag retained. |
| **`SR082`** (*SCALE*, Zhao et al.) | **Archival:** [ACL 2025 Long Papers](https://aclanthology.org/2025.acl-long.416/) (`2025.acl-long.416`, pp. 8473–8503; `arXiv:2502.10937`)<br>**Withdrawn Prior Version:** ICLR 2025 `#6097` (author-withdrawn Jan 19, 2025) | **INCLUDE** (`Peer-reviewed conference` + `RQ4` Longitudinal Pre-Post Audit) | `QA1=0` (`N=1` ablation only, Tier 3, no SC parity), `QA2=1`, `QA3=2`, `QA4=0`, `QA5=1`, `QA6=2`, `QA7=1` -> **`7/14` (`Moderate`)** | Under `Deliverable_C` `v1.2`: withdrawn `ICLR 2025 #6097` is excluded under `E8` and isolated in the `RQ4` Longitudinal Audit; the subsequent archival **ACL 2025** Long Paper deduplicates cleanly and passes `I1–I6` (evaluates `N >= 2` SCALE vs `N=1` single-agent coding baseline across 7 multi-class/multi-label tasks; `C1`, `C4` flagged). |

---

## 3. Task 3: Open-Text `NV` Reductions, Dispute Resolutions, and `QA2` Latency Audit

### 3.1 Resolved Factual Disputes
1. **`SR005` (*Should we be going MAD?*, [arXiv:2311.17371](https://arxiv.org/abs/2311.17371)) — `C1` Verdict: KEEP `C1` (with sub-regime annotation):**  
   Live verification confirms **Table 2** reports out-of-the-box peak/median scores where `Multi-Persona (MAD)` (MedQA `0.58/0.57`, PubMedQA `0.70/0.69`, MMLU `0.72/0.69`, CosmosQA `0.46/0.42`, CIAR `0.52/0.50`, GPQA `0.29/0.29`, Chess `0.33/0.29`) is compared against `Medprompt` (`0.65/0.63`, `0.77/0.77`, `0.74/0.73`, `0.48/0.47`, `0.54/0.50`, `0.27/0.25`) and `Self-Consistency` at unmatched sequential API/token cost (`C1`), *alongside* Pareto compute-matched sweeps in Appendix Figures 1–13 (`Tier 1` sub-regime). Keep `C1` for default Table 2 comparisons while documenting the Tier 1 Pareto frontier plots.
2. **`SR007` (*Stop Overvaluing MAD*, [arXiv:2502.08788](https://arxiv.org/abs/2502.08788)) — `Heter-MAD` Delta Verdict: Strictly Over `Homog-MAD` (NOT Direct vs `SAS`):**  
   Open text confirms **`Heter-SoM` improves `SoM-average` by `+6.4%`** and **`Heter-EoT` improves `EoT-average` by `+8.2%`** (`GPT-4o-mini` & `Llama-3.1-70B`)—strictly within-framework heterogeneous vs. homogeneous comparisons, NOT direct `Heter-MAD minus SAS CoT/SC` deltas. Conformity/sycophancy collapse (agents abandoning correct initial answers under peer majority pressure) is confirmed.
3. **`SR010` (*Self-MoA*, [arXiv:2502.00674](https://arxiv.org/abs/2502.00674)) vs. `SR011` — Correction Confirmed:**  
   `Self-MoA` achieves **`65.7%`** vs. **`59.1%`** for `Mixed-MoA` on AlpacaEval 2.0 LC (`-6.6 pp` / `-10.0%` relative degradation from mixing weaker models). The `65.1%` value cited in `evidence_matrix.json` was erroneously cross-conflated from `SR011` (`MoA`, `arXiv:2406.04692`) and must be corrected to **`59.1%`**.
4. **`SR012` (*ColMAD*, [arXiv:2510.20963](https://arxiv.org/abs/2510.20963)) — Verbatim Abstract Verdict:**  
   Verbatim abstract quote verified: *"we show that ColMAD significantly outperforms previous MAD protocols **up to 10 percentage points**. Under the same budgets, ColMAD effectively brings non-trivial improvements over SA methods..."* (`paired_comparisons` should anchor to the verbatim **`+10 pp`** abstract claim rather than conflating subset figures like `10–19 pp` as overall headline).

### 3.2 Targeted Open-Text `NV` Reductions & `QA2` Latency Audit (`SR001`–`SR039`)

| Study | Open-Text `NV` Reductions Verified | `wall_clock_latency` Finding | Current `QA2` | Audited `QA2` |
| :--- | :--- | :--- | :---: | :---: |
| **`SR001`** ([2512.08296](https://arxiv.org/abs/2512.08296)) | Resolved `agent_count_n`: **`n_a in {1, 3, 5, 7, 9}`**; models span OpenAI GPT-5, Google Gemini 2.x, Anthropic Claude Sonnet; `10,000` bootstrap resamples; exact error amplifications (`4.4x`, `5.1x`, `7.8x`, `17.2x`), `~45%` SAS saturation ($\beta=-0.096, p<0.001$). *Nature Machine Intelligence* (`10.1038/s42256-026-01268-y`) raw supplement & `pass^k` remain paywalled/`NV`. | Raw wall-clock seconds remain `NV`; `QA2=2` rests on normalized tokens + orchestration turn counts | `2` | **`2` (turn-proxy sensitivity caveat)** |
| **`SR002`** ([2604.02460](https://arxiv.org/abs/2604.02460)) | Resolved backbones (`Qwen3-30B-A3B`, `DeepSeek-R1-Distill-Llama-70B`, `Gemini 2.5 Flash/Pro`), 5 MAS topologies (`Sequential`, `Subtask-parallel`, `Parallel-roles`, `Debate`, `Ensemble`), benchmarks (`FRAMES`, `MuSiQue 4-hop`), sample 1k-tok point (`~0.418 SAS vs ~0.379 Seq MAS`). | Thinking-token matching (`100..10,000`) only; **wall-clock runtime omitted** | `2` | **`1` (DOWNGRADE)** |
| **`SR003`** ([2601.12307](https://arxiv.org/abs/2601.12307)) | Resolved split sizes (`HumanEval 131, MBPP 341, GSM8K 1,055, MATH 486, HotpotQA 800, DROP 800, TravelPlanner 180`). | Explicitly reports **Average Latency (`s`) & Throughput (`samples/s`)** on vLLM + USD/tokens | `2` | **`2` (CONFIRMED)** |
| **`SR004`** ([2610.23246](https://arxiv.org/abs/2610.23246)) | Resolved 5 models (`Llama-3.2-3B`, `Qwen2.5-7B`, `Falcon3-7B`, `Gemma-2-9B`, `Gemma3-12B`) + **Table 10 wall-clock minutes**. | **Table 10 exact minutes** (`21–336 min` Debate vs `6–34 min` Probe; `5x–9x` overhead) | `1` | **`2` (UPGRADE)** |
| **`SR008`** ([2511.07784](https://arxiv.org/abs/2511.07784)) | Resolved backbone families (`GPT`, `Claude`, `Qwen`, `DeepSeek`, `Llama`), Table 1 `6` factors, Table 2 `Het-Mix A–D` on Knight–Knave–Spy (Tables 4–5 numeric regression cells remain in PDF-only layout). | Not reported separately in open abstract/HTML | `1` | `1` |
| **`SR017`** ([2410.11782](https://arxiv.org/abs/2410.11782)) | Resolved **Table 2 GSM8K Training/Inference Time & Tokens** (`Complete: 2.4h inf / 9.8e6 tok`; `DyLAN: 2.8h train, 4.6h inf / 2.2e7 tok`; `GPTSwarm: 2.1h train, 2.8h inf / 1.4e7 tok`). | **Table 2 wall-clock hours** explicitly reported alongside token counts | `1` | **`2` (UPGRADE)** |
| **`SR020`** ([2604.12262](https://arxiv.org/abs/2604.12262)) | Resolved A100 mean latency + cost multipliers (`12.79x` ARC-Easy `+26.78 pp`, `16.66x` MedQA `+52.22 pp`, `13.71x` MedMCQA `+40.22 pp`). | **Mean A100 latency (`2.45s` vs `2.34s` on ARC-Challenge)** | `2` | **`2` (CONFIRMED)** |
| **`SR025`** ([2607.07989](https://arxiv.org/abs/2607.07989)) | Resolved **Hand-Crafted subset (`Qwen-7B`)**: `AgentLocate` **`315s` vs `6,752s`** (`AgenTracer`) and **`$0.148` vs `$3.204`**. | **`315s` vs `6,752s` (`>20x` wall-clock speedup)** + USD cost | `2` | **`2` (CONFIRMED)** |
| **`SR032`** ([2407.01502](https://arxiv.org/abs/2407.01502)) | Resolved `backbone_models = ["GPT-4"]`, Table A1 95% CIs (`Direct $1.93 [1.91–1.95]`, `LATS $134.50 [123.98–147.13]`, `Warming $2.45` at `93.2%`). | **USD-only (`$0.27–$134.50`)**; latency discussed qualitatively only | `2` | **`1` (DOWNGRADE)** |
| **`SR034`** ([2602.16666](https://arxiv.org/abs/2602.16666)) | Verified formula: $R_{\text{Con}}^{\text{Res}} = \exp(-\text{mean CV over cost, time, API calls})$. | Execution time enters **only inside normalized dimensionless CV index**, not raw seconds | `2` | **`1` (DOWNGRADE)** |
| **`SR039`** ([94tlGxmqkN](https://openreview.net/forum?id=94tlGxmqkN)) | Verified **`11.3 pp`** false-negative drop and **`68.2%`** Hard-subset evaluation runtime/resource cut. | **`68.2%` runtime cut** + LLM-judge token elimination (absolute USD totals omitted) | `1` | **`2` (UPGRADE)** |

---

## 4. Task 4: Verified BibTeX & Venue Metadata (Missed Surveys + Repaired Entries)

Full machine-ready BibTeX blocks with complete author lists (zero `"et al."` on named works) are stored in `verified_bibtex_entries` inside [agent3_9_remediation_wave.json](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/agents/agent3_9_remediation_wave.json). Key corrections verified live:

- **Restored Background (`Kim2026_USENIX_Security`):** Juhee Kim, Xiaoyuan Liu, Zhun Wang, Shi Qiu, Bo Li, Wenbo Guo, Dawn Song (7 authors). *SoK: Attack and Defense Landscape of Agentic AI Systems*, USENIX Security '26 (`arXiv:2603.11088`).
- **10 Missed Surveys Verified Completely:**
  1. `Deng2025_CSUR_Security`: Zehang Deng et al. (all 7 authors), *ACM Computing Surveys* 57(7), Art. 182, pp. 1–36, July 2025, DOI `10.1145/3716628`.
  2. `Wei2026_TMLR_AgenticReasoning`: Tianxin Wei et al. (all **30** authors incl. #16 Yanjun Zhao), *TMLR* 2026, [OpenReview:2HIxxXIq2u](https://openreview.net/forum?id=2HIxxXIq2u), `arXiv:2601.12538`.
  3. `Anonymous2026_ACL_ARR_FailureAttribution`: Anonymous (ACL ARR 2026 Submission `#2880/#3533`), *"From Failure Attribution to Reliability Enhancement in LLM-based Multi-Agent Systems"* (explicitly verified distinct from Wang et al., *IEEE TSE* 52(11), 2026, DOI `10.1109/TSE.2026.3717765`).
  4. `Huang2026_TMLR_AgentMemory`: Wei-Chieh Huang et al. (all **60** authors), *TMLR* 2026, [OpenReview:XycbogUAeJ](https://openreview.net/forum?id=XycbogUAeJ).
  5. `Zhang2026_TMLR_AgenticRL`: Guibin Zhang et al. (all **25** authors), *TMLR* 2026, [OpenReview:RY19y2RI1O](https://openreview.net/forum?id=RY19y2RI1O).
  6. `Ke2025_TMLR_LLMReasoning`: Zixuan Ke et al. (all **12** authors), *TMLR* 2025, [OpenReview:SlsZZ25InC](https://openreview.net/forum?id=SlsZZ25InC).
  7. `Khan2026_Preprints_MASEvolution`: Asifullah Khan et al. (all **10** authors), Preprints.org June 2026, DOI `10.20944/preprints202606.0358.v1`.
  8. `Wang2026_arXiv_ClassicalToFoundationMAS`: Zixiang Wang et al. (all **8** authors), `arXiv:2604.18133`.
  9. `Badica2025_arXiv_ContemporaryAgentTech`: Costin Bădică et al. (all **7** authors), `arXiv:2509.02515`.
  10. `Rahman2025_arXiv_LLMPoweredSwarms`: Muhammad Atta Ur Rahman, Melanie Schranz, Samira Hayat (all **3** authors), `arXiv:2506.14496`.
- **Repaired Broken Existing Entries in `bibliography.bib` / Manuscript Refs:**
  - `Hu2024_CSUR_GameAgents` (`v1 [24]`): Fixed author count (`7 -> 9`: Sihao Hu, Tiansheng Huang, Gaowen Liu, Ramana Rao Kompella, Fatih Ilhan, Selim Furkan Tekin, Yichang Xu, Zachary Yahn, Ling Liu) and updated from preprint-only to *ACM Computing Surveys* accepted/scheduled (2026) alongside `arXiv:2404.02039`.
  - `Chowa2026_AIRE` (`[10]`): Expanded `"et al."` to all **8** authors (`Sadia Sultana Chowa, Riasad Alvi, S M Asif Ur Rahman, Md Abdur Rahman, Mohaimenul Azam Khan Raiaan, Md Rafiqul Islam, Mukhtar Hussain, Sami Azam` — noting published 3rd author spelling `S M Asif Ur Rahman` vs arXiv `Subhey Sadi Rahman`), *Artificial Intelligence Review* 59(2), Art. 71, pp. 1–59, DOI `10.1007/s10462-025-11471-9`.
  - `Yue2026_EMNLP_Findings` (`v1 [69]`/`v2 [68]`): Added archival ACL Anthology URL (`https://aclanthology.org/2026.findings-emnlp.1393/`), DOI `10.18653/2026.findings-emnlp.1393`, pp. `29630–29658`, exact middle initial `Dhaval C Patel`.
  - `Mohammadi2025_KDD_Eval` (`v1 [37]`/`v2 [36]`): Added KDD '25 V.2 DOI `10.1145/3711896.3736570`, pp. `1–11`.
  - `Xia2025_Agentless` (`v1 [62]`/`v2 [61]`): Added *PACMSE* Vol. 2, Issue FSE, Art. FSE037, pp. `801–824`, DOI `10.1145/3715754`.
  - **Ref `[1]` (`AbouAli2026_AIRE`):** Vol. 59, Art. 11, DOI `10.1007/s10462-025-11422-4`.
  - **Ref `[2]` (`Alaanzy2026_AIRE`):** Vol. 59 advance online publication, DOI `10.1007/s10462-026-11731-2` (physical issue/article # pending issue compilation).
  - **Ref `[16]` (`Du2026_CSUR`):** Vol. 58, No. 9, Art. 223, pp. `1–37`, DOI `10.1145/3789261`.
  - **Ref `[21]` (`Geng2026_CSUR_MARL`):** Vol. 58, No. 14, pp. `1–37`, DOI `10.1145/3817113`.
  - **Ref `[23]` (`He2026_CSUR`):** Vol. 58, No. 6, Art. 119, pp. `1–36`, DOI `10.1145/3773080`.
  - **Ref `[77->76]` (`Zhang2026_CSUR_Generalizability`):** Vol. 58, No. 10, Art. 263, pp. `1–44`, DOI `10.1145/3794858`.
  - **Ref `[59->58]` (`Wang2026_AACL_TRIAGE`):** Replaced GitHub URL with canonical ACL Anthology URL `https://aclanthology.org/2026.aacl-short.50/`, DOI `10.18653/2026.aacl-short.50`, pp. `376–397`.

---

## 5. Validation Verification

Programmatic validation executed after final write of [agent3_9_remediation_wave.json](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/agents/agent3_9_remediation_wave.json):
- `jsonschema.Draft202012Validator` against [extraction_schema.json](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/extraction_schema.json): **`16/16` `INCLUDE` records passed with `0` schema errors**.
- Total extracted `paired_comparisons` tuples across `SR085`–`SR100`: **`64` pure non-nested `MAS vs. SAS` tuples** (`0` `MAS vs. MAS`, `0` nested averages).
- BibTeX audit across all `39` entries: **`0` brace mismatches**, **`0` `"et al."` placeholders** on named author lists.
