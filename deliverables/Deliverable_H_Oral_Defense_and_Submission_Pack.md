# Deliverable H — Submission Pack, Venue Compliance Checklists, and Oral Defense Guide

**Package Scope:** Publication submission assets and oral/referee defense preparation guide for *When Do LLM Multi-Agent Systems Outperform Single Agents? A Systematic Review of Compute-Normalized Evidence, Coordination Topologies, Failure Mechanisms, and Evaluation Validity* (`Protocol v1.4`: 59 included studies, 34 comparative studies across 87 cleaned comparisons, 25 non-comparative diagnostic/validity studies, 124 verified references).

---

## 1. Submission Cover Letters

### 1.1 Primary Venue Cover Letter — *ACM Computing Surveys (CSUR)*

> **Subject:** New Systematic Survey Submission — *When Do LLM Multi-Agent Systems Outperform Single Agents? A Systematic Review of Compute-Normalized Evidence, Coordination Topologies, Failure Mechanisms, and Evaluation Validity*  
> **To:** Editor-in-Chief and Associate Editors, *ACM Computing Surveys*
>
> Dear Editor-in-Chief and Editorial Board,
>
> We submit our original systematic review manuscript for consideration as a Survey Article in *ACM Computing Surveys*.
>
> Existing surveys catalog multi-agent LLM orchestration frameworks, tool APIs, trajectory failures, and security threats, yet none systematically measures how much of the reported multi-agent accuracy advantage shrinks when single-agent baselines spend equal tokens, tool calls, prompting quality, and upfront optimization cost.
>
> Following PRISMA 2020 and Kitchenham–Charters standards under a single-campaign open-web protocol (`2026-11-20`), we screened 100 deduplicated records into 59 included studies (2023–2026), comprising 34 comparative studies across 87 cleaned paired comparisons plus 25 mechanistic failure, security, and evaluation-validity studies (explicitly separating *More Agents Is All You Need* / *Agent Forest* as a solo-voting boundary check rather than an interactive team). When single-agent baselines move from weak single-pass or unequal-budget setups (`69.4%` multi-agent win rate, `50/72` comparisons, Wilson 95% CI `58.0%–78.9%`) to equal-compute strong single-agent controls (`Tier 1`: `n = 7` studies, `15` comparisons), multi-agent win rates decline to `20.0%` (`3/15`, Wilson CI `7.0%–45.2%`) while outright losses reach `46.7%` (`7/15`)—a `-49.4` percentage-point difference (`95%` cluster-bootstrap CI `-75.3` to `-25.8` points; study-weighted `-45.4` points, exact permutation `p = 0.0154`; strict majority Fisher `p = 0.0106`; Archival-Only `-46.8` points, permutation `p = 0.0353`). Furthermore, `12/12` (`100%`) comparative learned or optimized frameworks omit upfront search or training costs from headline efficiency tables, `12/14` (`85.7%`) dense debate studies document sycophantic peer conformity, and `0/34` (`0%`) comparative studies report multi-trial consistency (`pass^k`). We synthesize these results using a Moderate-to-High calibrated GRADE certainty framework, three independent design axes, and a conditional 5-step deployment checklist, accompanied by self-contained Section 12 Appendices A–E and 124 verified references.
>
> **Originality & AI Disclosure:** This work is original, unpublished, and not under concurrent review elsewhere. Automated LLM screening workflows assisted initial triage, structured extraction, and Python statistical checks under continuous human supervision, conflict adjudication, and source-data verification (detailed in Section 3 and Section 11).
>
> Sincerely,  
> [Author Placeholder]

---

### 1.2 Secondary Journal Submission Letter — *Transactions on Machine Learning Research (TMLR)* (Survey Certification Track)

> **Subject:** Survey Certification Submission — *When Do LLM Multi-Agent Systems Outperform Single Agents? A Systematic Review of Compute-Normalized Evidence...*
>
> Dear Editorial Team and *TMLR* Reviewers,
>
> We submit this systematic review to *TMLR* for Survey Certification. Aligned with TMLR's emphasis on claims–evidence parity and accessible scholarly writing, the paper uses paired within-study comparisons rather than cross-benchmark averaging (87 deduplicated comparisons across 34 comparative studies plus 25 failure/security/validity audits), full cluster-bootstrap and Wilson score intervals alongside exact study-weighted permutation tests (`p = 0.0154`), plain-English concept explanations backed by a Glossary Table (Table 1), a security-vs.-liveness governance section (Section 6.3), and transparent public OpenReview rejection case audits.
>
> Mandatory first-page LLM disclosure, double-blind anonymization instructions, complete Section 12 Appendices A–E, and companion `data/` / `scripts/` verification pipelines accompany the submission.

---

## 2. Target Venue Compliance Checklists

### 2.1 *ACM Computing Surveys (CSUR)* Pre-Submission Checklist
- **Article Length & Format:** Ready for LaTeX conversion using acmart (acmsmall, screen) and ACM-Reference-Format; self-contained manuscript includes Main Synthesis (Sections 1–9), 124 References (Section 10), Declarations (Section 11), and Section 12 Reproducibility Appendices A–E (verbatim `Q1–Q6` strings, 59-study QA item ledger, all 87 comparisons + 34 study win shares, cleaning log, and 41 excluded records) alongside 17 main tables and 4 high-DPI figures + multi-node Mermaid diagrams.
- **Unstructured Abstract Gate (<= 100 words):** 90 whitespace words (100 hyphen/slash-split tokens), zero LaTeX markup, zero backticks, exact statistical synchronization.
- **CCS Concepts & Keywords:** Official 4-line ACM CCS taxonomy with significance weights (500/300/300/100) and plain keyword string without trailing period.
- **Figures & Tables:** Four 300-DPI PNG figures paired with real multi-node Mermaid sources (Two-Column PRISMA 2020 Flowchart, Stratified Win/Loss & Sensitivity Bar Chart with 95% CIs, Paired Effect-Size Forest Plot, and Conditional 5-Step Deployment Guide) plus clean single-page-width synthesis tables.
- **Reference Hygiene:** 124/124 exact 1:1 BibTeX-to-text parity, verified titles/pages (`[12]`, `[6]`, `[86]`), zero "et al." author truncations, zero internal pipeline notes or double URLs.

### 2.2 *TMLR* Survey Certification Readiness Checklist
- **Double-Blind Hygiene:** Remove author lines and local workspace paths so Declarations points cleanly to Section 12 and anonymized companion data/code files.
- **Mandatory First-Page LLM Footnote:** *"Automated LLM workflows assisted candidate triage, JSON extraction, and Python statistical verification under continuous human supervision; the human authors verified every reported number, adjudicated every screening dispute, and accept full scholarly responsibility for all claims."*
- **Plain-English Accessibility:** Core terms defined upfront in Table 1; zero unintroduced shorthand tags in narrative prose; intuitive examples provided before every mathematical formula.

---

## 3. Oral & Referee Defense Q&A Preparation Guide (18 Anticipated Questions)

### Category A — Core Thesis, Scope & Statistical Rigor

1. **Q1: Why write a systematic review on *when multi-agent teams beat solo AI* instead of surveying all agent frameworks?**  
   **Answer:** Existing surveys already catalog agent frameworks, memory designs, and prompting tricks, yet none systematically tested whether claimed multi-agent accuracy gains hold once solo baselines spend equal tokens and upfront search budgets. Across 87 cleaned paired comparisons, multi-agent win rates decline from 69.4% under unequal/weak controls (`50/72`, Wilson `58.0%–78.9%`) to 20.0% (`3/15` wins, Wilson `7.0%–45.2%`; `46.7%` losses) under equal-compute Tier 1 controls (-49.4 percentage points).

2. **Q2: Why didn't you average raw accuracy scores across benchmarks like GSM8K, Finance-Agent, and SWE-bench?**  
   **Answer:** Averaging raw scores across incompatible tasks mixes units. Instead, we keep every comparison **paired within the exact same study, model backbone, and dataset** (`MAS minus Solo`), stratify outcomes by single-agent baseline quality (Tier 1 vs. Tier 2A vs. Tier 2B vs. Tier 3), and examine continuous percentage-point gaps strictly at a single unweighted study level (Table 11 Panel A) alongside exact binomial SEs and inverse-variance weights across multi-model splits (Panel B).

3. **Q3: Isn't Tier 1 relatively small (n = 7 studies, 15 comparisons)? Could one paper with 5 rows bias the result?**  
   **Answer:** We directly checked for study-clustering bias in Table 8: when giving every paper equal weight (`1.0` per study), Tier 1 averages **12.9%** wins vs. **58.3%** in Tier 2+3 (-45.4 percentage points; exact 20,000-shuffle permutation **p = 0.0154**; strict >50% majority Fisher **p = 0.0106**, >=50% Fisher **p = 0.0282**). Moving *Agent Forest* into `RQ4` `C3` solo-voting boundary checks, *OneFlow* into Tier 2B, and *Denisov-Blanch et al.* into Tier 2A keeps Tier 1 strictly pure.

4. **Q4: Could author allegiance or targeted Wave-2 additions explain the Tier 1 drop?**  
   **Answer:** Two direct checks rule this out. First, **Within-Study Paired Contrasts** (Table 10) track 6 papers where the **same authors on identical datasets** test both weak and fair controls—in all 6 papers (*Smit et al.*, *Wang et al.*, *Zhang et al.*, *Debate or Vote*, *Optima*, *Gao et al.*), tightening the solo baseline shrinks or reverses multi-agent gains. Second, **Wave-1 Only** (`71.0%` Tier 2+3 wins, `-51.0` points, Fisher `p = 0.0075`) and **Wave-2 Only** (`68.3%` Tier 2+3 wins) sit right next to each other.

5. **Q5: How stable is the headline finding if preprints and workshop papers are removed?**  
   **Answer:** Restricting solely to peer-reviewed **Archival Journals & Conferences** (25 comparative studies, 67 comparisons) yields 22.2% Tier 1 wins (`2/9`, Wilson `6.3%–54.7%`, 4 studies in *Nature Machine Intelligence*, *NeurIPS*, *ICML*, *TMLR*) vs. 69.0% in Tier 2+3 (-46.8 percentage points; study-weighted `10.0%` vs `62.3%`, permutation **p = 0.0353**). We grade this archival sub-slice conservatively at **Low-to-Moderate GRADE Certainty** because `n = 4` archival Tier 1 studies limits binary Fisher power (`p = 0.0957`).

### Category B — Intuition & Mathematical Concepts

6. **Q6: Explain `pass@k` vs. `pass^k` simply in one concrete example.**  
   **Answer:** Imagine testing an agent 10 times (`n = 10`) on one task where it succeeds 6 times (`c = 6`). Sampling `k = 4` draws **without replacement** (approaching `p^k` as `n >> k`): **pass@4** asks "Did at least 1 try succeed?" (`99.5%`), rewarding noisy retries, whereas **pass^4** asks "Did *all 4* random picks succeed?" (`C(6,4)/C(10,4) = 15/210 = 7.1%`). Jensen's inequality also shows why plugging average pass rate into `p_bar^k` cannot substitute for multi-trial runs. Yet **`0/34` (`0%`)** comparative studies reported `pass^k` (and only `3/59` overall).

7. **Q7: Why does the Data Processing Inequality predict handoff losses on sequential chains, yet allow gains on Finance-Agent (+80.8% relative)?**  
   **Answer:** Information theory's Data Processing Inequality governs a **closed-book relay** where Agent 2 sees *only* Agent 1's summary without re-reading raw input `X` or calling tools (*Tran & Kiela* `-3.9` to `-4.1 pp` on 4-hop `FRAMES`/`MuSiQue`). When workers in a centralized team gather **distinct external documents or tool outputs** exceeding one model's context window (*Kim et al.* `Finance-Agent`, `+80.8%` relative), new external evidence breaks the closed-book Markov chain.

8. **Q8: What does the break-even equation `Q* = C_search / (c_SAS - c_MAS)` tell us about automated frameworks like Optima or AFlow?**  
   **Answer:** All **`12/12` (`100%`)** comparative learned/optimized frameworks spend large upfront GPU or search budgets before testing—such as `<12` hours on 8x A100 GPUs for HotpotQA/GSM8K and `~24` hours for MATH in *Optima*, or `2.1–2.8` hours in *DyLAN* / *GPTSwarm* / *G-Designer*—while omitting them from efficiency tables (`22/34` comparative studies are static zero-search). Using identical runtime units (or adding accuracy value `$v` per accuracy point per query), upfront cost recovers only when post-deployment savings stay strictly positive; `0/10` learned sparse-graph studies currently pass Tier 1 parity.

9. **Q9: How does `Self-MoA` challenge Mixture-of-Agents (`MoA`)?**  
   **Answer:** Standard *Mixture-of-Agents* mixed multiple open models against single-pass GPT-4o (`Tier 3`). Under matched proposer sampling budgets, *Self-MoA* (*TMLR 2026*) demonstrated that resampling the **single strongest model** outperforms heterogeneous mixtures on AlpacaEval 2.0 (`65.7%` vs. `59.1%`, `-6.6 pp`). Similarly, *Agent Forest* (`More Agents Is All You Need` `[51]`) shows independent repeated sampling from one LLM raises accuracy without inter-agent communication (`RQ4` `C3` boundary check).

10. **Q10: How are modern LLM agent teams fundamentally different from classical Swarm Intelligence or classical multi-agent systems?**  
    **Answer:** Classical swarms coordinate hundreds to millions of lightweight `O(1)` mathematical units reacting via numeric rules or pheromones, and classical BDI/MARL systems pass compact symbols or state vectors. Modern LLM teams pass huge natural-language prompts across finite context windows using 2 to 15 heavy models (up to ~1,000 in sparse DAGs like MacNet), creating persuasion cascades, peer flattery, context-window crowding, and text prompt-injection surfaces.

### Category C — Mechanisms, Security, & Review Methodology

11. **Q11: Why include single-agent benchmark audits like *PatchDiff*, *WebArena Verified*, and *tau-bench* in a multi-agent survey?**  
    **Answer:** Under `RQ4`, those audits establish **execution-harness noise floors**: *PatchDiff* finds weak unit tests inflate SWE-bench by `6.2–6.4 pp` (`29.6%` behavioral divergence), and *WebArena Verified* removes `11.3 pp` of false grading errors. While interactive SWE/web errors differ from closed-form MCQA, they show `+2–5 pp` coding/web deltas on unhardened harnesses sit within measurement noise.

12. **Q12: Why include *Agent Forest* (`[51]`) in RQ4 instead of Tier 3 MAS, and why exclude *AgentDebug* and *Router-R1*?**  
    **Answer:** Per Section 3.4's rule, *Agent Forest* (`More Agents Is All You Need`) runs independent parallel tries from *one* LLM (`N = 1`) and aggregates via voting—just like *Self-Consistency* and *Self-MoA*—so coding it as `RQ4` `C3` avoids double-counting solo voting as an interactive multi-agent team. *AgentDebug* (`Excl-01`) logs intra-agent module bugs without multi-agent teamwork, and *Router-R1* routes queries via one stateless policy LLM.

13. **Q13: How were all three model splits of *Bertalanič & Fortuna* (`CAIS '26`) handled statistically?**  
    **Answer:** Rather than cherry-picking the `-27.6 pp` loss on `Ministral-3-8B` (`n = 100`), Table 11 Panel A shows both the 3-model unweighted study mean (`-6.54 pp`, `n=5, k=9`) and the primary large-N mean (`-4.88 pp`, `n=5, k=7`) using `[6]`'s main `Qwen2.5-7B` split (`n = 1,017`, `58.8% vs. 61.0% = -2.2 pp`), while Panel B prints exact binomial SEs (`2.17 pp` vs. `6.93` and `6.43 pp`) and inverse-variance weights (`82.5%` on `Qwen2.5-7B`; IV-weighted mean `-4.55 pp`).

14. **Q14: How did you handle unexposed summary details (`NV`) without guessing?**  
    **Answer:** Zero missing values were guessed or imputed: `404` scalar fields (`478` leaf strings) across `58/59` records are explicitly coded `"not verifiable from accessible open summary"` where open preprints or HTML texts report relative gains or normalized curves without raw cell tables (such as *Kim et al.*'s relative percentages on `arXiv:2512.08296`).

15. **Q15: Why can connecting agents together reduce security and availability?**  
    **Answer:** *Hagag et al.* (ICML 2026) test 13 `Inspect AI` architectures on identical base models and measure up to **3.8x higher attack success rates** over `single_agent` when tools are wired across agents. *CORBA* disables `~92%–100%` of broadcast agents in `1.6–1.9` turns unless anomaly-pruned (*G-Safeguard*), and *Sheshanarayana & Goli* show summarizing verifier traces drops `30.9%` of valid audit flags unless provenance hashes preserve evidence links.

16. **Q16: How should engineers read the 5-Step Conditional Deployment Guide in Figure 4?**  
    **Answer:** As a synthesis-derived checklist requiring prospective randomized trials—not an absolute rule. Especially in Step 5 (`Regime D`), **`0/10` learned sparse-graph systems currently pass Tier 1 parity**, so teams should favor simple centralized orchestrator-workers or static pruned graphs with hard turn caps and sandboxing until learned graphs beat equal-compute baselines with amortized cost logs.

17. **Q17: How were AI workflows used in screening and verification?**  
    **Answer:** Two blinded automated LLM screening workflows conducted initial triage (`Stage 1 kappa = 0.9533`, `Stage 2 = 0.74`, pooled raw pass agreement `163/170 = 95.9%`, end-to-end `95/100 = 95.0%`, explicitly reported as inter-model rather than human rater agreement), while human authors authored all inclusion/parity rules, checked primary sources and OpenReview logs, resolved every disagreement, curated all 124 references, and verified every calculation via `scripts/compute_stats.py` and `scripts/verify_audit.py`.

18. **Q18: What single follow-up experiment would best fill Table 17's empty Tier 1 cells?**  
    **Answer:** A **prospective compute- and dollar-matched randomized trial** comparing *AFlow*, *Optima*, *DyLAN*, and *SAIGE* directly against equal-compute *Self-MoA* and isolated self-correction on database-state-checked harnesses (*WebArena Verified*, *Finance-Agent*)—measuring `pass^5`, wall-clock latency, full break-even query volume `Q*`, and `Inspect AI` adversarial robustness.
