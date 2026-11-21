<!-- Source Subagent ConversationId: f71e3c87-a3ef-45d5-b016-0f889dc7a349 | Delivered: 2026-11-20T09:03:16Z | Verbatim Unedited Referee Report -->

# Independent Editorial & Compliance Referee Report (Reviewer D)

**Role:** Reviewer D — Editorial Quality, Readability & ACM CSUR Compliance Critic (Phase 8 Pass 6 & Phase 9 Audit)  
**Primary Artifacts Audited:** `reviews/manuscript_v2_edited.md`, `data/bibliography.bib`, `deliverables/Deliverable_A_Journal_Intelligence_Report.md`, `agents/agent4_openreview_analysis.md` (cross-checked against `agents/agent11_editing_log.md`, `agents/agent2_journal_intelligence.md`, `agents/agent9_citation_audit.md`, `agents/agent6_screening_audit.md`, and `data/quality_appraisal.csv`).

---

## 1. Overall Editorial Assessment & CSUR/TMLR Fit Recommendation

**Editorial Recommendation:** **Major Revision Required Before Submission (Do Not Submit As-Is to ACM CSUR or TMLR).**

The underlying scholarly synthesis is exceptionally well suited in *scope and analytical substance* to **ACM Computing Surveys (CSUR)** (Primary Target) and **Transactions on Machine Learning Research (TMLR)** (Backup Target 1). It fills a clear white space in the 2025–2026 CSUR LLM-agent portfolio, avoids chronological paper-listing via an original four-axis taxonomy and conditional decision framework, enforces anti-pooling paired synthesis, and directly addresses TMLR Criterion 1 (claims–evidence parity) and Criterion 2 (clear communication) pitfalls documented in `agent4_openreview_analysis.md`.

However, the manuscript currently fails **hard formatting, notational, citation-hygiene, and pedagogical-accessibility gates** that create immediate desk-rejection or mandatory major-revision risk at both venues:
- **ACM CSUR Fit:** Structurally non-compliant as drafted. The manuscript begins with a broken heading hierarchy (`## 2. Abstract` with **no Section 1**, shifting Introduction to `## 4.`), relies on ASCII box art for PRISMA (Figure 1), packs 16–23 dense rows across 8-column Markdown tables (`Table 4`, `Table 5`), omits ACM DOIs/article numbers on published ACM papers (`[36]`, `[61]`, `[16]`, `[23]`, `[76]`), misclassifies a CSUR-accepted portfolio paper (`[24]`) as an `arXiv` preprint, drops a peer-reviewed USENIX Security '26 SoK (`Kim2026_USENIX_Security`) to satisfy a brittle cliché grep (creating an `85` vs. `86` BibTeX mismatch), leaks internal record/schema IDs (`SR002`, `F17`, `F18`), and wraps 32 citation brackets in inline code backticks.
- **TMLR Fit:** Directly triggers **two verified OpenReview failure patterns** from `agent4_openreview_analysis.md`: (1) **Case T2 (*Generalist Game Agents*)**—overloaded, colliding `"Tier"` and single-letter labels (`Tier 1–4` vs. `Tier I–V` vs. `Tier A–C` plus `T1–T6`, `B1–B4`, `Q1–Q6` vs. `Q0–Q4` vs. `Q`, `S1–S4` vs. `S01–S11`); and (2) **Case T8 (*Evaluating World Models*)**—late or missing definitions for core codes (`C1`–`C6` used ~30 times before definition on Line 355, undefined `DPI` variables, `OAS`, `CosMAD`, `FM-2.3`). Additionally, the manuscript lacks TMLR's mandatory first-page LLM-disclosure footnote, uses non-anonymized internal pipeline role titles (`Discovery Specialist`, `Review Methodologist`, `Research Director`) that blur human vs. AI screening accountability, and requires `tmlr.sty` (`natbib`) restructuring.

---

## 2. Major Concerns

### Major Concern 1 — Overloaded `"Tier"` Terminology & Colliding Alphanumeric Code Systems
- **Severity:** **Blocking**
- **Manuscript Location:** Throughout Sections 4, 6.4, 8.1–8.4, 9.1–9.2, 10, Tables 3–10, and Figure 2 (`L44–47`, `L127–134`, `L185–203`, `L334–338`, `L392–394`, `L405–446`, `L466–468`).
- **Criticism:** The manuscript violates *Generalist Game Agents* (`agent4_openreview_analysis.md`, Case T2: overlapping `L1–L5` axes forced revision) at far higher severity by deploying **three distinct `"Tier"` scales** alongside **fourteen other alphanumeric code series (`17` total code systems)**, several of which collide directly in the same sentences, tables, and diagrams.
- **Supporting Evidence:**
  1. **Three-way `"Tier"` collision:**
     - `Tier 1`–`Tier 4` (95 occurrences) = *SAS Baseline Rigor* (`Tier 1` Gold to `Tier 4` Absent).
     - `Tier A`–`Tier C` (15 occurrences) = *Publication Status* (`Tier A` Archival, `Tier B` Workshop, `Tier C` Preprint).
     - `Tier I`–`Tier V` (7 occurrences) = *Epistemic Confidence Separation* (`Tier I` Strongly Supported to `Tier V` Unanswered Questions).
     - `Tier 1` (Arabic) and `Tier I` (Roman) appear **inside the same table cells and consecutive sentences**: Table 9 (`L413`: `Tier I — Strongly Supported ... Replicated across multiple Tier 1 controls`; `L416`: `Tier IV ... Supported by Tier 2 evidence ... require Tier 1 amortized confirmation`), and Section 10 (`L466` `Tier I empirical consensus and the unresolved Tier IV–V questions` followed two lines later at `L468` by `Tier 1 strong SAS baselines`). Meanwhile, `Tier A` sits adjacent to `Tier 1`–`Tier 3` in Section 8.1.1 (`L189`) and Table 8 Panel B (`L392` vs. `L394`).
  2. **Failed deduplication in Section 9.2 (`L423–425`):** Section 9.2 explicitly announces *"To eliminate overloaded tier labels, our synthesis-derived taxonomy classifies multi-agent evaluations along four orthogonal axes (`T × B × S × V`)"*, yet:
     - Introduces **`T1`–`T6`** (Topologies), which visually resembles abbreviated `Tier 1–4` (`Deliverable_E` `L88` literally abbreviated `Tiers (T1/T2/T3/T4/N/A)` using `T1–T4`!).
     - Introduces **`B1`–`B4`** solely as a redundant alias for `Tier 1`–`Tier 4` (`B1 Tier 1 ... B2 Tier 2 ...`), forcing readers to remember *both* `Tier 1` and `B1` while never replacing `Tier 1–4`, `Tier A–C`, or `Tier I–V`.
  3. **Three additional single-letter collisions:**
     - **`Q` overload:** `Q1`–`Q6` = Boolean search queries (Sec. 6.2, 26 hits) vs. `Q0`–`Q4` = Figure 2 Mermaid decision nodes (`L433–440`, 21 hits) vs. `Q` / `Q_break-even` = deployment query volume inside node `Q4` of the exact same diagram (`L439`: `Q4{"Amortizable Over Q > Q_break-even?"}`) vs. `QA1`–`QA7`.
     - **`S` overload:** `S01`–`S11` = executed searches (Sec. 6.2–6.3) vs. `S1`–`S4` = Task Structure axis (Sec. 9.2 `L426`).
- **Proposed Correction:**
  1. Reserve `"Tier"` **exclusively** for one scale—or better, replace `"Tier"` on at least two scales with semantic labels:
     - Keep **`R1`–`R4`** or **`Tier 1`–`Tier 4`** (or better: **`Control Parity` (`Gold-Parity`, `Unmatched-Strong`, `Weak-SinglePass`, `No-SAS`)** or **`B1`–`B4`** everywhere if adopting `T × B × S × V`, eliminating `Tier 1–4` altogether).
     - Rename `Tier A`–`Tier C` to plain publication labels (**`Archival`**, **`Workshop`**, **`Preprint`**—never `"Tier A–C"`).
     - Rename `Tier I`–`Tier V` to **`Epistemic Grade E1–E5`** or semantic confidence bands (**`High-Confidence Consensus`**, **`Context-Bounded`**, **`Moderated Conflict`**, **`Open Hypothesis`**, **`Evidence Gap`**—avoiding `E1–E8` exclusion collision!).
  2. Rename `Q0`–`Q4` Mermaid node IDs to `D0`–`D4` (`Decision 0–4`), spell out search executions (`Search 1–11`) and queries (`Query 1–6`) in prose, and use consistent taxonomy axis names (`Topo-1..6` or plain names) instead of `T1–T6`.

---

### Major Concern 2 — ACM CSUR Structural & Format Non-Compliance, Abstract Boundary Risk, and Blurred Screening Accountability
- **Severity:** **Blocking**
- **Manuscript Location:** Title/Front-Matter (`L1–23`), Abstract (`L5–7`), Section 6.3 (`L78–121`), Section 6.5 (`L140`), Section 14 (`L667–673`).
- **Criticism:** Several structural and policy issues violate ACM CSUR (`acmart`) conventions, put the Abstract right on the edge of the 100-word desk-reject gate, and blur human vs. AI screening accountability in a way that threatens both CSUR and TMLR acceptance.
- **Supporting Evidence:**
  1. **Missing Section 1 & shifted section numbering:** The manuscript jumps from `# Title` (`L1`) to `## 2. Abstract` (`L5`), `## 3. ACM CCS Concepts and Keywords` (`L11`), and `## 4. Introduction` (`L23`). **There is no `## 1.` heading anywhere in the file.** In ACM `acmart` (`\documentclass[manuscript]{acmart}`), Title, Author block, Abstract, CCS Concepts, and Keywords are unnumbered front-matter, and **Introduction is Section 1** (`\section{Introduction}`), not Section 4. Shifting every section number (`4–14` instead of `1–11`) looks like an unedited internal template artifact. Author block / anonymized double-blind placeholder (for TMLR) and CCS XML importance weights (`500`/`300`/`100` from `dl.acm.org/ccs/ccs.cfm`) are also missing.
  2. **Abstract (`L7`) 100-word boundary risk & jargon:** Whitespace word count is `92` words (`<= 100`), **but** it contains `10` hyphenated, en-dashed, or slashed compounds (`multi-agent`, `(LLM-MAS)`, `equal-compute`, `single-agent`, `2023–November`, `compute-matched`, `9/10`, `0/24`, `synthesis-derived`, `four-axis`), expanding to **97–102 tokens** under tokenizers that split on hyphens/slashes/en-dashes (`92 + 10 = 102`), risking automated ScholarOne/editorial kickback. Furthermore, the Abstract embeds raw Markdown code backticks (`` `pass^k` ``), uses `pass^k` without glossing it, omits the unit `"pp"` on `-50.1` (`(-57.0 percentage points; -50.1 in archival studies)`), and ends with `"proposing a synthesis-derived four-axis taxonomy"` without indicating what the axes or workflow cover.
  3. **Blurred human vs. AI screening accountability (`L78` vs. `L140`):** Section 6.3 (`L78`) writes: *"Two independent reviewers (Discovery Specialist and Review Methodologist) blinded to each other's decisions screened 100% of deduplicated records... with disagreements arbitrated by the Research Director."* Then Section 6.5 (`L140`) states: *"AI agents assisted under continuous human/Research Director supervision in... running blinded Stage 1 and Stage 2 screening votes (with every boundary dispute adjudicated by the Research Director)..."* Leaving pipeline agent-role titles (`Discovery Specialist`, `Review Methodologist`, `Research Director`) in manuscript prose makes it read as though AI subagents performed the dual-independent screening and arbitration themselves—violating both CSUR/Springer editorial expectations for human scholarly judgment and TMLR accountability norms (`agent2_journal_intelligence.md` L66, L88).
  4. **Missing TMLR portability markers:** If TMLR is Backup Target 1 (`Deliverable_A`), `manuscript_v2_edited.md` lacks the mandatory **first-page LLM-disclosure footnote** and contains un-anonymizable internal directory references (`L671`: `data/evidence_matrix.json`, `deliverables/Deliverable_C_Systematic_Review_Protocol.md`).
- **Proposed Correction:**
  1. Remove numeric prefixes from Title/Abstract/CCS/Keywords; renumber **Introduction as Section 1** (`1. Introduction` through `11. Declarations`), and insert an author/affiliation placeholder (plus CCS XML significance placeholders).
  2. Tighten Abstract to **82–86 whitespace words** (comfortably `<= 95` even with hyphen splitting), remove backticks, replace `pass^k` with plain English (`multi-trial consistency`), add `"pp"` after `-50.1`, and summarize the four-axis taxonomy and decision workflow cleanly. Example (85 words):
     > *Large language model multi-agent systems (LLM-MAS) are widely promoted for reasoning, coding, and tool use, yet prior surveys rarely test whether gains survive equal-compute single-agent controls. This PRISMA review synthesizes 44 studies (2023–2026; 49 paired comparisons). MAS win 75.8% of unmatched or weak comparisons, falling to 18.8% wins and 50.0% losses under compute-matched parity (-57.0 percentage points; -50.1 pp in archival studies). Negative returns stem from error amplification, conformity, handoff loss, unamortized search costs (9/10 optimizers), absent multi-trial consistency reporting (0/24 studies), and harness distortion, motivating a four-axis taxonomy and decision workflow.*
  3. Replace internal pipeline persona names (`Discovery Specialist`, `Review Methodologist`, `Research Director`) in Section 6.3/6.5 with human author attribution (e.g., *"Two authors independently screened... with disagreements adjudicated by a third author"*) and accurately state the exact division of human validation vs. AI-assisted workflow tooling—adding a first-page footnote placeholder if porting to TMLR.

---

### Major Concern 3 — Reference & Citation Hygiene Failures: Censored `Kim2026_USENIX_Security`, BibTeX Count Mismatch, Misclassified `[24]`, and Missing ACM/Proceedings Metadata
- **Severity:** **Significant** (approaching Blocking for ACM CSUR reference audit)
- **Manuscript Location:** Section 4 (`L29`), Table 1 (`L41`), Section 9.3 (`L458`), Section 13 (`[1]`–`[85]`, `L493–663`), Section 14 (`L671`), `data/bibliography.bib`.
- **Criticism:** Spot-checking Section 13 against `data/bibliography.bib`, `agent2_journal_intelligence.md`, and primary sources reveals that Pass 3's removal of `Kim2026_USENIX_Security` (`agent11_editing_log.md` L18, L62–64) degraded scholarly coverage and broke BibTeX parity, while multiple Section 13 entries mislabel venue status, truncate authors, or omit verified ACM DOIs/article numbers.
- **Supporting Evidence:**
  1. **Arbitrary removal of `Kim2026_USENIX_Security` & `86` vs. `85` mismatch:**
     - `agent11_editing_log.md` (`L18, L62–64`) confirms `Kim2026_USENIX_Security` (*SoK: Attack and Defense Landscape of Agentic AI Systems*, USENIX Security '26, `arXiv:2603.11088`) was removed **solely** because its preprint title contained the string `"Landscape of"`, failing a full-file banned-cliché regex.
     - **Immediate contradiction:** Section 14 (`L671`) still claims `complete BibTeX database (data/bibliography.bib, 86 entries)`, whereas Section 13 has **`85` entries (`[1]`–`[85]`)**—leaving `Kim2026_USENIX_Security` orphaned in `bibliography.bib`.
     - **Scholarly gap in Sections 4 and 9.3:** In `v1`, Section 4 (`L29`) cited `safety [13, 28]` and Section 9.3 (`L445`) cited `memory poisoning, tool misuse, and inter-agent privilege escalation ([13, 23, 28])`. Removing `[28]` left Section 4 citing **only** an unrefereed arXiv preprint (`Dantas et al. [13]`) for external safety/security surveys and stripped the flagship **peer-reviewed USENIX Security '26 SoK** directly out of Section 9.3's threat-surface claim! Censoring a peer-reviewed reference because of a word in its *own verbatim title* is editorial malpractice.
  2. **Internal contradiction & author truncation on `[24]` (*Hu et al.*):** Section 4 (`L29`) and Table 1 (`L41`) present `[24]` as a published/accepted article in the **`ACM Computing Surveys (CSUR)` Portfolio** (`2024 – July 2026 / ACM Computing Surveys (Journal)`). Yet Section 13 (`L541`) and `bibliography.bib` (`@misc`) classify `[24]` as `2024 ... arXiv:2404.02039 (cs.AI); Preprint` **and** omit two co-authors (`Yichang Xu` and `Zachary Yahn`) from the 9-author CSUR-accepted paper (`Sihao Hu, Tiansheng Huang, Gaowen Liu, Ramana Rao Kompella, Fatih Ilhan, Selim Furkan Tekin, Yichang Xu, Zachary Yahn, and Ling Liu`).
  3. **Author truncation (`et al.`) in `[10]`:** `[10]` (*Chowa et al.*, *AIRE* 2026) truncates an 8-author journal article with `, et al.` (`Sadia Sultana Chowa, Riasad Alvi, Subhey Sadi Rahman, Md. Abdur Rahman, et al.`), violating ACM Reference Format (while `[20]` lists 27 authors and `[84]` lists 26!) and omitting `Vol. 59, Art. 71`.
  4. **Omitted verified ACM/Springer metadata (`[1, 10, 16, 23, 36, 61, 76]`):**
     - `[36]` (*Mohammadi et al.*, `KDD '25`) cites only `https://arxiv.org/abs/2507.21504`, omitting its verified ACM DOI (`10.1145/3711896.3736570`).
     - `[61]` (*Xia et al.*, `Agentless`, *PACMSE* Vol. 2 FSE) cites `https://arxiv.org/abs/2407.01489`, omitting its verified ACM DOI (`10.1145/3715754`) and pages (`801–824`)—a glaring omission in an ACM CSUR submission.
     - `[1]` (`Vol. 59, Art. 11`), `[16]` (`Vol. 58, No. 9, Art. 223`), `[23]` (`Art. 162`), and `[76]` (`Vol. 58, No. 10, Art. 263`) omit volume/issue/article metadata that **already appears in `agents/agent2_journal_intelligence.md` (`L58–82`)**!
  5. **Conference entries linked solely to `arXiv`, GitHub, or generic OpenReview group URLs:** Nine `@inproceedings` entries (`[5, 8, 22, 47, 55, 62, 68, 70, 82]`) carry only `arxiv.org` URLs without proceedings pages/DOIs/OpenReview forum links; `[58]` (*TRIAGE*, AACL-IJCNLP 2026) links to a **GitHub repo** (`https://github.com/jimmywang585/triage-failure-attribution`) rather than a paper URL; and `[3, 4, 11, 12, 80]` link to generic OpenReview group portals (`https://openreview.net/group?id=TMLR`, etc.) instead of specific paper/submission identifiers. Moreover, `[69]` uses `DOI: https://doi.org/10.18653/v1/2025.acl-long.757` while other ACL Anthology entries (`[6, 7, 9, 41, 79, 81]`) omit DOIs, and publisher locations/pages (`[59]` ICSE '26) are uneven.
- **Proposed Correction:**
  1. **Restore `Kim2026_USENIX_Security`** (citing its USENIX Security '26 title *SoK: Attack and Defense Landscape of Agentic AI Systems*, `arXiv:2603.11088`) into Section 4 (`L29`), Section 9.3 (`L458`), and Section 13 (`86/86` exact match with `bibliography.bib`); exempt verbatim third-party bibliographic titles from prose cliché filters.
  2. Update `[24]` (`Hu2024_CSUR_GameAgents`) in Section 13 and `bibliography.bib` with all 9 authors and explicit `"Accepted, ACM Computing Surveys; preprint arXiv:2404.02039"` status (or move `[24]` out of Table 1's published CSUR list if awaiting DOI assignment, clarifying status transparently).
  3. Expand `[10]` (`Chowa et al.`) to all 8 authors (`... Mohaimenul Azam Khan Raiaan, Md Rafiqul Islam, Mukhtar Hussain, and Sami Azam`) with `Vol. 59, Art. 71`, and populate verified DOIs/article numbers/pages for `[1, 16, 23, 36, 61, 76]`.
  4. Standardize Section 13 to `ACM-Reference-Format.bst` (consistent `https://doi.org/...` links, publisher/city on `@inproceedings`, explicit `arXiv` preprint note where proceedings pagination is pending, and explicit `Code repository:` label on `[58]` instead of treating a GitHub URL as the publication locator).

---

### Major Concern 4 — Raw Internal Record/Schema ID Leaks (`SR002`, `F17`, `F18`) & Code-Backtick Formatting Artifacts
- **Severity:** **Significant**
- **Manuscript Location:** Section 8.1.3 (`L235`), Section 8.3 (`L287`), Section 8.4.1 (`L326`), Section 10 (`L472`), and 32 citation blocks across Sections 6.4–11 (`L127`, `L207`, `L239`, `L243`, `L245`, `L277`, `L279`, `L314`, `L318`, `L354`, `L399`, `L424–427`, `L445`, `L458`, `L460`, `L480`).
- **Criticism:** Internal database record keys, extraction-schema field IDs, and Markdown code formatting leaked directly from intermediate synthesis scripts (`Deliverable_E`, `extraction_schema.json`) into the final edited manuscript, creating glaring production-quality blemishes.
- **Supporting Evidence:**
  1. **Raw ID leaks in prose:**
     - `L235`: `when single-agent inputs suffer extreme noise or context rot (\`SR002\` [51])` — raw screening ledger ID `SR002` leaked alongside `[51]` (from `Deliverable_E` `L76`).
     - `L287`: `Across all 44 studies (\`F17\`), documented failure causes cluster...` — internal `extraction_schema.json` field code `F17` leaked verbatim (`Deliverable_E` `L106`).
     - `L326`: `Table 7 details track and criterion distributions alongside multi-label confounder incidence (\`F18\`).` — internal schema field code `F18` leaked verbatim (`Deliverable_E` `L125`).
     - `L472`: `` `MAST` `FM-2.3` [5] `` — unexpanded raw MAST subcode dropped into Section 10 without ever explaining earlier that `FM-2.3` denotes *"failure to ask for clarification"*.
  2. **Backticked citations & ordinary prose values:** `32` citation lists are enclosed in inline Markdown code ticks (e.g., `` `[3, 4, 31, 46, 65, 77]` `` at `L127`, `` `[8, 14, 28, 33, 39, 48, 51, 63, 73]` `` at `L207`, `` `[69, 71, 72, 74, 85]` `` at `L243, L277, L424, L460`). Hundreds of ordinary counts and percentages (`\`260\``, `\`6\``, `\`75.8%\``, `\`Tier 1\``, `\`SAS\``, `\`CoT\``) are also styled as monospace code tokens, degrading typographic naturalness.
- **Proposed Correction:**
  1. Replace `` (`SR002` [51]) `` with `(Tran and Kiela [51])`; delete `` (`F17`) `` and `` (`F18`) ``; replace `` `MAST` `FM-2.3` [5] `` with `legitimate inter-agent clarification (MAST's failure-to-ask-clarification category [5])`.
  2. Strip all backticks from citation lists (`[3, 4, 31, 46, 65, 77]`), ordinary numbers/percentages (`260`, `75.8%`), and standard prose acronyms (`SAS`, `MAS`, `CoT`, `RL`), reserving monospace strictly for literal API parameters (`thoughts_token_count`), codebase/package identifiers, and schema/JSON field keys where genuinely technical.

---

### Major Concern 5 — Pedagogical & Beginner Accessibility Gaps (`C1`–`C6` Late Definition, Undefined `DPI` Symbols, `QA3 = 1` vs. `9/10` Knot, and Unexpanded Jargon)
- **Severity:** **Significant**
- **Manuscript Location:** Abstract (`L7`), Table 1 (`L35–40`), Section 5 (`L60`), Section 6.5 (`L138`), Section 7.1 (`L154–156`), Sections 8.1–8.4 (`L197–399`), Section 9.2 (`L433`), Section 10 (`L472`).
- **Criticism:** A technically literate M.Tech student reading sequentially from Section 7 onward (and earlier) encounters critical analytical codes, information-theoretic notation, and metric abbreviations **hundreds of lines before they are defined**—or with missing variable definitions, missing scoring anchors, and an apparent arithmetic discrepancy on `QA3 = 1` vs. `9/10`.
- **Supporting Evidence:**
  1. **`C1`–`C6` used ~30 times before ever being defined:** `C1`–`C6` appear in Table 1 (`L35`), Section 5 (`L60`), Table 3 (`L197`), Section 8.1.3 (`L236–237`), throughout Section 8.2 / Table 5 (`L243–281`), and Table 6 (`L294`), yet **are never defined anywhere until Table 7 Panel B on Line 355 (Section 8.4.1)**!
  2. **Incomplete mathematical/metric explanations in Section 7.1:**
     - **`DPI` (`L156`):** Writes $I(X; \hat{Z}_{\text{MAS}}) \le I(X; Z_{\text{SAS}})$ without defining $X$ (target query/answer), $Z_{\text{SAS}}$ (single-agent latent reasoning state), or $\hat{Z}_{\text{MAS}}$ (natural-language summary handed across agents), nor stating the underlying Markov chain $X \to Z_{\text{SAS}} \to \hat{Z}_{\text{MAS}}$.
     - **`pass^k` (`L154`):** Appears unexpanded in Abstract (`L7`) and Intro (`L27, L39, L46`) prior to Section 7.1; in `L154`, lacks a brief concrete numerical contrast (e.g., for per-trial success $\hat{p} = 0.6$ over $k=8$ trials, $\text{pass}@8 = 99.9\%$ whereas $\text{pass}^8 = 1.7\%$).
     - **`VTFR` (`L383`, `L454`):** States `"provenance recovers 85.5%"` / `"85.5% VTFR recovery"` without clarifying `85.5% of transport failures` (ambiguous to a newcomer whether `85.5%` is post-recovery accuracy or error-reduction rate).
     - **`QA1`–`QA7` (`L138`):** Lists criterion names without summarizing what distinguishes score `0`, `1`, and `2`, leaving `QA3 = 1` vs. `QA3 = 2` in Table 5 unanchored until Section 8.4.1.
  3. **Confusing `QA3 = 1` vs. `9/10` (`C6`) cross-mapping (`L270, L277, L350`):** Table 7 Panel B (`L350`) reports `QA3` score counts (`0`: 0, `1`: 10, `2`: 34) right next to `9/10 (90.0%) optimization-bearing studies omit upfront search/training cost (C6)`. A careful reader assumes `9/10` is 9 of the 10 `QA3 = 1` papers—yet `L277` reveals that `Chang et al. [6]` (`QA3 = 1` in Table 5 `L270` and `quality_appraisal.csv`) is *excluded* while `Kapoor et al. [26]` (`QA3 = 2`!) is *included* as the 10th optimization-bearing study.
  4. **Unexpanded acronyms & table shorthand:** `OAS` (`L271`, `L308`) and `CosMAD` (`L228`, `L296`) are **never expanded anywhere in the paper**; `PRISMA`, `HE` (`HumanEval`), `CLEAR`, `ABC`, `APB`, `ATBench`, `PRB`, `SLA`, `FIPA`, `PPO`, `QMIX`, `ToT`, `LATS`, `MCP`, `A2A`, `Het NV`, `Homog.`, and `Indep./Cent./Dec.` are never spelled out; `$R_{\text{Con}}^{\text{Traj-S}}$` (`L377`) is undefined; `P-ASR` and `PTN` appear in Table 6 (`L307`) before being expanded in `L315`; and `NV`/`NR` is defined below Table 4 (`L230`, where `NR` does not even appear) while omitted beneath Table 5 (`L252–272`, where `NR` first appears).
- **Proposed Correction:**
  1. Move a concise **Confounder Taxonomy (`C1`–`C6`) and Quality Scoring Anchor (`QA1`–`QA7`, 0/1/2 rules)** table/box into **Section 6.5 (Methods)** or **Section 7.1**, prior to all Section 8 usage.
  2. Define $X, Z_{\text{SAS}}, \hat{Z}_{\text{MAS}}$ and the Markov chain in Section 7.1 (`L156`); add a 1-sentence concrete numeric illustration of `pass@k` vs. `pass^k` (`L154`); clarify `"85.5% of transport failures"` on `VTFR` (`L383`, `L454`); and explicitly reconcile `QA3 = 1` (`10` studies incl. `[6]`) vs. offline `optimization-bearing` (`10` studies incl. `[26]`, excl. `[6]`) in both `L277` and Table 7 Panel B (`L350`).
  3. Expand every acronym on first use (`PRISMA`, `OAS`, `CosMAD`, `CLEAR`, `ABC`, `HumanEval`, `FIPA`, `PPO`, `QMIX`, `MCP`, `A2A`, `SLA`, `$R_{\text{Con}}^{\text{Traj-S}}$`), expand `P-ASR`/`PTN` in Table 6 or footnote, and standardize `NV`/`NR` notes under Tables 4 and 5.

---

### Major Concern 6 — Cross-Section Redundancy (Sections 4, 8, 9, 12), Wall-of-Text Density, and Overstuffed Wide Tables (`Table 4` & `Table 5`)
- **Severity:** **Significant**
- **Manuscript Location:** Section 4 (`L29, L44–47`), Section 8 (`8,005` words; Tables 4 & 5 `L209–275`), Section 9.1 (`Table 9`, `L411–417`), Section 9.3 (`L456–460`), Section 12 (`L489`).
- **Criticism:** At `18,287` words (`14,487` in body sections), the manuscript repeats the exact same descriptive statistics 5–10 times across Sections 2, 4, 8, 9, and 12, packs key paragraphs past 150–180 words, and places two massive 8-column matrices directly into the main body (`Table 4`: 16 rows; `Table 5`: 23 rows).
- **Supporting Evidence:**
  1. **Stat-by-stat repetition:** `9/10` (`C6`) appears on **9 lines** (`L7, L38, L46, L277, L281, L350, L413, L460, L489`); `75.8%`/`18.8%`/`-57.0 pp` on **6–7 lines** (`L7, L45, L187, L196–199, L413, L489`); `17.2x`/`4.4x` on **8–10 lines**; `0/24` (`pass^k`) on **7 lines**.
  2. **Structural overlap between Sections 8 and 9:** Section 9.1 (**Table 9**, `L411–417`) largely re-narrates every quantitative count already synthesized in Sections 8.1–8.4 instead of offering concise, high-level epistemic claims pointing back to Section 8 subsections. Similarly, **Section 9.3** (`L458–460`) re-summarizes `CORBA` (`~92%–100%`, `1.60–1.90` turns), `VTFR` (`30.9%`), `MAST`, `PatchDiff`, `TraceElephant`, `9/10 C6`, and `OneFlow` almost immediately after Section 8.2/8.3/8.4.2 and Table 10.
  3. **Wall-of-text density:** `L29` (181 words), `L125` (178 words), `L237` (173 words), `L489` (171 words), `L70` (150 words), `L236` (150 words), `L140` (142 words), and `L277` (138 words) are heavy single-paragraph blocks dense with parentheticals and citations.
  4. **Unprintable wide tables:** `Table 4` (8 cols × 16 rows) and `Table 5` (8 cols × 23 rows) contain long prose cells that will overflow ACM `acmsmall` or `tmlr.sty` column margins. Notably, `Deliverable_E` (`L88`) synthesized `RQ2` cleanly via a **5-row Topology-Class summary table**, reserving the 23-row matrix for supplemental documentation.
- **Proposed Correction:**
  1. Replace Table 5's 23-row study-by-study dump in the main text with `Deliverable_E`'s crisp **5-row Topology-Class Summary Table**, moving the 23-row per-study audit matrix to an **Appendix / Online Supplement**. Keep Table 4 in the main text (as the flagship `Tier 1` evidence anchor), but merge/repeat study metadata cleanly and separate `% relative` vs. `pp` units explicitly.
  2. Streamline **Table 9** (Section 9.1) into crisp synthesis propositions with cross-references (`Sec. 8.1–8.4`) instead of repeating raw parenthetical numbers, and tighten **Section 9.3** to focus on *synthesizing security-vs.-liveness and lifecycle-economics trade-offs* rather than re-quoting Section 8 metrics.
  3. Split `L29`, `L70`, `L125`, `L236–237`, and `L489` into shorter 70–110-word paragraphs (or compact bullet lists for `I1–I6` / `E1–E8` in `L125`) for CSUR readability.

---

## 3. Minor Concerns

1. **Citation-unit inconsistency in Table 4 (`L213–228`):** Column 6 (`Paired Delta`) mixes relative percentage deltas (`+80.8% / +80.9% relative`, `-6.6% relative`) with absolute percentage-point deltas (`-3.9 pp`, `-4.1 pp`, `+10 to +19 pp`) and qualitative inequalities (`SAS >= MAD in 93%`) without an explicit unit cue in the column header (`Paired Delta (\Delta_{MAS-SAS}, pp or % rel.)`).
2. **Author name casing & consistency (`L382` vs. `L529`, `L237` vs. `L326`):** `El Hattami` (`L382`) vs. `El hattami` (`L529`) differs in capitalization. Also check `L29` (`at least 27 secondary surveys`): in `L125` (`E4`), 27 cited references include `[30]` (*La Malfa et al.*, a position paper rather than a survey), and restoring `Kim2026_USENIX_Security` raises the secondary-review/position pool to `28` (27 surveys + 1 position paper). Clarify `"at least 27 secondary surveys"` accurately.
3. **ASCII PRISMA Flow Diagram (`L80–121`):** Figure 1 uses plaintext `+---+` ASCII box drawing and folds the `Publication-Status Stratification` breakdown inside the PRISMA flow box. Both CSUR (`acmart`) and TMLR require vector graphics (TikZ/PDF/SVG) matching the standard PRISMA 2020 3-stage layout, with the `Publication-Status Stratification` broken out into a clean standalone table in Section 6.4.
4. **Apparent `QA2 = 2` vs. Wall-Clock Latency Count Mismatch (`L279` vs. `L349`):** `L279` states only `5/44 (11.4%)` studies report direct runtime `[26, 35, 48, 63, 72]`, whereas `quality_appraisal.csv` assigns `QA2 = 2` (`9` studies) to `[6, 26, 28, 35, 45, 48, 51, 62, 63]`—omitting `[6, 28, 45, 51, 62]` from `L279` while including `[72]` (`QA2 = 1`). Add a one-sentence explanation clarifying that `QA2 = 2` credits comprehensive overhead/token-or-turn accounting even when absolute wall-clock seconds are not tabulated (`[6, 28, 45, 51, 62]`), whereas `[72]` reports qualitative wall-clock speedup without full USD accounting (`QA2 = 1`).
5. **Multi-row Table 4/5 missing status repetition (`L213–228`):** Multi-row studies (`Kim et al.`, `Tran & Kiela`, `Zhang et al.`, `Li et al.`, `Chen et al.`) display the venue/status badge only on their first row; if Table 4 splits across a page boundary in PDF typesetting, subsequent rows lose status visibility. Add `ibid.` / status tags or group rows cleanly.
6. **Repository paths in Section 14 (`L671`):** Referencing internal workspace paths (`data/evidence_matrix.json`, `deliverables/Deliverable_C_Systematic_Review_Protocol.md`) reads like an internal lab archive; prepare a public archival repository URL / Zenodo DOI (for CSUR) or anonymized repository link (for TMLR double-blind review).
7. **Editorial minor polish:** In `L138`, clarify `applicable_max_score = 12` vs `14` concisely; in `L557` (`[32]`), spell out `September 2026` consistently; in `L19`, remove the trailing period from the ACM Keywords list.

---

## 4. Terminology, Formatting & Prose Checklist

| Audit Dimension | Current Status | Key Findings & Required Action |
| :--- | :---: | :--- |
| **Abstract (`<= 100` words, unstructured)** | **BORDERLINE / REVISE** | `92` whitespace words, but `97–102` tokens if hyphen/en-dash/slash split; embeds `` `pass^k` `` backticks & undefined metric; missing `pp` after `-50.1`. Trim to `~84` words in plain prose. |
| **Heading Hierarchy & `acmart` Front-Matter** | **FAIL** | Missing `## 1.` (`Title` $\to$ `## 2. Abstract` $\to$ `## 4. Introduction`); shift Intro to **Section 1** (`1–11`), add Author/Affiliation + CCS weights (`500`/`300`/`100`). |
| **ACM Policy on Authorship / AI Disclosure** | **PASS w/ REVISION** | Methods (`L140`) & Declarations (`L673`) properly disclose AI tooling & human liability, **but** `L78` (`Discovery Specialist`, `Review Methodologist`, `Research Director`) blurs human vs. AI screening roles; clarify human authorship & add TMLR 1st-page footnote option. |
| **Overloaded `"Tier"` & Code Notation (`TMLR T2/T8`)** | **FAIL** | Three `"Tier"` scales (`Tier 1–4`, `Tier A–C`, `Tier I–V`), redundant `B1–B4`, `T1–T6` vs. `Tier 1–4`, `Q1–Q6` vs. `Q0–Q4` vs. `Q`, `S01–S11` vs. `S1–S4`. Consolidate and rename orthogonally. |
| **Reference & BibTeX Reconciliation (`[1]`–`[85]`)** | **FAIL** | `85` refs in Sec. 13 vs. `86` claimed in Sec. 14 (`bibliography.bib`); restore `Kim2026_USENIX_Security`; fix `[24]` CSUR status + missing 2 authors; expand `[10]` `et al.`; add verified ACM DOIs (`[36, 61]`) & CSUR/AIRE vol./art. nos. (`[1, 16, 23, 76]`). |
| **In-Text Citation Hygiene & Schema Leaks** | **FAIL** | `85/85` numeric match and `0` missing spaces, **but** leaks raw IDs `SR002` (`L235`), `F17` (`L287`), `F18` (`L326`), `FM-2.3` (`L472`), plus `32` backticked citation brackets. |
| **Beginner / M.Tech Accessibility (Sec. 7+)** | **NEEDS REVISION** | `C1`–`C6` used ~30x before `L355` definition; `DPI` vars ($X, Z_{\text{SAS}}, \hat{Z}_{\text{MAS}}$) undefined (`L156`); `QA3=1` vs. `9/10` ambiguous; `OAS`, `CosMAD`, `PRISMA`, `HE`, `CLEAR`, `ABC` unexpanded; `NV`/`NR` missing under Table 5. |
| **Table Readability & Prose Conciseness** | **NEEDS REVISION** | Table 5 (23×8) & Table 4 (16×8) too wide for print; `L29, L70, L125, L236–237, L489` exceed 140–180w; heavy stat repetition across Sec. 4, 8, 9 (`Table 9`, `Sec. 9.3`), and 12; ASCII Figure 1 needs vector conversion. |

---

*Submitted by Reviewer D (Editorial Quality, Readability & ACM CSUR Compliance Critic).*
