# Agent 6 Independent Screening & Quality Appraisal Audit (`v1.2` Remediation Wave `S12`–`S13`: `SR085`–`SR100`)

**Role:** Agent 6 (Independent Second Screener & Quality Appraiser)  
**Governing Protocol:** [Deliverable_C_Systematic_Review_Protocol.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/deliverables/Deliverable_C_Systematic_Review_Protocol.md) (`v1.0`–`v1.2`, Sec. 2.3–2.5, Sec. 4.1–4.3, Sec. 5.1–5.2, Sec. 6, Sec. 8)  
**Schema Reference:** [quality_appraisal.csv](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/quality_appraisal.csv) (first 15 rows inspected strictly for schema/tier conventions)  
**Companion Vote Ledger:** [agent6_remediation_votes.csv](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/agents/agent6_remediation_votes.csv)  
**Blinding & Independence Attestation:** Executed strictly independently without inspecting any Agent 3/9 outputs (`agents/agent3_9_*` unread). All 16 records (`SR085`–`SR100`) were verified via live `search_web` queries on November 20, 2026 across `arXiv`, `OpenReview`, `ACL Anthology`, `ACM Digital Library / CAIS`, `NeurIPS Proceedings`, `PMLR`, and `GitHub`.

---

## 1. Executive Summary of `S12`–`S13` Remediation Wave Outcomes

* **Total Candidate Records Screened:** `16` (`SR085`–`SR100`)
* **Stage 1 (Title, Abstract & Venue Metadata):** `16` `INCLUDE` (all `16` within `2023–2026` English window, empirical LLM/agentic subjects; `SR095` advanced conservatively to Stage 2 per Sec. 5.2 because its title/abstract states *"multi-LLM routing and aggregation"*)
* **Stage 2 (Open Full-Text & Structured Open-Summary Eligibility):**
  * **`INCLUDE`:** **`15`** (`SR085`–`SR094`, `SR096`–`SR100`)
  * **`EXCLUDE`:** **`1`** (`SR095` — *Router-R1*, excluded under **`E3`**)
* **Publication-Status Breakdown among `15` Included Records (Sec. 4.3):**
  * **`Peer-reviewed journal` (`Tier A`):** `1` (`SR085` *More Agents Is All You Need*, TMLR 2024)
  * **`Peer-reviewed conference` (`Tier A`):** `11` (`SR087`, `SR088`, `SR089` [ACM CAIS 2026], `SR092`, `SR093`, `SR094`, `SR096`, `SR097` [NeurIPS 2026], `SR098` [ICML 2026], `SR099`, `SR100`)
  * **`Preprint (arXiv / Preprints.org)` (`Tier C`):** `3` (`SR086`, `SR090` [also active ACL ARR Aug 2026 Sub #1068], `SR091`) — all `3` pass the mandatory Preprint Gate (`total_raw_score >= 6/14` and `QA7 >= 1`).
* **Baseline Rigor Tier Distribution among `15` Included Records (Sec. 2.3):**
  * **`Tier 1 (Compute/Token-Matched Strong SAS)`:** `0`
  * **`Tier 2 (Strong SAS, Unmatched Compute or Unamortized Search)`:** `11` (`SR086`–`SR094`, `SR096`, `SR098`) — noting that in `SR087`, `SR088`, and `SR089`, unmatched compute actually favored MAS while SAS (`Majority Voting` / `Isolated Self-Correction`) matched or outperformed MAS.
  * **`Tier 3 (Weak Zero-Shot Single-Pass SAS Only)`:** `1` (`SR085` *Agent Forest*)
  * **`Tier 4 (Invalid or Absent LLM SAS Comparator)`:** `2` (`SR099` *NetSafe*, `SR100` *G-Safeguard*)
  * **`N/A-Diagnostic`:** `1` (`SR097` *VerifyMAS*, `applicable_max_score = 12`)
* **Composite Rigor Band Distribution among `15` Included Records (Sec. 6.1):**
  * **`High` (`>= 78.0%`):** `2` (`SR090` `11/14`, `SR098` `11/14`)
  * **`Moderate` (`42.5%–77.9%`):** `12` (`SR085` `9/14`, `SR086` `8/14`, `SR087` `8/14`, `SR088` `7/14`, `SR089` `10/14`, `SR091` `10/14`, `SR092` `7/14`, `SR093` `7/14`, `SR094` `7/14`, `SR096` `7/14`, `SR097` `8/12`, `SR099` `7/14`)
  * **`Low` (`< 42.5%`):** `1` (`SR100` `5/14` — flagged per Sec. 6.1 for `RQ4` audit visibility; never cited as conclusive effectiveness proof)

---

## 2. Summary Screening & Appraisal Matrix (`SR085`–`SR100`)

| ID | Short Title | Year | Verified Venue | Status (`F04`) | Stg 1 | Stg 2 (`E`) | Proposed SAS Tier | `QA1`–`QA7` | Score | Band |
| :--- | :--- | :---: | :--- | :--- | :---: | :---: | :--- | :--- | :---: | :---: |
| **`SR085`** | *More Agents Is All You Need* (`Agent Forest`) | 2024 | TMLR 2024 | `Peer-reviewed journal` | INC | INC (`N/A`) | `Tier 3` | `1,1,2,1,1,2,1` | `9/14` (`64.3%`) | `Moderate` |
| **`SR086`** | *Single-agent or Multi-agent Systems? Why Not Both?* | 2025 | `arXiv:2505.18286` | `Preprint` | INC | INC (`N/A`) | `Tier 2` | `1,1,2,0,1,1,2` | `8/14` (`57.1%`) | `Moderate` |
| **`SR087`** | *Debate or Vote: Which Yields Better Decisions...* | 2025 | NeurIPS 2025 Spotlight | `Peer-reviewed conference` | INC | INC (`N/A`) | `Tier 2` | `1,0,2,0,1,2,2` | `8/14` (`57.1%`) | `Moderate` |
| **`SR088`** | *Multi-LLM Debate: Framework, Principals, and Interventions* | 2024 | NeurIPS 2024 | `Peer-reviewed conference` | INC | INC (`N/A`) | `Tier 2` | `1,0,2,0,1,1,2` | `7/14` (`50.0%`) | `Moderate` |
| **`SR089`** | *The Cost of Consensus: Isolated Self-Correction Prevails...* | 2026 | ACM CAIS 2026 | `Peer-reviewed conference` | INC | INC (`N/A`) | `Tier 2` | `1,1,2,1,2,1,2` | `10/14` (`71.4%`) | `Moderate` |
| **`SR090`** | *When Does Multi-Agent Collaboration Help? An Entropy Perspective* | 2026 | `arXiv:2602.04234` *(ARR Aug '26 #1068)* | `Preprint` | INC | INC (`N/A`) | `Tier 2` | `1,2,2,1,1,2,2` | `11/14` (`78.6%`) | `High` |
| **`SR091`** | *Rethinking Multi-Agent Collaboration: When More Is Less* (`SAIGE`) | 2026 | `arXiv:2609.19759` | `Preprint` | INC | INC (`N/A`) | `Tier 2` | `1,1,2,1,2,1,2` | `10/14` (`71.4%`) | `Moderate` |
| **`SR092`** | *DyLAN: Dynamic LLM-Powered Agent Network* | 2024 | COLM 2024 | `Peer-reviewed conference` | INC | INC (`N/A`) | `Tier 2` | `1,1,1,0,1,2,1` | `7/14` (`50.0%`) | `Moderate` |
| **`SR093`** | *AgentDropout: Dynamic Agent Elimination...* | 2025 | ACL 2025 | `Peer-reviewed conference` | INC | INC (`N/A`) | `Tier 2` | `1,1,1,0,1,2,1` | `7/14` (`50.0%`) | `Moderate` |
| **`SR094`** | *Optima: Optimizing Effectiveness and Efficiency...* | 2025 | Findings of ACL 2025 | `Peer-reviewed conference` | INC | INC (`N/A`) | `Tier 2` | `1,1,1,0,1,2,1` | `7/14` (`50.0%`) | `Moderate` |
| **`SR095`** | *Router-R1: Teaching LLMs Multi-Round Routing & Aggregation...* | 2025 | NeurIPS 2025 | `Peer-reviewed conference` | INC | **EXC (`E3`)** | `N/A` | `N/A` | `N/A` | `N/A` |
| **`SR096`** | *EvoAgent: Towards Automatic Multi-Agent Generation...* | 2025 | NAACL 2025 | `Peer-reviewed conference` | INC | INC (`N/A`) | `Tier 2` | `1,1,1,0,1,2,1` | `7/14` (`50.0%`) | `Moderate` |
| **`SR097`** | *VerifyMAS: Hypothesis Verification for Failure Attribution...* | 2026 | NeurIPS 2026 (Poster) | `Peer-reviewed conference` | INC | INC (`N/A`) | `N/A-Diagnostic` | `N/A,1,1,0,2,2,2` | `8/12` (`66.7%`) | `Moderate` |
| **`SR098`** | *Architecture Matters for Multi-Agent Security* (`Hagag et al.`) | 2026 | ICML 2026 (PMLR 306) | `Peer-reviewed conference` | INC | INC (`N/A`) | `Tier 2` | `1,0,2,2,2,2,2` | `11/14` (`78.6%`) | `High` |
| **`SR099`** | *NetSafe: Exploring the Topological Safety of Multi-agent System* | 2025 | Findings of ACL 2025 | `Peer-reviewed conference` | INC | INC (`N/A`) | `Tier 4` | `0,0,2,0,1,2,2` | `7/14` (`50.0%`) | `Moderate` |
| **`SR100`** | *G-Safeguard: A Topology-Guided Security Lens and Treatment...* | 2025 | ACL 2025 | `Peer-reviewed conference` | INC | INC (`N/A`) | `Tier 4` | `0,0,1,0,1,2,1` | `5/14` (`35.7%`) | `Low` |

---

## 3. Critical Methodological & Protocol Boundary Adjudications

### 3.1 `E8` Status, Venue Upgrades & Identifier Hygiene Verification
1. **Zero `E8` Rejections/Withdrawals Found:** Live OpenReview and venue verification confirmed that none of the 16 candidates holds a `Withdrawn`, `Publicly rejected`, or `Retracted` decision.
2. **Preprint-to-Archival & Venue Verifications (Sec. 5.1):**
   * **`SR089` (*The Cost of Consensus*):** Initially referenced as an `arXiv:2605.00914` preprint, live verification confirmed archival publication in the *Proceedings of the ACM Conference on AI and Agentic Systems (CAIS '26)*, May 2026 (`DOI: 10.1145/3786335.3813137`). Coded strictly as **`Peer-reviewed conference`**.
   * **`SR090` (*When Does Multi-Agent Collaboration Help?*):** Verified as `arXiv:2602.04234` and also tracked on OpenReview under an active submission to **ACL ARR August 2026** (`Submission #1068`, titled *Understanding Large Language Models-based Multi-Agent Collaboration Through Entropy Dynamics*, last modified September 2026, not rejected or withdrawn). Per Sec. 4.3 Rule 5, coded as **`Preprint (arXiv / Preprints.org)`** and passed through the `QA1`–`QA7` Preprint Gate (`11/14 High`).
   * **`SR097` (*VerifyMAS*):** Verified genuine, non-fabricated, and accepted as a Poster at **NeurIPS 2026** (`arXiv:2605.17467`; official repository `https://github.com/mala-lab/VerifyMAS`). Coded as **`Peer-reviewed conference`**.
   * **OpenReview ID Verification Catch:** Initial search snippets surfaced conflated OpenReview IDs (`sehRvaIPQQ` actually belongs to *Let Models Speak Ciphers*; `EHg5GDnyq1` actually belongs to *AgentVerse*; `arXiv:2408.14575` actually belongs to *EVINCE*). Independent per-ID title confirmation verified the authentic canonical identifiers: `iUjGNJzrF1` and NeurIPS hash `934252acd87f254d5d4672fbde283bd2` for `SR087` (*Debate or Vote*); `sy7eSEXdPC` and NeurIPS PDF `32e07a110c6c6acf1afbf2bf82b614ad` for `SR088` (*Multi-LLM Debate*); and `XII0Wp1XA9` for `SR092` (*DyLAN*).

### 3.2 `SR085` (*More Agents Is All You Need* / `Agent Forest`): `I2(a)` Boundary Stratum vs. `E3`
* **Empirical Mechanism (`Self-Consistency` Equivalence):** Core `Agent Forest` (`arXiv:2402.05120`, TMLR `bgzUSZ8aeg`) instantiates $N$ independent parallel calls of the **exact same LLM** with the **exact same prompt** (`T > 0`) and aggregates via majority or similarity voting—with no distinct agent personas, isolated state/memory, or inter-agent communication. As TMLR OpenReview reviewers (`bgzUSZ8aeg`) explicitly remarked, core `Agent Forest` is operationally equivalent to generalized **Self-Consistency (`CoT-SC`)** ($N=1$ LLM repeated sampling extended beyond CoT to MMLU, Chess, HumanEval, GSM8K, and MATH).
* **Protocol Adjudication (`INCLUDE` under `I2(a)` Boundary Stratum):** Despite that mechanistic equivalence to single-LLM repeated sampling, **Protocol Sec. 2.4** (lines 100–102) and **Sec. 2.5** (line 111) **explicitly admit `Agent Forest`** under **`Parallel / Voting LLM Collectives (Independent / Voting Ensemble)`** as a mandatory boundary stratum (`I2(a)`), specifically to isolate pure sampling/voting scaling from stateful interactive deliberation (`C3`). Furthermore, `SR085` conducts direct comparative evaluations (Table 3) integrating/comparing against stateful MAS (`LLM-Debate`, `SPP`, `Reflection`) as well as proposing `Step-wise` and `Hierarchical` (multi-model) Agent Forest variants.
* **Agent 6 Judgment:** **`INCLUDE` (`I2(a)`)**, strictly tagged as `Boundary Stratum: Independent/Voting Ensemble` (`Tier 3` in primary Table 2 against $N=1$ `Single`; `QA1=1`, `9/14 Moderate`), with explicit warning against conflating `Agent Forest` with interactive multi-agent collaboration (`C3`).

### 3.3 `SR095` (*Router-R1*): Stage 2 `EXCLUDE` (`E3`) Judgment
* **Surface Ambiguity (`Stage 1 = INCLUDE`):** `Router-R1` (`arXiv:2506.09033`, NeurIPS 2025 `DWf4vroKWJ`) frames itself as *"Multi-Round Routing and Aggregation"*, interleaving `<think>` and `<route>` actions across multiple turns and candidate LLMs (`Qwen2.5-72B`, `Llama-3.3-70B`, `Mixtral-8x22B`, etc.) per query—warranting conservative advancement to Stage 2 under Sec. 5.2.
* **Stage 2 Disqualification (`E3`):** Detailed verification of the open manuscript and Tables 1–2 confirms three disqualifying criteria under **Sec. 2.4–2.5** and **Sec. 4.2 `E3`**:
  1. **Single-Agent Architecture:** The authors explicitly frame `Router-R1` as a **single-agent RL policy LLM** (`Qwen2.5-3B` / `Llama-3.2-3B`) calling external candidate LLMs as **stateless black-box API tools** inside a single evolving context window—directly modeled after `Search-R1` calling a search retriever—without distinct autonomous agent roles, isolated persistent states, or inter-agent peer critique.
  2. **Zero MAS Comparators:** Tables 1–2 evaluate `Router-R1` exclusively against single-model baselines (`Direct`, `CoT`, `SFT`, `RAG`, `Search-R1`) and single-round routers (`Prompt LLM`, `KNN Router`, `MLP Router`, `BERT Router`, `RouterDC`, `GraphRouter`, `FrugalGPT`, `Prompt LLM*`, `KNN Router*`). Neither `MoA` nor any interactive MAS framework is included.
  3. **Outside Sec. 2.5 Exception Clause:** Sec. 2.5's exception for routing papers applies strictly to studies modeling `SAS→MAS` escalation or intra-MAS routing *"against MAS/SAS baselines (e.g., CascadeDebate, MasRouter, Gao et al. 2025)"*, which `Router-R1` does not satisfy.
* **Agent 6 Judgment:** **`EXCLUDE` at Stage 2 (`E3`)**.

### 3.4 Amortization (`QA3` / `C6`) & Comparative Baseline Tiering Across `SR092`–`SR100`
* **Optimization Frameworks (`SR092` *DyLAN*, `SR093` *AgentDropout*, `SR094` *Optima*, `SR096` *EvoAgent*):** All four include competitive SAS comparators (`CoT`, `Complex CoT`, `Self-Consistency`, `Self-Refine`, `SPP`, `ReAct`/`LATS`), earning `QA1 = 1` (`Tier 2`) rather than `Tier 1` because they do **not** match total compute/tokens with strong SAS AND omit quantitative upfront search/optimization costs from main comparative cost tables (`QA3 = 1`, `C6`):
  * *DyLAN* (`SR092`) explicitly states in Sec. 3.2/main experiments that Tables 2–4 report **only Stage 2 `#Calls`**, omitting Stage 1 Team Optimization API calls from comparative tables (while Table 5 lists role prompts and Appendix C gives dataset statistics).
  * *AgentDropout* (`SR093`) reports prompt/completion tokens (`Ptok`/`Ctok`) during inference without folding adjacency-matrix training steps into comparative token totals.
  * *Optima* (`SR094`) notes offline MCTS + iterative SFT/DPO training took `<12h on 8× A100` in setup, yet headline `<10% tokens` claims compare inference-only tokens without break-even (`Q_break-even`) amortization.
  * *EvoAgent* (`SR096`) acknowledges evolutionary generation overhead qualitatively without tabulating upfront evolutionary search token/USD budgets in main comparative tables.
* **Security & Diagnostic Studies (`SR097`–`SR100`):**
  * *VerifyMAS* (`SR097`) is a pure MAS trajectory failure-attribution evaluator on `Who&When` and `Aegis-Bench` (`I2(b)`, paralleling *MAST* and *Who&When*), properly coded **`N/A-Diagnostic`** (`applicable_max_score = 12`).
  * *Architecture Matters for Multi-Agent Security* (`SR098`, Hagag et al., ICML 2026) directly compares 12 MAS architectures against a full-tool standalone `Single-Agent` baseline on identical backbones and `Inspect AI` sandboxes (`BrowserART`, `OS-Harm`, `SWE-bench`), yet receives `Tier 2` (`QA1 = 1`) and `QA2 = 0` strictly because the authors disclose they did not centrally log per-call token/cost or latency metrics. Its 95% bootstrap CIs (`QA4 = 2`), stage-wise security audit (`QA5 = 2`), public repo (`QA6 = 2`), and candid negative findings (`QA7 = 2`) yield **`11/14 High`**.
  * *NetSafe* (`SR099`) and *G-Safeguard* (`SR100`) compare MAS topologies (`chain`/`tree`/`star`/`circle`/`complete`) or GNN-pruned MAS solely against unguarded MAS and node-level text filters (`Llama-Guard`/`PromptGuard`), with **zero quantitative standalone SAS baseline** (`Tier 4`, `QA1 = 0`).

---

## 4. Per-Study Verification & Appraisal Ledger (`SR085`–`SR100`)

### `SR085` — *More Agents Is All You Need* (`Agent Forest`)
* **Citation & Year:** Junyou Li, Qin Zhang, Yangbin Yu, Qiang Fu, Deheng Ye (2024).
* **Verified Venue & Status:** *Transactions on Machine Learning Research (TMLR)*, Oct 2024 — **`Peer-reviewed journal`**.
* **Verified Evidence URLs:** [OpenReview (`bgzUSZ8aeg`)](https://openreview.net/forum?id=bgzUSZ8aeg) | [arXiv:2402.05120](https://arxiv.org/abs/2402.05120) | [GitHub (`MoreAgentsIsAllYouNeed/AgentForest`)](https://github.com/MoreAgentsIsAllYouNeed/AgentForest)
* **Screening:** Stage 1 `INCLUDE`; Stage 2 `INCLUDE` (`I2(a)` Boundary Stratum: `Independent/Voting Ensemble`, plus Table 3 comparison/stacking on `LLM-Debate` & `CoT-SC`).
* **Tier & QA (`9/14 Moderate`):**
  * `QA1 = 1` (`Tier 3`): Table 2 pits $N$-sample `Agent Forest` against $N=1$ `Single` pass across `Llama2-13B/70B`, `GPT-3.5-Turbo`, `GPT-4` without equal-token `CoT-SC` parity in primary tables.
  * `QA2 = 1`: Table 5 reports single-agent token counts and linear scaling with $N$; omits wall-clock latency.
  * `QA3 = 2`: Training-free parallel sampling-and-voting.
  * `QA4 = 1`: Table 2 plots sample-level standard error (`SE`), lacking $k \ge 3$ independent random-seed dispersion (explicitly noted by TMLR `bgzUSZ8aeg` reviewers).
  * `QA5 = 1`: Standard `GSM8K`, `MATH`, `MMLU`, `Chess`, `HumanEval` benchmarks without contamination/harness audit.
  * `QA6 = 2`: Official repository `MoreAgentsIsAllYouNeed/AgentForest` + prompts/hyperparameters.
  * `QA7 = 1`: Frames repeated single-LLM sampling-and-voting under an `"Agent Forest"` / `"More Agents"` framing despite equivalence to generalized `Self-Consistency`, though candidly exposes task-difficulty dependence and saturation.

### `SR086` — *Single-agent or Multi-agent Systems? Why Not Both?*
* **Citation & Year:** Mingyan Gao, Yanzi Li, Banruo Liu, Yifan Yu, Phillip Wang, Ching-Yu Lin, Fan Lai (May 2025).
* **Verified Venue & Status:** Public preprint (`arXiv:2505.18286`); no OpenReview rejection/withdrawal found — **`Preprint (arXiv / Preprints.org)`**.
* **Verified Evidence URLs:** [arXiv:2505.18286](https://arxiv.org/abs/2505.18286)
* **Screening:** Stage 1 `INCLUDE`; Stage 2 `INCLUDE` (`I2(a)` & Sec. 2.5 `SAS→MAS` escalation exception `Gao et al. 2025`). Passes Preprint Gate (`8/14 >= 6`, `QA7 = 2`).
* **Tier & QA (`8/14 Moderate`):**
  * `QA1 = 1` (`Tier 2`): Evaluates `ChatDev`/`MetaGPT`/MAS vs tool-equipped SAS on `OpenAI-o3`, `Gemini-2.5-Pro`, `GPT-4o`, `Llama-3.1` across `SWE-bench`, `MATH-500`, `AIME`, `DS-1000`, without equal-token `Best-of-N`/`SC` parity.
  * `QA2 = 1`: Formalizes prefill+decode token cost function $C(r)$ and reports cost savings (`up to 20%` / `88.1%`); omits quantitative wall-clock latency seconds.
  * `QA3 = 2`: `Agent Cascade` uses verifier checks (`SAS` -> verify -> escalate to `MAS`) and `Agent Routing` uses zero-shot LLM difficulty rating (no RL/MCTS weight training).
  * `QA4 = 0`: Reports point-estimate accuracy/cost trade-offs without multi-seed SD/CIs.
  * `QA5 = 1`: Standard/verifiable coding & math benchmarks with shared tools, lacking formal leakage audit.
  * `QA6 = 1`: Detailed design in `arXiv:2505.18286`, no public GitHub repo linked in v1 preprint.
  * `QA7 = 2`: Accurately reports narrowing MAS-over-SAS margins on frontier models and hybrid cascade gains matching tables.

### `SR087` — *Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?*
* **Citation & Year:** Hyeong Kyu Choi, Xiaojin Zhu, Yixuan Li (2025).
* **Verified Venue & Status:** **NeurIPS 2025 Spotlight** — **`Peer-reviewed conference`**.
* **Verified Evidence URLs:** [OpenReview (`iUjGNJzrF1`)](https://openreview.net/forum?id=iUjGNJzrF1) | [NeurIPS 2025 Abstract (`934252acd87f254d5d4672fbde283bd2`)](https://papers.neurips.cc/paper_files/paper/2025/hash/934252acd87f254d5d4672fbde283bd2-Abstract-Conference.html) | [arXiv:2508.17536](https://arxiv.org/abs/2508.17536) | [GitHub (`deeplearning-wisc/debate-or-vote`)](https://github.com/deeplearning-wisc/debate-or-vote)
* **Screening:** Stage 1 `INCLUDE`; Stage 2 `INCLUDE` (`I2(a)` & `I2(b)` across 7 benchmarks + Martingale theory).
* **Tier & QA (`8/14 Moderate`):**
  * `QA1 = 1` (`Tier 2`): Benchmarks Decentralized/Sparse/Centralized MAD against `Majority Voting (T=0)` ($N$ independent samples) and `Single Agent` on identical models (`Qwen2.5-7B-Instruct`, `Llama-3.1-8B-Instruct`); unmatched total debate tokens (MAD receives $T$-round compute yet MV matches/outperforms MAD).
  * `QA2 = 0`: Omits systematic token count/USD tables and wall-clock latency.
  * `QA3 = 2`: Inference-only debate/voting and prompted belief-bias interventions (`MAD-Conformist`/`MAD-Follower`).
  * `QA4 = 0`: Primary tables/charts report dataset accuracies without multi-seed SD or error bars.
  * `QA5 = 1`: Standard 7 NLP benchmarks (`T=1.0`, `p=0.9`, `max_tokens=512`), without formal contamination audit.
  * `QA6 = 2`: Public repository `deeplearning-wisc/debate-or-vote` + decoding configs.
  * `QA7 = 2`: Strong negative/explanatory claims (MV explains most MAD gains; Martingale curse) match empirical tables and proofs.

### `SR088` — *Multi-LLM Debate: Framework, Principals, and Interventions*
* **Citation & Year:** Andrew Estornell, Yang Liu (2024).
* **Verified Venue & Status:** **NeurIPS 2024** Main Conference — **`Peer-reviewed conference`**.
* **Verified Evidence URLs:** [OpenReview (`sy7eSEXdPC`)](https://openreview.net/forum?id=sy7eSEXdPC) | [NeurIPS 2024 PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/32e07a110c6c6acf1afbf2bf82b614ad-Paper-Conference.pdf)
* **Screening:** Stage 1 `INCLUDE`; Stage 2 `INCLUDE` (`I2(a)` & `I2(b)` formalizing misconception convergence and testing 3 interventions vs `Single-Agent`, `Majority`, and `Debate`).
* **Tier & QA (`7/14 Moderate`):**
  * `QA1 = 1` (`Tier 2`): Evaluates `Single-Agent` and `Majority` voting alongside standard `Debate` across `GPT`/`Llama`/`Mistral` models on `MMLU`, `HellaSwag`, `CSQA`, `MedMCQA`, `HH-RLHF`, without equal-token scaling of `Majority` vs multi-round debate.
  * `QA2 = 0`: Neither token/USD expenditures nor wall-clock latencies are systematically tabulated.
  * `QA3 = 2`: Zero upfront RL/MCTS training (inference-time Bayesian/pruning interventions).
  * `QA4 = 0`: Single-run benchmark accuracies without multi-seed SD or CIs.
  * `QA5 = 1`: Standard QA/NLI/alignment benchmarks without leakage audits.
  * `QA6 = 1`: Detailed algorithms/interventions in NeurIPS proceedings, but no official GitHub repository linked in the NeurIPS 2024 release.
  * `QA7 = 2`: Theoretical convergence-to-misconception results and intervention improvements align with empirical tables.

### `SR089` — *The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate*
* **Citation & Year:** Blaž Bertalanič, Carolina Fortuna (May 2026).
* **Verified Venue & Status:** *Proceedings of the ACM Conference on AI and Agentic Systems (CAIS '26)* — **`Peer-reviewed conference`** *(upgraded from arXiv preprint via live DOI verification)*.
* **Verified Evidence URLs:** [ACM DOI `10.1145/3786335.3813137`](https://doi.org/10.1145/3786335.3813137) | [arXiv:2605.00914](https://arxiv.org/abs/2605.00914)
* **Screening:** Stage 1 `INCLUDE`; Stage 2 `INCLUDE` (`I2(a)` & `I2(b)` evaluating $N=10$ homogeneous MAD over $R=3$ rounds vs `Isolated Self-Correction` & stochastic noise control, quantifying sycophancy `85.5%`, contextual fragility `70.0%`, and consensus collapse `32.3 pp`).
* **Tier & QA (`10/14 Moderate`):**
  * `QA1 = 1` (`Tier 2`): Strong iterative `Isolated Self-Correction` SAS baseline + stochastic noise control on identical `Qwen2.5-7B`, `Llama-3.1-8B`, `Ministral-3-8B` models; MAS consumes `2.1×–3.4×` more tokens than SAS yet SAS still wins/ties.
  * `QA2 = 1`: Quantifies exact token consumption (up to `28,631` tokens/problem; `2.1×–3.4×` multiplier), omits wall-clock execution seconds.
  * `QA3 = 2`: Zero upfront search/training.
  * `QA4 = 1`: Evaluates $K/T$ ablations, Appendix C confidence calibration, and Appendix G run-level variance, though primary tables lack full $k \ge 3$ seed SD/95% CIs across every cell.
  * `QA5 = 2`: Hardened `GSM-Hard` & `MMLU-Hard` evaluations + stochastic noise controls isolating peer content from context length.
  * `QA6 = 1`: Publishes full prompts in Appendix A (`A.1`/`A.2`), though no public GitHub repo URL appears in the paper text.
  * `QA7 = 2`: Negative findings on homogeneous MAD process loss match all tables and failure-pathway decompositions.

### `SR090` — *When Does Multi-Agent Collaboration Help? An Entropy Perspective*
* **Citation & Year:** Yuxuan Zhao, Sijia Chen, Ningxin Su (Feb 2026).
* **Verified Venue & Status:** `arXiv:2602.04234` + active OpenReview submission to **ACL ARR August 2026** (`Submission #1068` under *Understanding Large Language Models-based Multi-Agent Collaboration Through Entropy Dynamics*; neither rejected nor withdrawn) — **`Preprint (arXiv / Preprints.org)`**.
* **Verified Evidence URLs:** [arXiv:2602.04234](https://arxiv.org/abs/2602.04234) | [GitHub (`AgenticFinLab/multiagent-entropy`)](https://github.com/AgenticFinLab/multiagent-entropy) | [Project Page (`multiagent-entropy.github.io`)](https://multiagent-entropy.github.io/)
* **Screening:** Stage 1 `INCLUDE`; Stage 2 `INCLUDE` (`I2(a)` & `I2(b)` across 6 reasoning + 2 agentic tasks & 245 entropy features; SAS beats MAS in `~43.3%` of cases). Passes Preprint Gate (`11/14 >= 6`, `QA7 = 2`).
* **Tier & QA (`11/14 High`):**
  * `QA1 = 1` (`Tier 2`): Evaluates SAS vs diverse MAS topologies and `Entropy Judger` across 8 benchmarks without equal-token matching between SAS and MAS.
  * `QA2 = 2`: Logs both per-agent/round token costs and execution latencies.
  * `QA3 = 2`: Training-free `Entropy Judger` selection from `pass@k` trajectories.
  * `QA4 = 1`: Multi-sample `pass@k` evaluations across 8 benchmarks, without per-cell multi-seed SD/CIs in summary tables.
  * `QA5 = 1`: Standard reasoning/agentic tasks with consistent instructions, lacking formal leakage audit.
  * `QA6 = 2`: Public repository `AgenticFinLab/multiagent-entropy` + full prompts/role configs.
  * `QA7 = 2`: Balanced claims highlighting `43.3%` SAS wins and round-1 entropy lock-in matching tables.

### `SR091` — *Rethinking Multi-Agent Collaboration: When More Is Less* (`SAIGE`)
* **Citation & Year:** Yishuo Yuan, Yibo Wu, Yihan Zhang, Minyuan Sun, Shenliang Li, Xinkai Ma, Yifan Li, Jiaheng Liu (Sept 2026).
* **Verified Venue & Status:** Public preprint (`arXiv:2609.19759`); no OpenReview rejection/withdrawal found — **`Preprint (arXiv / Preprints.org)`**.
* **Verified Evidence URLs:** [arXiv:2609.19759](https://arxiv.org/abs/2609.19759)
* **Screening:** Stage 1 `INCLUDE`; Stage 2 `INCLUDE` (`I2(a)` evaluating `SAIGE`, `TDAG`, `DynTaskMAS`, `GoA` vs unified `Codex CLI` `Single-Agent` across `Terminal Bench 2.1`, `NL2Repo Bench`, `AgentIF-OneDay`, `Deep Research Bench II`). Passes Preprint Gate (`10/14 >= 6`, `QA7 = 2`).
* **Tier & QA (`10/14 Moderate`):**
  * `QA1 = 1` (`Tier 2`): Tool-equipped `Single-Agent` on identical `Codex CLI` harness & base model (`DeepSeek-V4-Pro`), evaluated at natural unmatched token budgets.
  * `QA2 = 1`: Reports cumulative multi-agent token/context consumption; omits wall-clock execution latency.
  * `QA3 = 2`: Training-free on-demand semantic graph evolution.
  * `QA4 = 1`: Averages outcomes over `k = 3` execution runs per task without full SD/CI dispersion tables.
  * `QA5 = 2`: Unified `Codex CLI` harness across 4 modern long-horizon benchmarks cleanly separating tightly coupled sequential vs sparse-dependency workflows.
  * `QA6 = 1`: Algorithmic specification in `arXiv:2609.19759`, no public GitHub URL in preprint text.
  * `QA7 = 2`: Candidly documents where `Single-Agent` beats MAS on sequential workflows alongside `SAIGE` efficiency gains on sparse-dependency tasks.

### `SR092` — *A Dynamic LLM-Powered Agent Network for Task-Oriented Agent Collaboration* (`DyLAN`)
* **Citation & Year:** Zijun Liu, Yanzhe Zhang, Peng Li, Yang Liu, Diyi Yang (2024).
* **Verified Venue & Status:** **COLM 2024** — **`Peer-reviewed conference`**.
* **Verified Evidence URLs:** [OpenReview (`XII0Wp1XA9`)](https://openreview.net/forum?id=XII0Wp1XA9) | [arXiv:2310.02170](https://arxiv.org/abs/2310.02170) | [GitHub (`SALT-NLP/DyLAN`)](https://github.com/SALT-NLP/DyLAN)
* **Screening:** Stage 1 `INCLUDE`; Stage 2 `INCLUDE` (`I2(a)` dynamic two-stage MAS topology vs `Single`, `CoT`, `Complex CoT`, `PHP`, `ReAct`, `Reflexion`, `LATS`, `LLM-Debate`).
* **Tier & QA (`7/14 Moderate`):**
  * `QA1 = 1` (`Tier 2`): Competitive SAS baselines (`CoT`, `Complex CoT`, `ReAct`, `Reflexion`, `LATS`) without equal-token parity or Stage 1 optimization amortization.
  * `QA2 = 1`: Tables 2–4 report Stage 2 API `#Calls` only, omitting full token/USD totals and wall-clock latency.
  * `QA3 = 1`: Sec. 3.2 describes Stage 1 Team Optimization qualitatively, while Tables 2–4 report only Stage 2 inference `#Calls` and omit quantitative Stage 1 API/token overhead from main tables and appendices (`C6`).
  * `QA4 = 0`: Single-run/`T=0` aggregate scores without $k \ge 3$ random-seed SD/CIs.
  * `QA5 = 1`: Standard `MATH`, `HumanEval`, `MMLU`, `GSM8K`, `Chess`, `GPQA-Diamond` tasks without formal leakage audit.
  * `QA6 = 2`: Public repository `SALT-NLP/DyLAN` + Table 5 role prompts.
  * `QA7 = 1`: Presents Stage 2 `#Calls` efficiency without accounting for Stage 1 agent-selection search calls in headline cost comparisons.

### `SR093` — *AgentDropout: Dynamic Agent Elimination for Token-Efficient and High-Performance LLM-Based Multi-Agent Collaboration*
* **Citation & Year:** Zhexuan Wang, Yutong Wang, Xuebo Liu, Liang Ding, Miao Zhang, Jie Liu, Min Zhang (2025).
* **Verified Venue & Status:** **ACL 2025** (Main Long Papers) — **`Peer-reviewed conference`**.
* **Verified Evidence URLs:** [ACL Anthology (`2025.acl-long.1170`)](https://aclanthology.org/2025.acl-long.1170/) | [arXiv:2503.18891](https://arxiv.org/abs/2503.18891) | [GitHub (`wangzx1219/AgentDropout`)](https://github.com/wangzx1219/AgentDropout)
* **Screening:** Stage 1 `INCLUDE`; Stage 2 `INCLUDE` (`I2(a)` node/edge dropout MAS vs `Vanilla`, `CoT`, unpruned MAS, `AgentPrune` across 6 benchmarks).
* **Tier & QA (`7/14 Moderate`):**
  * `QA1 = 1` (`Tier 2`): Includes `Vanilla` & `CoT` SAS without equal-token `SC` parity or amortized adjacency-optimization cost.
  * `QA2 = 1`: Reports inference prompt/completion tokens (`Ptok`/`Ctok`, `-21.6%`/`-18.4%`), omits wall-clock latency.
  * `QA3 = 1`: Learns round-wise node/edge adjacency matrices via iterative training steps described qualitatively without including optimization token budgets in comparative inference tables (`C6`).
  * `QA4 = 0`: Single-run aggregate accuracy/token scores without multi-seed SD/CIs.
  * `QA5 = 1`: Standard 6 benchmarks (`MMLU`, `GSM8K`, `AQuA`, `MultiArith`, `SVAMP`, `HumanEval`) without formal contamination/EvalPlus audit.
  * `QA6 = 2`: Public repository `wangzx1219/AgentDropout` + ACL 2025 text.
  * `QA7 = 1`: Headline token efficiency omits adjacency-training compute and equal-compute `SC` SAS comparators.

### `SR094` — *Optima: Optimizing Effectiveness and Efficiency for LLM-Based Multi-Agent System*
* **Citation & Year:** Weize Chen, Jiarui Yuan, Chen Qian, Cheng Yang, Zhiyuan Liu, Maosong Sun (2025).
* **Verified Venue & Status:** **Findings of ACL 2025** — **`Peer-reviewed conference`**.
* **Verified Evidence URLs:** [ACL Anthology (`2025.findings-acl.601`)](https://aclanthology.org/2025.findings-acl.601/) | [arXiv:2410.08115](https://arxiv.org/abs/2410.08115) | [GitHub (`thunlp/Optima`)](https://github.com/thunlp/Optima)
* **Screening:** Stage 1 `INCLUDE`; Stage 2 `INCLUDE` (`I2(a)` iterative MCTS + SFT/DPO/RL MAS training vs `CoT`, `Self-Consistency`, vanilla MAS).
* **Tier & QA (`7/14 Moderate`):**
  * `QA1 = 1` (`Tier 2`): Compares against `CoT` and `Self-Consistency` on `Llama 3` backbones, but compares post-trained MAS inference tokens without amortizing MCTS/SFT/DPO training compute.
  * `QA2 = 1`: Reports inference token consumption and `%` reduction curves; omits systematic wall-clock latency tables.
  * `QA3 = 1`: Mentions offline training budget (`<12h on 8× A100 GPUs`) in setup/discussion, but omits training token/USD expenditure and break-even $Q_{\text{break-even}}$ alongside comparative inference savings (`C6`).
  * `QA4 = 0`: Evaluates across optimization iterations without $k \ge 3$ random-seed SD/CIs in main tables.
  * `QA5 = 1`: Standard tasks without formal leakage/harness audit.
  * `QA6 = 2`: Public repository `thunlp/Optima` + project page.
  * `QA7 = 1`: Headline `"up to 2.8× performance with <10% tokens"` reflects inference-only tokens without amortizing MCTS/RL/DPO training costs.

### `SR095` — *Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning*
* **Citation & Year:** Haozhen Zhang, Tao Feng, Jiaxuan You (2025).
* **Verified Venue & Status:** **NeurIPS 2025** (Poster) — **`Peer-reviewed conference`**.
* **Verified Evidence URLs:** [OpenReview (`DWf4vroKWJ`)](https://openreview.net/forum?id=DWf4vroKWJ) | [arXiv:2506.09033](https://arxiv.org/abs/2506.09033) | [GitHub (`ulab-uiuc/Router-R1`)](https://github.com/ulab-uiuc/Router-R1)
* **Screening:** Stage 1 `INCLUDE` (conservative advance); Stage 2 **`EXCLUDE` (`E3`)**.
* **Rationale:** Self-described as a **single-agent RL LLM router** (`think`/`route` sequential policy modeled on `Search-R1`) invoking stateless external LLM APIs without inter-agent role interaction or persistent peer states; Tables 1–2 compare solely against single-LLM baselines (`Direct`, `CoT`, `SFT`, `RAG`, `Search-R1`) and single-round routers (`Prompt LLM`, `KNN Router`, `MLP`, `BERT`, `RouterDC`, `GraphRouter`, `FrugalGPT`) with **zero** MAS comparators (`MoA`, `MAD`, `AutoGen`) and no `SAS→MAS` escalation. Excluded under **Sec. 2.5** & **Sec. 4.2 `E3`**.

### `SR096` — *EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms*
* **Citation & Year:** Siyu Yuan, Kaitao Song, Jiangjie Chen, Xu Tan, Dongsheng Li, Deqing Yang (2025).
* **Verified Venue & Status:** **NAACL 2025** (Main Long Papers) — **`Peer-reviewed conference`**.
* **Verified Evidence URLs:** [ACL Anthology (`2025.naacl-long.315`)](https://aclanthology.org/2025.naacl-long.315/) | [arXiv:2406.14228](https://arxiv.org/abs/2406.14228) | [GitHub (`siyuyuan/evoagent`)](https://github.com/siyuyuan/evoagent)
* **Screening:** Stage 1 `INCLUDE`; Stage 2 `INCLUDE` (`I2(a)` evolutionary MAS generation vs `Direct`, `CoT`, `Self-Refine`, `SPP`, `AgentVerse`, `AutoAgents`).
* **Tier & QA (`7/14 Moderate`):**
  * `QA1 = 1` (`Tier 2`): Includes iterative SAS baselines (`CoT`, `Self-Refine`, `SPP`) alongside `Direct` without equal-token parity or amortized evolutionary search cost.
  * `QA2 = 1`: Reports partial time-efficiency comparisons in appendix analyses; omits systematic per-task token + wall-clock latency tables in main results.
  * `QA3 = 1`: Acknowledges evolutionary generation token/time overhead qualitatively without quantitative upfront search token/USD accounting and break-even analysis in main comparative tables (`C6`).
  * `QA4 = 0`: Single-run aggregate accuracy/success rates without $k \ge 3$ seed SD/CIs.
  * `QA5 = 1`: Standard reasoning/knowledge benchmarks without formal leakage audits.
  * `QA6 = 2`: Public repository `siyuyuan/evoagent` + `evo-agent.github.io`.
  * `QA7 = 1`: Broadly claims automatic MAS superiority without compute-matched `SC`/`Self-Refine` parity or full evolutionary search-cost amortization.

### `SR097` — *VerifyMAS: Hypothesis Verification for Failure Attribution in LLM-based Multi-Agent Systems*
* **Citation & Year:** Hezhe Qiao, Hanghang Tong, Ee-Peng Lim, Bing Liu, Guansong Pang (2026).
* **Verified Venue & Status:** **NeurIPS 2026** (Accepted Poster; verified real & indexed) — **`Peer-reviewed conference`**.
* **Verified Evidence URLs:** [arXiv:2605.17467](https://arxiv.org/abs/2605.17467) | [GitHub (`mala-lab/VerifyMAS`)](https://github.com/mala-lab/VerifyMAS)
* **Screening:** Stage 1 `INCLUDE`; Stage 2 `INCLUDE` (`I2(b)` MAS trajectory failure attribution across `Who&When` and `Aegis-Bench`).
* **Tier & QA (`8/12 Moderate` Diagnostic):**
  * `QA1 = N/A-Diagnostic` (`applicable_max_score = 12`): Non-comparative MAS trajectory failure-attribution evaluator (Sec. 2.3 & Sec. 6 Note).
  * `QA2 = 1`: Qualitatively notes preserved inference efficiency on long trajectories without systematic quantitative token + latency tables.
  * `QA3 = 1`: Details hypothesis-SFT loss ($\mathcal{L}_{\text{HSFT}}$) and verifier fine-tuning pipeline without quantitative GPU-hour/token training budgets.
  * `QA4 = 0`: Reports pair/agent/mode F1 scores without multi-run variance/SD/CIs.
  * `QA5 = 2`: Evaluates on standard MAS attribution benchmarks `Who&When` & `Aegis-Bench` across `Qwen`/`GPT`/`Gemini` backbones.
  * `QA6 = 2`: Public repository `mala-lab/VerifyMAS` + `arXiv:2605.17467` taxonomy.
  * `QA7 = 2`: Claims accurately reflect trajectory/agent localization F1 gains without MAS-over-SAS overclaiming.

### `SR098` — *Architecture Matters for Multi-Agent Security* (`Hagag et al.`)
* **Citation & Year:** Ben Hagag, William L. Anderson, Christian Schroeder de Witt, Sarah Scheffler (2026).
* **Verified Venue & Status:** **ICML 2026** (*PMLR 306:39306–39329*) — **`Peer-reviewed conference`**.
* **Verified Evidence URLs:** [PMLR (`v306/hagag26a`)](https://proceedings.mlr.press/v306/hagag26a.html) | [arXiv:2604.23459](https://arxiv.org/abs/2604.23459) | [GitHub (`benhagag10/Architecture-Matters-for-Multi-Agent-Security`)](https://github.com/benhagag10/Architecture-Matters-for-Multi-Agent-Security)
* **Screening:** Stage 1 `INCLUDE`; Stage 2 `INCLUDE` (`I2(a)` & `I2(b)` benchmarking 13 architectural configs — standalone full-tool `Single-Agent` vs 12 MAS role/topology `star`/`chain`/`mesh`/memory designs across `BrowserART`, `OS-Harm`/`OSWorld`, `SWE-bench`, finding MAS up to `3.8×` higher attack success rate than SAS).
* **Tier & QA (`11/14 High`):**
  * `QA1 = 1` (`Tier 2`): Full-tool standalone SAS baseline on identical `GPT-4o`, `Claude Sonnet`, `Llama` models & `Inspect AI` harnesses; authors explicitly disclose per-call token/cost data were not centrally retained, preventing `Tier 1` token parity verification.
  * `QA2 = 0`: Both token/USD logs and wall-clock latency omitted.
  * `QA3 = 2`: Zero upfront RL/MCTS training across the 13 static architecture configurations.
  * `QA4 = 2`: Reports 95% bootstrap confidence intervals across configurations/trials.
  * `QA5 = 2`: Rigorous stage-wise security/utility evaluation (`PR`/`ER`/`HA`/`HT`) across 3 realistic execution sandboxes (`BrowserART`, `OS-Harm`, `SWE-bench`) on `UK AISI Inspect AI`.
  * `QA6 = 2`: Official repository `benhagag10/Architecture-Matters-for-Multi-Agent-Security` releasing code, environments, judges, and prompt sets.
  * `QA7 = 2`: Balanced claims demonstrating `3.8×` ASR vulnerability variance across MAS vs SAS designs matching empirical sweeps.

### `SR099` — *NetSafe: Exploring the Topological Safety of Multi-agent System*
* **Citation & Year:** Miao Yu et al. (2025). *(Exact verified ACL Anthology entry: `2025.findings-acl.150`)*
* **Verified Venue & Status:** **Findings of ACL 2025** — **`Peer-reviewed conference`**.
* **Verified Evidence URLs:** [ACL Anthology (`2025.findings-acl.150`)](https://aclanthology.org/2025.findings-acl.150/) | [arXiv:2410.15686](https://arxiv.org/abs/2410.15686) | [GitHub (`Ymm-cll/NetSafe`)](https://github.com/Ymm-cll/NetSafe)
* **Screening:** Stage 1 `INCLUDE`; Stage 2 `INCLUDE` (`I2(b)` & `I2(a)` evaluating misinformation, bias, and harmful-info spread across `chain`, `tree`, `star`, `circle`, `complete` MAS topologies via `RelCom`, e.g. `-29.7%` star-graph degradation).
* **Tier & QA (`7/14 Moderate`):**
  * `QA1 = 0` (`Tier 4`): Evaluates MAS topologies strictly against each other with zero quantitative standalone SAS comparator.
  * `QA2 = 0`: Omits token/USD expenditure and wall-clock latency tables.
  * `QA3 = 2`: Training-free `RelCom` topological evaluation.
  * `QA4 = 0`: Omits systematic multi-seed SD/CIs in primary topology tables.
  * `QA5 = 1`: Standard datasets under 3 controlled attack types (`misinformation`, `bias`, `harmful`) without leakage or SAS-parity controls.
  * `QA6 = 2`: Public repository `Ymm-cll/NetSafe` + ACL Findings 2025 specifications.
  * `QA7 = 2`: Topological vulnerability findings (`star` vs longer-distance graphs) accurately match reported experiments.

### `SR100` — *G-Safeguard: A Topology-Guided Security Lens and Treatment on LLM-based Multi-agent Systems*
* **Citation & Year:** Shilong Wang, Guibin Zhang, Miao Yu, Guancheng Wan, Fanci Meng, Chongye Guo, Kun Wang, Yang Wang (2025).
* **Verified Venue & Status:** **ACL 2025** (Main Long Papers) — **`Peer-reviewed conference`**.
* **Verified Evidence URLs:** [ACL Anthology (`2025.acl-long.359`)](https://aclanthology.org/2025.acl-long.359/) | [arXiv:2502.11127](https://arxiv.org/abs/2502.11127) | [GitHub (`wslong20/G-safeguard`)](https://github.com/wslong20/G-safeguard)
* **Screening:** Stage 1 `INCLUDE`; Stage 2 `INCLUDE` (`I2(a)` & `I2(b)` GNN utterance-graph anomaly detection & edge pruning defense against prompt injection, tool, and memory attacks).
* **Tier & QA (`5/14 Low`):**
  * `QA1 = 0` (`Tier 4`): Compares against unguarded MAS (`AutoGen`/chain/star) and node-level text guardrails (`Llama-Guard`/`PromptGuard`), with zero standalone SAS baseline on the evaluated benchmarks/attacks.
  * `QA2 = 0`: Omits quantitative token overhead and wall-clock latency tables.
  * `QA3 = 1`: Trains supervised inductive GNN over labeled attack utterance graphs using frozen `Sentence-BERT` embeddings without tabulating GNN training or attack-labeling costs.
  * `QA4 = 0`: Reports recovery (`>40%`) and ASR metrics without multi-seed SD/CIs.
  * `QA5 = 1`: Standard `MMLU`/`CSQA` and attack suites across topologies without formal leakage or SAS-parity controls.
  * `QA6 = 2`: Public repository `wslong20/G-safeguard` + ACL 2025 release.
  * `QA7 = 1`: Claims minimal latency/token overhead qualitatively via out-of-band GNN framing without tabular token/latency proof or standalone SAS risk baseline.
