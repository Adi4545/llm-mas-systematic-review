# Agent 9 Citation Verification & Quality Appraisal Audit (`Phase 5 Wave 4B`)

**Auditor:** Agent 9 (Evidence and Citation Auditor)  
**Audit Date:** 2026-11-20  
**Scope:** Primary-source bibliographic verification, complete BibTeX compilation ([bibliography.bib](../data/bibliography.bib), **86 entries**), Protocol `v1.0` Section 6 `QA1`–`QA7` quality appraisal ([quality_appraisal.csv](../data/quality_appraisal.csv), **44 included studies**), Section 4.3 Rule 4 Preprint Gate audit, Phase 2 *Kim et al.* (`180` vs `260`) discrepancy resolution, and headline numerical claim spot-checks.

---

## 1. Executive Summary & Audit Outcome

| Audit Dimension | Result | Notes & Provenance |
|---|---|---|
| **Included Studies Verified** | **44 / 44 (100%)** | Every included study (`SR001`–`SR023`, `SR025`–`SR040`, `SR069`, `SR075`, `SR076`, `SR079`, `SR082`) verified against primary publisher/arXiv/OpenReview/ACL/PMLR sources. |
| **Compiled BibTeX Entries** | **86 unique entries** (`@article`: 20, `@inproceedings`: 40, `@misc`: 25, `@techreport`: 1) | Balanced braces (`depth = 0`), unique keys, zero syntax errors; spans all 44 included studies, 27 excluded/Table-1 surveys, 7 methodological/contrast works, and 8 RQ4 OpenReview audit cases. |
| **Publication-Status Upgrades** | **2 preprints upgraded to Peer-reviewed conference** | `SR007` (*Zhang et al.* -> **NeurIPS 2025 Position Paper Track Spotlight**, `OpenReview:tMJvb9JDsd`); `SR037` (*Zhu et al., ABC* -> **NeurIPS 2025 D&B Track**, `OpenReview:E58HNCqoaA`). Verified corpus composition shifts from `3 Journal / 27 Conf / 3 Workshop / 11 Preprint` to **`3 Journal / 29 Conf / 3 Workshop / 9 Preprint`** (`32/44 = 72.7%` Tier A Archival; `35/44 = 79.5%` Peer-Reviewed incl. Workshops). |
| **Critical Identifier Errors Caught** | **4 bogus/swapped IDs + 3 dead forum hashes + 2 year fixes + 6 author fixes** | Caught `SR012` *ColMAD* wrong physics arXiv ID (`2510.18375` -> `2510.20963`), `SR011` *MoA* wrong OpenReview hash (`PhMrGCMIRL`), `SR033` *$\tau$-bench* malformed reviewer-ID hash (`EMki-p3GC` -> `roNSXZpUDN`), `SR027` *TRIAGE* unverified ACL slug (`2026.aacl-short.347`), `SR032` (`2024 -> 2025`), `SR079` (`2025 -> 2026`), and `SR007`/`SR009`/`SR026`/`SR034`/`SR005`/`SR016`/`SR037`/`SR076`/`SR082` updates. |
| **Overall QA Rigor (`N = 44`)** | **26 High (59.1%), 18 Moderate (40.9%), 0 Low (0.0%)** | Mean **`77.5%`**, Median **`78.6%`**, Range **`57.1%`–`100.0%`**. Zero `Low` studies remain after dual-reviewer screening and the `E8` rejection-audit filter. |
| **Section 4.3 Rule 4 Preprint Gate** | **9 / 9 verified preprints PASS (100%)** | All 9 verified preprints (and both upgraded upstream preprints `SR007`, `SR037` under the 11-preprint sensitivity view) satisfy `total_raw_score >= 6` and `QA7 >= 1` (min `9/14 = 64.3%`, min `QA7 = 2`). |

> [!NOTE]
> Upstream ledgers ([included_studies.csv](../data/included_studies.csv) and [screening_records.csv](../data/screening_records.csv)) were preserved unmodified per Agent 9 read-only guardrails on upstream Phase 3/4 files. All verified identifiers, upgraded publication statuses, corrected author lists/years, and recovered proceedings pages are codified in [bibliography.bib](../data/bibliography.bib), [quality_appraisal.csv](../data/quality_appraisal.csv), and this audit report.

---

## 2. Resolution of Phase 2 Flag & Full Discrepancy Log

### 2.1 Resolution of *Kim et al.* (`SR001`) `180` vs `260` Configuration Count

Upstream Phase 2 (`phase_2_3_gate.md` / Agent 3 discovery) flagged an apparent configuration-count mismatch between **`180` configurations** (reported in earlier citations) and **`260` configurations** (reported in the July 2026 journal version). Primary-source inspection resolves this cleanly as an **expanded archival revision between preprint v1 and journal publication**:

| Version | Title & Venue | Date | Evaluated Scope |
|---|---|---|---|
| **Preprint v1** (`arXiv:2512.08296` v1) | *Towards a Science of Scaling Agent Systems: When and Why Agent Systems Work* | Dec 2025 | **180 configurations** across **4 benchmarks** (*Finance-Agent, BrowseComp-Plus, PlanCraft, Workbench*), 5 agent architectures (SAS + 4 MAS topologies), and 3 frontier LLM families. |
| **Archival Article / v3** ([Nature Machine Intelligence Vol. 8, pp. 1157–1172](https://doi.org/10.1038/s42256-026-01268-y)) | *Capable language models can outgrow the benefits of collaboration* (`doi:10.1038/s42256-026-01268-y`) | July 24, 2026 | Expanded to **260 configurations** across **6 benchmarks** (retaining the 4 core evaluation domains and adding **SWE-bench Verified** and **Terminal-Bench** for out-of-sample / domain validation). |

**Harmonization Rule for Synthesis:** Downstream extractors and synthesis tables MUST cite **`260` configurations across `6` benchmarks** when referencing the archival *Nature Machine Intelligence* (`2026`) regression model (`SR001`), while parenthetically noting **`180` configurations across `4` core benchmarks** when referencing the initial `arXiv:2512.08296` v1 controlled sweep so that no reader mistakes version expansion for an arithmetic contradiction.

### 2.2 Master Metadata, Status & Identifier Discrepancy Log

Every substantive error or update discovered relative to upstream Phase 3/4 CSVs (`included_studies.csv` / `screening_records.csv`) is itemized below:

1. **Critical Wrong / Conflated Identifiers Caught (`4` Included Records):**
   - **`SR012` (*ColMAD*, Chen et al., ICML 2026):** Upstream CSV cited `arXiv:2510.18375`, which actually resolves to an unrelated ultracold-atom physics preprint (*"Dynamically generating superflow in a bosonic ring via phase imprinting"* by Ke-Ji Chen & Fan Wu). Primary-source verification confirmed the true ID is **`arXiv:2510.20963`** (*"When and Why Does Multi-Agent Debate Fail and Does It Really Underperform?"* / earlier working title *"Towards Scalable Oversight with Collaborative Multi-Agent Debate in Error Detection"*).
   - **`SR011` (*MoA*, Wang et al., ICLR 2025):** Upstream CSV cited `OpenReview:PhMrGCMIRL`, which actually resolves to a completely different ICLR 2024 submission (*"Fusing Models with Complementary Expertise"* by Hongyi Wang et al.). Removed bogus hash and anchored `SR011_wang2025mixture` to canonical `https://arxiv.org/abs/2406.04692`.
   - **`SR033` ($\tau$-bench, Yao et al., ICLR 2025):** Upstream CSV cited `OpenReview:EMki-p3GC`, which concatenated two reviewer/note IDs (`EMki` and `p3GC`) rather than the submission forum ID. Reverse lookup verified the true OpenReview forum ID is **`roNSXZpUDN`** (`https://openreview.net/forum?id=roNSXZpUDN`).
   - **`SR027` (*TRIAGE*, Xizhi Wang, AACL-IJCNLP 2026):** Upstream CSV cited `ACL:2026.aacl-short.347`. Anthology lookup returned zero results for `2026.aacl-short.347` (the sequential short-paper range ends far earlier; e.g., `2026.aacl-short.34` belongs to Srijith Ravikumar). Confirmed publication in ACL Anthology *AACL-IJCNLP 2026 Vol. 2 Short Papers*; marked exact Anthology slug `"not verifiable"` in BibTeX note and anchored `url` to the verified author repository (`https://github.com/jimmywang585/triage-failure-attribution`).
2. **Unverifiable / Conflated OpenReview Hashes Audited (`4` Records):**
   - **`SR007` (*Zhang et al.*):** Upstream note referenced candidate `OpenReview:kfLtCPBset` (zero OpenReview hits). Reverse lookup confirmed canonical forum **`https://openreview.net/forum?id=tMJvb9JDsd`** (NeurIPS 2025 Position Paper Track Spotlight).
   - **`SR023` (*AgenTracer*, ICLR 2026):** Candidate hash `Sx038qxjek` belongs to *CRITIC* (ICLR 2024), and alternate candidate `l05DseqvuD` failed reverse verification; anchored cleanly to verified `https://arxiv.org/abs/2509.03312`.
   - **`SR025` (*AgentLocate*, COLM 2026):** Candidate hash `5RmOQVmCRO` failed reverse lookup; anchored cleanly to `https://arxiv.org/abs/2607.07989`.
   - **`SR079` (*When Consensus Is Not Correctness*, KDD 2026 Workshop):** Candidate workshop hash `lWCLnGrHhH` failed isolated verification and was omitted; anchored to verified workshop group `https://openreview.net/group?id=KDD.org/2026/Workshop/Agentic_AI` alongside the verified prior rejected TMLR submission IDs (`TMLR Paper 9844` and `TMLR Paper 11271`).
3. **Publication-Status Upgrades (`Preprint` -> `Peer-reviewed conference`) & Archival URL Upgrades:**
   - **`SR007` (*Zhang et al.*):** Upgraded from `Preprint (arXiv / Preprints.org)` (`arXiv:2502.08788`, working title *"If Multi-Agent Debate is the Answer, What is the Question?"*) to **`Peer-reviewed conference`** (**NeurIPS 2025 Position Paper Track Spotlight**, `https://openreview.net/forum?id=tMJvb9JDsd`, archival title *"Position: Stop Overvaluing Multi-Agent Debate—We Must Rethink Evaluation and Embrace Model Heterogeneity"*).
   - **`SR037` (*Zhu et al., ABC*):** Upgraded from `Preprint (arXiv / Preprints.org)` (`arXiv:2507.02825`, title variant *"...for Building..."*) to **`Peer-reviewed conference`** (**NeurIPS 2025 Datasets and Benchmarks Track**, `https://openreview.net/forum?id=E58HNCqoaA`, archival title *"Establishing Best Practices in Building Rigorous Agentic Benchmarks"*).
   - **Preprint-to-Proceedings Canonicalization (`8` Included + `3` Excluded Records):** Upgraded arXiv/draft URLs to canonical proceedings/journal URLs with verified volume/page numbers for **`SR009`** (ICML 2026 PMLR `v306` pp. `24461–24477`, title updated to *"Truthfulness Does Not Scale Like Reasoning: Why Polling Fails as a Proxy Verifier"*), **`SR010`** (TMLR published March 2026 `OpenReview:K6WwK8URlV`, replacing draft hash `SDY0kddnVO`), **`SR013`** (`PMLR v235`, pp. `11733–11763`), **`SR026`** (`ACL 2026.acl-long.912`, pp. `19888–19905`), **`SR034`** (`PMLR v306`, pp. `102769–102820`), **`SR036`** (ICSE 2026 `doi:10.1145/3744916.3764576`), **`SR039`** (`OpenReview:94tlGxmqkN`), plus excluded surveys **`SR044`** (upgraded *Findings of ACL 2025* -> **`Findings of ACL 2026`**, `2026.findings-acl.1330`, pp. `26690–26714`, year `2025 -> 2026`), **`SR048`** (`OpenReview:ypRg1TvQaM`), **`SR057`** (`PMLR v267`, pp. `16904–16930`), and **`SR058`** (`doi:10.3389/frai.2025.1593017`). Recovered exact proceedings pages for **`SR005`**, **`SR006`**, **`SR015`**, **`SR017`**, **`SR019`** (plus `doi:10.18653/v1/2025.acl-long.757`), **`SR020`**, **`SR022`**, **`SR029`**, **`SR030`**, **`SR031`**, **`SR069`**, and **`SR082`**.
4. **Publication Year Corrections (`3` Records):**
   - **`SR032` (*AI Agents That Matter*):** Corrected `2024` (arXiv v1 date) -> **`2025`** (published in *TMLR* on **June 13, 2025**, `OpenReview:zi7g1W899z`).
   - **`SR079` (*When Consensus Is Not Correctness*):** Corrected `2025` (prior rejected TMLR-9844 year) -> **`2026`** (included KDD 2026 Workshop version; prior rejected TMLR-9844/11271 retained separately under `TMLR2025_WhenConsensus_9844`).
   - **`SR055` (*Gao et al.* self-evolving agents survey):** Corrected `2025` -> **`2026`** (TMLR Survey Certified Jan 2026, `OpenReview:CTr3bovS5F`).
   - *(See also `SR044` above: `2025 -> 2026`.)*
5. **Author List Corrections & Expansions (`8` Records):**
   - **`SR005` (*Smit et al.*):** Corrected first author name and author order (`Andries Petrus Smit; Nathan Grinsztajn; Paul Duckworth; Thomas D. Barrett; Arnu Pretorius`).
   - **`SR016` (*AgentPrune*):** Restored omitted 9th author **Tianlong Chen**.
   - **`SR034` (*Rabanser et al.*):** Corrected 4th author **`Kangwook Liu` -> `Kangheng Liu`**.
   - **`SR037` (*Zhu et al., ABC*):** Added omitted co-author **Arvind Narayanan** (26 authors total on OpenReview `E58HNCqoaA`) and corrected **Antony Kellerman -> `Antony Kellermann`** (`Andy K. Zhang`, `Jasjeet S. Sekhon`).
   - **`SR076` (*MADA-RL*):** Expanded `et al.` to complete 6-author list (`Martino M. L. Pulici; Cuong Xuan Chu; Evgeny Kharlamov; Zifeng Ding; Volker Tresp; Yunpu Ma`).
   - **`SR082` (*SCALE*):** Corrected last two authors' order to **`Tianlong Chen; Huan Liu`** per `2025.acl-long.416`.
   - **`SR056` (*Generalist Game Agents Survey*):** Restored first 3 equal-contribution authors omitted upstream (`Kuan Zhang; Dongchen Liu; Qiyue Zhao`; 15 authors total).
   - **`SR080` (*Agent Harness Engineering Survey*):** Expanded truncated 5-author list to complete **19 authors** (`Junjie Li` through `Chandan K. Reddy`) on `OpenReview:3hXEPbG0dh`.

---

## 3. Headline Numerical Claim Spot-Checks (Primary-Source Verification)

Spot-checking critical quantitative claims cited across Phases 1–4 against open primary abstracts and proceedings HTML/PDF snippets confirmed the following exact anchor figures:

- **`SR001` (*Kim et al.*, NMI 2026 / arXiv:2512.08296):** Confirmed **`180`** (v1, 4 benchmarks) -> **`260`** (v3 / *Nature Machine Intelligence* 2026, 6 benchmarks) scaling audit; up to **+80.8% / +80.9%** parallelizable gains (*Finance-Agent*) vs **-39% to -70%** sequential degradation (*PlanCraft*) and **5.1x–17.2x** error amplification.
- **`SR002` (*Tran & Kiela*, 2026):** Confirmed **`336` configurations** ($4 \times 6 \times 2 \times 7$), **95% bootstrap confidence intervals**, and documented Gemini 2.5 `thoughts_token_count` discrepancy under equal thinking budgets.
- **`SR019` (*MasRouter*, ACL 2025):** Confirmed **`52.07%`** overhead drop on HumanEval and **`17.21%–28.17%`** API cost reduction reported, with controller training overhead disclosed in Appendix Table 12 rather than headline inference tables.
- **`SR021` (*MAST*, NeurIPS 2025 D&B):** Confirmed **`1,642`** annotated trajectories in `MAST-Data` across **7 MAS frameworks**, **14** unique failure modes, overall failure rates of **~41%–86.7%**, and human inter-annotator agreement **$\kappa = 0.88$** across 150 traces.
- **`SR022` (*Who&When*, ICML 2025):** Confirmed **`127`** failure logs; best automated attribution attains **53.5%** agent-level and **14.2%** step-level accuracy.
- **`SR026` (*TraceElephant*, ACL 2026):** Confirmed partial vs full trace observability ablation boosts step-level localization by up to **+76.0%–76.5%**.
- **`SR027` (*TRIAGE*, AACL-IJCNLP 2026):** Confirmed **59.3%** single-gold-label ambiguity in *Who&When*, motivating severity-ranked multi-candidate triage over **326** traces (**1,184** candidates).
- **`SR031` (*Too Polite to Disagree*, SIGDIAL 2026):** Confirmed **+10.5%** discussion accuracy gain across 6 open-source LLMs via probing peer priors.
- **`SR033` ($\tau$-bench, ICLR 2025):** Confirmed `pass^k` reliability decay dropping from **<50% `pass^1`** to **<25% `pass^8`** in Retail.
- **`SR036` (*PatchDiff*, ICSE 2026):** Confirmed **7.8%** developer-test failures on *SWE-bench Verified*, **29.6%** behavioral divergence (**28.6%** incorrect plausible patches), bounding score inflation to **6.2 pp** (arXiv v2) / **6.2–6.4 pp** across preprint/archival versions.
- **`SR037` (*ABC*, NeurIPS 2025 D&B):** Confirmed task/outcome/reporting flaws driving up to **100% relative metric skew** and **-33%** difficulty overestimation (*CVE-Bench*).
- **`SR038` (*BenchJack*, 2026):** Confirmed **219** exploitable harness flaws discovered across **10** agent benchmarks, dropping to **<10%** hackability post-patching on 4 benchmarks.
- **`SR040` (*VTFR*, NeurIPS 2026 Workshop):** Confirmed Verifier Transport Failure Rates of **30.9%** (delegation), **31.0%** (macro-actions), and **20.3%** (compaction), recovering **85.5%** via provenance anchors.
- **`SR069` (*CORBA*, ACL 2026 Findings):** Confirmed topology-dependent Denial-of-Collaboration attack achieving **~92%–100%** blocking attack success (`P-ASR`) across AutoGen/CAMEL setups.
- **`SR079` (*When Consensus Is Not Correctness*, KDD 2026 Workshop):** Confirmed **18%–47%** miscoverage due to diversity collapse across 2,700 traces and conformal calibration fix.
- **`SR082` (*SCALE*, ACL 2025):** Confirmed **+15.4%** accuracy and **+41.1%** human-codebook agreement over single-agent ($N=1$) ablation.

---

## 4. Quality Appraisal (`QA1`–`QA7`) Distribution & Risk-of-Bias Summary

Quality appraisal followed Protocol `v1.0` Section 6 (`QA1`–`QA7`, each `0`–`2`). Comparative studies are scored out of **`14`**, whereas non-comparative RQ3 mechanistic / RQ4 validity studies receive `QA1 = N/A-Diagnostic` and are scored out of **`12`**. Rigor bands follow Protocol thresholds: **High** (`>= 78.0%`: `11–14/14` or `10–12/12`), **Moderate** (`42.5%–77.9%`: `6–10/14` or `6–9/12`), **Low** (`< 42.5%`: `0–5`).

### 4.1 Overall & Stratified Distribution (`N = 44`)

| Stratum (Verified Status) | $n$ | High (`>=78.0%`) | Moderate (`42.5%–77.9%`) | Low (`<42.5%`) | Mean % | Median % | Min–Max % |
|---|---:|---:|---:|---:|---:|---:|---:|
| **All Included Studies** | **44** | **26 (59.1%)** | **18 (40.9%)** | **0 (0.0%)** | **77.5%** | **78.6%** | **57.1%–100.0%** |
| **Peer-Reviewed Archival** *(3 Journal + 29 Conf)* | 32 | 18 (56.3%) | 14 (43.8%) | 0 (0.0%) | 76.9% | 78.6% | 57.1%–100.0% |
| **Workshop** *(Tier B Track)* | 3 | 2 (66.7%) | 1 (33.3%) | 0 (0.0%) | 83.3% | 83.3% | 75.0%–91.7% |
| **Preprint** *(Verified remaining Tier C)* | 9 | 6 (66.7%) | 3 (33.3%) | 0 (0.0%) | 77.8% | 78.6% | 64.3%–92.9% |
| *Sensitivity: Upstream 11-Preprint View (incl. `SR007`, `SR037`)* | *11* | *8 (72.7%)* | *3 (27.3%)* | *0 (0.0%)* | *78.4%* | *78.6%* | *64.3%–92.9%* |

### 4.2 Corpus Track & SAS Baseline Rigor Tier Breakdown

| Corpus Track | $n$ | High | Moderate | Low | Mean % | Median % | SAS Rigor Tier Distribution |
|---|---:|---:|---:|---:|---:|---:|---|
| **Primary Comparative Effectiveness & Topology (RQ1/RQ2)** | 23 | 10 | 13 | 0 | 72.4% | 71.4% | **Tier 1:** 10; **Tier 2:** 8; **Tier 3:** 4; **Tier 4:** 1 (`SR075`) |
| **Mechanistic Failure & Conformity Analysis (RQ3)** | 12 | 7 | 5 | 0 | 79.7% | 83.3% | **N/A-Diagnostic:** 11; **Tier 3:** 1 (`SR030`) |
| **Evaluation Validity & Harness Reliability Audit (RQ4)** | 9 | 9 | 0 | 0 | 87.9% | 83.3% | **N/A-Diagnostic:** 9 |

### 4.3 Per-Criterion Score Profile (`QA1`–`QA7`)

| Criterion | Score `0` | Score `1` | Score `2` | `N/A` | Mean ($/2.0$) | Stratum Mean (Archival / Wkshp / Preprint) | Key Structural Diagnostic |
|---|---:|---:|---:|---:|---:|---|---|
| **`QA1` SAS Baseline Rigor** | 1 | 13 | 10 | 20 | **1.38** *(n=24)* | 1.39 *(n=18)* / N/A / 1.33 *(n=6)* | Only 10/24 comparative studies use compute/token-matched Tier 1 SAS controls. |
| **`QA2` Cost & Latency Accounting** | 1 | 34 | 9 | 0 | **1.18** *(n=44)* | 1.16 / 1.00 / 1.33 | **Weakest overall domain:** 34/44 studies omit either wall-clock latency or full USD/token cost parity. |
| **`QA3` Amortization Transparency** | 0 | 10 | 34 | 0 | **1.77** *(n=44)* | 1.75 / 2.00 / 1.78 | Graph/RL/MCTS optimizers (`SR015`–`SR019`, `SR076`) rarely integrate upfront search break-even `Q` into headline gains. |
| **`QA4` Multi-Run & Statistical Rigor** | 0 | 29 | 15 | 0 | **1.34** *(n=44)* | 1.28 / 1.67 / 1.44 | **Second-weakest domain:** 29/44 lack systematic multi-seed dispersion (`k >= 3` SD/CI) or hypothesis testing across cells. |
| **`QA5` Harness Integrity** | 0 | 21 | 23 | 0 | **1.52** *(n=44)* | 1.47 / 1.67 / 1.67 | RQ4/RQ3 audits drive `QA5=2`, while many RQ1/RQ2 benchmark sweeps ignore leakage/parsing controls (`QA5=1`). |
| **`QA6` Reproducibility & Code** | 0 | 12 | 32 | 0 | **1.73** *(n=44)* | **1.88** / 1.67 / **1.22** | Main Archival advantage: Peer-reviewed papers provide public GitHub/HF artifacts (`1.88` vs `1.22` for Preprints). |
| **`QA7` Claims-Evidence Parity** | 0 | 9 | 35 | 0 | **1.80** *(n=44)* | **1.72** / 2.00 / **2.00** | All 9 `QA7=1` minor-inflation ratings occur in Peer-Reviewed Archival framework papers (`SR011`, `SR013`–`SR018`, `SR030`, `SR082`). |

### 4.4 Section 4.3 Rule 4 Preprint Gate Verification

Per Protocol `v1.0` Section 4.3 Rule 4, every preprint must achieve **`total_raw_score >= 6`** AND **`qa7_claims_parity >= 1`** to remain eligible for synthesis:

| `record_id` | Short Name | Verified Status | Score | `%` | `QA7` | Rigor Band | Gate Status |
|---|---|---|---:|---:|---:|---|---|
| `SR002` | Tran & Kiela (2026) — Equal Thinking Budgets | Preprint | `13/14` | `92.9%` | `2` | High | **PASS (`TRUE`)** |
| `SR003` | Xu et al. (2026) — OneFlow Strong SAS | Preprint | `11/14` | `78.6%` | `2` | High | **PASS (`TRUE`)** |
| `SR004` | Nguyen et al. (2026) — Think More or Read More | Preprint | `11/14` | `78.6%` | `2` | High | **PASS (`TRUE`)** |
| `SR008` | Wu et al. (2025) — Can LLM Agents Really Debate? | Preprint | `10/14` | `71.4%` | `2` | Moderate | **PASS (`TRUE`)** |
| `SR028` | Deshpande et al. (2025) — TRAIL | Preprint | `10/12` | `83.3%` | `2` | High | **PASS (`TRUE`)** |
| `SR035` | Mehta (2025) — CLEAR Enterprise Framework | Preprint | `10/12` | `83.3%` | `2` | High | **PASS (`TRUE`)** |
| `SR038` | Wang et al. (2026) — BenchJack | Preprint | `10/12` | `83.3%` | `2` | High | **PASS (`TRUE`)** |
| `SR075` | Szlatincsán et al. (2026) — Observe, Share, or Predict? | Preprint | `9/14` | `64.3%` | `2` | Moderate | **PASS (`TRUE`)** |
| `SR076` | Pulici et al. (2026) — MADA-RL | Preprint | `9/14` | `64.3%` | `2` | Moderate | **PASS (`TRUE`)** |
| *`SR007`* | *Zhang et al. (2025) — Stop Overvaluing MAD* | *Upgraded -> Peer-reviewed conf* | *`11/14`* | *`78.6%`* | *`2`* | *High* | *`N/A-PeerReviewed` (clears gate)* |
| *`SR037`* | *Zhu et al. (2025) — ABC* | *Upgraded -> Peer-reviewed conf* | *`10/12`* | *`83.3%`* | *`2`* | *High* | *`N/A-PeerReviewed` (clears gate)* |

**Preprint Gate Outcome:** **0 preprints failed.** All 9 verified preprints (and both upgraded archival papers from the upstream 11-preprint pool) pass cleanly.

---

## 5. Complete Primary-Source Verification Ledger

### 5.1 Included Studies (`N = 44`)

| `record_id` | Citekey (`bibliography.bib`) | Year | Verified Venue | Verified Canonical ID / Pages / DOI | Canonical URL | Verified Status | QA Score & Band |
|---|---|---:|---|---|---|---|---|
| `SR001` | `SR001_kim2026capable` | 2026 | *Nature Machine Intelligence* | Vol. 8, pp. `1157–1172`; `doi:10.1038/s42256-026-01268-y`; (`arXiv:2512.08296`) | [doi.org/10.1038/s42256-026-01268-y](https://doi.org/10.1038/s42256-026-01268-y) | Peer-reviewed journal | `13/14` (`92.9%`) **High** |
| `SR002` | `SR002_tran2026single` | 2026 | arXiv | `arXiv:2604.02460` | [arxiv.org/abs/2604.02460](https://arxiv.org/abs/2604.02460) | Preprint | `13/14` (`92.9%`) **High** |
| `SR003` | `SR003_xu2026rethinking` | 2026 | arXiv | `arXiv:2601.12307` | [arxiv.org/abs/2601.12307](https://arxiv.org/abs/2601.12307) | Preprint | `11/14` (`78.6%`) **High** |
| `SR004` | `SR004_nguyen2026think` | 2026 | arXiv | `arXiv:2610.23246` | [arxiv.org/abs/2610.23246](https://arxiv.org/abs/2610.23246) | Preprint | `11/14` (`78.6%`) **High** |
| `SR005` | `SR005_smit2024should` | 2024 | ICML 2024 | PMLR Vol. 235, pp. `45883–45905`; (`arXiv:2311.17371`) | [proceedings.mlr.press/v235/smit24a.html](https://proceedings.mlr.press/v235/smit24a.html) | Peer-reviewed conf | `12/14` (`85.7%`) **High** |
| `SR006` | `SR006_wang2024rethinking` | 2024 | ACL 2024 Main | `ACL:2024.acl-long.331`, pp. `6106–6131`; (`arXiv:2402.18272`) | [aclanthology.org/2024.acl-long.331/](https://aclanthology.org/2024.acl-long.331/) | Peer-reviewed conf | `11/14` (`78.6%`) **High** |
| `SR007` | `SR007_zhang2025stop` | 2025 | NeurIPS 2025 Position (Spotlight) | `OpenReview:tMJvb9JDsd`; (`arXiv:2502.08788`) **[Upgraded]** | [openreview.net/forum?id=tMJvb9JDsd](https://openreview.net/forum?id=tMJvb9JDsd) | Peer-reviewed conf | `11/14` (`78.6%`) **High** |
| `SR008` | `SR008_wu2025can` | 2025 | arXiv | `arXiv:2511.07784` | [arxiv.org/abs/2511.07784](https://arxiv.org/abs/2511.07784) | Preprint | `10/14` (`71.4%`) **Moderate** |
| `SR009` | `SR009_denisovblanch2026truthfulness` | 2026 | ICML 2026 | PMLR Vol. 306, pp. `24461–24477`; (`arXiv:2603.06612`) | [proceedings.mlr.press/v306/denisov-blanch26a.html](https://proceedings.mlr.press/v306/denisov-blanch26a.html) | Peer-reviewed conf | `12/14` (`85.7%`) **High** |
| `SR010` | `SR010_li2026rethinking` | 2026 | TMLR (Mar 2026) | `OpenReview:K6WwK8URlV` (draft `SDY0kddnVO`; `arXiv:2502.00674`) | [openreview.net/forum?id=K6WwK8URlV](https://openreview.net/forum?id=K6WwK8URlV) | Peer-reviewed journal | `11/14` (`78.6%`) **High** |
| `SR011` | `SR011_wang2025mixture` | 2025 | ICLR 2025 Poster | `arXiv:2406.04692` *(bogus `PhMrGCMIRL` removed)* | [arxiv.org/abs/2406.04692](https://arxiv.org/abs/2406.04692) | Peer-reviewed conf | `9/14` (`64.3%`) **Moderate** |
| `SR012` | `SR012_chen2026when` | 2026 | ICML 2026 | PMLR Vol. 306; `arXiv:2510.20963` *(fixed from `2510.18375`)* | [arxiv.org/abs/2510.20963](https://arxiv.org/abs/2510.20963) | Peer-reviewed conf | `11/14` (`78.6%`) **High** |
| `SR013` | `SR013_du2024improving` | 2024 | ICML 2024 | PMLR Vol. 235, pp. `11733–11763`; (`arXiv:2305.14325`) | [proceedings.mlr.press/v235/du24e.html](https://proceedings.mlr.press/v235/du24e.html) | Peer-reviewed conf | `9/14` (`64.3%`) **Moderate** |
| `SR014` | `SR014_qian2025scaling` | 2025 | ICLR 2025 Poster | `OpenReview:K3n5jPkrU6`; (`arXiv:2406.07155`) | [openreview.net/forum?id=K3n5jPkrU6](https://openreview.net/forum?id=K3n5jPkrU6) | Peer-reviewed conf | `9/14` (`64.3%`) **Moderate** |
| `SR015` | `SR015_zhuge2024gptswarm` | 2024 | ICML 2024 Oral | PMLR Vol. 235, pp. `62743–62767`; (`arXiv:2402.16823`) | [proceedings.mlr.press/v235/zhuge24a.html](https://proceedings.mlr.press/v235/zhuge24a.html) | Peer-reviewed conf | `9/14` (`64.3%`) **Moderate** |
| `SR016` | `SR016_zhang2025cut` | 2025 | ICLR 2025 | `OpenReview:LkzuPorQ5L`; (`arXiv:2410.02506`) | [openreview.net/forum?id=LkzuPorQ5L](https://openreview.net/forum?id=LkzuPorQ5L) | Peer-reviewed conf | `8/14` (`57.1%`) **Moderate** |
| `SR017` | `SR017_zhang2025gdesigner` | 2025 | ICML 2025 | PMLR Vol. 267, pp. `76678–76692`; (`arXiv:2410.11782`) | [proceedings.mlr.press/v267/zhang25cu.html](https://proceedings.mlr.press/v267/zhang25cu.html) | Peer-reviewed conf | `9/14` (`64.3%`) **Moderate** |
| `SR018` | `SR018_zhang2025aflow` | 2025 | ICLR 2025 Oral | `OpenReview:z5uVAKwmjf`; (`arXiv:2410.10762`) | [openreview.net/forum?id=z5uVAKwmjf](https://openreview.net/forum?id=z5uVAKwmjf) | Peer-reviewed conf | `8/14` (`57.1%`) **Moderate** |
| `SR019` | `SR019_yue2025masrouter` | 2025 | ACL 2025 Main | `ACL:2025.acl-long.757`, pp. `15549–15572`; `doi:10.18653/v1/2025.acl-long.757` | [aclanthology.org/2025.acl-long.757/](https://aclanthology.org/2025.acl-long.757/) | Peer-reviewed conf | `9/14` (`64.3%`) **Moderate** |
| `SR020` | `SR020_chang2026cascadedebate` | 2026 | ACL 2026 Industry | `ACL:2026.acl-industry.93`, pp. `1329–1340`; (`arXiv:2604.12262`) | [aclanthology.org/2026.acl-industry.93/](https://aclanthology.org/2026.acl-industry.93/) | Peer-reviewed conf | `10/14` (`71.4%`) **Moderate** |
| `SR021` | `SR021_cemri2025why` | 2025 | NeurIPS 2025 D&B | `arXiv:2503.13657`; GitHub `MAST` | [arxiv.org/abs/2503.13657](https://arxiv.org/abs/2503.13657) | Peer-reviewed conf | `11/12` (`91.7%`) **High** |
| `SR022` | `SR022_zhang2025which` | 2025 | ICML 2025 | PMLR Vol. 267, pp. `76583–76599`; (`arXiv:2505.00212`) | [proceedings.mlr.press/v267/zhang25cq.html](https://proceedings.mlr.press/v267/zhang25cq.html) | Peer-reviewed conf | `10/12` (`83.3%`) **High** |
| `SR023` | `SR023_zhang2026agentracer` | 2026 | ICLR 2026 Poster | `arXiv:2509.03312` *(Sub 3262; forum hash unverifiable)* | [arxiv.org/abs/2509.03312](https://arxiv.org/abs/2509.03312) | Peer-reviewed conf | `8/12` (`66.7%`) **Moderate** |
| `SR025` | `SR025_xia2026who` | 2026 | COLM 2026 | `arXiv:2607.07989` *(forum hash unverifiable)* | [arxiv.org/abs/2607.07989](https://arxiv.org/abs/2607.07989) | Peer-reviewed conf | `9/12` (`75.0%`) **Moderate** |
| `SR026` | `SR026_chen2026seeing` | 2026 | ACL 2026 Main | `ACL:2026.acl-long.912`, pp. `19888–19905`; (`arXiv:2604.22708`) | [aclanthology.org/2026.acl-long.912/](https://aclanthology.org/2026.acl-long.912/) | Peer-reviewed conf | `10/12` (`83.3%`) **High** |
| `SR027` | `SR027_wang2026triage` | 2026 | AACL-IJCNLP 2026 Short | Anthology indexed *(slug `2026.aacl-short.347` unverified)* | [github.com/jimmywang585/triage-failure-attribution](https://github.com/jimmywang585/triage-failure-attribution) | Peer-reviewed conf | `11/12` (`91.7%`) **High** |
| `SR028` | `SR028_deshpande2025trail` | 2025 | arXiv | `arXiv:2505.08638`; GitHub `patronus-ai/trail-benchmark` | [arxiv.org/abs/2505.08638](https://arxiv.org/abs/2505.08638) | Preprint | `10/12` (`83.3%`) **High** |
| `SR029` | `SR029_choi2025empirical` | 2025 | Findings of ACL 2025 | `ACL:2025.findings-acl.265`, pp. `5123–5139`; (`arXiv:2506.01332`) | [aclanthology.org/2025.findings-acl.265/](https://aclanthology.org/2025.findings-acl.265/) | Peer-reviewed conf | `9/12` (`75.0%`) **Moderate** |
| `SR030` | `SR030_pitre2025consensagent` | 2025 | Findings of ACL 2025 | `ACL:2025.findings-acl.1141`, pp. `22112–22133` | [aclanthology.org/2025.findings-acl.1141/](https://aclanthology.org/2025.findings-acl.1141/) | Peer-reviewed conf | `9/14` (`64.3%`) **Moderate** |
| `SR031` | `SR031_kasprova2026too` | 2026 | SIGDIAL 2026 | `ACL:2026.sigdial-1.56`, pp. `795–814`; (`arXiv:2604.02668`) | [aclanthology.org/2026.sigdial-1.56/](https://aclanthology.org/2026.sigdial-1.56/) | Peer-reviewed conf | `10/12` (`83.3%`) **High** |
| `SR032` | `SR032_kapoor2025agents` | 2025 | TMLR (Jun 2025) | `OpenReview:zi7g1W899z`; (`arXiv:2407.01502`) **[Year fixed]** | [openreview.net/forum?id=zi7g1W899z](https://openreview.net/forum?id=zi7g1W899z) | Peer-reviewed journal | `12/12` (`100.0%`) **High** |
| `SR033` | `SR033_yao2025taubench` | 2025 | ICLR 2025 Poster | `OpenReview:roNSXZpUDN` *(fixed from `EMki-p3GC`)*; (`arXiv:2406.12045`) | [openreview.net/forum?id=roNSXZpUDN](https://openreview.net/forum?id=roNSXZpUDN) | Peer-reviewed conf | `10/12` (`83.3%`) **High** |
| `SR034` | `SR034_rabanser2026towards` | 2026 | ICML 2026 | PMLR Vol. 306, pp. `102769–102820`; (`arXiv:2602.16666`) | [proceedings.mlr.press/v306/rabanser26a.html](https://proceedings.mlr.press/v306/rabanser26a.html) | Peer-reviewed conf | `12/12` (`100.0%`) **High** |
| `SR035` | `SR035_mehta2025beyond` | 2025 | arXiv | `arXiv:2511.14136` | [arxiv.org/abs/2511.14136](https://arxiv.org/abs/2511.14136) | Preprint | `10/12` (`83.3%`) **High** |
| `SR036` | `SR036_wang2026are` | 2026 | ICSE 2026 | `doi:10.1145/3744916.3764576`; (`arXiv:2503.15223`) | [doi.org/10.1145/3744916.3764576](https://doi.org/10.1145/3744916.3764576) | Peer-reviewed conf | `10/12` (`83.3%`) **High** |
| `SR037` | `SR037_zhu2025establishing` | 2025 | NeurIPS 2025 D&B | `OpenReview:E58HNCqoaA`; (`arXiv:2507.02825`) **[Upgraded]** | [openreview.net/forum?id=E58HNCqoaA](https://openreview.net/forum?id=E58HNCqoaA) | Peer-reviewed conf | `10/12` (`83.3%`) **High** |
| `SR038` | `SR038_wang2026do` | 2026 | arXiv | `arXiv:2605.12673`; GitHub `benchjack/benchjack` | [arxiv.org/abs/2605.12673](https://arxiv.org/abs/2605.12673) | Preprint | `10/12` (`83.3%`) **High** |
| `SR039` | `SR039_elhattami2025webarena` | 2025 | NeurIPS 2025 SEA Wkshp | `OpenReview:94tlGxmqkN`; GitHub `ServiceNow/webarena-verified` | [openreview.net/forum?id=94tlGxmqkN](https://openreview.net/forum?id=94tlGxmqkN) | Workshop | `11/12` (`91.7%`) **High** |
| `SR040` | `SR040_sheshanarayana2026do` | 2026 | NeurIPS 2026 Wkshp | `arXiv:2611.18471`; GitHub `Disha1001/Verification-Transport` | [arxiv.org/abs/2611.18471](https://arxiv.org/abs/2611.18471) | Workshop | `10/12` (`83.3%`) **High** |
| `SR069` | `SR069_zhou2026corba` | 2026 | Findings of ACL 2026 | `ACL:2026.findings-acl.342`, pp. `6899–6908`; (`arXiv:2502.14529`) | [aclanthology.org/2026.findings-acl.342/](https://aclanthology.org/2026.findings-acl.342/) | Peer-reviewed conf | `10/12` (`83.3%`) **High** |
| `SR075` | `SR075_szlatincsan2026observe` | 2026 | arXiv *(TMLR #13141 review)* | `arXiv:2610.16895`; (`OpenReview:SMe5HYmSff`) | [arxiv.org/abs/2610.16895](https://arxiv.org/abs/2610.16895) | Preprint | `9/14` (`64.3%`) **Moderate** |
| `SR076` | `SR076_pulici2026madarl` | 2026 | arXiv *(TMLR #10674 review)* | `arXiv:2607.18006`; (`OpenReview:1tnHPWFS9I`) | [arxiv.org/abs/2607.18006](https://arxiv.org/abs/2607.18006) | Preprint | `9/14` (`64.3%`) **Moderate** |
| `SR079` | `SR079_dai2026when` | 2026 | KDD 2026 Agentic AI Wkshp | Group `KDD.org/2026/Workshop/Agentic_AI` *(prior `TMLR-9844/11271`)* | [openreview.net/group?id=KDD.org/2026/Workshop/Agentic_AI](https://openreview.net/group?id=KDD.org/2026/Workshop/Agentic_AI) | Workshop | `9/12` (`75.0%`) **Moderate** |
| `SR082` | `SR082_zhao2025scale` | 2025 | ACL 2025 Main | `ACL:2025.acl-long.416`, pp. `8473–8503`; (`arXiv:2502.10937`) | [aclanthology.org/2025.acl-long.416/](https://aclanthology.org/2025.acl-long.416/) | Peer-reviewed conf | `9/14` (`64.3%`) **Moderate** |

### 5.2 Methodological, Contrast & Excluded Prior Surveys (`34` BibTeX Entries)

| Role / Screening Record | Citekey (`bibliography.bib`) | Year | Verified Venue / Status | Verified Identifier / URL |
|---|---|---:|---|---|
| Methodological SLR Standard | `Kitchenham2007` | 2007 | Keele/Durham EBSE-2007-01 | Technical Report v2.3 |
| PRISMA 2020 Reporting Standard | `Page2021_PRISMA` | 2021 | *BMJ* Vol. 372, p. `n71` | [doi.org/10.1136/bmj.n71](https://doi.org/10.1136/bmj.n71) |
| Terminological Gate (`SR054`, E4) | `LaMalfa2025` | 2025 | NeurIPS 2025 Position Track | [openreview.net/forum?id=FfsxgSZW0c](https://openreview.net/forum?id=FfsxgSZW0c) |
| RQ3 SAS Contrast (`SR024`, E3) | `Zhu2026_AgentDebug` | 2026 | ICML 2026 FAGEN Workshop | [arxiv.org/abs/2509.25370](https://arxiv.org/abs/2509.25370) |
| Weight-Space PSO (`SR057`, E2) | `SR057_feng2025modelswarms` | 2025 | ICML 2025 (PMLR Vol. 267, pp. `16904–16930`) | [proceedings.mlr.press/v267/feng25o.html](https://proceedings.mlr.press/v267/feng25o.html) |
| Classical Swarm NetLogo (`SR058`, E2) | `SR058_jimenezromero2025swarm` | 2025 | *Frontiers in AI* Vol. 8, Art. `1593017` | [doi.org/10.3389/frai.2025.1593017](https://doi.org/10.3389/frai.2025.1593017) |
| Strong SAS Pipeline (`SR065`, E3) | `SR065_xia2025agentless` | 2025 | ACM FSE 2025 / *PACMSE* Vol. 2, `FSE037` | [arxiv.org/abs/2407.01489](https://arxiv.org/abs/2407.01489) |
| `SR041` (E4 MAD Survey) | `SR041_motger2026mad` | 2026 | arXiv *(CSUR under review)* | [arxiv.org/abs/2607.26212](https://arxiv.org/abs/2607.26212) |
| `SR042` (E4 MAD Survey) | `SR042_tillmann2025mad` | 2025 | arXiv Preprint | [arxiv.org/abs/2506.00066](https://arxiv.org/abs/2506.00066) |
| `SR043` (E4 Trajectory Survey) | `SR043_wang2026trajectory` | 2026 | *IEEE TSE* Vol. 52, No. 11, pp. `3406–3426` | [doi.org/10.1109/TSE.2026.3717765](https://doi.org/10.1109/TSE.2026.3717765) |
| `SR044` (E4 Eval Survey) | `SR044_yehudai2026evaluation` | 2026 | Findings of ACL 2026, pp. `26690–26714` **[Upgraded]** | [aclanthology.org/2026.findings-acl.1330/](https://aclanthology.org/2026.findings-acl.1330/) |
| `SR045` (E4 Workflow Survey) | `SR045_yue2026static` | 2026 | Findings of EMNLP 2026 | [arxiv.org/abs/2603.22386](https://arxiv.org/abs/2603.22386) |
| `SR046` (E4 Comm Survey) | `SR046_yan2026beyond` | 2026 | arXiv Preprint *(v. May 2026)* | [arxiv.org/abs/2502.14321](https://arxiv.org/abs/2502.14321) |
| `SR047` (E4 Efficiency Survey) | `SR047_li2026efficiency` | 2026 | Preprints.org *(Table 1 neighbor)* | [doi.org/10.20944/preprints202609.1639.v1](https://doi.org/10.20944/preprints202609.1639.v1) |
| `SR048` (E4 Routing Survey) | `SR048_moslem2026dynamic` | 2026 | *TMLR* (`OpenReview:ypRg1TvQaM`) | [openreview.net/forum?id=ypRg1TvQaM](https://openreview.net/forum?id=ypRg1TvQaM) |
| `SR049` (E4 MAS Review) | `SR049_alaanzy2026autonomous` | 2026 | *Artificial Intelligence Review* | [doi.org/10.1007/s10462-026-11731-2](https://doi.org/10.1007/s10462-026-11731-2) |
| `SR050` (E4 MARL Survey) | `SR050_geng2026scaling` | 2026 | *ACM CSUR* Vol. 58, No. 14, pp. `1–37` | [doi.org/10.1145/3817113](https://doi.org/10.1145/3817113) |
| `SR051` (E4 Security Survey) | `SR051_he2026security` | 2026 | *ACM CSUR* Vol. 58, No. 6 | [doi.org/10.1145/3773080](https://doi.org/10.1145/3773080) |
| `SR052` (E4 Opt. Survey) | `SR052_du2026optimization` | 2026 | *ACM CSUR* (`arXiv:2503.12434`) | [doi.org/10.1145/3789261](https://doi.org/10.1145/3789261) |
| `SR053` (E4 Classic Survey) | `SR053_wang2024autonomous` | 2024 | *Frontiers of Computer Science* | [link.springer.com/article/10.1007/s11704-024-40231-1](https://link.springer.com/article/10.1007/s11704-024-40231-1) |
| `SR055` (E4 Self-Evolving Survey) | `SR055_gao2026selfevolving` | 2026 | *TMLR* Survey Certified *(Jan 2026)* **[Year fixed]** | [openreview.net/forum?id=CTr3bovS5F](https://openreview.net/forum?id=CTr3bovS5F) |
| `SR056` (E4 Game Agents Survey) | `SR056_zhang2026generalist` | 2026 | *TMLR* (`OpenReview:SDkEq8Fzvl`) **[15 authors]** | [openreview.net/forum?id=SDkEq8Fzvl](https://openreview.net/forum?id=SDkEq8Fzvl) |
| Table 1 AIRE Survey | `Chowa2026_AIRE` | 2026 | *Artificial Intelligence Review* | [doi.org/10.1007/s10462-025-11471-9](https://doi.org/10.1007/s10462-025-11471-9) |
| Table 1 AIRE Survey | `AbouAli2026_AIRE` | 2026 | *Artificial Intelligence Review* | [doi.org/10.1007/s10462-025-11422-4](https://doi.org/10.1007/s10462-025-11422-4) |
| CSUR Generalizability Survey | `Zhang2026_CSUR_Generalizability` | 2026 | *ACM CSUR* | [doi.org/10.1145/3794858](https://doi.org/10.1145/3794858) |
| CSUR Game Agents Survey | `Hu2024_CSUR_GameAgents` | 2024 | arXiv *(CSUR portfolio)* | [arxiv.org/abs/2404.02039](https://arxiv.org/abs/2404.02039) |
| JAIR Agentic LLM Survey | `Plaat2025_JAIR` | 2025 | *JAIR* Vol. 84 | [doi.org/10.1613/jair.1.18675](https://doi.org/10.1613/jair.1.18675) |
| IJCAI 2024 MAS Survey | `Guo2024_IJCAI` | 2024 | IJCAI-24 Survey Track | [arxiv.org/abs/2402.01680](https://arxiv.org/abs/2402.01680) |
| Table 1 Collaboration Survey | `Tran2025_MAS` | 2025 | arXiv Preprint | [arxiv.org/abs/2501.06322](https://arxiv.org/abs/2501.06322) |
| KDD 2025 Eval Survey | `Mohammadi2025_KDD` | 2025 | KDD '25 | [arxiv.org/abs/2507.21504](https://arxiv.org/abs/2507.21504) |
| Orchestration Survey | `Zhu2026_FutureInternet` | 2026 | *Future Internet* Vol. 18, No. 6, Art. `326` | [doi.org/10.3390/fi18060326](https://doi.org/10.3390/fi18060326) |
| Safe LLM Agents (PRISMA) | `Dantas2026_SafeAgents` | 2026 | arXiv Preprint | [arxiv.org/abs/2608.14590](https://arxiv.org/abs/2608.14590) |
| USENIX Security Survey | `Kim2026_USENIX_Security` | 2026 | USENIX Security 2026 | [arxiv.org/abs/2603.11088](https://arxiv.org/abs/2603.11088) |
| Coordination Reliability Review | `Mallampati2026_Reliability` | 2026 | ResearchGate Preprint (`416608744`) | [researchgate.net/publication/416608744](https://www.researchgate.net/publication/416608744) |

### 5.3 RQ4 OpenReview Rejection & Withdrawal Audit Cases (`8` BibTeX Entries)

| Record / Case ID | Citekey (`bibliography.bib`) | Year | Verified Disposition | Key Verification & Audit Note |
|---|---|---:|---|---|
| `SR077` (E8) | `SR077_tmlr7332_agenticnet` | 2025 | **Publicly rejected** (TMLR Paper 7332) | AE Tim Rudner; rebuttal exact-match dropped MBPP `100% -> 77.5%`, MATH L5 trailed Vanilla CoT. |
| `SR078` (E8) | `SR078_tmlr7253_disagreement` | 2025 | **Publicly rejected** (TMLR Paper 7253) | AE Huazheng Wang; `99.2%` proxy disagreement measured without correctness gain over parallel SAS. |
| `TMLR-9844/11271` | `TMLR2025_WhenConsensus_9844` | 2025 | **Publicly rejected** (TMLR Papers 9844 & 11271) | AE Peng Li; later revised & accepted at KDD 2026 Agentic AI Workshop (**included as `SR079`**). |
| `SR080` (E8/E4) | `SR080_li2026harness` | 2026 | **Withdrawn** (TMLR, June 30, 2026) | `OpenReview:3hXEPbG0dh` (**19 authors expanded**); strictly *Withdrawn*, NOT rejected. |
| `SR081` (E8) | `SR081_ruan2025swarmbench` | 2025 | **Withdrawn** (ICLR 2026 Sub) | `arXiv:2505.04364`; *SwarmBench* withdrawn at ICLR 2026 on OpenReview. |
| `ICLR2025-6097` | `ICLR2025_SCALE_6097` | 2025 | **Withdrawn** (ICLR 2025 Sub #6097, Jan 19, 2025) | Criticized for missing baselines/cost; revised & accepted at ACL 2025 (**included as `SR082`**). |
| `SR083` (E8) | `SR083_yao2025peacemaker` | 2025 | **Withdrawn** (ICLR 2026 Sub #8079) | `arXiv:2509.23055`; tracked as status-boundary methodological note on debater/judge sycophancy. |
| `SR084` (E8/E4) | `SR084_zhang2025selfplay` | 2025 | **Publicly rejected** (TMLR Paper 4567, May 2025) | `arXiv:2408.01072`; AE Marc Lanctot; excluded as both non-empirical RL survey and TMLR rejection. |

---

## 6. Explicitly Unverified Publisher Metadata & Access Boundaries

In compliance with the **Zero-Fabrication & Access-Honesty Protocol** (`Protocol Section 3.2B` and `Section 7.2`), fields that could not be verified from open primary publisher HTML, arXiv, OpenReview, ACL Anthology, or PMLR snippets were **omitted from `bibliography.bib` rather than guessed**:

1. **Paywalled / Unexposed Publisher Page Ranges, Volumes, & Article Numbers:**
   - **`SR036` (*PatchDiff*, ICSE 2026):** `doi:10.1145/3744916.3764576` verified; ACM DL full proceedings page numbers were not exposed in open snippets and were omitted.
   - **`SR012` (*ColMAD*, ICML 2026):** Confirmed PMLR Vol. 306 ICML 2026 acceptance (`arXiv:2510.20963` + `github.com/LFhase/ColMAD`); exact PMLR Vol. 306 paper slug and page range were not exposed in open indexing snippets and were omitted.
   - **`SR049` (*Artificial Intelligence Review*):** `doi:10.1007/s10462-026-11731-2` verified; Springer Nature paywall blocked open access to volume/article numbers.
   - **`SR051` (*ACM CSUR*):** `doi:10.1145/3773080` and Vol. 58 No. 6 verified; article/page range omitted.
   - **`SR052` (*ACM CSUR*):** `doi:10.1145/3789261` verified; upstream Vol. 58 No. 9 Art. 223 could not be independently exposed from open Springer/ACM snippets and was documented only in `note` rather than formal `volume`/`pages` BibTeX fields.
   - **`SR053` (*Frontiers of Computer Science*):** `doi:10.1007/s11704-024-40231-1` verified; Springer volume/pages omitted.
   - **`Chowa2026_AIRE` & `AbouAli2026_AIRE` (*Artificial Intelligence Review*):** DOIs `10.1007/s10462-025-11471-9` and `10.1007/s10462-025-11422-4` verified; Springer article/volume numbers omitted, and `Chowa2026_AIRE` uses `and others` beyond the 4th author because the publisher preview truncated co-authors behind the paywall.
   - **`Zhang2026_CSUR_Generalizability` (`doi:10.1145/3794858`) & `Hu2024_CSUR_GameAgents`:** ACM CSUR volume/article numbers (and `Hu2024` publisher DOI) not exposed in open snippets.
2. **Unverifiable Conference Forum Hashes / ACL Slugs:**
   - **`SR011` (*MoA*, ICLR 2025), `SR023` (*AgenTracer*, ICLR 2026), `SR025` (*AgentLocate*, COLM 2026), `SR079` (*When Consensus Is Not Correctness*, KDD 2026 Workshop):** Exact OpenReview submission forum hashes failed reverse verification (`SR011` upstream `PhMrGCMIRL` and `SR023` candidate `Sx038qxjek` belonged to unrelated ICLR 2024 papers; `SR023` `l05DseqvuD`, `SR025` `5RmOQVmCRO`, and `SR079` `lWCLnGrHhH` had zero open hits) and were omitted in favor of verified arXiv/group URLs.
   - **`SR027` (*TRIAGE*, AACL-IJCNLP 2026):** Exact ACL Anthology slug (`2026.aacl-short.347` unverified) and pages marked `"not verifiable"` until ACL Anthology direct index resolution; verified code/dataset repository linked cleanly.
   - **`SR045` (*Findings of EMNLP 2026*):** Accepted venue verified; exact ACL Anthology paper URL and page range not yet indexed in accessible snippets.
   - **ACL Anthology `10.18653` DOIs:** Only `SR019` (`10.18653/v1/2025.acl-long.757`) had its DOI directly confirmed in search snippets; canonical `aclanthology.org` URLs and verified page ranges were recorded for the remaining ACL/Findings/SIGDIAL entries (`SR006`, `SR020`, `SR026`, `SR029`, `SR030`, `SR031`, `SR044`, `SR069`, `SR082`) without extrapolating unprinted DOI strings.
3. **`QA4` Multi-Run Dispersion Granularity (`Open Summaries vs Full Appendices`):**
   - For archival papers and preprints whose full statistical appendix tables were only partially exposed via search snippets (`29/44` scored `QA4 = 1`), `QA4` conservatively credits `1` whenever systematic multi-benchmark/multi-model sweeps or `p`-values were documented without verified per-cell `k >= 3` seed standard deviations or confidence intervals—avoiding optimistic inflation of stochastic rigor claims.
