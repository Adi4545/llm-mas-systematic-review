# Phase 2 & Phase 3 Quality Gate Log — Topic Selection, Saturation Audit & RQ Formulation

**Date:** November 20, 2026  
**Gate Owner:** Agent 1 (Research Director)  
**Inputs Audited:**
- `agents/agent5_topic_novelty_matrix.md` (Agent 5 — Research Gap & Novelty Analyst)
- `agents/agent3_topic_feasibility_probe.md` (Agent 3 — Literature Discovery Probe)
- `agents/agent8_topic_challenge.md` (Agent 8 — Evaluation Feasibility Challenger)
- `deliverables/Deliverable_B_Topic_and_Novelty_Report.md`

---

## 1. What Was Done
1. Launched Agents 5, 3, and 8 in parallel to independently evaluate candidate topics across novelty saturation, primary-literature density, and statistical/evaluation comparability.
2. Screened 42 verified 2023–2026 surveys/position papers across 10 candidate topics (`T1–T10`) and probed 84 primary/diagnostic empirical studies across 7 thematic clusters.
3. Challenged every candidate on baseline comparability, metric validity, risk of invalid cross-study pooling, and beginner/M.Tech defensibility.
4. Selected Primary Topic (`T1` integrated with topology strata, failure mechanisms, and evaluation validity audit), Fallback Topic (`T10`), and formulated 4 non-overlapping Research Questions (`RQ1–RQ4`).

## 2. Sources Actually Accessed
- Live `search_web` queries across `arxiv.org`, `openreview.net`, `aclanthology.org`, `proceedings.neurips.cc`, `mlr.press`, `dl.acm.org`, `link.springer.com`, `ieeexplore.ieee.org`, `preprints.org`, and `researchgate.net`.

## 3. What Was Established
1. **Heavy Saturation in Most Standalone Subtopics:** Standalone surveys on MAS security (`T5`: 6 surveys incl. CSUR *He et al.* & USENIX *Kim et al.*), communication topology (`T4`: *Yue et al.*, *Yan et al.*, *Zhu et al.*, *Li et al.*, CSUR *Geng et al.*), evaluation/harness catalogs (`T2`: 6 surveys), broad MAD/failure attribution (`T3`: *Motger et al.*, *Wang et al.* IEEE TSE 2026, *ACL ARR 2026* #2880/#3533), termination (`T9`: *Mallampati & Nagoriya*, *Dantas et al.*), and classical-vs.-LLM swarms (`T8`: 4 overlapping works) are crowded or preempted.
2. **Sparse Standalone Corpora (`T6`, `T7`):** Uncertainty-aware SAS→MAS escalation (`T6`) and MAS-specific `pass^k` reproducibility (`T7`) lack mature standalone MAS empirical corpora (<12–15 MAS-specific studies after separating single-agent works).
3. **Clear White Space (`T1` Integrated Framing):** Zero CSUR, TMLR, AIRE, JAIR, or arXiv systematic review audits head-to-head MAS-vs.-SAS empirical studies across compute-matched vs. unmatched regimes, topology strata, mechanistic failure drivers, and evaluation confounders—supported by a verified `Rich` primary corpus (25–45+ primary/diagnostic studies).

## 4. What Remains Uncertain & Access Limitations
- Several 2026 primary empirical studies and competing surveys (`preprints202609.1639`, `ACL ARR #2880/#3533`, *Kim et al.* *Nature Machine Intelligence* 2026 final vs. `arXiv:2512.08296` version differences, *Xu et al.* `2601.12307` OpenReview decision) had partial snippet visibility or unverified conference decision updates; final Phase 5 screening will verify exact statuses and numbers or explicitly tag `"not reported"`.
- Full PDFs behind Springer/ACM/IEEE paywalls remain inaccessible verbatim unless accompanied by open `arXiv`/institutional versions.

## 5. Agent Disagreements, Factual Audits & Evidence-Based Resolutions
1. **Scope Boundary Disagreement (Agent 5 vs. Agent 8 & Agent 3 on Topology `T4`):**
   - *Agent 5 position:* Rejected `T4` outright (62/100) due to crowding by *Yan et al.*, *Zhu et al.*, *Li et al.*, and *Yue et al.*, keeping `T1` tightly centered on SAS-vs.-MAS parity and 6 confounders.
   - *Agent 8 & Agent 3 position:* Argued that pure `T1` cannot explain *why* MAS succeeds or fails economically unless **coordination topology** (voting vs. chain vs. centralized star vs. sparse adaptive DAG) and **amortized search/training cost** are coded explicitly alongside SAS parity.
   - *Director Resolution:* **Integrated Compromise.** Reject `T4` as a standalone catalog of GNN/MCTS pruning algorithms, **but include Coordination Topology + Amortization Accounting explicitly as RQ2**—treating topology strictly as an empirical moderator of MAS-vs.-SAS effectiveness and total lifecycle cost.
2. **Metadata Audit Catch (Agent 3 Citation Swap):**
   - During cross-verification of `agents/agent3_topic_feasibility_probe.md` (line 231), Agent 1 detected that Agent 3 misattributed DOI `10.1145/3817113` (*Geng et al.* — actually CSUR MARL scaling survey) under Cluster 5 (Security), whereas CSUR's security survey is **He et al. (`10.1145/3773080`)**, correctly verified by Agent 2 and Agent 5. Corrected in `Deliverable_B` and logged for Phase 5 citation verification.
3. **Version-Consistency Flag (*Kim et al.* `arXiv:2512.08296`):**
   - Agent 5 noted `260` configurations, while Agent 3 noted `180 configurations (expanded to 260) / Nature Machine Intelligence (mid-2026)`. Director flagged this for strict primary-source verification during Phase 5 data extraction so exact preprint vs. published figures are never conflated.

## 6. Major Methodological Decisions
1. **Primary Topic Locked:** *When Do LLM Multi-Agent Systems Outperform Single Agents? A Systematic Review of Compute-Normalized Evidence, Coordination Topologies, Failure Mechanisms, and Evaluation Validity.*
2. **Fallback Topic Locked:** `T10` (*Inter-Agent Conformity Bias, Sycophancy Cascades, and Consensus Collapse in LLM Multi-Agent Systems*).
3. **Strict Anti-Pooling & Anti-Causal Rules:** Prohibit cross-benchmark score averaging; enforce within-study paired SAS-vs.-MAS coding (`Tier 1–4` baseline rigor); use conditional empirical-association phrasing rather than "universal causal laws."
4. **RQ1–RQ4 Locked:** Four orthogonal, non-assumption-loaded RQs mapping 1:1 to future Results subsections.

## 7. Gate Pass/Fail Verdict
**PASS — Quality Gate 2 & 3 Cleared.** Topic novelty against 42 prior surveys is verified, primary corpus density is confirmed (`Rich`), and RQ1–RQ4 are precisely operationalized to drive Phase 4 Protocol design.
