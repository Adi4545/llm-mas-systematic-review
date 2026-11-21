# Deliverable D — Literature Evidence Register (`Protocol v1.4`, Updated Corpus `N = 59`)

**Updated:** 2026-11-20 (`Protocol v1.4` Complete Open-Web Verification & Statistical Reconciliation)  
**Authoritative Data Ledger:** [evidence_matrix.json](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/evidence_matrix.json) (`59/59` records, `0` Draft 2020-12 JSON Schema errors)  
**Sibling Ledgers:** [search_log.json](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/search_log.json) (`S01`–`S13`), [screening_records.csv](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/screening_records.csv) (`100` records), [quality_appraisal.csv](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/quality_appraisal.csv) (`59` rows), [bibliography.bib](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/data/bibliography.bib) (`124` entries), and [tuple_cleanup_log.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/reviews/tuple_cleanup_log.md).

---

## 1. PRISMA 2020 Identification, Screening & Inclusion Summary (`Searches 1–13`)

- **Total Raw Records Identified:** `142` (`126` Wave 1 [`S01`–`S11`] + `16` Wave 2 [`S12`–`S13`], consolidated campaign date `2026-11-20`).
- **Duplicates & Preprint-to-Archival Versions Collapsed:** `42` (`27` version merges + `15` cross-query/snowball overlaps).
- **Unique Records Screened at Stage 1:** `100` (`SR001`–`SR100`; full dual-pass Stage 1 agreement = `98.0%`, `98/100`, inter-model Cohen's $\kappa = 0.9533$; Wave 1 baseline $\kappa = 0.9489`).
- **Excluded at Stage 1:** `30` (`E4` Secondary Surveys: `15`, `E3` Single-Agent/No MAS: `6`, `E8` Rejected/Withdrawn Primary Versions: `6`, `E7` Unrelated Task Scope: `3`).
- **Stage 2 Open Full-Text & Structured Open-Summary Eligibility (`n = 70` dual-reviewed):** `3`-class agreement = `92.86%` (`65/70`, inter-model $\kappa = 0.74`); pooled screening-judgment agreement across `170` decisions = **`163/170` (`95.9%`)**; end-to-end record agreement across `100` unique records = **`95.0%`** (`95/100`, $\kappa = 0.897`). *(Disclosure: agreement metrics measure inter-model dual-pass screening consistency backed by 100% human-author source verification.)*
- **Excluded at Stage 2:** `11` (`E5` Abstract/Paywall Only: `3`, `E3` Single-Agent/Router: `3`, `E2` Non-Empirical: `2`, `E7` Outside Scope: `2`, `E4` Survey: `1`).
- **Final Included Corpus (`N = 59`):**
  - **Archival (`43` / `72.9%`):** `4` Peer-reviewed journals + `39` Peer-reviewed conference papers.
  - **Workshop (`4` / `6.8%`):** `4` peer-reviewed workshop papers (`SR012` *ColMAD* ICML Workshop, `SR039` *WebArena Verified* NeurIPS Workshop, `SR040` *Verifier Transport* NeurIPS Workshop, `SR079` *CMAD* KDD Workshop).
  - **Preprint (`12` / `20.3%`):** `12` open preprints passing strict `>= 6/14 (12)` & `QA7 >= 1` gate.
  - **Comparative vs. Diagnostic Split:** `34` comparative MAS-vs-SAS studies (`87` cleaned comparisons) + `25` non-comparative mechanistic/security/validity studies (incl. `SR085` *Agent Forest* classified under `RQ4` `C3` solo-voting boundary).

---

## 2. Included Study Register (`N = 59`)

| Study ID | Ref # | Short Citation & Title | Venue & Year | Status | Track | SAS Parity Tier | QA Items & Score (`Pct`, Band) | Confounders (`C1`–`C6`) |
| :--- | :---: | :--- | :--- | :---: | :---: | :--- | :---: | :--- |
| `SR001` | `[46]` | Kim et al. (2026) - Scaling Agent Systems | Nature Machine Intelligence (Vol. 8, pp. 1157-1172) (2026) | Archival | `RQ1/2` | Tier 1 | `2-2-2-1-2-2-2` = `13/14` (`92.9%`, High) | None Observed |
| `SR002` | `[78]` | Tran & Kiela (2026) - Equal Thinking Budgets | arXiv (2026) | Preprint | `RQ1/2` | Tier 1 | `2-1-2-2-2-1-2` = `12/14` (`85.7%`, High) | C2, C5 |
| `SR003` | `[96]` | Xu et al. (2026) - OneFlow Strong SAS | arXiv / OpenReview (2026) | Preprint | `RQ1/2` | Tier 2 | `1-2-1-2-1-1-2` = `10/14` (`71.4%`, Moderate) | C6, C5 |
| `SR004` | `[61]` | Nguyen et al. (2026) - Think More or Read More | arXiv (2026) | Preprint | `RQ1/2` | Tier 1 | `2-2-2-1-2-1-2` = `12/14` (`85.7%`, High) | C5 |
| `SR005` | `[74]` | Smit et al. (2024) - Should We Be Going MAD? | ICML 2024 (PMLR Vol. 235) (2024) | Archival | `RQ1/2` | Tier 1 | `2-2-2-1-1-2-2` = `12/14` (`85.7%`, High) | C5 |
| `SR006` | `[84]` | Wang et al. (2024) - Rethinking Bounds of LLM Reasoning | ACL 2024 (Main) (2024) | Archival | `RQ1/2` | Tier 2 | `1-1-2-1-2-2-2` = `11/14` (`78.6%`, High) | C1, C5, C4 |
| `SR007` | `[110]` | Zhang et al. (2025) - Stop Overvaluing MAD (NeurIPS Spotlight) | NeurIPS 2025 (Position Paper Track Spotlight) (2025) | Archival | `RQ1/2` | Tier 1 | `2-1-2-1-2-1-2` = `11/14` (`78.6%`, High) | C5 |
| `SR008` | `[92]` | Wu et al. (2025) - Can LLM Agents Really Debate? | arXiv / OpenReview (2025) | Preprint | `RQ1/2` | Tier 2 | `1-1-2-1-2-1-2` = `10/14` (`71.4%`, Moderate) | C1 |
| `SR009` | `[22]` | Denisov-Blanch et al. (2026) - Truthfulness vs Polling | ICML 2026 (PMLR Vol. 306, pp. 24461-24477) (2026) | Archival | `RQ1/2` | Tier 2 | `1-1-2-2-2-1-2` = `11/14` (`78.6%`, High) | C1, C3 |
| `SR010` | `[53]` | Li et al. (2026) - Self-MoA (TMLR) | TMLR (2026) | Archival | `RQ1/2` | Tier 1 | `2-1-2-1-1-2-2` = `11/14` (`78.6%`, High) | C3, C5 |
| `SR011` | `[82]` | Wang et al. (2025) - Mixture-of-Agents (MoA) | ICLR 2025 (2025) | Archival | `RQ1/2` | Tier 3 | `1-1-2-1-1-2-1` = `9/14` (`64.3%`, Moderate) | C1, C3, C5 |
| `SR012` | `[15]` | Chen et al. (2026) - ColMAD (ICML Wkshp) | ICML 2026 Workshop on Failure Modes of Agentic AI (arXiv:2510.20963) (2026) | Workshop | `RQ1/2` | Tier 1 | `2-1-2-1-1-2-2` = `11/14` (`78.6%`, High) | None Observed |
| `SR013` | `[25]` | Du et al. (2024) - Multiagent Debate (ICML 2024) | ICML 2024 (PMLR Vol. 235) (2024) | Archival | `RQ1/2` | Tier 2 | `1-1-2-1-1-2-1` = `9/14` (`64.3%`, Moderate) | C1, C5 |
| `SR014` | `[67]` | Qian et al. (2025) - MacNet (ICLR 2025) | ICLR 2025 (2025) | Archival | `RQ1/2` | Tier 2 | `1-1-2-1-1-2-1` = `9/14` (`64.3%`, Moderate) | C1, C5 |
| `SR015` | `[124]` | Zhuge et al. (2024) - GPTSwarm (ICML 2024 Oral) | ICML 2024 (PMLR Vol. 235) (2024) | Archival | `RQ1/2` | Tier 2 | `1-1-1-2-1-2-1` = `9/14` (`64.3%`, Moderate) | C1, C4, C5, C6 |
| `SR016` | `[106]` | Zhang et al. (2025) - AgentPrune (ICLR 2025) | ICLR 2025 (2025) | Archival | `RQ1/2` | Tier 3 | `1-1-1-1-1-2-1` = `8/14` (`57.1%`, Moderate) | C1, C5, C6 |
| `SR017` | `[107]` | Zhang et al. (2025) - G-Designer (ICML 2025) | ICML 2025 (PMLR Vol. 267) (2025) | Archival | `RQ1/2` | Tier 3 | `1-2-1-2-1-2-1` = `10/14` (`71.4%`, Moderate) | C1, C5, C6 |
| `SR018` | `[112]` | Zhang et al. (2025) - AFlow (ICLR 2025 Oral) | ICLR 2025 Oral (2025) | Archival | `RQ1/2` | Tier 2 | `1-1-1-1-1-2-1` = `8/14` (`57.1%`, Moderate) | C1, C4, C5, C6 |
| `SR019` | `[105]` | Yue et al. (2025) - MasRouter (ACL 2025) | ACL 2025 (Main) (2025) | Archival | `RQ1/2` | Tier 2 | `1-1-1-1-1-2-2` = `9/14` (`64.3%`, Moderate) | C1, C5, C6 |
| `SR020` | `[10]` | Chang et al. (2026) - CascadeDebate (ACL Ind.) | ACL 2026 (Industry Track) (2026) | Archival | `RQ1/2` | Tier 2 | `1-2-1-1-1-1-2` = `9/14` (`64.3%`, Moderate) | C1, C5, C3, C6 |
| `SR021` | `[9]` | Cemri et al. (2025) - MAST (NeurIPS 2025 D&B) | NeurIPS 2025 (D&B Track) (2025) | Archival | `RQ3` | N/A | `NA-1-2-2-2-2-2` = `11/12` (`91.7%`, High) | None Observed |
| `SR022` | `[116]` | Zhang et al. (2025) - Who&When (ICML 2025) | ICML 2025 (PMLR Vol. 267) (2025) | Archival | `RQ3` | N/A | `NA-1-2-1-2-2-2` = `10/12` (`83.3%`, High) | C5 |
| `SR023` | `[108]` | Zhang et al. (2026) - AgenTracer (ICLR 2026) | ICLR 2026 (2026) | Archival | `RQ3` | N/A | `NA-1-2-1-1-2-2` = `9/12` (`75.0%`, Moderate) | None Observed |
| `SR025` | `[95]` | Xia et al. (2026) - AgentLocate (COLM 2026) | COLM 2026 (2026) | Archival | `RQ3` | N/A | `NA-2-2-1-2-1-2` = `10/12` (`83.3%`, High) | None Observed |
| `SR026` | `[13]` | Chen et al. (2026) - TraceElephant (ACL 2026) | ACL 2026 (2026) | Archival | `RQ3` | N/A | `NA-1-2-1-2-2-2` = `10/12` (`83.3%`, High) | C5 |
| `SR027` | `[86]` | Wang (2026) - TRIAGE (AACL-IJCNLP 2026) | AACL-IJCNLP 2026 (Short Papers) (2026) | Archival | `RQ3` | N/A | `NA-1-2-2-2-2-2` = `11/12` (`91.7%`, High) | C5 |
| `SR028` | `[23]` | Deshpande et al. (2025) - TRAIL | arXiv (2025) | Preprint | `RQ3` | N/A | `NA-1-2-1-2-2-2` = `10/12` (`83.3%`, High) | None Observed |
| `SR029` | `[17]` | Choi et al. (2025) - Group Conformity (ACL Findings) | Findings of ACL 2025 (2025) | Archival | `RQ3` | N/A | `NA-0-2-2-1-2-2` = `9/12` (`75.0%`, Moderate) | None Observed |
| `SR030` | `[63]` | Pitre et al. (2025) - CONSENSAGENT (ACL Findings) | Findings of ACL 2025 (2025) | Archival | `RQ3` | Tier 3 | `1-1-2-1-1-2-1` = `9/14` (`64.3%`, Moderate) | C1, C4, C5 |
| `SR031` | `[42]` | Kasprova et al. (2026) - Too Polite to Disagree (SIGDIAL) | SIGDIAL 2026 (2026) | Archival | `RQ3` | N/A | `NA-1-2-1-2-2-2` = `10/12` (`83.3%`, High) | None Observed |
| `SR032` | `[41]` | Kapoor et al. (2025) - AI Agents That Matter (TMLR) | TMLR (2025) | Archival | `RQ4` | N/A | `NA-1-2-2-2-2-2` = `11/12` (`91.7%`, High) | C5 |
| `SR033` | `[99]` | Yao et al. (2025) - tau-bench (ICLR 2025) | ICLR 2025 (2025) | Archival | `RQ4` | N/A | `NA-1-2-2-1-2-2` = `10/12` (`83.3%`, High) | C5 |
| `SR034` | `[69]` | Rabanser et al. (2026) - Science of AI Agent Reliability | ICML 2026 (2026) | Archival | `RQ4` | N/A | `NA-1-2-2-2-2-2` = `11/12` (`91.7%`, High) | C5 |
| `SR035` | `[57]` | Mehta (2025) - CLEAR Enterprise Framework | arXiv (2025) | Preprint | `RQ4` | N/A | `NA-2-2-2-1-1-2` = `10/12` (`83.3%`, High) | None Observed |
| `SR036` | `[88]` | Wang et al. (2026) - PatchDiff (ICSE 2026) | ICSE 2026 (2026) | Archival | `RQ4` | N/A | `NA-1-2-1-2-2-2` = `10/12` (`83.3%`, High) | C5 |
| `SR037` | `[123]` | Zhu et al. (2025) - ABC (NeurIPS 2025 D&B) | NeurIPS 2025 (D&B Track) (2025) | Archival | `RQ4` | N/A | `NA-1-2-1-2-2-2` = `10/12` (`83.3%`, High) | C5 |
| `SR038` | `[80]` | Wang et al. (2026) - BenchJack | arXiv (2026) | Preprint | `RQ4` | N/A | `NA-1-2-1-2-2-2` = `10/12` (`83.3%`, High) | C5 |
| `SR039` | `[26]` | El Hattami et al. (2025) - WebArena Verified | NeurIPS 2025 Workshop (Scaling Environments for Agents) (2025) | Workshop | `RQ4` | N/A | `NA-2-2-2-2-2-2` = `12/12` (`100.0%`, High) | C5 |
| `SR040` | `[73]` | Sheshanarayana & Goli (2026) - VTFR (NeurIPS Workshop) | NeurIPS 2026 Workshop (Who Verifies the Agents?) (2026) | Workshop | `RQ4` | N/A | `NA-1-2-1-2-2-2` = `10/12` (`83.3%`, High) | C5 |
| `SR069` | `[120]` | Zhou et al. (2026) - CORBA (ACL Findings) | Findings of ACL 2026 (2026) | Archival | `RQ3` | N/A | `NA-1-2-1-2-2-2` = `10/12` (`83.3%`, High) | None Observed |
| `SR075` | `[76]` | Szlatincsan et al. (2026) - Observe, Share, or Predict? | TMLR (Paper 13141) (2026) | Preprint | `RQ3` | N/A | `NA-1-2-1-2-1-2` = `9/12` (`75.0%`, Moderate) | C1, C3 |
| `SR076` | `[65]` | Pulici et al. (2026) - MADA-RL | TMLR (Paper 10674) (2026) | Preprint | `RQ1/2` | Tier 2 | `1-1-1-2-1-1-2` = `9/14` (`64.3%`, Moderate) | C1, C5, C6 |
| `SR079` | `[19]` | Dai (2026) - When Consensus Is Not Correctness (KDD Wkshp) | KDD 2026 Workshop on Evaluation and Trustworthiness of Agentic AI (2026) | Workshop | `RQ3` | N/A | `NA-0-2-2-1-1-2` = `8/12` (`66.7%`, Moderate) | C3 |
| `SR082` | `[118]` | Zhao et al. (2025) - SCALE (ACL 2025) | ACL 2025 (Main Long Papers) (2025) | Archival | `RQ1/2` | Tier 3 | `1-1-2-1-1-2-1` = `9/14` (`64.3%`, Moderate) | C1, C4 |
| `SR085` | `[51]` | Li et al. (2024) - More Agents Is All You Need (TMLR) | Transactions on Machine Learning Research (TMLR) (2024) | Archival | `RQ4` | N/A | `NA-1-2-1-1-2-1` = `8/12` (`66.7%`, Moderate) | C3, C5 |
| `SR086` | `[30]` | Gao et al. (2025) - Why Not Both? (arXiv) | arXiv preprint (2025) | Preprint | `RQ1/2` | Tier 2 | `1-1-2-0-1-1-2` = `8/14` (`57.1%`, Moderate) | C1, C4, C5 |
| `SR087` | `[16]` | Choi et al. (2025) - Debate or Vote (NeurIPS Spotlight) | Advances in Neural Information Processing Systems (NeurIPS 2025, Spotlight) (2025) | Archival | `RQ1/2` | Tier 2 | `1-0-2-0-1-2-2` = `8/14` (`57.1%`, Moderate) | C1, C3, C5 |
| `SR088` | `[27]` | Estornell & Liu (2024) - Multi-LLM Debate (NeurIPS) | Advances in Neural Information Processing Systems (NeurIPS 2024) (2024) | Archival | `RQ1/2` | Tier 2 | `1-0-2-0-1-1-2` = `7/14` (`50.0%`, Moderate) | C1, C5 |
| `SR089` | `[6]` | Bertalanic & Fortuna (2026) - Cost of Consensus (ACM CAIS) | Proceedings of the ACM Conference on AI and Agentic Systems (CAIS 2026) (2026) | Archival | `RQ1/2` | Tier 2 | `1-1-2-1-2-1-2` = `10/14` (`71.4%`, Moderate) | C1, C5 |
| `SR090` | `[119]` | Zhao et al. (2026) - Entropy Perspective (arXiv) | arXiv preprint (2026) | Preprint | `RQ1/2` | Tier 2 | `1-2-2-1-1-2-2` = `11/14` (`78.6%`, High) | C1, C5 |
| `SR091` | `[103]` | Yuan et al. (2026) - SAIGE When More Is Less (arXiv) | arXiv preprint (2026) | Preprint | `RQ1/2` | Tier 2 | `1-1-2-1-2-1-2` = `10/14` (`71.4%`, Moderate) | C1, C4, C5 |
| `SR092` | `[55]` | Liu et al. (2024) - DyLAN (COLM) | Conference on Language Modeling (COLM 2024) (2024) | Archival | `RQ1/2` | Tier 2 | `1-1-1-0-1-2-1` = `7/14` (`50.0%`, Moderate) | C1, C4, C5, C6 |
| `SR093` | `[89]` | Wang et al. (2025) - AgentDropout (ACL) | Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025, Volume 1: Long Papers) (2025) | Archival | `RQ1/2` | Tier 3 | `1-1-1-0-1-2-1` = `7/14` (`50.0%`, Moderate) | C1, C4, C5, C6 |
| `SR094` | `[14]` | Chen et al. (2025) - Optima (Findings ACL) | Findings of the Association for Computational Linguistics: ACL 2025 (2025) | Archival | `RQ1/2` | Tier 2 | `1-1-1-0-1-2-1` = `7/14` (`50.0%`, Moderate) | C1, C5, C6 |
| `SR096` | `[102]` | Yuan et al. (2025) - EvoAgent (NAACL) | Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL 2025, Volume 1: Long Papers) (2025) | Archival | `RQ1/2` | Tier 2 | `1-1-1-0-1-2-1` = `7/14` (`50.0%`, Moderate) | C1, C4, C5, C6 |
| `SR097` | `[68]` | VerifyMAS (2026) - Hypothesis Verification (NeurIPS) | Advances in Neural Information Processing Systems (NeurIPS 2026) (2026) | Archival | `RQ3` | N/A | `NA-1-2-0-2-2-2` = `9/12` (`75.0%`, Moderate) | C5 |
| `SR098` | `[34]` | Hagag et al. (2026) - Architecture Matters Security (ICML) | Proceedings of the 43rd International Conference on Machine Learning (ICML 2026) (Proceedings of Machine Learning Research, Vol. 306) (2026) | Archival | `RQ1/2` | Tier 2 | `1-0-2-2-2-2-2` = `11/14` (`78.6%`, High) | C1, C5 |
| `SR099` | `[101]` | Yu et al. (2025) - NetSafe Topological Safety (Findings ACL) | Findings of the Association for Computational Linguistics: ACL 2025 (2025) | Archival | `RQ3` | N/A | `NA-0-2-1-1-2-2` = `8/12` (`66.7%`, Moderate) | C5 |
| `SR100` | `[85]` | Wang et al. (2025) - G-Safeguard Security Lens (ACL) | Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025, Volume 1: Long Papers) (2025) | Archival | `RQ3` | N/A | `NA-0-2-0-1-2-1` = `6/12` (`50.0%`, Moderate) | C5 |

---

## 3. Excluded Record Ledger (`N = 41`)

| Excl ID | Record ID | Title | Year | Venue / Source | Stage Excluded | Code | Primary Exclusion Rationale |
| :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- |
| `Excl-01` | `SR024` | Where LLM Agents Fail and How They Can Learn From Failures | 2026 | ICML FAGEN Workshop 2026 | Stage 2 | `E3` | Verified ICML FAGEN Workshop paper (AgentDebug); separates 17 intra-agent module failure modes across Memory, Reflection, Planning, Action, System. |
| `Excl-02` | `SR041` | Multi-Agent Debate Strategies: Survey, Taxonomy, and Challenges | 2026 | arXiv (Under review at ACM CSUR) | Stage 1 | `E4` | Competing systematic survey of 141 MAD studies; excluded as secondary literature (E4), used for backward snowballing and Table 1 differentiation. |
| `Excl-03` | `SR042` | Literature Review Of Multi-Agent Debate For Problem-Solving | 2025 | arXiv | Stage 1 | `E4` | Competing literature review of Multi-Agent Debate profiles and topologies; excluded as secondary survey (E4). |
| `Excl-04` | `SR043` | A Survey for LLM Agent Trajectory Analysis: From Failure Attribution to Enhancement | 2026 | IEEE Transactions on Software Engineering (Vol. 52, No. 11) | Stage 1 | `E4` | Competing IEEE TSE 2026 survey on trajectory failure attribution; excluded as secondary review (E4), used for backward snowballing and Table 1 differentiation. |
| `Excl-05` | `SR044` | Survey on Evaluation of LLM-based Agents | 2026 | Findings of ACL 2026 | Stage 1 | `E4` | Competing general agent evaluation survey; excluded as secondary literature (E4). |
| `Excl-06` | `SR045` | From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents | 2026 | Findings of EMNLP 2026 | Stage 1 | `E4` | Competing survey of LLM agent workflow optimization (status kept conservatively as Preprint since EMNLP acceptance was not exposed in live search); excluded (E4). |
| `Excl-07` | `SR046` | Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | 2026 | arXiv | Stage 1 | `E4` | Competing communication-centric survey of LLM-MAS; excluded as secondary review (E4). |
| `Excl-08` | `SR047` | Efficiency in LLM Multi-Agent Systems: A Survey | 2026 | Preprints.org | Stage 1 | `E4` | Competing survey on efficiency control points in LLM-MAS; excluded as secondary literature (E4), retained for Table 1 differentiation. |
| `Excl-09` | `SR048` | Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey | 2026 | TMLR (2026) | Stage 1 | `E4` | Competing survey on single-query model routing and cascading (TMLR status unverified in search snippet); excluded as secondary literature (E4). |
| `Excl-10` | `SR049` | Autonomous agents and multi-agent systems: a comprehensive review | 2026 | Artificial Intelligence Review | Stage 1 | `E4` | Competing broad AIRE survey (2018-2026 agent blueprints); excluded as secondary literature (E4). |
| `Excl-11` | `SR050` | Scaling Up Multi-Agent Reinforcement Learning for Large Agent Teams and Long-Horizon Tasks: A Survey | 2026 | ACM Computing Surveys (Vol. 58, Issue 14) | Stage 1 | `E4` | Competing ACM CSUR survey focused on classical MARL team scaling; excluded as secondary review (E4). |
| `Excl-12` | `SR051` | The Emerged Security and Privacy of LLM Agent: A Survey with Case Studies | 2026 | ACM Computing Surveys (Vol. 58, Issue 6) | Stage 1 | `E4` | Competing ACM CSUR survey on LLM agent security and privacy; excluded as secondary literature (E4). |
| `Excl-13` | `SR052` | A Survey on the Optimization of Large Language Model-based Agents | 2026 | ACM Computing Surveys (Vol. 58, No. 9) | Stage 1 | `E4` | Competing ACM CSUR survey on general LLM agent optimization; excluded as secondary review (E4). |
| `Excl-14` | `SR053` | A survey on large language model based autonomous agents | 2024 | Frontiers of Computer Science | Stage 1 | `E4` | Competing Springer FCS foundational LLM autonomous agents survey; excluded as secondary literature (E4). |
| `Excl-15` | `SR054` | Large Language Models Miss the Multi-agent Mark | 2025 | NeurIPS 2025 (Position Paper Track) | Stage 2 | `E4` | Stage 2 full-text review confirms non-empirical position paper without primary MAS-vs-SAS quantitative benchmarks (E4); retained for Section 2 Terminological Gate. |
| `Excl-16` | `SR055` | A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence | 2026 | TMLR (Survey Certified) | Stage 1 | `E4` | Competing TMLR Survey-Certified review of self-evolving agents; excluded as secondary review (E4). |
| `Excl-17` | `SR056` | Towards Generalist Game Agents: A Survey of Foundation Models in Virtual Worlds | 2026 | TMLR | Stage 1 | `E4` | Competing TMLR survey on generalist game agents; excluded as secondary review (E4). |
| `Excl-18` | `SR057` | Model Swarms: Collaborative Search to Adapt LLM Experts via Swarm Intelligence | 2025 | ICML 2025 (PMLR Vol. 267) | Stage 2 | `E2` | Stage 2 confirms PSO search operates over static checkpoint weight space rather than communicating inference-time LLM agents (E2 per Section 2.5). |
| `Excl-19` | `SR058` | Multi-Agent Systems Powered by Large Language Models: Applications in Swarm Intelligence | 2025 | Frontiers in Artificial Intelligence | Stage 2 | `E2` | Stage 2 confirms NetLogo replication of classical ACO foraging and Boids flocking lacking SAS-vs-MAS benchmark tasks (E2). |
| `Excl-20` | `SR059` | RouteLLM: Learning to Route LLMs with Preference Data | 2025 | ICLR 2025 | Stage 1 | `E3` | Single-query weak-to-strong model router lacking inter-agent collaboration or SAS-to-MAS escalation (E3 per Section 2.5). |
| `Excl-21` | `SR060` | AutoMix: Automatically Mixing Language Models | 2024 | NeurIPS 2024 | Stage 1 | `E3` | Single-query POMDP routing/self-verification between weak and strong models without multi-agent collaboration (E3). |
| `Excl-22` | `SR061` | Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing | 2024 | ICLR 2024 | Stage 1 | `E3` | Single-query difficulty-aware LLM routing without multi-agent architecture or coordination (E3). |
| `Excl-23` | `SR062` | RouterBench: A Benchmark for Multi-LLM Routing System | 2024 | arXiv | Stage 1 | `E3` | Benchmark strictly for single-query multi-LLM selection without inter-agent interaction (E3). |
| `Excl-24` | `SR063` | Self-Refine: Iterative Refinement with Self-Feedback | 2023 | NeurIPS 2023 | Stage 1 | `E3` | Single-agent iterative self-feedback study without multi-agent role splitting or MAS comparator (E3). |
| `Excl-25` | `SR064` | Reflexion: Language Agents with Verbal Reinforcement Learning | 2023 | NeurIPS 2023 | Stage 1 | `E3` | Single-agent episodic verbal self-reflection loop without multi-agent peer interaction (E3). |
| `Excl-26` | `SR065` | Agentless: Demystifying LLM-Based Software Engineering Agents | 2025 | ACM FSE 2025 (PACMSE) | Stage 2 | `E3` | Stage 2 confirms deterministic 3-phase single-agent SWE pipeline lacking multi-agent architecture (E3); cited as strong SAS baseline template. |
| `Excl-27` | `SR066` | AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents | 2024 | NeurIPS 2024 (D&B Track) | Stage 1 | `E7` | Single-agent tool-use indirect prompt-injection security benchmark excluded per Section 2.5 (E7). |
| `Excl-28` | `SR067` | InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents | 2024 | Findings of ACL 2024 | Stage 1 | `E7` | Single-agent indirect prompt-injection benchmark without MAS coordination analysis (E7 per Section 2.5). |
| `Excl-29` | `SR068` | Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents | 2025 | ICLR 2025 | Stage 1 | `E7` | Single-agent security benchmark covering prompt injection and memory poisoning without MAS topology comparators (E7). |
| `Excl-30` | `SR070` | GNNs as Predictors of Agentic Workflow Performances | 2025 | LoG 2025 | Stage 2 | `E7` | Stage 2 confirms FLORA-Bench evaluates surrogate GNN workflow accuracy prediction without end-to-end MAS-vs-SAS task outcomes (E7). |
| `Excl-31` | `SR071` | Multi-Agent LLM-based Metamorphic Testing for REST APIs | 2026 | IEEE COMPSAC 2026 | Stage 2 | `E7` | Stage 2 confirms domain-specific REST API metamorphic oracle generation (ARMeta) without MAS-vs-SAS or coordination-failure evidence (E7). |
| `Excl-32` | `SR072` | Towards Automated or Assisted Requirements Extraction and Analysis Using an LLM-Based Multi-Agent System: A Case Study | 2025 | IEEE ICE/ITMC 2025 | Stage 2 | `E5` | Paywalled IEEE Xplore conference proceedings lacking any verified open-access mirror or arXiv preprint; methodology/outcomes unverifiable (E5). |
| `Excl-33` | `SR073` | Modular Approach for Controlling Multi-Agent Systems with Natural Language | 2025 | IEEE ISQED 2025 | Stage 2 | `E5` | Paywalled IEEE Xplore proceedings lacking open-access full text or arXiv preprint mirror; experimental data unverifiable (E5). |
| `Excl-34` | `SR074` | Multi-Agent Sycophancy Is a Pretrained Mid-Layer Vulnerability | 2026 | ICLR 2027 (OpenReview Sub #48858) | Stage 2 | `E5` | Active double-blind ICLR 2027 submission (Sep 2026) without de-anonymized public preprint or finalized review decision; excluded on hold (E5). |
| `Excl-35` | `SR077` | AgenticNet: Rethinking Multi-agent System Architectures with LLM-based Networks | 2025 | TMLR (Paper 7332) | Stage 1 | `E8` | Publicly rejected by TMLR under Criterion 1 (rebuttal strict exact-match drop MBPP 100%->77.5% and cost-matched MATH Level 5 trailing CoT); excluded from primary pool (E8), tracked for RQ4 Rejection Audit. |
| `Excl-36` | `SR078` | Inducing Disagreement in Multi-Agent LLM Executive Teams: Only the Devil's Advocate Works | 2025 | TMLR (Paper 7253) | Stage 1 | `E8` | Publicly rejected by TMLR (measured disagreement proxy 99.2% without outcome quality; isolated sampling labeled debate); excluded (E8), tracked for RQ4 Rejection Audit. |
| `Excl-37` | `SR080` | Agent Harness Engineering: A Survey | 2026 | TMLR | Stage 1 | `E8` | Verified author withdrawal on June 30 2026 (strictly Withdrawn, not rejected); also non-empirical survey (E4); excluded (E8). |
| `Excl-38` | `SR081` | Benchmarking LLMs' Swarm Intelligence | 2025 | ICLR 2026 / arXiv | Stage 1 | `E8` | Verified withdrawn at ICLR 2026 (SwarmBench); excluded from primary pool (E8), tracked in status-boundary audit. |
| `Excl-39` | `SR083` | Peacemaker or Troublemaker: How Sycophancy Shapes Multi-Agent Debate | 2025 | ICLR 2026 (Sub #8079) | Stage 1 | `E8` | Verified withdrawn at ICLR 2026 (Sub #8079); excluded from primary synthesis (E8), tracked as status-boundary methodological note. |
| `Excl-40` | `SR084` | A Survey on Self-play Methods in Reinforcement Learning | 2025 | TMLR (Paper 4567) | Stage 1 | `E8` | Verified rejected by TMLR May 2025 (also non-empirical MARL self-play survey E4); excluded (E8). |
| `Excl-41` | `SR095` | Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning | 2025 | Advances in Neural Information Processing Systems (NeurIPS 2025) | Stage 2 | `E3` | Director Arbitration: Uphold Agent 6 EXCLUDE (E3). Single RL-trained policy LLM calling external models as stateless black-box API tools analogous to Search-R1 without persistent N>=2 MAS roles or SAS->MAS escalation (contrasts Agent 3 INCLUDE boundary view; retained as cited E3 boundary contrast in manuscript). |

---

## 4. Machine Validation & Access Boundaries

- Schema check (`Draft202012Validator` vs. `extraction_schema.json`): **`59/59` (`0` errors)**.
- Exact `QA3 == 1` vs. `C6` alignment across comparative learned/optimized frameworks: **`True` (`12/12` comparative studies, `0%` amortized; vs. `22/34` static zero-search comparative studies)**.
- Missingness inventory (`"not verifiable from accessible open summary"`): **`404`** direct scalar fields (`478` total leaf strings) across `58/59` records where open summaries/preprints report normalized plots or relative changes without raw cell matrices (`SR001` NMI `arXiv:2512.08296` open mirror, `SR036` ICSE open mirror), with zero imputed values.
