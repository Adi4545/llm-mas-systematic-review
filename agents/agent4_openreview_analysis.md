# Agent 4 Investigation Report: OpenReview & Public Peer-Review Analysis (2024–2026)

**Role:** OpenReview and Peer-Review Investigator  
**Scope:** Transactions on Machine Learning Research (TMLR, OpenReview journal), top ML conferences/workshops on OpenReview (ICLR, NeurIPS, ICML, KDD Workshop), and publisher open/confidential peer-review policies (2024–2026)  
**Target Domain:** Autonomous AI Agents, LLM-Based Agents, Multi-Agent Systems (MAS), Agentic AI, and AI Agent Swarms

---

## 1. Methodology, Verification Protocol, and Access-Honesty Boundaries

### 1.1 Investigative Protocol & Anti-Conflation Safeguards
All records in this report were verified through targeted `search_web` queries over `openreview.net`, `jmlr.org`, `iclr.cc`, `neurips.cc`, `icml.cc`, `aclanthology.org`, `peerj.com`, publisher policy pages (`acm.org`, `springernature.com`, `elsevier.com`), and canonical `arxiv.org` mirrors. Every OpenReview forum identifier (`forum?id=...`) cited directly in this report was independently re-queried by ID to rule out search-snippet conflation:

- **Verified forum IDs retained:** `CTr3bovS5F`, `cjU3YbcRr8`, `SDkEq8Fzvl`, `CsoSWpR5xC`, `3hXEPbG0dh`, `SMe5HYmSff`, `VtmBAGCN7o`, `EHg5GDnyq1`, `EnXJfQqy0K`, `zAdUB0aCTQ`, `z5uVAKwmjf`, `K3n5jPkrU6`, `FfsxgSZW0c`.
- **Conflated IDs detected and excluded:** Initial broad queries surfaced candidate hashes (`Sx038qxjek`, `TrwE8l9aJzs`, `WE_vluYUL-X`, `RQmgTYQ5tR`) that upon direct ID lookup belonged to different papers (`Sx038qxjek` = *CRITIC*, ICLR 2024; `TrwE8l9aJzs` = *Learning Zero-Shot Cooperation with Humans*, ICLR 2023; `WE_vluYUL-X` = *ReAct*, ICLR 2023; `RQmgTYQ5tR` = unverified). Where a submission's exact 10-character hash could not be independently verified without risk of conflation, this report provides the verified OpenReview submission/paper number, canonical venue URL, and/or arXiv identifier instead of guessing a `forum?id=`.

### 1.2 Explicit Access Boundaries & Editorial Distinctions
1. **Journal vs. Conference/Workshop Separation:**  
   - **TMLR** (*Transactions on Machine Learning Research*) is a peer-reviewed archival journal hosted on OpenReview (`jmlr.org/tmlr`), evaluated continuously by **Action Editors (AEs)** and reviewers on two core criteria—(1) *Are claims supported by accurate, convincing, and clear evidence?* and (2) *Would some in TMLR's audience be interested and does the paper communicate findings clearly?*—explicitly excluding subjective "novelty" or "SOTA" thresholds as rejection grounds, and reserving *Survey Certification* (AE/reviewer nominated, Editor-in-Chief approved) for exceptionally thorough surveys.  
   - **ICLR, NeurIPS, and ICML (plus archival tracks/workshops)** are deadline-bound conference/workshop venues governed by Area Chairs (ACs) and Program Chairs, where novelty, algorithmic significance, empirical gains, and cost-benefit trade-offs routinely trigger rejection even for sound work. Conference accept/reject decisions are never portrayed here as journal editorial decisions.
2. **Status Precision (`Accepted` vs. `Rejected` vs. `Desk-Rejected` vs. `Withdrawn` vs. `Under Review`):**  
   - Author-initiated **withdrawals** (e.g., TMLR `3hXEPbG0dh`, ICLR 2025 `SCALE`, ICLR 2024 *Evaluating Multi-Agent Coordination*) are strictly separated from editorial **rejections** or **desk-rejections** and are never relabeled as rejections without explicit decision evidence.
3. **Traditional Journal & Open-Publisher Opacity:**  
   - **ACM Computing Surveys (CSUR):** Single-anonymous review with strict confidentiality covering manuscript text, title, authorship, and referee reports (`acm.org`).  
   - **Springer *Artificial Intelligence Review* (AIRE) & *JAAMAS* (*Journal of Autonomous Agents and Multiagent Systems*):** Double-blind peer review with strict confidentiality barring public disclosure of rejected manuscripts or confidential reviewer reports (`springernature.com`).  
   - **Elsevier journals (e.g., *Information Fusion*, *Knowledge-Based Systems*, *Engineering Applications of AI*):** Confidential referee reports and unpublished/rejected submissions are inaccessible.  
   - **PeerJ Computer Science:** Offers *opt-in* open peer review history. Two verified multi-agent LLM articles—*Adaptive LLM-based multi-agent systems to enhance quantitative trading performance* (DOI: `10.7717/peerj-cs.3630`, Academic Editor Ankit Vishnoi, published March 12, 2026) and *A large language model-driven scientific literature surveys generation framework based on multi-agents and retrieval-augmented generation* (DOI: `10.7717/peerj-cs.3882`, Academic Editor Bilal Alatas, published May 27, 2026)—were inspected; however, their verbatim reviewer reports were not indexed/accessible via public web search.  
   - **OpenReview Indexing Limits:** Because OpenReview renders many 2024–2026 review threads client-side and restricts withdrawn/pending review visibility, verbatim reviewer forms were directly retrieved for a subset of submissions while others exposed only decision metadata, AE names, author revision notes, or follow-up peer-reviewed literature critiques. Every case record explicitly marks what comes from **documented OpenReview reviewer/AE/AC records** versus **access gaps** versus **paper-reported or post-publication methodological critiques**.

---

## 2. TMLR Journal Peer-Review Records on OpenReview (2024–2026)

We document **14 TMLR journal records** spanning Accepted + Survey-Certified surveys (5), Rejected / Desk-Rejected manuscripts (6), Withdrawn surveys (1), and Active Under-Review submissions (2).

### 2.1 Accepted & Survey-Certified TMLR Journal Surveys

#### Case T1: *A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence*
- **Venue & Year:** TMLR (Journal, 2025/2026); Huan-ang Gao, Jiayi Geng, Wenyue Hua, Mengkang Hu, et al.
- **Canonical URL:** https://openreview.net/forum?id=CTr3bovS5F
- **Documented Status:** **Accepted with Survey Certification** (Journal; Action Editor: **Yutian Chen**)
- **Documented Reviewer & AE Strengths / Criticisms:**
  - *Strengths:* Timely synthesis of the shift from static LLMs to adaptive, self-evolving agentic systems; accepted with TMLR *Survey Certification*.
  - *Criticisms (Reviewers):* (1) **Conceptual boundary overlap**—initial draft did not clearly distinguish "self-evolving agents" from established paradigms like Continual/Lifelong Learning, Self-Improving LLMs, Curriculum Learning, and Adaptive Agents; (2) **Encyclopedic listing vs. analytical depth**—sections initially listed methods repetitively rather than building an analytical narrative on trade-offs; (3) **Scope dilution**—including basic SFT and standard RL diluted focus and overlapped with general agent surveys; (4) **Inadequate safety & risk governance**—lacked rigorous coverage of autonomy risks, goal drift, misalignment, and unsafe autonomous tool/code generation; (5) **Programmatic evaluation section**—discussion of dynamic benchmarks and longitudinal metrics lacked deep critical analysis.
  - *AE Caveat:* AE Yutian Chen noted that prescriptive/comparative generalizations remain constrained by the lack of unified quantitative syntheses across heterogeneous works.
- **Author Rebuttal / Revision Actions:** Authors sharpened conceptual boundaries (test-time adaptation, non-parametric evolution, active exploration vs. lifelong/curriculum learning and model editing); expanded the safety/broader-impacts section (sandboxing tool creation, self-modification guardrails, alignment drift monitoring); and restructured the *what/when/how/where* taxonomy around explicit trade-offs.
- **Lessons for Our Systematic Review:** Do not write an encyclopedic "paper catalog"; explicitly delimit LLM-MAS boundaries from classical MAS/MARL and single-agent self-improvement; include dedicated safety, misalignment, and sandboxing governance; and explicitly discuss cross-benchmark incomparability instead of fabricating unified rankings.

#### Case T2: *Towards Generalist Game Agents: A Survey of Foundation Models in Virtual Worlds*
- **Venue & Year:** TMLR (Journal, accepted Oct/Nov 2026); Kuan Zhang, Dongchen Liu, Qiyue Zhao, Yiming Li, et al.
- **Canonical URL:** https://openreview.net/forum?id=SDkEq8Fzvl (preprint: `arXiv:2605.09965`)
- **Documented Status:** **Accepted** (Journal; Action Editor: **Sungwoong Kim**)
- **Documented Reviewer & AE Strengths / Criticisms:**
  - *Strengths:* Four-era historical synthesis formalized via goal-conditioned POMDPs and four-pillar lifecycle (*Dataset, Model, Harness, Benchmark*).
  - *Criticisms (Reviewers & AE):* (1) **Overlapping taxonomic notation**—using `"L1–L5"` across multiple distinct taxonomies (capability progression, model classes, evaluation stages) caused reader confusion; (2) **Formalism edge cases**—Section 2.2 (Eq. 2) normalization and reference denominators failed to handle scores $>1$ for superhuman agents; (3) **Inclusion criteria & cutoff rigor**—reviewers demanded explicit methodological boundaries separating generalist foundation-model agents from narrow single-game RL and explicit curation-window documentation through 2026.
- **Author Rebuttal / Revision Actions:** Relabeled the Section 7 roadmap as `S1–S5` to separate it from Section 6's `L1–L5` minimum-model-class tiers; completely rewrote Section 2.2 mathematical bounds; documented strict inclusion filtering through early 2026 and sharpened the four-pillar dependency analysis showing how harness privileges and compute budgets confound reported scores.
- **Lessons for Our Systematic Review:** Never reuse overloaded tier labels (`L1–L5`) across different taxonomic axes; audit every formal definition/equation for edge cases; document exact search cutoff dates and PRISMA/inclusion-exclusion criteria; and isolate *harness/compute confounds* when comparing agent frameworks.

#### Case T3: *Large Language Model-based Data Science Agent: A Survey*
- **Venue & Year:** TMLR (Journal, 2025/2026; Submission 5567); Ke Chen, Peiran Wang, Yaoning Yu, Xianyang Zhan, Haohan Wang.
- **Canonical URL:** `https://openreview.net/group?id=TMLR` (TMLR Submission 5567; `arXiv:2508.02744`; exact `forum?id=` hash not separately retrieved)
- **Documented Status:** **Accepted** (Journal; Action Editor: **Stefan Lee**)
- **Documented Reviewer Criticisms & Revision Actions:**
  - *Access boundary:* Individual verbatim initial reviewer weakness forms were not separately indexed; however, OpenReview revision summaries document the exact changes implemented in response to TMLR peer review.
  - *Revision Actions Implemented:* (1) Restructured the introduction around **five progressive Research Questions (RQs)** bridging general agent design (single-agent, multi-agent, dynamic generation) and data science workflows; (2) Added **quantitative landscape analyses** mapping methodological trends; (3) Upgraded Section 5 from a passive benchmark list to a **critical synthesis of structural benchmark flaws** (isolated steps vs. end-to-end pipelines, rigid formats, overly clean inputs); (4) Refined **Advanced Reflection Mechanisms** toward cross-stage, long-horizon error attribution and added future directions on *Data-Centric Diagnostics* and *Uncertainty-Aware Workflow Planning*.
- **Lessons for Our Systematic Review:** Anchor the review in explicit progressive RQs; pair qualitative taxonomy with quantitative corpus statistics; and critically evaluate benchmark ecological validity rather than summarizing leaderboard scores.

#### Case T4: *A Survey on Large Language Model-Based Social Agents in Game-Theoretic Scenarios*
- **Venue & Year:** TMLR (Journal, published May 9, 2025); Xiachong Feng, Longxu Dou, Minzhi Li, Qinghao Wang, Yu Guo, Haochuan Wang, Chang Ma, Lingpeng Kong.
- **Canonical URL:** https://openreview.net/forum?id=CsoSWpR5xC
- **Documented Status:** **Accepted** (Journal; Action Editor: **Yonatan Bisk**)
- **Documented Reviewer Strengths / Criticisms:**
  - *Strengths (Reviewers `uaWb`, `xzPJ`):* Well-structured three-pillar synthesis (*Game Framework*, *Social Agent Modules* [Preferences, Beliefs, Reasoning], *Evaluation Protocol* [game-agnostic, game-specific, behavioral]).
  - *Criticisms / Requested Changes:* Minor editorial/structural fixes—correcting typos, fixing text placement in early sections, and adding a dedicated **Broader Impact** section (a mandatory TMLR compliance check).
- **Author Rebuttal / Revision Actions:** Authors corrected placement/typos and added the Broader Impact statement prior to final acceptance.
- **Lessons for Our Systematic Review:** Clean prose, disciplined early-section signposting, and an explicit *Broader Impact / Ethics & Governance* section are hard compliance gates in TMLR-style journal review.

#### Case T5: *Dynamic Agent Skills: A Lifecycle Survey and Taxonomy of Evolving Skill Libraries*
- **Venue & Year:** TMLR (Journal, accepted July 2026); Yubo Li.
- **Canonical URL:** https://openreview.net/forum?id=cjU3YbcRr8
- **Documented Status:** **Accepted with Survey Certification** (Journal; Action Editor: **Tommaso R. Cesari**)
- **Documented Review Context & Access Boundary:** Long survey synthesizing 124 papers (2023–2026) via a 6-sense artifact taxonomy (`SKILL.md` packages, code functions, workflow graphs, adapters, etc.), an 8-stage lifecycle, and a 10-operator vocabulary. Verbatim reviewer weakness bullets were not indexed in search snippets beyond forum metadata and author-list revision updates; explicit *Survey Certification* confirms TMLR rewards unifying operational vocabularies that standardize disparate engineering systems without conflating them.
- **Lessons for Our Systematic Review:** Standardize overloaded community terms (e.g., "agent", "swarm", "protocol", "skill", "orchestration") via an explicit formal vocabulary and lifecycle schema before classifying papers.

---

### 2.2 Rejected & Desk-Rejected TMLR Journal Submissions

#### Case T6: *AgenticNet: Rethinking Multi-agent System Architectures with LLM-based Networks*
- **Venue & Year:** TMLR (Journal, Paper 7332, 2025/2026)
- **Canonical URL:** `https://openreview.net/group?id=TMLR` (TMLR Paper 7332; candidate hash `RQmgTYQ5tR` unverified in follow-up lookup and excluded)
- **Documented Status:** **Rejected by TMLR** (Journal; Action Editor: **Tim Georg Johann Rudner**)
- **Documented Reviewer & AE Strengths / Criticisms:**
  - *Strengths:* Creative neural-network/MLP-inspired layered MAS topology (planners → executors → synthesizers) with heuristic prompt backpropagation; broad benchmarking (AIME24, GSM8K, MATH500, HumanEval, MBPP).
  - *Critical Weaknesses (Reviewers & AE):*
    1. **Direct Text–Table Contradictions (Overclaiming):** Abstract/intro claimed AgenticNet *"consistently outperforms"* all baselines, contradicted by Table 1 where it trailed *MaAS* on GSM8K and *MermaidFlow* on MATH.
    2. **Negative Ablation Contradictions:** Table 2 ablations showed the proposed training/adaptation mechanism *degraded* performance (MATH dropping 96.4% → 83.2%; MBPP dropping 100% → 97.2%), contradicting the paper's claims for the feedback loop.
    3. **Severe Rebuttal Protocol Discrepancies:** When authors re-ran under a `"strict exact-match"` protocol in rebuttal, metrics shifted dramatically (e.g., MBPP dropping 100% → 77.5%), undermining trust in the original evaluation pipeline.
    4. **Inference-Compute Confound:** Cost-matched comparisons added during rebuttal (e.g., MATH Level 5) showed gains were driven by inference-compute scaling; under matched cost, AgenticNet barely beat Vanilla CoT and trailed simpler baselines (*MultiPersona*, *LLM-Debate*, *LLM-Blender*).
    5. **Fixed-Topology Rigidity:** Forced sequential layers added unnecessary latency/overhead for simpler tasks.
- **Author Rebuttal / Revision Actions:** Authors performed `"strict exact-match"` re-runs and cost-matched experiments during rebuttal; these revisions exposed rather than resolved the claims–evidence gap, triggering AE rejection under TMLR Criterion 1.
- **Lessons for Our Systematic Review:** Flag **inference-compute confounds** and **claims–table contradictions** as primary methodological risks when reviewing primary MAS architecture papers; never take headline "consistently outperforms" claims at face value without checking ablations and cost-matched baselines.

#### Case T7: *Inducing Disagreement in Multi-Agent LLM Executive Teams: Only the Devil's Advocate Works*
- **Venue & Year:** TMLR (Journal, Submission 7253, 2025/2026)
- **Canonical URL:** `https://openreview.net/group?id=TMLR` (TMLR Submission 7253)
- **Documented Status:** **Rejected by TMLR** (Journal; Action Editor: **Huazheng Wang**)
- **Documented Reviewer & AE Criticisms:**
  1. **Unjustified Domain Transfer:** Assumed higher disagreement is inherently beneficial for LLM collectives based on human organizational psychology without theoretical or empirical justification for LLMs.
  2. **Proxy Metric Insufficiency:** Measured almost solely *disagreement rate* (99.2% Devil's Advocate vs. 48.3% baseline across 480 team decisions) without measuring downstream decision/outcome quality or distinguishing productive divergence from noise.
  3. **Architecture–Claim Mismatch:** Used context-isolated parallel sampling rather than interactive multi-agent deliberation/debate, invalidating claims about multi-agent deliberation dynamics.
  4. **Unanalyzed Inauthentic Dissent:** Noted 4.9% of agents recommended options they privately rated lower under Devil's Advocate assignment, without analyzing quality trade-offs.
- **Author Rebuttal / Revision Actions:** Reviewers requested justifying disagreement's value, adding outcome-quality metrics, toning down deliberation claims, and analyzing inauthentic dissent; final rebuttal details not further indexed beyond the rejection decision.
- **Lessons for Our Systematic Review:** Separate **process proxy metrics** (disagreement rate, message count, role diversity) from **downstream task accuracy/decision quality**, and verify whether papers claiming "interactive debate" actually implement multi-turn interaction rather than isolated parallel sampling.

#### Case T8: *Evaluating World Models with LLM for Decision Making* (revised to *LLM-Based World Models Can Make Decisions Solely, But Rigorous Evaluations are Needed*)
- **Venue & Year:** TMLR (Journal, 2025/2026); Chang Yang, Xinrun Wang, Junzhe Jiang, Qinggang Zhang, Xiao Huang.
- **Canonical URL:** `https://openreview.net/group?id=TMLR`
- **Documented Status:** **Desk-Rejected by Action Editor** (initial TMLR submission); subsequently revised and published under the updated title.
- **Documented AE Criticisms:**
  - Desk-rejected prior to reviewer assignment due to: (1) a **very high number of grammar errors** throughout the manuscript, and (2) **extensive undefined jargon** impairing readability (violating TMLR Criterion 2 on clear communication).
- **Author Revision Actions:** Authors substantially rewrote the prose, defined terminology, restructured motivating observations across 31 environments, and re-titled the work to reflect calibrated empirical claims.
- **Lessons for Our Systematic Review:** Even technically interesting manuscripts face immediate desk rejection at journals if terminology is undefined or writing quality degrades readability; define every MAS/agentic term rigorously at first use.

#### Case T9: *When Consensus Is Not Correctness: Diversity Collapse and Manufactured Overconfidence in Multi-Agent LLM Debate*
- **Venue & Year:** TMLR Paper 9844 (Journal) & KDD Workshop on Agentic AI Evaluation and Trustworthiness; Chengxiao Dai.
- **Canonical URL:** `https://openreview.net/group?id=TMLR` (TMLR Paper 9844)
- **Documented Status:** **Rejected by TMLR** (Journal; Action Editor: **Peng Li**); **Accepted (Workshop)** at KDD Agentic AI Evaluation Workshop.
- **Documented Criticisms & Access Boundary:** Verbatim TMLR reviewer comments and AE rejection rationale for Paper 9844 are **not publicly indexed/accessible** in web search, and the KDD workshop record is archival without public meta-reviews. *Methodological note (from paper abstract):* Highlights a core MAS evaluation flaw—endogenous consensus causes inter-agent correlation $\rightarrow 1$ ("diversity collapse"), inflating perceived confidence precisely where error is highest.
- **Lessons for Our Systematic Review:** Journal rejection does not invalidate a diagnostic finding (which may still clear workshop peer review); simultaneously, TMLR's strict evidence standard means proposed remedies (e.g., split-conformal certificates) face higher validation bars at archival journals than at specialized workshops.

#### Case T10: *RePrompt: Reflection-based Automatic Prompting for LLM Agents*
- **Venue & Year:** TMLR (Journal; also ICLR 2025 submission track; `arXiv` title *RePrompt: Planning by Automatic Prompt Engineering for Large Language Models Agents*); Weizhe Chen, Sven Koenig, Bistra Dilkina.
- **Canonical URL:** `https://openreview.net/group?id=TMLR`
- **Documented Status:** **Rejected by TMLR** (Journal; Action Editor: **Xingchen Wan**).
- **Documented Criticisms & Access Boundary:** Exact verbatim TMLR reviewer weaknesses, AE decision letter, and author rebuttal are **not publicly accessible/indexed** in search snippets beyond verified rejection status and AE attribution.
- **Lessons for Our Systematic Review:** Public search indexing of rejected TMLR threads is partial; systematic reviewers analyzing peer-review outcomes must avoid extrapolating undocumented reasons where verbatim AE letters are unavailable.

#### Case T11: *A Survey on Self-Play Methods in Reinforcement Learning*
- **Venue & Year:** TMLR Paper 4567 (Submitted March 2025; Rejected May 2025; `arXiv:2408.01072`); Ruize Zhang, Zelai Xu, Chengdong Ma, Chao Yu, et al.
- **Canonical URL:** `https://openreview.net/group?id=TMLR` (TMLR Paper 4567)
- **Documented Status:** **Rejected by TMLR** (Journal; Action Editor: **Marc Lanctot**; Long submission $>12$ pages).
- **Documented Criticisms & Access Boundary:** Exact verbatim reviewer critiques and AE decision rationale are **not publicly indexed** in search snippets; verified metadata confirms TMLR rejects even comprehensive long surveys when TMLR's claims–evidence or communication standards are unmet.

---

### 2.3 Withdrawn & Active Under-Review TMLR Journal Records

#### Case T12: *Agent Harness Engineering: A Survey*
- **Venue & Year:** TMLR (Journal, 2026); Junjie Li, Xi Xiao, Yunbei Zhang, Chen Liu, ..., Chandan K. Reddy.
- **Canonical URL:** https://openreview.net/forum?id=3hXEPbG0dh
- **Documented Status:** **Withdrawn by Authors** on **June 30, 2026** (subsequently updated as an OpenReview Archive Direct Upload/preprint). *Note:* Strictly **Withdrawn**, NOT documented as Rejected.
- **Documented Review Context & Access Boundary:** Formal public reviewer reports or AE evaluations are **not publicly visible/indexed** post-withdrawal. The manuscript itself frames the "agent harness" infrastructure layer via a 7-layer taxonomy (**ETCLOVG**) mapping 170+ open-source projects.
- **Lessons for Our Systematic Review:** Distinguishing *withdrawn* OpenReview preprints/archive uploads from *peer-reviewed journal publications* is mandatory during literature screening—our review must classify uncertified/withdrawn preprints separately from peer-reviewed archival work.

#### Case T13: *Observe, Share, or Predict? Disentangling Partner Information in Embodied Multi-Agent Collaboration*
- **Venue & Year:** TMLR (Journal, Paper 13141, 2026); Adrián Szlatincsán, Filippo Ziliotto, Bruno Lepri, Luciano Serafini, Massimiliano Luca, Tommaso Campari.
- **Canonical URL:** https://openreview.net/forum?id=SMe5HYmSff
- **Documented Status:** **Under Review** (Active double-blind TMLR submission).
- **Documented Review Context & Access Boundary:** AE hidden/unassigned and reviewer critiques **not yet publicly visible** during active double-blind review.

#### Case T14: *MADA-RL: Multi-Agent Debate-Aware Reinforcement Learning for Parameter-Efficient Reasoning in Compact Models*
- **Venue & Year:** TMLR (Journal, Paper 10674, 2026)
- **Canonical URL:** `https://openreview.net/group?id=TMLR` (TMLR Paper 10674)
- **Documented Status:** **Under Review** (Journal; Action Editor: **Zhirong Wu**).
- **Documented Review Context & Access Boundary:** Reviewer reports and final decision **not yet publicly released/finalized**.

---

## 3. Conference & Workshop Peer-Review Records on OpenReview (2024–2026)

We document **17 conference/workshop OpenReview records** (`C1`–`C17`) across ICLR (2024, 2025, 2026), NeurIPS (2024, 2025), and ICML (2026), clearly separated from TMLR journal decisions.

### 3.1 Rejected & Withdrawn Conference Submissions (and Longitudinal Resubmission Trajectories)

#### Case C1: *LLM-Deliberation: Evaluating LLMs with Interactive Multi-Agent Negotiation Games* (ICLR 2024 Reject → NeurIPS 2024 Accept)
- **Venue & Year:** ICLR 2024 Conference Track → revised and published at **NeurIPS 2024** as *Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation*; Sahar Abdelnabi, Amr Gomaa, Sarath Sivaprasad, Lea Schönherr, Mario Fritz.
- **Canonical URL:** `https://openreview.net/group?id=ICLR.cc/2024/Conference` (project repo: `github.com/S-Abdelnabi/LLM-Deliberation`)
- **Documented Status:** **Rejected** at **ICLR 2024** (Conference decision); subsequently revised and **Accepted** at **NeurIPS 2024**.
- **Documented Reviewer & Area Chair Criticisms (ICLR 2024 OpenReview):**
  - *Strengths:* Timely evaluation of LLM agents in scorable multi-issue, multi-party negotiation games.
  - *Criticisms (AC Meta-Review & Reviewers):* (1) **Limited technical novelty**—relied primarily on standard prompting of off-the-shelf LLMs without proposing a new algorithm or architecture; (2) **Predictable findings**—observing GPT-4 outperform smaller models offered limited deep diagnostic surprises; (3) **Safety-alignment confounders**—adversarial/competitive roles triggered LLM refusal/guardrail artifacts, confounding strategic reasoning evaluation; (4) **Template narrowness**—heavy reliance on specific base game templates; AC recommended adding fine-tuning, tree/graph-of-thought planning, or deeper analysis of decision mechanisms.
- **Author Rebuttal / Longitudinal Revision:** Authors incorporated detailed prompt templates, multiple game difficulty/issue/agent variants, and explicit modeling of cooperative, competitive, and malicious stakeholder dynamics before securing **NeurIPS 2024** acceptance.
- **Lessons for Our Systematic Review:** Top ML conferences routinely reject pure "prompting + evaluation benchmark" papers for lacking algorithmic novelty unless diagnostic insights are surprising and template/guardrail confounders are explicitly controlled.

#### Case C2: *Evaluating Multi-Agent Coordination Abilities in Large Language Models* (ICLR 2024 Withdrawn → NAACL Findings Accept)
- **Venue & Year:** ICLR 2024 Conference Track (Submitted Sept 21, 2023) → revised and published in **NAACL Findings** as *LLM-Coordination: Evaluating and Analyzing Multi-agent Coordination Abilities in Large Language Models*; Saaket Agashe, Yue Fan, Xin Eric Wang (with Anthony Reyna in NAACL version).
- **Canonical URL:** `https://openreview.net/group?id=ICLR.cc/2024/Conference` (note: `TrwE8l9aJzs` was verified as a different ICLR 2023 paper and excluded)
- **Documented Status:** **Withdrawn** at **ICLR 2024** (NOT labeled rejected); later **Accepted** at **NAACL Findings**.
- **Documented Reviewer Criticisms (ICLR 2024 OpenReview):**
  - *Strengths:* Addressed cooperative AI and zero-shot partner robustness across five coordination axes (Theory of Mind, Situated Reasoning, Sustained Coordination, Robustness to Partners, Explicit Assistance).
  - *Criticisms:* (1) **Over-tailored evaluation axes & narrow environments**—evaluation relied heavily on *Overcooked*, *CollabCapture*, and *CollabEscape*, casting doubt on general validity of the five criteria; (2) **Mismatched baselines**—compared LLM-Co against classical RL (PPO, PBT) while omitting contemporary LLM-based agent baselines; (3) **Missing human experiments**—claimed to evaluate human-AI coordination while relying solely on behavioral cloning (BC) and proxy policies without real human trials; (4) **Scalability, prompt sensitivity, and API cost**.
- **Author Rebuttal / Longitudinal Revision:** Authors withdrew from ICLR 2024 and expanded the benchmark (e.g., adding *CoordQA* explicitly testing Theory of Mind and joint planning) for NAACL Findings.
- **Lessons for Our Systematic Review:** Never evaluate an LLM-MAS solely against classical RL (PPO/PBT) without contemporary LLM-agent baselines, and never claim "human-AI coordination" on proxy/BC partners alone.

#### Case C3: *SCALE: Augmenting Content Analysis via LLM Agents and AI-Human Collaboration*
- **Venue & Year:** ICLR 2025 Conference Track (Submission ID: 6097); Chengshuai Zhao, Zhen Tan, Chau-Wai Wong, Xinyan Zhao, Huan Liu, Tianlong Chen.
- **Canonical URL:** `https://openreview.net/group?id=ICLR.cc/2025/Conference` (Submission 6097)
- **Documented Status:** **Withdrawn** by authors on **January 19, 2025** (Conference submission; NOT labeled rejected).
- **Documented Reviewer Criticisms (ICLR 2025 OpenReview):**
  1. **Missing Cost/Efficiency Comparison:** Justified the framework by claiming human annotation is slow and expensive, yet failed to report actual wall-clock time and API cost vs. human effort.
  2. **Insensitive / Missing Baselines:** Omitted traditional ML classifiers and single-prompt LLM baselines across evaluated tasks.
  3. **Task Performance Failures:** Underperformed on 3 out of 7 evaluated tasks, raising robustness doubts.
  4. **Shallow Technical Contribution:** "Domain-knowledge incorporation" amounted primarily to prompt engineering rather than substantive architectural depth.
  5. **Narrow Evaluation Scope:** Relied on isolated single-coding/codebook-update accuracy without holistic framework quality or qualitative human evaluations.
- **Author Rebuttal / Outcome:** Authors withdrew on January 19, 2025; verbatim rebuttal text not indexed.
- **Lessons for Our Systematic Review:** Whenever a multi-agent paper motivates itself on *cost/labor reduction*, reviewers demand empirical cost-and-latency accounting plus single-prompt baselines proving multi-agent overhead is warranted.

#### Cases C4–C6: *Multi-Agent Causal Discovery Using Large Language Models*, *Seeker: Enhancing Exception Handling in Code with a LLM-based Multi-Agent Approach*, and *HeurAgenix: A Multi-Agent LLM-Based Paradigm for Adaptive Heuristic Evolution and Selection in Combinatorial Optimization*
- **Venue & Year:** ICLR 2025 Conference Track (3 distinct withdrawn submissions).
- **Canonical URL:** `https://openreview.net/group?id=ICLR.cc/2025/Conference`
- **Documented Status:** All three are verified **Withdrawn** ICLR 2025 conference submissions (NOT portrayed as rejected).
- **Access Boundary & Context:** Because ICLR 2025 withdrawn forums restrict public scraping of raw referee score sheets, verbatim reviewer bullets were **not publicly indexed** in search results for these three submissions. Notably, *HeurAgenix* later released extended iterations addressing inference-cost bottlenecks by distilling the heuristic selector into a fine-tuned lightweight model, underscoring the recurring conference pressure on multi-agent API/compute overhead.

---

### 3.2 Accepted Conference Benchmarks, Multi-Agent Frameworks, Failure Analyses & Position Papers

#### Case C7: *AgentBench: Evaluating LLMs as Agents*
- **Venue & Year:** ICLR 2024 Conference Track; Xiao Liu, Hao Yu, Hanchen Zhang, et al.
- **Canonical URL:** https://openreview.net/forum?id=zAdUB0aCTQ
- **Documented Status:** **Accepted (Poster)** at **ICLR 2024**
- **Documented Reviewer Scores & Criticisms (OpenReview):**
  - *Scores:* Ratings spanned **6 ("marginally above the acceptance threshold", Reviewer `39pk`, Soundness: 2 fair)** to **8 ("accept, good paper")**; Reviewer `eDe1` rated Soundness **3 (good)**.
  - *Strengths:* Timely evaluation of LLMs as autonomous sequential decision-makers across 8 interactive environments and ~27–29 open-source/commercial LLMs.
  - *Criticisms:* (1) **Lack of actionable diagnostics**—reported success rates without pinpointing actionable fixes or granular error taxonomies (e.g., tool syntax vs. strategic planning errors); (2) **Simplified/contrived environments**—stripped 2D/3D context from tasks like ALFWorld into text/code setups and lacked automated complexity generators; (3) **Static prompt bias**—one fixed prompt template across all models risked favoring models compatible with that prompt style; (4) **Text/code modality skew**.
- **Author Rebuttal / Revision Actions:** Authors posted detailed official OpenReview responses in November 2023 defending/clarifying environment designs and diagnostic breakdowns prior to acceptance.
- **Lessons for Our Systematic Review:** Even landmark accepted benchmarks face sharp scrutiny over **prompt-template sensitivity**, **environment oversimplification**, and **diagnostic granularity**—key dimensions our review's benchmark evaluation rubric must grade explicitly.

#### Case C8: *Building Cooperative Embodied Agents Modularly with Large Language Models* (CoELA)
- **Venue & Year:** ICLR 2024 Conference Track; Hongxin Zhang, Weihua Du, Jiaming Shan, Qinhong Zhou, Yilun Du, Joshua B. Tenenbaum, Tianmin Shu, Chuang Gan.
- **Canonical URL:** https://openreview.net/forum?id=EnXJfQqy0K
- **Documented Status:** **Accepted** at **ICLR 2024**
- **Documented Reviewer Scores & Criticisms (OpenReview):**
  - *Score:* **8 ("Accept, good paper")**, Confidence **4**.
  - *Criticisms:* (1) **Suboptimal communication module**—ablations revealed agents could misinterpret actions and lacked dynamic bi-directional verification loops (clarifying questions, explicit hand-off confirmation); (2) **Scalability limits** with larger object counts, complex interactions, and longer horizons; (3) **Missing communication cost–effectiveness trade-off**—lacked token/compute accounting for continuous natural-language messaging.
- **Author Rebuttal / Revision Actions:** Verbatim author rebuttal text not retrieved in search snippets.
- **Lessons for Our Systematic Review:** Even high-scoring (8/10) accepted multi-agent papers are criticized for lacking bi-directional verification handoffs and token-cost vs. accuracy Pareto curves.

#### Case C9: *MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework*
- **Venue & Year:** ICLR 2024 Conference Track; Sirui Hong, Mingchen Zhuge, Jonathan Chen, ..., Jürgen Schmidhuber.
- **Canonical URL:** `https://openreview.net/forum?id=VtmBAGCN7o`
- **Documented Status:** **Accepted (Oral)** at **ICLR 2024**
- **Access Boundary vs. Post-Publication / Follow-Up Critiques:** Verbatim raw OpenReview reviewer scorecards for `VtmBAGCN7o` were not retrieved in search snippets (`not publicly accessible/indexed via web search`). *Post-publication & follow-up peer-reviewed critiques (explicitly separated from initial OpenReview reviews):* Public community discussions scrutinized baseline comparisons and API-version reproducibility; subsequent peer-reviewed MAS failure papers (e.g., MAST) documented linear SOP assembly-line rigidity, high token/latency overhead across multiple role passes, and upstream-to-downstream error amplification when early roles (Product Manager/Architect) hallucinate.
- **Author Rebuttal / Revision Actions:** Not accessible/not reported in indexed search snippets.
- **Lessons for Our Systematic Review:** Do not conflate Oral conference prestige with immunity from architectural fragility; record baseline-version sensitivity and SOP rigidity alongside headline success.

#### Case C10: *AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors*
- **Venue & Year:** ICLR 2024 Conference Track; Weize Chen, Yusheng Su, Jingwei Zuo, et al.
- **Canonical URL:** `https://openreview.net/forum?id=EHg5GDnyq1`
- **Documented Status:** **Accepted (Poster)** at **ICLR 2024**
- **Documented Review / Literature Context:** Indexed in OpenReview and PeerCheck tracking; recognized for multi-domain breadth (reasoning, coding, tool use, Minecraft) and documenting emergent group behaviors (*volunteer, conformity, destructive*). Verbatim individual numerical scores were not retrieved in raw form; recurring methodological limitations noted in literature include high token/latency overhead, strong sensitivity to base LLM backbone (GPT-3.5 vs. GPT-4), and error propagation in dense communication loops.
- **Author Rebuttal / Revision Actions:** Not accessible/not reported in indexed search snippets.
- **Lessons for Our Systematic Review:** Separate empirical "emergent behavior" labels from prompt-induced artifacts and track backbone-model dependence across frameworks.

#### Cases C11–C12: *AFlow: Automating Agentic Workflow Generation* & *Scaling Large Language Model-based Multi-Agent Collaboration* (MacNet)
- **Venues & Years:**
  - *AFlow:* ICLR 2025 **Accepted (Oral)** — `https://openreview.net/forum?id=z5uVAKwmjf` (Jiayi Zhang et al.)
  - *MacNet:* ICLR 2025 **Accepted (Poster)** — `https://openreview.net/forum?id=K3n5jPkrU6` (Chen Qian et al.)
- **Access Boundary & Documented Follow-Up Critiques:** Verbatim raw ICLR 2025 referee score sheets were not exposed in search snippets (`not publicly accessible/indexed`). Subsequent peer-reviewed/OpenReview studies (*JudgeFlow*, *AgentTailor*, *GoA*, *NEXA*) document concrete methodological weaknesses in both paradigms: (1) **AFlow** relies on coarse end-to-end execution rewards lacking node-level error credit assignment, incurs heavy search-time MCTS API costs, and remains bounded by predefined primitive operators; (2) **MacNet** relies on static/random DAG topologies rather than instance-adaptive routing and exhibits performance plateauing from context accumulation and token bloat at 1,000+ agents.
- **Author Rebuttal / Revision Actions:** Not accessible/not reported in indexed search snippets.
- **Lessons for Our Systematic Review:** Contrast search-time vs. inference-time cost profiles and distinguish static DAG topologies from dynamic, query-adaptive orchestration.

#### Case C13: *Why Do Multi-Agent LLM Systems Fail?* (MAST)
- **Venue & Year:** **NeurIPS 2025** Track on Datasets and Benchmarks; Mert Cemri, Melissa Z. Pan, Ion Stoica, Matei Zaharia, Joseph E. Gonzalez, et al.
- **Canonical URL:** `https://arxiv.org/abs/2503.13657` (NeurIPS 2025 OpenReview proceedings; exact `forum?id=` not separately retrieved)
- **Documented Status:** **Accepted** at **NeurIPS 2025 Datasets and Benchmarks Track**
- **Access Boundary & Substantive Diagnostic Relevance:** Verbatim NeurIPS 2025 reviewer comments were not indexed in search snippets. Critically, MAST itself is a landmark peer-reviewed audit of MAS failure modes across 1,600+ annotated traces ($\kappa = 0.88$) and 7 frameworks (41%–86.7% failure rates), categorizing failures into **System Design/Specification (~44.2%)**, **Inter-Agent Misalignment (~32.35%)**, and **Task Verification/Termination (~23.5%)**.
- **Author Rebuttal / Revision Actions:** Not accessible/not reported in indexed search snippets.
- **Lessons for Our Systematic Review:** Anchor our failure-mode synthesis in empirically validated taxonomies (with reported inter-annotator agreement $\kappa = 0.88$) rather than ad-hoc failure anecdotes.

#### Case C14: *Large Language Models Miss the Multi-agent Mark*
- **Venue & Year:** **NeurIPS 2025** Position Paper Track; Emanuele La Malfa, Gabriele La Malfa, Samuele Marro, Jie M. Zhang, Elizabeth Black, Michael Luck, Philip Torr, Michael J. Wooldridge.
- **Canonical URL:** https://openreview.net/forum?id=FfsxgSZW0c
- **Documented Status:** **Accepted** at **NeurIPS 2025 Position Paper Track**
- **Access Boundary & Substantive Relevance:** Verbatim NeurIPS 2025 reviewer scores were not indexed in search snippets. The accepted position paper documents four systemic conceptual failures in contemporary LLM-MAS papers: (1) misappropriating classical MAS terminology without genuine agent autonomy/incentives; (2) trivial static text prompts masquerading as structured environments; (3) rigid sequential/parallel prompt chaining labeled as asynchronous communication protocols; and (4) superficial claims of "emergent behavior" lacking complex-systems rigor.
- **Author Rebuttal / Revision Actions:** Not accessible/not reported in indexed search snippets.
- **Lessons for Our Systematic Review:** Directly bridge classical MAS theory (autonomy, social protocols, decentralized environments) with LLM-MAS engineering so reviewers from traditional MAS venues (*JAAMAS*) cannot fault terminological misuse.

#### Cases C15–C17: 2026 Frontier Diagnostic & Coordination Acceptances (*AgenTracer*, *Emergent Coordination*, *AgentDebug*)
- **C15 — *AgenTracer: Who Is Inducing Failure in the LLM Agentic Systems?*** (`arXiv:2509.03312`; Guibin Zhang et al.) — **Accepted (Poster)** at **ICLR 2026** (Submission 3262). Verbatim 2026 referee score sheets and author rebuttals are **not publicly accessible/indexed** in search snippets (`Sx038qxjek` from a secondary snippet belonged to ICLR 2024 *CRITIC* and was excluded). Addresses step/agent-level failure attribution (showing frontier reasoning LLMs score $<10\%$ on root-cause attribution). *Lesson:* Integrate credit-assignment and root-cause localization as core evaluation dimensions.
- **C16 — *Emergent Coordination in Multi-Agent Language Models*** (`arXiv:2510.05174`; Christoph Riedl) — **Accepted (Poster)** at **ICLR 2026**. Verbatim referee score sheets and rebuttals are **not publicly accessible/indexed** (`EnXJfQqy0K` from an initial snippet belonged to CoELA and was excluded). Introduces PID of Time-Delayed Mutual Information (TDMI) to separate spurious temporal coupling from genuine cross-agent synergy, noting open methodological challenges around stylized task simplicity, prompt-induced differentiation confounders, and model-scale dependence (GPT-4 vs. Llama-3.1-8B). *Lesson:* Demand information-theoretic or counterfactual controls before accepting "emergent coordination" claims.
- **C17 — *AgentDebug: Where LLM Agents Fail and How They Can Learn From Failures*** (`arXiv:2509.25370`; Kunlun Zhu, Jiaxuan You, et al.) — **Accepted / Presented** at **ICML 2026 FAGEN Workshop** (*Failure Modes in Agentic AI*). Verbatim workshop review comments and rebuttals are **not publicly accessible/indexed**. Establishes *AgentErrorTaxonomy* across Memory, Reflection, Planning, Action, and System-level failures, reinforcing the methodological gap between coarse task success metrics and root-cause error attribution. *Lesson:* Separate failure detection from root-cause isolation and closed-loop recovery when cataloging agent reliability methods.

---

## 4. Peer-Review Lessons & Rejection-Risk Matrix

The matrix below synthesizes verified empirical failure triggers across **Conference Norms (ICLR/NeurIPS/ICML)**, **Open-Review Journal Norms (TMLR)**, and **Expected Traditional Journal Norms (ACM CSUR, Springer AIRE, Springer JAAMAS)**, separating documented OpenReview decisions/AE feedback from expected confidential journal standards grounded in publisher policies.

| Failure Category | Verified Conference Norms (ICLR / NeurIPS / ICML) | Verified TMLR Journal Norms (Claims–Evidence & Survey Certification) | Expected Traditional Journal Norms (ACM CSUR / AIRE / JAAMAS) *(Inferred from Editorial Policies; Confidential Rejections Inaccessible)* | Mitigation Protocol for Our Systematic Review |
| :--- | :--- | :--- | :--- | :--- |
| **1. Novelty / Overlap** | **Major rejection trigger:** Standard prompting wrappers or applying existing agent templates to new domains are rejected as incremental engineering (*LLM-Deliberation*, *SCALE*). | **Explicitly NOT a rejection criterion:** TMLR forbids rejecting purely for lack of novelty or SOTA, *except* for surveys where scope fails to separate from overlapping paradigms (*Self-Evolving Agents* initially flagged for overlapping Continual/Lifelong Learning & basic SFT/RL). | **High survey overlap sensitivity (CSUR/AIRE):** Survey journals reject reviews that duplicate existing recent LLM-agent surveys without a distinct organizing lens, broader temporal span, or deeper theoretical synthesis. | Differentiate our review explicitly from existing single-agent/domain surveys (e.g., Data Science Agents, Game Agents, Self-Evolving Agents, Harness Engineering) via a unified MAS/Swarm architectural, protocol, and failure-mode synthesis. |
| **2. Methodology / Protocol** | **High scrutiny on authentic MAS mechanics:** Reviewers reject papers claiming human-AI coordination using only BC proxies (*Evaluating Multi-Agent Coordination*) or domain integration reduced to prompt phrasing (*SCALE*). | **Strict design–claim alignment:** *Inducing Disagreement* (Sub 7253) rejected because context-isolated parallel sampling could not substantiate claims about interactive multi-agent deliberation; *Generalist Game Agents* forced to fix Eq. 2 POMDP edge cases. | **PRISMA & reproducibility rigor:** CSUR/AIRE/JAAMAS require transparent search strings, inclusion/exclusion rules, deduplication counts, screening criteria, and formal MAS/distributed-AI conceptual fidelity (*Miss the Multi-agent Mark*). | Publish full search query strings, date cutoffs, inclusion/exclusion criteria, screening flow counts, and separate genuine asynchronous MAS protocols from sequential LLM prompt chains. |
| **3. Evaluation / Baselines** | **Compute & baseline rigor:** Omitting single-prompt/ML baselines (*SCALE*) or contemporary LLM baselines in favor of classical RL (*Evaluating Multi-Agent Coordination*), or ignoring cost/latency trade-offs (*CoELA*, *SCALE*). | **Hard Criterion 1 gate:** *AgenticNet* (Paper 7332) rejected after rebuttal `"strict exact-match"` re-runs shifted MBPP 100%→77.5% and cost-matched comparisons showed it trailed simpler baselines (*MultiPersona*, *LLM-Debate*, *LLM-Blender*). *Inducing Disagreement* rejected for measuring disagreement rate without outcome quality. | **Critical appraisal of primary studies:** Traditional surveys are downgraded if they uncritically report primary-paper accuracy tables without auditing cost-matched compute fairness, prompt sensitivity, seed variance, or failure modes. | Audit primary frameworks on **token/API cost-matched baselines**, **benchmark contamination/template bias**, and **process vs. outcome metrics**; never aggregate incompatible scores into misleading leaderboards. |
| **4. Literature Coverage** | **Fast-moving baseline currency:** Expect coverage of concurrent ICLR/NeurIPS frameworks (e.g., ReAct, MetaGPT, AgentVerse, AFlow, MacNet, MAST) and realistic benchmarks beyond toy grids. | **Survey Certification threshold:** *Generalist Game Agents* required strict curation-window documentation through early 2026 and inclusion boundary justification; *Dynamic Agent Skills* unified 124 papers (2023–2026) under an explicit operator schema. | **Historical + cross-disciplinary depth:** JAAMAS and CSUR expect bridging **classical MAS theory** (Wooldridge, distributed AI, game theory, swarm coordination, BDI) with **modern 2023–2026 LLM-MAS & Swarm systems**. | Explicitly link classical MAS/Swarm foundations (autonomy, social protocols, decentralized coordination, emergence) with 2023–2026 LLM-MAS architectures and open-source/preprint ecosystems. |
| **5. Scope / Clarity** | **Readability & diagnostic utility:** *AgentBench* criticized for lacking actionable diagnostic takeaways and using overloaded/imprecise MAS terms; rushed presentation hurts borderline scores. | **Desk-reject & notation gate:** *Evaluating World Models* **desk-rejected** by AE for high grammar errors and undefined jargon; *Generalist Game Agents* required renaming `L1–L5` roadmap steps to `S1–S5`; *Social Agents* required clean placement + Broader Impact section. | **Pedagogical clarity & visual taxonomy:** CSUR/AIRE expect a crystal-clear non-overlapping taxonomy, consistent notation, concise comparative tables, and zero undefined buzzwords ("agentic", "swarm", "harness"). | Enforce a single non-overlapping taxonomic vocabulary (decoupling *architecture*, *coordination topology*, *communication protocol*, and *verification/safety*), define all terms upfront, and include a Broader Impact/Governance section. |
| **6. Overclaiming / Integrity** | **Skepticism of "emergence" & SOTA hype:** *AgentVerse* and *Emergent Coordination* reviews/literature probe whether "emergence" is merely prompt-engineered artifact or model-scale noise; safety alignment confounders flagged in *LLM-Deliberation*. | **Zero tolerance for claim–evidence mismatch:** *AgenticNet* rejected when "consistently outperforms" claims contradicted Table 1 & Table 2 ablations; *Self-Evolving Agents* required explicit caveats on lack of quantitative synthesis and expanded safety/goal-drift analysis. | **Conservative, calibrated synthesis:** Traditional journals enforce strict separation between **peer-reviewed archival evidence** and **unreviewed preprints/withdrawn drafts**, plus rigorous ethical/risk analysis (collusion, cascading failure, misalignment). | Audit every section for **claims–evidence parity**; separate peer-reviewed conference/journal results from arXiv preprints and withdrawn submissions (`3hXEPbG0dh`, ICLR withdrawals); and anchor failure/risk sections in verified taxonomies (*MAST*, *AgentErrorTaxonomy*, *Diversity Collapse*). |

---

## 5. Actionable Pre-Submission Checklist for Our Systematic Review

Drawn directly from the 31 verified OpenReview records (14 TMLR journal, 17 conference/workshop) above:

1. **Enforce Claims–Evidence Parity (TMLR Criterion 1 Gate):** Verify that every summary statement in our Abstract, Introduction, and Discussion strictly matches the quantitative tables and primary evidence—never use "consistently outperforms" or sweeping superiority generalizations where benchmarks diverge (*AgenticNet* lesson).
2. **Audit Compute-Matched & Single-Agent Baselines:** When comparing MAS frameworks in our synthesis tables, add explicit columns noting whether primary papers evaluated **token/API cost-matched single-agent baselines** (CoT, Self-Consistency, ReAct) and whether improvements persist under equalized compute (*AgenticNet*, *SCALE*, *CoELA*, *MAST* lessons).
3. **Separate True MAS from Prompt Chains:** Adopt the diagnostic lens of *Large Language Models Miss the Multi-agent Mark* (`FfsxgSZW0c`) and *Inducing Disagreement* (Sub 7253) to distinguish true decentralized/interactive MAS from sequential prompt chaining or isolated parallel sampling.
4. **Prevent Overloaded Notation & Undefined Jargon:** Establish a formal taxonomy table early, ensure distinct labels across taxonomic axes (`S1–S5` vs. `L1–L5` lesson from *Generalist Game Agents*), and eliminate undefined buzzwords and prose defects (*Evaluating World Models* desk-rejection lesson).
5. **Document Exact Screening & Temporal Boundaries:** Explicitly report database queries, cutoff dates (through 2026), inclusion/exclusion rules, and **explicitly tag publication status** (Journal vs. Conference/Workshop vs. Preprint vs. Withdrawn) so withdrawn submissions like `3hXEPbG0dh` are never misrepresented as peer-reviewed journal findings.
6. **Integrate Safety, Failure Attribution, and Broader Impact:** Dedicate rigorous subsections to structural failure modes (*MAST*, *AgentDebug*, *AgenTracer*), endogenous consensus collapse (*When Consensus Is Not Correctness*), autonomy/self-modification sandboxing (*Self-Evolving Agents*), and Broader Impact (*Social Agents* TMLR requirement).
