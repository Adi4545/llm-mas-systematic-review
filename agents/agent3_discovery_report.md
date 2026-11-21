# Agent 3 Discovery & Primary Screening Report (Phase 5 Wave 4A)

**Role:** Agent 3 (Literature Discovery Specialist)  
**Execution Date:** `2026-11-20`  
**Protocol Version:** `v1.0` ([Deliverable_C_Systematic_Review_Protocol.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/deliverables/Deliverable_C_Systematic_Review_Protocol.md))  
**Outputs Produced:**
- Search Log: [search_log.json](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/search_log.json)
- Candidate Screening Ledger (Pre-Agent-6): [screening_records.csv](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/screening_records.csv)

---

## 1. Executive Summary & Access-Honesty Declaration

Systematic open-web literature searches (`Q1`–`Q6`) and 1-hop backward/forward citation snowballing were executed on `November 20, 2026` using `search_web` across `arxiv.org`, `openreview.net`, `aclanthology.org`, `proceedings.neurips.cc`, `proceedings.mlr.press`, `dl.acm.org`, `link.springer.com`, `ieeexplore.ieee.org`, `nature.com`, `preprints.org`, and `semanticscholar.org`.

In strict adherence to the protocol's zero-fabrication and access-honesty covenant:
- **No closed-database index counts were fabricated** (no Scopus or Clarivate Web of Science bulk API/export access exists in this environment). Every `raw_hits_logged` integer in [search_log.json](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/search_log.json) reflects the exact count of distinct candidate papers surfaced and logged per executed search run.
- **Every record in [screening_records.csv](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/screening_records.csv) (`N = 84` unique deduplicated records)** carries verified authors, publication status as of `November 20, 2026`, canonical identifier, and an inspected `verified_url`.
- **Independent Dual-Screening Readiness:** All `stage1_agent6_*`, `stage2_agent6_*`, `final_decision`, and `final_exclusion_code` fields are initialized to `PENDING` so Agent 6 can screen independently without seeing locked final adjudications.

---

## 2. Search Execution & Deduplication Summary

Across **11 structured search executions (`S01`–`S11`)** spanning protocol queries `Q1`–`Q6`, 1-hop backward snowballing (`S10`), and 1-hop forward snowballing (`S11`), **`126` raw candidate records** were identified (`105` from `Q1`–`Q6`; `21` from snowballing). Applying the Section 5.1 deduplication and Preprint-to-Archival Linkage rules collapsed **`42` duplicate hits** (`27` preprint-to-archival/cross-portal merges and `15` cross-query/snowball overlaps), leaving **`84` unique candidate records** entering Stage 1 screening.

| Protocol Query / Source | Search IDs | Raw Hits Logged | Duplicates Collapsed | Unique New Records Added | Primary Scope Covered |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **`Q1`** | `S01`, `S02` | 20 | 7 | 13 | SAS-vs.-MAS compute/token-matched empirical benchmarks |
| **`Q2`** | `S03` | 13 | 5 | 8 | Coordination topologies, graph pruning, GNN/MCTS amortization |
| **`Q3`** | `S04`, `S05` | 21 | 9 | 12 | Error propagation, cascades, conformity/sycophancy, failure attribution |
| **`Q4`** | `S06` | 17 | 4 | 13 | Evaluation validity, `pass^k` decay, harness exploits, leakage audits |
| **`Q5`** | `S07` | 14 | 5 | 9 | Selective `SAS→MAS` escalation vs. single-query routers & classical swarms |
| **`Q6`** | `S08`, `S09` | 20 | 3 | 17 | OpenReview status audits (`Rejected`/`Withdrawn`/`Under review`) & publisher paywalls |
| **`Snowball-Backward`** | `S10` | 13 | 4 | 9 | 1-hop reference screening from Section 3.4 anchors & prior surveys |
| **`Snowball-Forward`** | `S11` | 8 | 5 | 3 | 1-hop citing works through `2026-11-20` via Semantic Scholar / open web |
| **TOTAL** | **`S01`–`S11`** | **`126`** | **`42`** | **`84`** | **`126 - 42 = 84` unique deduplicated records** |

### Preprint-to-Archival Linkage Accounting
- **18 peer-reviewed archival records** (`SR001`, `SR005`, `SR006`, `SR010`, `SR011`, `SR014`, `SR015`, `SR016`, `SR017`, `SR018`, `SR020`, `SR022`, `SR029`, `SR031`, `SR033`, `SR052`, `SR054`, `SR056`) retain a non-arXiv archival `canonical_id` (`doi:`, `PMLR:`, `ACL:`, `OpenReview:`) with their earlier `arXiv` identifier cross-linked in `linked_preprint_ids`.
- **26 peer-reviewed conference/workshop/journal records** retain their verified open-access `arXiv` identifier as `canonical_id` / `verified_url` (where proceedings pages were behind portals or lacked direct persistent slugs in search summaries) while accurately recording their verified acceptance in `venue` and `publication_status` (9 of which involved paired OpenReview/proceedings + arXiv deduplication merges during `S01`–`S09`, giving `18 + 9 = 27` preprint-to-archival merges).
- **2 non-archival audit records** (`SR082` *SCALE* and `SR084` *TMLR Paper 4567*) carry cross-linked `arXiv` identifiers in `linked_preprint_ids` for longitudinal tracking without duplicating records.

---

## 3. Exact Pre-Agent-6 PRISMA 2020 Screening Flow

*(All counts verified programmatically against [search_log.json](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/search_log.json) and [screening_records.csv](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/screening_records.csv) via Python `csv`/`json` checks.)*

```text
+-----------------------------------------------------------------------------+
| PRISMA 2020 IDENTIFICATION & SCREENING FLOW (PRE-AGENT-6 AGENT 3 LEDGER)    |
+-----------------------------------------------------------------------------+
| Identification:                                                             |
|   - Records retrieved via Boolean Queries Q1-Q6:          105               |
|   - Records added via backward/forward snowballing:        21               |
|   - Total raw records identified:                         126               |
|   - Duplicate / preprint-to-archival records merged:      -42               |
|   = Unique candidate records entering Stage 1:             84               |
+-----------------------------------------------------------------------------+
| Screening Stage 1 (Title, Abstract & Venue Metadata — Agent 3):             |
|   - Records screened at Stage 1:                           84               |
|   - Stage 1 exclusions (`EXCLUDE`):                       -32               |
|       * E4 (Competing surveys / reviews):                  15               |
|       * E8 (Withdrawn / publicly rejected audit cases):     8               |
|       * E3 (Single-query routers / single-agent loops):     6               |
|       * E7 (Single-agent prompt-injection benchmarks):      3               |
|   = Records advancing to Stage 2 (`PASS_TO_STAGE2`):       52               |
+-----------------------------------------------------------------------------+
| Eligibility Stage 2 (Full Text / Verified Open Summary — Agent 3):          |
|   - Records assessed at Stage 2:                           52               |
|   - Stage 2 exclusions (`EXCLUDE`):                       -12               |
|       * E5 (Paywalled IEEE / unverified double-blind):      5               |
|       * E7 (Surrogate predictor / adversarial / narrow):    3               |
|       * E2 (Weight-space PSO / classical NetLogo swarms):   2               |
|       * E3 (Deterministic 3-phase SAS pipeline Agentless):  1               |
|       * E4 (Non-empirical position essay La Malfa et al.):  1               |
|   = Agent 3 Stage 2 Included Studies (`INCLUDE`):          40               |
|       * Primary Comparative Effectiveness & Topology (RQ1/RQ2): 20          |
|       * Mechanistic Failure & Conformity Studies (RQ3):         11          |
|       * Evaluation-Validity & Reliability Audits (RQ4):          9          |
+-----------------------------------------------------------------------------+
| Independent Dual-Screening Status:                                          |
|   - Agent 6 Stage 1/2 votes & Final Arbitration:    PENDING (All 84 rows)   |
+-----------------------------------------------------------------------------+
```

### 3.1 Breakdown of the 40 Included Studies by Track & Publication Status

| Synthesis Track | Record IDs | Count | Journal (`Tier A`) | Conference (`Tier A`) | Workshop (`Tier B`) | Preprint (`Tier C`) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Primary Comparative (`RQ1`/`RQ2`)** | `SR001`–`SR020` | **20** | 2 | 14 | 0 | 4 |
| **Mechanistic Failure & Conformity (`RQ3`)** | `SR021`–`SR031` | **11** | 0 | 9 | 1 | 1 |
| **Evaluation-Validity & Reliability Audits (`RQ4`)** | `SR032`–`SR040` | **9** | 1 | 2 | 2 | 4 |
| **Total Included Corpus (Pre-Agent-6)** | **`SR001`–`SR040`** | **40** | **3** | **25** | **3** | **9** |

* **Peer-Reviewed Archival Core (`Peer-reviewed journal` + `Peer-reviewed conference`):** **28 / 40 (70.0%)**  
* **Peer-Reviewed Including Workshops (`Tier A` + `Tier B`):** **31 / 40 (77.5%)**  
* **Qualified Preprints (`Tier C`):** **9 / 40 (22.5%)** — supporting the mandatory dual sensitivity analysis (*Peer-Reviewed Only* vs. *Peer-Reviewed + Preprints*) in Phase 6.

### 3.2 Full 84-Record Publication-Status Distribution

| Exact `publication_status` Label | Total Records (`N = 84`) | Included (`INCLUDE`) | Excluded (`EXCLUDE`) | Primary Exclusion Codes |
| :--- | :---: | :---: | :---: | :--- |
| `Peer-reviewed journal` | 11 | 3 | 8 | `E4` (8 competing CSUR/AIRE/TSE/TMLR/FCS surveys) |
| `Peer-reviewed conference` | 41 | 25 | 16 | `E4` (2), `E3` (5), `E7` (5), `E2` (1), `E5` (2 paywalled IEEE), `E4/S2` (1) |
| `Workshop` | 3 | 3 | 0 | — |
| `Preprint (arXiv / Preprints.org)` | 18 | 9 | 9 | `E4` (6), `E3` (1), `E2` (1), `E7` (1) |
| `Under review` | 3 | 0 | 3 | `E5` (3 double-blind / unfinalized OpenReview holds) |
| `Publicly rejected` | 4 | 0 | 4 | `E8` (4 TMLR public rejections tracked for RQ4 audit) |
| `Withdrawn` | 4 | 0 | 4 | `E8` (4 OpenReview withdrawals tracked for status-boundary audit) |
| **Total** | **84** | **40** | **44** | **`E2:2, E3:7, E4:16, E5:5, E7:6, E8:8`** |

---

## 4. Notable Publication-Status Verifications, Corrections & Anti-Conflation Findings

Direct `search_web` verification on `November 20, 2026` resolved multiple status ambiguities and prevented snippet-conflation errors from propagating into Phase 5–6:

1. **Kim et al. (`arXiv:2512.08296`) Confirmed `Peer-reviewed journal` (`SR001`):** Verified published online July 24, 2026 in *Nature Machine Intelligence* (Vol. 8, pp. 1157–1172, `doi:10.1038/s42256-026-01268-y`) under its archival title *"Capable language models can outgrow the benefits of collaboration"*; `arXiv:2512.08296` (*"Towards a Science of Scaling Agent Systems"*) is merged as `linked_preprint_ids`.
2. **Self-MoA (Li et al., `arXiv:2502.00674`) Confirmed `Peer-reviewed journal` (`SR010`):** Verified accepted/published in *TMLR* (`https://openreview.net/forum?id=SDY0kddnVO`).
3. **Denisov-Blanch et al. (`arXiv:2603.06612`) Confirmed `Peer-reviewed conference` (`SR009`):** Verified accepted and presented at **ICML 2026** (concurrent proceedings title *"Truthfulness Does Not Scale Like Reasoning: Why Polling Fails as a Proxy Verifier"*).
4. **ColMAD (Chen et al., `arXiv:2510.18375`) Confirmed `Peer-reviewed conference` & De-Conflated (`SR012`):** Verified accepted at **ICML 2026** under `arXiv:2510.18375`; an initial multi-query snippet conflated `arXiv:2506.02951` with ColMAD, whereas isolated lookup verified `arXiv:2506.02951` belongs to *Adaptive Graph Pruning for Multi-Agent Communication* (Li et al., ECAI 2025).
5. **Model Swarms (Feng et al., ICML 2025) arXiv ID Corrected (`SR057`):** Isolated verification caught a false-match identifier (`arXiv:2410.16065` belongs to an astrophysics paper on Alpha Centauri) and verified the true identifier as `arXiv:2410.11163` (ICML 2025, PMLR 267; excluded under `E2` because PSO operates over checkpoint weights rather than communicating LLM agents).
6. **Preprints Maintained Conservatively as `Preprint (arXiv / Preprints.org)`:** *Tran & Kiela* (`2604.02460`, `SR002`), *Xu et al.* (*OneFlow*, `2601.12307`, `SR003`), *Nguyen et al.* (`2610.23246`, `SR004`), *Zhang et al.* (`2502.08788`, `SR007`), *Wu et al.* (`2511.07784`, `SR008`), *Deshpande et al.* (*TRAIL*, `2505.08638`, `SR028`), *Mehta* (*CLEAR*, `2511.14136`, `SR035`), *Zhu et al.* (*ABC*, `2507.02825`, `SR037`), *Wang et al.* (*BenchJack*, `2605.12673`, `SR038`), plus competing surveys *Yue et al.* (`2603.22386`, `SR045`) and *Moslem & Kelleher* (`2603.04445`, `SR048`), did not expose confirmed archival conference/journal acceptance in live `search_web` checks and are therefore kept strictly in `Preprint (arXiv / Preprints.org)`.
7. **Tracked `E8` Rejection & Withdrawal Audit Cases (`SR077`–`SR084`):**
   - *Publicly rejected (`4`):* `TMLR 7332` (*AgenticNet*, `SR077`), `TMLR 7253` (*Inducing Disagreement*, `SR078`), `TMLR 9844` (*When Consensus Is Not Correctness*, `SR079`), and `TMLR 4567` (*Survey on Self-Play Methods in RL*, `arXiv:2408.01072`, `SR084`).
   - *Withdrawn (`4`):* `TMLR 3hXEPbG0dh` (*Agent Harness Engineering: A Survey*, withdrawn June 30, 2026, `SR080`), *SwarmBench* (`arXiv:2505.04364`, withdrawn at ICLR 2026, `SR081`), *SCALE* (`ICLR 2025 Sub #6097`, withdrawn Jan 19, 2025, `SR082` — noting revised social-science content-analysis version later published at ACL 2025 `2025.acl-long.416` / `arXiv:2502.10937` remains outside `I2` MAS-vs.-SAS scope), and *Peacemaker or Troublemaker* (`arXiv:2509.23055`, withdrawn at ICLR 2026 Sub #8079, `SR083`).
8. **Verification of Previously Flagged Identifiers:** Unlike earlier feasibility-probe flags, targeted lookups confirmed that both `arXiv:2608.12921` (*E2-Explainer*, Li et al.) and `arXiv:2609.11737` (*ORCH*, embodied wildfire coordination) resolve to real 2026 arXiv preprints.

---

## 5. Access Boundaries & Paywall Exclusions (`E5`)

1. **No Closed Bibliographic Exports:** Neither **Scopus** nor **Clarivate Web of Science** bulk query/export endpoints are available; discovery reflects open academic indexing (`arXiv`, `OpenReview`, `ACL Anthology`, `PMLR`, `NeurIPS`, `Nature`, `ACM DL`, `SpringerLink`, `IEEE Xplore`, `Preprints.org`, `Semantic Scholar`).
2. **Paywalled Proceedings Without Open Preprints (`E5`):** Two verified IEEE Xplore papers surfaced in `Q6`—*Eberhardt et al. (2025)* (`10.1109/ice/itmc65658.2025.11106535`, `SR072`) and *Brazeau (2025)* (`10.1109/isqed65160.2025.11014337`, `SR073`)—lacked accessible open full texts or arXiv preprints upon targeted verification and were excluded at Stage 2 under `E5`. Conversely, *Khan et al. (2026)* (`IEEE COMPSAC`, `SR071`) had a verified open mirror (`arXiv:2605.28321`), allowing full-text Stage 2 assessment (excluded under `E7` narrow REST API testing scope).
3. **Double-Blind / Unfinalized `Under review` Holds (`E5`):** Three active OpenReview submissions—*Multi-Agent Sycophancy Is a Pretrained Mid-Layer Vulnerability* (`ICLR 2027 Sub #48858`, `SR074`), *Observe, Share, or Predict?* (`TMLR SMe5HYmSff`, `SR075`), and *MADA-RL* (`TMLR Paper 10674`, `SR076`)—lack finalized peer-review decisions or de-anonymized public empirical preprints and are held out under `E5`.

---

## 6. Handoff to Agent 6 (Independent Stage 1 & Stage 2 Dual Screening)

Agent 6 should now independently screen all **84 deduplicated records** in [screening_records.csv](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/screening_records.csv) by populating `stage1_agent6_decision`, `stage1_agent6_code`, `stage2_agent6_decision`, and `stage2_agent6_code` prior to computing pre-arbitration Cohen's $\kappa$ at Stage 1 and Stage 2 and handing conflicts to Agent 1 for arbitration.
