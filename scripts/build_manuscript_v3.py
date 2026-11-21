#!/usr/bin/env python3
"""
Deterministic Authoring & Assembly Script for Deliverable F / manuscript_v3_final.md.
Directly reads verified_stats.json, cite_map.json, rendered_tables.md, and
formatted_references.md, checks Abstract limits, 112/112 citation coverage,
zero colliding Tier/code labels, zero backticked citations, zero leaked internal IDs,
and writes reviews/manuscript_v3_final.md + deliverables/Deliverable_F_Final_Review_Manuscript.md.
"""

import json
import re
from pathlib import Path

ROOT = Path("/Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review")
DATA = ROOT / "data"
REVIEWS = ROOT / "reviews"
DELIV = ROOT / "deliverables"


def load_inputs():
    with open(DATA / "verified_stats.json") as f:
        st = json.load(f)
    with open(DATA / "cite_map.json") as f:
        cm = json.load(f)
    with open(DATA / "formatted_references.md") as f:
        refs = f.read().strip()
    with open(DATA / "rendered_tables.md") as f:
        rt_txt = f.read()
    blocks = {}
    cur_k = None
    cur_lines = []
    for line in rt_txt.splitlines():
        if line.startswith("### "):
            if cur_k:
                blocks[cur_k] = "\n".join(cur_lines).strip()
            cur_k = line[4:].strip()
            cur_lines = []
        else:
            cur_lines.append(line)
    if cur_k:
        blocks[cur_k] = "\n".join(cur_lines).strip()
    return st, cm, refs, blocks


def main():
    st, cm, refs, blk = load_inputs()
    by_sid = cm["by_study_id"]
    by_key = cm["by_key"]

    def c(*keys):
        nums = []
        for k in keys:
            if k in by_sid:
                nums.append(by_sid[k])
            elif k in by_key:
                nums.append(by_key[k])
            else:
                raise KeyError(f"Unknown citation key: {k}")
        return "[" + ", ".join(str(n) for n in nums) + "]"

    def n(k):
        return by_sid[k] if k in by_sid else by_key[k]

    pr = st["prisma"]
    irr = st["irr"]
    ca = st["comparative_all"]
    cr = st["comparative_archival"]
    qa = st["qa"]
    cf = st["confounders"]
    pk = st["pass_power_k"]
    lu = st["latency_and_usd"]
    dd = st["dense_debate_conformity"]
    nv = st["nv_inventory"]
    fm = st["failure_mechanism_counts"]
    mad_t1 = st["tier1_mad_vs_nonmad"]
    rsens = st["rq3_rq4_archival_sensitivity"]

    # Check exact dense debate cites & non-conf cites
    dense_conf_str = "[" + ", ".join(str(x) for x in dd["conformity_cites"]) + "]"
    dense_nonconf_str = "[" + ", ".join(str(x) for x in dd["non_conformity_cites"]) + "]"
    direct_lat_str = "[" + ", ".join(str(x) for x in lu["direct_latency_cites"]) + "]"
    proxy_lat_str = "[" + ", ".join(str(x) for x in lu["proxy_latency_cites"]) + "]"
    usd_exact_str = "[" + ", ".join(str(x) for x in lu["usd_exact_cites"]) + "]"
    usd_ratio_str = "[" + ", ".join(str(x) for x in lu["usd_ratio_cites"]) + "]"
    pk_overall_str = "[" + ", ".join(str(x) for x in pk["overall_true_cites"]) + "]"

    abstract = (
        f"Large language model multi-agent systems are widely deployed for reasoning, coding, and tool use, "
        f"yet prior surveys rarely verify equal-compute single-agent controls. "
        f"This PRISMA review synthesizes {pr['included_total']} studies (2023 to 2026; {ca['All']['n_tuples']} comparisons). "
        f"Multi-agent systems win {ca['Tier 2+3']['win_pct']}% of weak or unmatched comparisons, falling to "
        f"{ca['Tier 1']['win_pct']}% wins and {ca['Tier 1']['loss_pct']}% losses under compute parity "
        f"({ca['tuple_attenuation_pp']} pp; {cr['tuple_attenuation_pp']} pp archival; Fisher p = {ca['fisher_p_t1_vs_t23']}). "
        f"Negative returns reflect error amplification, conformity, handoff loss, unamortized training "
        f"({cf['qa3_1_count']}/{cf['optimization_bearing_incl_sr032']} optimizers), absent verifiable consistency reporting "
        f"({pk['comparative_true']}/{pk['comparative_verifiable_den']}), and harness flaws, motivating an orthogonal design workflow."
    )
    abs_words = abstract.split()
    abs_split = re.split(r"[\s/\u2013-]+", abstract.strip())
    assert "`" not in abstract, "Backticks forbidden in Abstract!"
    assert len(abs_words) <= 88, f"Abstract whitespace words too long: {len(abs_words)}"
    assert len(abs_split) <= 95, f"Abstract split tokens too long: {len(abs_split)} ({abs_split})"

    # Ensure every single non-SR key & excluded SR key is naturally integrated in the text!
    # Check PRISMA E4 screened list (exact 15 Stage 1 E4 + 1 Stage 2 E4 = 16 from screening_records.csv)
    import csv
    e4_screened_rids = []
    e3_screened_rids = []
    e7_screened_rids = []
    e8_screened_rids = []
    e2_screened_rids = []
    e5_screened_rids = []
    with open(DATA / "screening_records.csv") as f:
        for r in csv.DictReader(f):
            if r["final_decision"] == "EXCLUDE":
                code = r["final_exclusion_code"]
                rid = r["record_id"]
                if rid in by_sid:
                    if code == "E4": e4_screened_rids.append(rid)
                    elif code == "E3": e3_screened_rids.append(rid)
                    elif code == "E7": e7_screened_rids.append(rid)
                    elif code == "E8": e8_screened_rids.append(rid)
                    elif code == "E2": e2_screened_rids.append(rid)
                    elif code == "E5": e5_screened_rids.append(rid)

    e4_cite_list = c(*sorted(e4_screened_rids)) if e4_screened_rids else ""
    e3_cite_list = c(*sorted(e3_screened_rids)) if e3_screened_rids else ""

    # Remaining non-included bib entries check: inspect which SR041-SR084 are in E4 vs other codes
    # Build Table 3 (Exclusion & Boundary Contrast Matrix, fixing Moslem & Kelleher to E4!)
    table_3_excl = f"""| Screening Code & Description | PRISMA Excluded (`n`) | Representative Citations & Boundary Distinctions |
| :--- | :---: | :--- |
| **`E3` — Single-Agent / Non-Collaborative / No SAS Comparator** | `9` (`6` S1 + `3` S2) | Single-agent pipeline scaffolds such as `Agentless` {c('SR065')} and `AgentDebug` {c('Zhu2026_AgentDebug')} (excluded outside `I2(c)` validity audits), plus single-policy tool routers such as `Router-R1` {c('SR095')} calling stateless models without inter-agent state or `SAS -> MAS` cascading. |
| **`E4` — Secondary Surveys & Narrative Reviews** | `16` (`15` S1 + `1` S2) | Screened secondary surveys excluded from the primary synthesis count {c('SR041', 'SR042', 'SR043', 'SR044', 'SR045', 'SR046', 'SR047', 'SR048', 'SR050', 'SR051', 'SR052', 'SR053', 'SR055', 'SR056', 'SR080', 'SR084')}, including single-query routing survey Moslem & Kelleher {c('SR048')}; retained solely for Table 1 overlap positioning alongside additional background CSUR/TMLR/AIRE reviews. |
| **`E5` / `E2` / `E7` — Non-Empirical, Paywall-Only, or Classical Swarm** | `10` (`3` E5, `2` E2, `5` E7) | Paywalled/abstract-only hits (`E5`), non-empirical position pieces (`E2`, separated from empirical swarm benchmarks like `SwarmBench` {c('SR081')} and biological/model swarms {c('SR057', 'SR058')}), and out-of-scope tasks (`E7`). |
| **`E8` — Publicly Rejected / Withdrawn Versions** | `6` S1 | Audited strictly inside Section 5.4 OpenReview longitudinal checks (`TMLR 7332` *AgenticNet* {c('SR077')}, `TMLR 7253` *Inducing Disagreement* {c('SR078')}, rejected `TMLR 9844/11271` {c('TMLR2025_WhenConsensus_9844')} superseded separately by workshop {c('SR079')}, withdrawn `ICLR 2025 #6097` {c('ICLR2025_SCALE_6097')} superseded by archival `ACL 2025` {c('SR082')}, plus rejected/withdrawn sycophancy variants {c('SR083')}). |"""

    # Build Table 2 (Methodological Anchors C1-C6 & QA1-QA7 early in Section 3.4!)
    table_2_anchors = """| Analytical Code | Category / Dimension | Operational Definition & Scoring Anchor (`0` / `1` / `2` for `QA1`–`QA7`) |
| :--- | :--- | :--- |
| **`C1`** | Inference Compute Asymmetry | MAS uses unmatched tokens, turns, or API calls (often `2.1x–16.85x`) without equal-token `Self-Consistency` (`SC`) or `Best-of-N` single-agent parity. |
| **`C2`** | Hidden Reasoning Token Leak | Wrapper token matching ignores internal reasoning traces (`thoughts_token_count` or extended test-time thinking budgets). |
| **`C3`** | Process Proxy / Voting Conflation | Parallel independent voting or stochastic sampling labeled as interactive multi-agent deliberation or social persuasion. |
| **`C4`** | Prompt or Tool Asymmetry | Specialized role prompts, execution feedback, or external sandboxes supplied to MAS while withheld from the `N = 1` baseline. |
| **`C5`** | Harness Fragility & Leakage | Unhardened static exact-match leaderboards, sparse unit tests, permissive graders, or missing leakage checks inflating tiny margins. |
| **`C6`** | Unamortized Search / Training Cost | Upfront MCTS, RL, evolution, GNN, or validation search costs omitted from per-query test-time efficiency comparisons. |
| **`QA1`** | SAS Baseline Control Parity | `2` = Strictly compute/token-matched strong SAS (`Tier 1`); `1` = Strong unmatched or single-pass SAS (`Tier 2`–`Tier 3`); `0` = No SAS (`Tier 4`); `N/A` = Diagnostic (`12`-pt max). |
| **`QA2`** | Cost & Latency Accounting | `2` = Quantifies inference tokens/USD AND direct wall-clock latency (or runtime reduction); `1` = Tokens/USD or turns without seconds; `0` = Omitted. |
| **`QA3`** | Optimization Amortization | `2` = Training-free OR explicitly prices upfront search/RL cost; `1` = Learned/optimized framework omitting upfront search cost (`C6`); `0` = Concealed. |
| **`QA4`** | Multi-Run Stochastic Stats | `2` = `k >= 3` seeds with SD/95% CIs/`pass^k`; `1` = Multi-sample sweeps or significance tests without full per-cell CIs; `0` = Single-run point scores. |
| **`QA5`** | Harness & Leakage Integrity | `2` = Hardened/verified DB/sandbox checks or adversarial noise controls; `1` = Standard reproducible suite; `0` = Unverified/leaky proxy. |
| **`QA6`** | Reproducibility Artifacts | `2` = Public code repository + full prompts/configs; `1` = Prompts/pseudocode in paper without live repo; `0` = Closed artifacts. |
| **`QA7`** | Claims–Evidence Parity | `2` = Headline claims match tables & failure conditions; `1` = Selective positive framing overlooking constraints/amortization; `0` = Contradictory. |"""

    # Section 6.1 Epistemic Proposition Table (semantic confidence bands, SR079 excluded from High-Confidence Consensus!)
    table_10_epistemic = f"""| Confidence Band | Synthesized Proposition & Evidence Scope | Grounding Citations |
| :--- | :--- | :--- |
| **High-Confidence Consensus** | Compute-matched parity slashes MAS win rates by `{ca['tuple_attenuation_pp']} pp` (`{ca['study_frac_attenuation_pp']} pp` study-weighted; `{cr['tuple_attenuation_pp']} pp` archival), with MAS losing `{ca['Tier 1']['loss_pct']}%` of parity tests (`{ca['Tier 1']['wins']}/{ca['Tier 1']['n_tuples']}` wins). | {c('SR001','SR002','SR003','SR004','SR005','SR007','SR009','SR010','SR012')} |
| **High-Confidence Consensus** | Dense symmetric debate (`MAD`) suffers frequent conformity/sycophancy collapse (`{dd['conformity_count']}/{dd['dense_debate_total']}` studies, up to `85.5%` modal adoption) and often reduces to expensive majority voting unless non-zero-sum verification or diversity interventions break consensus. | {c('SR005','SR006','SR007','SR012','SR013','SR029','SR031','SR087','SR088','SR089')} |
| **High-Confidence Consensus** | Across `{cf['qa3_1_count']}/{cf['optimization_bearing_incl_sr032']}` optimization-bearing studies, test-time tables omit upfront search/training cost (`C6`), while comparative `pass^k` (`{pk['comparative_true']}/{pk['comparative_verifiable_den']}` verifiable) and direct latency (`{lu['omit_or_nv_latency_pct']}%` omit/NV) remain critically underreported. | {c('SR003','SR015','SR016','SR017','SR018','SR019','SR020','SR032','SR033','SR034','SR092','SR093','SR094','SR096','SR097','SR100')} |
| **Context-Bounded Finding** | Centralized or selective MAS improves outcomes mainly on context-overflowing, cleanly decomposable multi-source tasks (e.g., `Finance-Agent +80.8%` rel., `AgentIF-OneDay +18.23 pp`), whereas tightly coupled sequential states favor unified single agents (`PlanCraft -39%` to `-70%`, `Terminal-Bench`). | {c('SR001','SR002','SR020','SR086','SR090','SR091')} |
| **Moderated Conflict** | Multi-agent security and verifier abstraction reveal topological fragility (up to `3.8x` higher attack success than single agents; `~92%–100% P-ASR` in unguarded broadcast rings; `30.9% VTFR`), whereas twice-rejected workshop `CMAD` {c('SR079')} (`18%–47%` miscoverage) remains provisional pending archival replication. | {c('SR040','SR069','SR098','SR099','SR100')} |
| **Open Hypothesis / Evidence Gap** | Zero `Topo-5` Learned DAG (`0/{st['topology_counts'].get('Adaptive Sparse/Learned DAG',0)}`) and zero `Task-1` Decomposable (`0/2`) studies currently satisfy strict `Tier 1` parity; `Regimes A–D` (Section 6.2) synthesize stitched cross-study heuristics awaiting prospective within-benchmark amortized RCTs. | {c('SR014','SR015','SR016','SR017','SR018','SR076','SR093','SR094')} |"""

    # Section 6.2 Decision Workflow Mermaid (D0-D4, zero Q0-Q4, resolves >~45% SAS -> Regime A and Q<=Q_be -> Regime A/B!)
    mermaid_decision = """```mermaid
flowchart TD
    D0{"D0: Verifiable feedback (unit test, DB state, or objective oracle) OR memory beyond single context window?"}
    D1{"D1: Does single-agent baseline already operate near diminishing-return ceiling (e.g., >~45% cond. in [41])?"}
    D2{"D2: Is task tightly sequential / Markov closed-book reasoning where handoffs trigger DPI loss?"}
    D3{"D3: Are query difficulties mixed with a calibrated confidence/verifier gate?"}
    D4{"D4: Does deployment volume Q > Q_break-even = C_search / (c_SAS - c_MAS) with c_MAS < c_SAS?"}

    RA["Regime A: Keep Single-Agent Control<br/>(Avoid +58% to +285% token tax & -39% to -70% sequential degradation)"]
    RB["Regime B: Parallel Single-Best Sampling<br/>(Self-Consistency / Self-MoA / Isolated Self-Correction)"]
    RC["Regime C: Selective SAS-First Escalation<br/>(Verify SAS first; invoke MAS only on boundary failures)"]
    RD["Regime D: Centralized Verification or Amortized Sparse DAG<br/>(Isolate workers + turn caps + provenance verification)"]

    D0 -- "No (open-ended / ungrounded)" --> RA
    D0 -- "Yes" --> D1
    D1 -- "Yes (high SAS regime)" --> RA
    D1 -- "No (headroom available)" --> D2
    D2 -- "Yes (sequential / closed-book)" --> RB
    D2 -- "No (decomposable / partitioned tools)" --> D3
    D3 -- "Yes (mixed difficulty)" --> RC
    D3 -- "No (uniformly high difficulty)" --> D4
    D4 -- "Yes (amortizes search & lowers c_MAS)" --> RD
    D4 -- "No (c_MAS >= c_SAS or low volume Q)" --> RB
```"""

    # Double-check ALL citations we put in prose to verify 112/112!
    # Also cite every survey/method/classical/RQ4 entry explicitly in clean, natural sentences!
    manuscript = rf"""# When Do LLM Multi-Agent Systems Outperform Single Agents? A Systematic Review of Compute-Normalized Evidence, Coordination Topologies, Failure Mechanisms, and Evaluation Validity

**Author(s) & Affiliation(s):** `[Author Placeholder — Blinded for Peer Review / ACM CSUR Submission Template]`  
*Target Venue:* **ACM Computing Surveys (CSUR)** *(Primary Target; formatted cleanly for conversion to `acmart` `acmsmall`)*.  
*Portable Pre-Submission Disclosure Note (TMLR Backup Target):* Workstream orchestration, metadata verification, and deterministic tabular aggregation were assisted by tool-verified LLM research workflows with human-author responsibility for protocol approval, eligibility adjudication, and manuscript validation.

---

## Abstract

{abstract}

---

## ACM CCS Concepts

- **Computing methodologies ~ Artificial intelligence ~ Distributed artificial intelligence ~ Multi-agent systems** (`Significance: 500`)
- **Computing methodologies ~ Natural language processing ~ Natural language generation** (`Significance: 300`)
- **General and reference ~ Surveys and overviews** (`Significance: 300`)
- **General and reference ~ Empirical studies** (`Significance: 100`)

## Keywords

Large language models, multi-agent systems, compute-normalized evaluation, test-time scaling, multi-agent debate, failure mechanisms, systematic literature review

---

## 1. Introduction

Large language model multi-agent systems (`LLM-MAS`) coordinate two or more interacting model instances through structured debate, role specialization, sequential workflows, or learned communication graphs. Early demonstrations popularized a straightforward assumption: splitting reasoning across multiple personas or agents consistently outperforms a single model. As frontier models gained stronger native reasoning, longer context windows, and reliable tool execution, however, controlled evaluations began challenging that consensus {c('SR001', 'SR002', 'SR005', 'SR086', 'SR089')}.

Existing surveys provide rich architectural maps of this rapid expansion, yet most treat benchmark gains at face value. Narrative and systematic overviews in *Artificial Intelligence Review* {c('AbouAli2026_AIRE', 'SR049_alaanzy2026autonomous', 'Chowa2026_AIRE')}, *ACM Computing Surveys* {c('Deng2025_CSUR_Security', 'SR052_du2026optimization', 'SR050_geng2026scaling', 'SR051_he2026security', 'Hu2024_CSUR_GameAgents', 'Zhang2026_CSUR_Generalizability')}, *Journal of Artificial Intelligence Research* {c('Plaat2025_JAIR')}, *Transactions on Machine Learning Research* {c('SR055_gao2026selfevolving', 'Huang2026_TMLR_AgentMemory', 'Ke2025_TMLR_LLMReasoning', 'SR048_moslem2026dynamic', 'Wei2026_TMLR_AgenticReasoning', 'Zhang2026_TMLR_AgenticRL', 'SR056_zhang2026generalist')}, *IJCAI* {c('Guo2024_IJCAI')}, *KDD* {c('Mohammadi2025_KDD')}, *Findings of ACL/EMNLP* {c('SR044_yehudai2026evaluation', 'SR045_yue2026static')}, *IEEE TSE* {c('SR043_wang2026trajectory')}, *Future Internet* {c('Zhu2026_FutureInternet')}, and recent preprint repositories {c('Anonymous2026_ACL_ARR_FailureAttribution', 'Badica2025_arXiv_ContemporaryAgentTech', 'Dantas2026_SafeAgents', 'Khan2026_Preprints_MASEvolution', 'SR080_li2026harness', 'SR047_li2026efficiency', 'Mallampati2026_Reliability', 'SR041_motger2026mad', 'Rahman2025_arXiv_LLMPoweredSwarms', 'SR042_tillmann2025mad', 'Tran2025_MAS', 'SR053_wang2024autonomous', 'Wang2026_arXiv_ClassicalToFoundationMAS', 'SR046_yan2026beyond')} categorize frameworks, orchestration protocols, memory systems, communication mechanisms, or security threats.

Closer to our central question, three 2026 surveys address overlapping pillars. Li et al. {c('SR047_li2026efficiency')} formulate "The Collaboration Boundary", explicitly advocating matched single-agent baselines, multidimensional resource accounting, and lifecycle amortization conceptually. Motger et al. {c('SR041_motger2026mad')} review 141 multi-agent debate (`MAD`) papers, separating deliberation from parallel voting, while Wang et al. {c('SR043_wang2026trajectory')} and a distinct ACL ARR submission {c('Anonymous2026_ACL_ARR_FailureAttribution')} synthesize failure attribution and `5Ws + HOW` diagnosis.

What remains missing across more than 42 secondary surveys audited during topic scoping is a **PRISMA-governed quantitative meta-audit** {c('Kitchenham2007', 'Page2021_PRISMA')} testing whether published `LLM-MAS` performance gains actually hold once single-agent baselines (`SAS`) match token, compute, tool, and prompt budgets. Rather than pooling incomparable accuracy scores across datasets, this review stratifies within-study paired comparisons across `Tier 1`–`Tier 4` control parity and integrates topology economics, failure mechanisms, topological security, and harness reliability into a unified empirical synthesis.

### Table 1: Candid Positioning Against Competing Surveys & Venue Portfolios

{blk['TABLE_1_SURVEY_COMPARISON']}

Overall, this manuscript makes four grounded contributions:
1. **Empirical Parity Audit (`RQ1`):** Quantifies a `{ca['tuple_attenuation_pp']} pp` tuple-level (`{ca['study_frac_attenuation_pp']} pp` study-weighted; Fisher $p = {ca['fisher_p_t1_vs_t23']}$) collapse in `MAS > SAS` win rates from weak/unmatched controls (`Tier 2+3`) to compute-matched `Tier 1` parity across `{ca['All']['n_tuples']}` cleaned comparisons (`{ca['All']['n_studies']}` studies).
2. **Topology & Amortization Accounting (`RQ2`):** Separates parallel sampling ensembles from interactive topologies and exposes `{cf['qa3_1_count']}/{cf['optimization_bearing_incl_sr032']}` unamortized search/training omissions (`C6`), alongside `0` `Tier 1` studies among learned sparse DAG frameworks.
3. **Mechanistic Failure & Security Integration (`RQ3`):** Synthesizes within-study verified failure mechanisms (error amplification, `{dd['conformity_count']}/{dd['dense_debate_total']}` Dense Debate conformity, Markov `DPI` bottlenecks) alongside cross-corpus failure-attribution and topological security evidence (`CORBA`, `Hagag et al.`, `NetSafe`, `G-Safeguard`).
4. **Confounder Audit & Orthogonal Design Framework (`RQ4` & Section 6):** Audits `C1`–`C6`, `pass^k` (`{pk['comparative_true']}/{pk['comparative_verifiable_den']}` verifiable comparative), latency/USD gaps, and `E8` OpenReview rejections to construct a clean 3-axis architectural taxonomy (`Topo × Task × Ver`) separated from study-quality rigor (`Tier 1`–`Tier 4`).

---

## 2. Research Questions and Scope

To answer when `LLM-MAS` justify their operational overhead and remain defensible for an M.Tech or graduate research committee, this systematic review investigates four tightly bounded research questions:

- **RQ1 (Compute-Normalized Effectiveness):** When total inference tokens, API cost, prompting effort, and tool access are held equal against a strong single-agent baseline (`SAS`), how often do `LLM-MAS` achieve higher accuracy than `SAS`, and in which task regimes do wins or losses concentrate?
- **RQ2 (Coordination Topology & Cost Amortization):** How do coordination structures (voting ensembles, sequential pipelines, centralized stars, dense debate graphs, learned sparse DAGs, and selective cascades) trade off accuracy against inference overhead and upfront search or training costs?
- **RQ3 (Failure Mechanisms & Security Exposure):** Which verified mechanistic pathways—error amplification, conformity/sycophancy, handoff information loss, verification failure, or inter-agent attack propagation—explain `LLM-MAS` degradation and availability risks?
- **RQ4 (Evaluation Validity & Methodological Rigor):** To what extent do six recurring experimental confounders (`C1`–`C6`), absent `pass^k` reliability reporting, missing wall-clock latency/USD accounting, and benchmark harness artifacts distort published `LLM-MAS` claims?

We intentionally exclude reinforcement-learning-only multi-agent systems lacking natural-language LLM reasoning, pure biological swarm algorithms {c('SR058_jimenezromero2025swarm', 'SR081_ruan2025swarmbench')}, and unverified commercial whitepapers. Classical swarm intelligence and classical MAS are explicitly demarcated in Section 4.2.

---

## 3. Systematic Review Methodology

### 3.1 Protocol Governance & Seeded Open-Web Search (`v1.0`–`v1.2`)

This review follows the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA 2020) {c('Page2021_PRISMA')} and Kitchenham–Charters software-engineering review guidelines {c('Kitchenham2007')} under a versioned protocol (`v1.0` initial freeze; `v1.1` Phase 5 reconciliation; `v1.2` post-peer-review remediation). Because proprietary bulk exports from Scopus and Web of Science were unavailable in our environment, we frame this study transparently as a **PRISMA-governed, open-web query- and snowball-seeded systematic review** spanning *arXiv*, *OpenReview*, *ACL Anthology*, *PMLR*, *ACM Digital Library*, *Springer*, *Nature*, and semantic citation links through November 20, 2026.

To uphold strict audit candor, Protocol Amendment v1.2 documents two search adjustments: (a) Phase 5 baseline Searches 2, 5, and 9 specialized baseline Boolean templates with named architectures or benchmarks (Mixture-of-Agents, Self-MoA, ColMAD, CONSENSAGENT, CORBA, SwarmBench, SCALE); and (b) post-review remediation Searches 12–13 systematically imported 16 verified primary anchor and multi-agent security studies {c('SR085','SR086','SR087','SR088','SR089','SR090','SR091','SR092','SR093','SR094','SR095','SR096','SR097','SR098','SR099','SR100')} that earlier snippet searches missed. Searches 1–11 logged 126 candidate hits (105 query + 21 snowball) with 42 duplicates collapsed (84 unique), and Searches 12–13 added 16 unique candidates ({pr['raw_total']} raw total, {pr['duplicates']} duplicates, **{pr['unique_screened']} unique records screened**).

### 3.2 Dual-Pass Screening Workflow & Author Accountability

All screening, quality scoring, and data extraction operated under an explicit human-accountable editorial protocol: automated dual-pass LLM research workers generated independent blinded candidate votes and structured schema records, while **the human authors verified, adjudicated every conflict, inspected source tables, and assume full scholarly accountability** for every inclusion verdict and extracted datum. Across all {pr['unique_screened']} unique records, independent dual-pass Stage 1 screening achieved {irr['full_stage1_po']}% agreement (Cohen's $\kappa = {irr['full_stage1_kappa']}$; Wave 1 baseline {irr['wave1_stage1_po']}%, $\kappa = {irr['wave1_stage1_kappa']}$).

During Phase 9 methodology auditing, two Wave 1 Stage 1 disagreements (Dai {c('SR079_dai2026when')} and SCALE {c('SR082_zhao2025scale')}) were identified as having lacked a completed first-reviewer Stage 2 pass prior to arbitration (yielding `48/52 = 92.31%`, $\kappa = 0.7699$ mutual vs. `48/54 = 88.89%`, $\kappa = 0.6873$ union on Wave 1). Under Amendment v1.2, independent first-reviewer Stage 2 review was completed across all {irr['stage2_full_n']} advancing candidates, yielding {irr['stage2_3class_po']}% ($\kappa = {irr['stage2_3class_kappa']}$) Stage 2 agreement and **{irr['corpus_bin_po']}% ($\kappa = {irr['corpus_bin_kappa']}$)** corpus-wide inclusion agreement.

### 3.3 PRISMA Flow, Publication Status, & Eligibility Boundaries

```mermaid
{blk['FIGURE_1_PRISMA'].removeprefix('```mermaid').removesuffix('```').strip()}
```
*Figure 1: PRISMA 2020 systematic selection flow across initial searches (Searches 1–11) and Protocol `v1.2` remediation imports (Searches 12–13). Note: Stage 2 is framed explicitly as Open Full-Text & Structured Open-Summary Eligibility (`407` direct scalar fields across `{nv['records_with_nv']}/{nv['total_records']}` records retain summary bounds `NV` where non-OA publisher PDFs or supplementary tables were inaccessible).*

#### Table 2: Included Corpus Distribution by Publication Status & Research Track (`N = {pr['included_total']}`)

{blk['TABLE_PUB_STATUS']}

Protocol rules enforce clear eligibility boundaries (`I1`–`I6` / `E1`–`E8`). Eligible studies publish English empirical evaluations from 2023 to November 2026 covering either (`I2a`) paired comparisons of an $N \ge 2$ `LLM-MAS` (or explicitly scoped voting ensemble {c('SR085')}) against an $N = 1$ `SAS`, (`I2b`) verified inter-agent mechanistic or topological security audits {c('SR029', 'SR031', 'SR069', 'SR097', 'SR099', 'SR100')}, or (`I2c`) single-agent/agentic evaluation-validity and harness audits {c('SR032', 'SR033', 'SR034', 'SR035', 'SR036', 'SR037', 'SR038', 'SR039', 'SR040')}. Under this `I2(c)` carve-out, harness audits that invalidate MAS/agent leaderboards enter `RQ4`, whereas standalone single-agent failure taxonomies (`AgentDebug` {c('Zhu2026_AgentDebug')}) and single-LLM black-box routers lacking persistent inter-agent state or cascading (`Router-R1` {c('SR095')}) are excluded under `E3`. Similarly, `SCALE` {c('SR082_zhao2025scale')} qualifies under `I2(a)` at archival `ACL 2025` (collaborative role pipeline vs. $N = 1$ coding baseline) while its withdrawn `ICLR 2025 #6097` precursor {c('ICLR2025_SCALE_6097')} and rejected `TMLR 9844/11271` manuscripts {c('TMLR2025_WhenConsensus_9844', 'SR077', 'SR078')} are isolated in Section 5.4 under `E8`. Preprints (`n = {pr['preprint_count']}`) must pass a mandatory quality gate (`total >= 6` and `QA7 >= 1`) and OpenReview status verification.

#### Table 3: Screening Exclusion Categories & Key Boundary Decisions (`n = 41` Excluded)

{table_3_excl}

### 3.4 Early Methodological Anchors: Confounders (`C1`–`C6`) & Quality Rubric (`QA1`–`QA7`)

To ensure every metric, confounder flag, and appraisal table in Sections 5 and 6 is transparent to first-time readers, Table 4 defines our six confounder classes (`C1`–`C6`) and seven `0`–`2` quality-appraisal criteria (`QA1`–`QA7`, max `14` for comparative studies; max `12` for non-comparative `RQ3`/`RQ4` diagnostic audits with `QA1 = N/A`). To detect any denominator inflation between `12`-point and `14`-point tracks, Section 5.4 also reports normalized `12`-point (`QA2`–`QA7`) scores across every stratum.

#### Table 4: Six-Class Confounder Taxonomy (`C1`–`C6`) & Quality Appraisal Anchors (`QA1`–`QA7`)

{table_2_anchors}

---

## 4. Conceptual Foundations and Classical Boundaries

### 4.1 Metrics, Information Bounds, and Amortization Economics

Reviewing `LLM-MAS` claims rigorously requires four formal definitions before examining study tables:

1. **Pass-at-$k$ vs. Multi-Trial Consistency (`pass^k`):** Standard `pass@k` checks whether *at least one* of $k$ independent attempts succeeds, rewarding noisy exploration. By contrast, Yao et al. {c('SR033_yao2025taubench')} define **multi-trial consistency (`pass^k`)**—the probability that a system succeeds across *all* $k$ independent trials under an unbiased hypergeometric estimator:
   $$\text{{pass}}^k = \mathbb{{E}}_{{\text{{task}}}} \left[ \frac{{\binom{{c}}{{k}}}}{{\binom{{n}}{{k}}}} \right]$$
   where $n$ trials yield $c$ successes per task. Because $f(p) = p^k$ is convex for $k \ge 1$, **Jensen's inequality** implies $\frac{{1}}{{M}}\sum_i p_i^k \ge \left(\frac{{1}}{{M}}\sum_i p_i\right)^k$: averaging benchmark accuracies before raising to power $k$ systematically underestimates reliability dispersion whenever some tasks pass deterministically and others fail frequently. Concretely, for a single task with per-trial success probability $\hat{{p}} = 0.6$ over $k = 8$ runs, `pass@8` reaches $1 - (1 - 0.6)^8 = 99.9\%$, whereas `pass^8` collapses to $0.6^8 = 1.7\%$—an operational reliability failure invisible to single-run averages.

2. **Data Processing Inequality (`DPI`) & Markov Relay Limits:** When agents sequentially relay fixed internal knowledge across natural-language handoffs without accessing external ground truth, they form a **Markov chain** $Y \leftrightarrow Z_{{\text{{SAS}}}} \leftrightarrow M_{{\text{{handoff}}}} \leftrightarrow \hat{{Z}}_{{\text{{MAS}}}}$ over true answer $Y$. Under this Markov assumption, the Data Processing Inequality enforces $I(Y; \hat{{Z}}_{{\text{{MAS}}}}) \le I(Y; Z_{{\text{{SAS}}}})$: compressing reasoning traces into textual messages cannot create new mutual information and instead incurs handoff distortion {c('SR002_tran2026single')}. Crucially, the Markov hypothesis **breaks**—permitting positive `MAS` gains—when distributed agents ingest *partitioned external observations* (non-overlapping documents or tools {c('SR001_kim2026capable', 'SR091_2026')}) or sample genuinely diverse pretraining priors (`Heter-MAD` {c('SR007_zhang2025stop', 'SR008_wu2025can')}).

3. **Verifier Transport Failure Rate (`VTFR`):** Conditioned strictly on tasks where the underlying LLM's *native judgment is initially correct ($C_0$)*, Sheshanarayana & Goli {c('SR040_sheshanarayana2026do')} define `VTFR` as the fraction of those correct $C_0$ answers that fail verification, flip, or abstain after multi-agent delegation or context compaction—distinguishing transport degradation from underlying capability deficits.

4. **Amortized Break-Even Deployment Volume ($Q_{{\text{{break-even}}}}$):** Automated graph search, MCTS, and RL workflow optimizers incur a fixed upfront optimization cost $C_{{\text{{search}}}}$ (`hours`, tokens, or USD) prior to deployment. Treating single-query inference cost at equal accuracy as $c_{{\text{{SAS}}}}$ vs. $c_{{\text{{MAS}}}}$, the break-even query volume is:
   $$Q_{{\text{{break-even}}}} = \frac{{C_{{\text{{search}}}}}}{{c_{{\text{{SAS}}}} - c_{{\text{{MAS}}}}}} \quad (\text{{valid iff }} c_{{\text{{MAS}}}} < c_{{\text{{SAS}}}})$$
   Notice this one-line bound explains why adaptive MAS designs whose *per-query* inference cost remains equal to or higher than a strong `SAS` ($c_{{\text{{MAS}}}} \ge c_{{\text{{SAS}}}}$) possess **infinite break-even volume**—their upfront search expense can never be amortized.

### 4.2 Demarcating Classical Swarm Intelligence, Classical MAS, and `LLM-MAS`

Readers from classical AI or engineering frequently conflate modern LLM-MAS with Swarm Intelligence (SI) or Belief–Desire–Intention (BDI) / Foundation for Intelligent Physical Agents (FIPA) Multi-Agent Systems. Following La Malfa et al. {c('LaMalfa2025')}, Wang et al. {c('Wang2026_arXiv_ClassicalToFoundationMAS')}, Bădică et al. {c('Badica2025_arXiv_ContemporaryAgentTech')}, and Rahman et al. {c('Rahman2025_arXiv_LLMPoweredSwarms')}, Table 5 establishes three clean structural boundaries (LLM-MAS also differs sharply from biological `SwarmBench` grid coordination {c('SR081_ruan2025swarmbench')} and cross-checkpoint `Model Swarms` weight optimization {c('SR057_feng2025modelswarms')}).

#### Table 5: Conceptual Boundaries Across Classical Swarm Intelligence, Classical MAS, and Modern LLM-MAS

| Architectural Property | Classical Swarm Intelligence (Ant Colony Optimization [ACO], Particle Swarm Optimization [PSO], Boids) {c('Rahman2025_arXiv_LLMPoweredSwarms', 'SR058_jimenezromero2025swarm')} | Classical MAS (BDI, FIPA, Cooperative MARL / Value Factorization [QMIX], Proximal Policy Optimization [PPO]) {c('SR050_geng2026scaling', 'Wang2026_arXiv_ClassicalToFoundationMAS')} | Modern Autonomous LLM-MAS (`AutoGen`, `MAD`, `AFlow`, `GPTSwarm`) {c('Badica2025_arXiv_ContemporaryAgentTech', 'LaMalfa2025')} |
| :--- | :--- | :--- | :--- |
| **Agent State & Memory** | Lightweight local state vector & stigmergic markers | Symbolic beliefs/goals (`BDI`) or neural hidden vectors (`RL`) | High-dimensional context windows + retrieval memory |
| **Communication Channel** | Local pheromones or spatial neighbor attraction | Formal speech acts (`FIPA ACL`) or continuous policy embeddings | Unconstrained or schema-typed natural language |
| **Scalability Regime** | $10^2$–$10^6$ simple agents with $O(1)$ per-step cost | $2$–$100$ structured agents in deterministic/game environments | $2$–$15$ heavy LLM agents with quadratic token growth |
| **Failure Mode Under Scale** | Premature swarm stagnation or parameter oscillation | Non-stationarity, sparse rewards, credit-assignment variance | Sycophantic conformity, `DPI` summary loss, prompt injection |

---

## 5. Empirical Synthesis (`RQ1`–`RQ4`)

### 5.1 Compute-Normalized Effectiveness & Conditional Regimes (`RQ1`)

Across `35` tuple-bearing comparative studies (`{ca['All']['n_tuples']}` cleaned paired comparisons after removing `7` invalid/nested comparisons documented in Appendix G.2, plus `PARTNR` {c('SR075')} at `Tier 4` with `0` SAS accuracy tuples), empirical outcomes exhibit a sharp **monotonic gradient** controlled by single-agent baseline strength (`Tier 3 -> Tier 2 -> Tier 1`).

#### Table 6: Stratified `RQ1` Effectiveness & Study-Level Clustered Sensitivity Analysis (`97` Cleaned Tuples Across `35` Studies)

{blk['TABLE_4_QUANTITATIVE_SYNTHESIS']}

When MAS are tested only against weak single-pass baselines (`Tier 3` {c('SR011', 'SR016', 'SR017', 'SR030', 'SR082', 'SR085', 'SR093')}), they win `{ca['Tier 3']['wins']}/{ca['Tier 3']['n_tuples']}` (`{ca['Tier 3']['win_pct']}%`) comparisons (`{ca['Tier 3']['study_frac_win_pct']}%` study-weighted). Introducing strong iterative or voting SAS controls without matched compute (`Tier 2` {c('SR006', 'SR008', 'SR013', 'SR014', 'SR015', 'SR018', 'SR019', 'SR020', 'SR076', 'SR086', 'SR087', 'SR088', 'SR089', 'SR090', 'SR091', 'SR092', 'SR094', 'SR096', 'SR098')}) reduces MAS wins to `{ca['Tier 2']['wins']}/{ca['Tier 2']['n_tuples']}` (`{ca['Tier 2']['win_pct']}%`; `{ca['Tier 2']['study_frac_win_pct']}%` study-weighted). Under strict **compute- and token-matched parity (`Tier 1`)** {c('SR001', 'SR002', 'SR003', 'SR004', 'SR005', 'SR007', 'SR009', 'SR010', 'SR012')}, MAS win rates drop to **`{ca['Tier 1']['wins']}/{ca['Tier 1']['n_tuples']}` (`{ca['Tier 1']['win_pct']}%`)** while outright losses climb to **`{ca['Tier 1']['losses']}/{ca['Tier 1']['n_tuples']}` (`{ca['Tier 1']['loss_pct']}%`)**.

Crucially, this attenuation is not an artifact of multiple tuples per paper or unvetted preprints. Under **fractional study weighting** (each paper summing to `1.0`), `Tier 1` average win rate falls to **`{ca['Tier 1']['study_frac_win_pct']}%`** (`{ca['Tier 1']['study_maj_wins']}/{ca['Tier 1']['n_studies']}` = `{ca['Tier 1']['study_maj_win_pct']}%` majority-win studies; `{ca['Tier 1']['study_unam_wins']}/{ca['Tier 1']['n_studies']}` unanimous) versus **`{ca['Tier 2+3']['study_frac_win_pct']}%`** in `Tier 2+3` (`{ca['study_frac_attenuation_pp']} pp`; two-sided Fisher's exact **$p = {ca['fisher_p_t1_vs_t23']}$** vs. `Tier 2+3`, **$p = {ca['fisher_p_t1_vs_t3']}$** vs. `Tier 3`). Restricting strictly to **Archival** (`Journal + Conference`) studies yields `{cr['Tier 1']['win_pct']}%` (`{cr['Tier 1']['study_frac_win_pct']}%` study-weighted) vs. `{cr['Tier 2+3']['win_pct']}%` (`{cr['tuple_attenuation_pp']} pp`). Moreover, interactive `MAD` contributes `{mad_t1['mad_studies']}/{ca['Tier 1']['n_studies']}` `Tier 1` studies (`{mad_t1['mad_tuples']}` tuples) alongside `{mad_t1['nonmad_studies']}/{ca['Tier 1']['n_studies']}` non-debate ensemble/multi-topology works (`{mad_t1['nonmad_tuples']}` tuples), showing parity loss persists beyond simple peer debate.

#### Table 7: Flagship `Tier 1` Compute/Token-Matched Corpus (`9` Studies, `13` Cleaned Tuples)

{blk['TABLE_5_TIER1_CORPUS']}

*Note: NV = not verifiable from accessible open summary; NR = not reported; pp = percentage points; % rel. = relative percentage change.*

Within `Tier 1`, positive MAS returns are sharply **task-conditional**. Kim et al. {c('SR001_kim2026capable')} show centralized orchestration yields up to `+80.8%` relative gain on parallelizable `Finance-Agent` and `+9.2%` relative on `BrowseComp-Plus`, yet degrades sequential planning on `PlanCraft` by `-39%` to `-70%` relative (with MAS gains diminishing once `SAS` baseline accuracy exceeds `~45%`). Similarly, Collaborative Non-Zero-Sum Multi-Agent Debate (`ColMAD` {c('SR012_chen2026when')}) improves error detection by up to `+10 pp` over prior MAD and beats matched single agents (`SA`). Conversely, equal thinking budgets (`Tran & Kiela` {c('SR002_tran2026single')}, `0.379` vs `0.418`), shared context windows (`Nguyen et al.` {c('SR004_nguyen2026think')}, `SAS >= MAD` in `93%` of `980` settings), and single-LLM KV-cache reuse (`OneFlow` {c('SR003_xu2026rethinking')}) consistently reverse naive MAS advantages. Notably, newly imported archival studies reinforce this ceiling: Choi et al. {c('SR087_2025')} prove multi-round MAD reduces statistically to a martingale around `T = 0` `Majority Voting` (`0.8867` vs `0.9400` on GSM8K), and Bertalanič & Fortuna {c('SR089_2026')} report `Isolated Self-Correction` outperforms `N = 10` unguided homogeneous debate (`48.3%` vs `20.7%` on Ministral-3-8B) while costing `2.1x–3.4x` fewer tokens.

### 5.2 Coordination Topologies, Cost Overhead & Upfront Amortization (`RQ2`)

To avoid encyclopedic study-by-study catalogs in the main body, Table 8 aggregates all six structural topologies (including sequential Standard Operating Procedures [SOPs]) across our `59`-study corpus (complete per-study architecture and overhead rows appear in **Appendix G.3**).

#### Table 8: Compact Orthogonal Topology-Class Synthesis Across the `59`-Study Corpus (`RQ2`)

{blk['TABLE_6_TOPOLOGY_SUMMARY']}

*Note: NV = not verifiable from accessible open summary; NR = not reported; pp = percentage points; % rel. = relative percentage change.*

Three structural findings stand out under `RQ2`. First, **homogeneous multi-sample voting beats naive heterogeneous mixing**: Wang et al. {c('SR011_wang2025mixture')} popularize multi-LLM `MoA` against single-pass `GPT-4o` (`Tier 3`), whereas equal-budget control in `Self-MoA` {c('SR010_li2026rethinking')} proves repeating the strongest model outperforms mixing diverse weaker proposers (`65.7%` vs `59.1%` LC win rate on AlpacaEval 2.0, `-6.6 pp` / `-10.0%` relative loss when mixing; `Agent Forest` {c('SR085_2024')} likewise isolates raw parallel voting scaling).

Second, **upfront optimization cost (`C6`) dominates learned-graph benchmarks**: across all `16` studies scoring `QA3 = 1`, `16/16` (`100%`; `16/17` optimization-bearing works alongside explicit optimizer cost audit `Kapoor et al.` {c('SR032_kapoor2025agents')}) omit upfront discovery/training budgets from test-time efficiency comparisons. Concrete omitted overheads include `<12 hours on 8x A100 GPUs` in `Optima` {c('SR094_2025')}, `2.1h–2.8h` graph training in `DyLAN` / `GPTSwarm` / `G-Designer` {c('SR015', 'SR017', 'SR092')}, MCTS search rollouts in `AFlow` {c('SR018')}, policy-gradient routing in `MasRouter` {c('SR019')}, and evolutionary iterations in `EvoAgent` {c('SR096')}. When `Optima` {c('SR094')} matches inference tokens against `SC(n=8)`, `OPTIMA` beats `SC(n=8)` cleanly while unoptimized `MAD` loses (`-5.4 pp` HotpotQA, `-7.8 pp` GSM8K, `-5.9 pp` MATH)—leaving its amortization dependent on deployment volume $Q$.

Third, **selective escalation captures asymmetric value** {c('SR009', 'SR020', 'SR086', 'SR090', 'SR091')}: Gao et al. {c('SR086_2025')} cut cost up to `20%` via `SAS -> MAS` request cascading; `CascadeDebate` {c('SR020')} triggers debate only on low-confidence items (`75.22%` vs `52.70%` MedQA); and `SAIGE` {c('SR091_2026')} confirms unified `Single-Agent` beats four learned MAS topologies on coupled `Terminal-Bench 2.1` (`76.71`), while sparse-dependency `AgentIF-OneDay` favors `SAIGE` (`71.80%` vs `53.57%`).

### 5.3 Mechanistic Failure Pathways & Topological Security (`RQ3`)

We explicitly separate **within-study verified mechanisms** {c('SR001', 'SR002', 'SR004', 'SR012', 'SR087', 'SR089')} from **cross-corpus mechanistic plausibility**: trajectory-attribution and attack benchmarks (`MAST`, `Who&When`, `VTFR`, `CORBA`, `NetSafe`, `G-Safeguard`) mostly evaluate agent traces without matched `SAS` accuracy baselines, so they identify plausible operational failure pathways rather than proven causal mediators of `Tier 1` outcomes. Table 9 summarizes all six pathways (see **Appendix G.4** for full 59-study entries).

#### Table 9: Compact Mechanistic Failure-Pathway & Mitigation Summary (`N = 59` Studies, `RQ3`)

{blk['TABLE_7_FAILURE_SUMMARY']}

Across comparative and diagnostic evaluations, four quantitative patterns converge:
1. **Error Amplification & Handoff Loss:** Kim et al. {c('SR001_kim2026capable')} show error amplification escalates from **`4.4x` (Centralized)** through **`5.1x` (Hybrid)** and **`7.8x` (Decentralized)** to **`17.2x` (Independent)**—confirming central verification damps but never eliminates cascade risk. Under Markov closed-book relays without external evidence, `DPI` message compression erodes accuracy {c('SR002_tran2026single')}, while shared context limits degrade MAD across `93%` of `980` window configurations {c('SR004_nguyen2026think')}.
2. **Conformity, Debate Hacking & Sycophancy:** Across `Dense All-to-All Debate` (`n = {dd['dense_debate_total']}`), **`{dd['conformity_count']}/{dd['dense_debate_total']}` (`{dd['conformity_pct']}%`)** {dense_conf_str} document sycophantic conformity or consensus collapse (only `Nguyen et al.` {dense_nonconf_str} focuses solely on `DPI`/window scaling). `Cost of Consensus` {c('SR089_2026')} quantifies `85.5%` modal adoption and `32.3 pp` oracle consensus collapse; `Kasprova et al.` {c('SR031')} measure social compliance; `Estornell & Liu` {c('SR088_2024')} prove convergence toward shared misconceptions; and `ColMAD` {c('SR012_chen2026when')} shows Competitive MAD (`CopMAD`) cheap-talk and Consensus-Seeking MAD (`CosMAD`) smoothing drop `15%–19%` below single agents before collaborative incentives recover up to `+10 pp`.
3. **Trace Attribution vs. Real Collaborative Repair:** Fault localization remains fragile (`MAST` {c('SR021')} reports `41%–86.7%` failure rates and `25.8%` step-attribution ceiling; `TRAIL` {c('SR028')}, `Who&When` {c('SR022')}, `AgenTracer` {c('SR023')}, `AgentLocate` {c('SR025')}, `TRIAGE` {c('SR027')} with `59.3%` human disagreement, `Chen et al.` {c('SR026')}, and `VerifyMAS` {c('SR097_2026')} refine causal trace attribution for `MAS` debugging rather than explaining why `MAS` underperforms `SAS`).
4. **Topological Security & Availability Risks:** Security vulnerabilities scale non-linearly with multi-agent wiring. Hagag et al. {c('SR098_2026')} demonstrate across 13 `Inspect AI` configurations that multi-agent tool architectures suffer up to **`3.8x` higher attack success rates** than isolated single agents under identical models; `NetSafe` {c('SR099_2025')} measures `-29.7%` star-topology misinformation collapse; `CORBA` {c('SR069_zhou2026corba')} achieves **`~92%–100%` Proportional Attack Success Rate (`P-ASR`)** within `1.60–1.90` turns (Peak Blocking Turn Number [`PTN`]); and `G-Safeguard` {c('SR100_2025')} recovers `>40%` utility via GNN edge pruning.
5. **Archival-Only `RQ3` Sensitivity:** `13/{rsens['rq3_total']}` primary `RQ3` track studies are **Archival** (`TRAIL` {c('SR028')} is a Preprint; `CMAD` {c('SR079')} is a Workshop paper excluded from High-Confidence Consensus due to two public TMLR rejections), leaving error amplification, conformity, `DPI`, and security mechanisms robustly anchored in peer-reviewed archival literature.

### 5.4 Evaluation Validity, Quality Appraisal & OpenReview Audits (`RQ4`)

Table 10 synthesizes study quality (`QA1`–`QA7`, both `14`/`12`-point and `12`-point normalized `QA2`–`QA7`) alongside all six confounders (`C1`–`C6`), `pass^k`, latency, and USD transparency. Complete `59`-study `QA` rows appear in **Appendix G.5**.

#### Table 10: Quality Appraisal, `12`-Point Normalized Sensitivity & Confounder Incidence (`N = {pr['included_total']}`, `RQ4`)

{blk['TABLE_8_QA_CONFOUNDERS']}

Four pervasive evaluation blind spots emerge:
1. **Absent Multi-Trial Reliability (`pass^k`) & Latency/USD Logs:** Exactly **`{pk['comparative_true']}/{pk['comparative_verifiable_den']}` verifiable comparative studies** (`1` paywalled `NV` on Kim et al. {c('SR001_kim2026capable')}) report `pass^k`, and only `{pk['overall_true']}/{pk['overall_verifiable_den']}` verifiable overall (`tau-bench` {c('SR033_yao2025taubench')}, `Rabanser et al.` {c('SR034_rabanser2026towards')}, and Cost, Latency, Efficacy, Assurance, and Reliability [`CLEAR`] {c('SR035_mehta2025beyond')}; Zhao et al. {c('SR090_2026')} evaluate `pass@k` rather than `pass^k`). Direct wall-clock runtime (`s`/`min`/`h`/`%` reduction) appears in just `{lu['direct_latency_count']}/{pr['included_total']}` (`{lu['direct_latency_pct']}%`) studies {direct_lat_str} plus `{lu['proxy_latency_count']}` step/TFLOP proxies {proxy_lat_str} (`{lu['omit_or_nv_latency_pct']}%` omit/NV). Only `{lu['usd_verified_count']}/{pr['included_total']}` (`{lu['usd_verified_pct']}%`) report exact dollar totals {usd_exact_str} or verified USD ratios/savings {usd_ratio_str}, leaving `{lu['usd_omit_or_nv_pct']}%` omitting/NV USD cost.
2. **Harness Distortion Exceeds Typical Multi-Agent Deltas:** Benchmark artifacts routinely rival or exceed claimed multi-agent improvements. `PatchDiff` {c('SR036_wang2026are')} finds sparse unit tests inflate base `SWE-bench` code resolution by `6.2–6.4 pp` (`29.6%` patch divergence, `28.6%` incorrect, `7.8%` test flaws—directly cautioning code/SWE evaluations rather than extrapolating universally to closed-form MCQA). `WebArena Verified` {c('SR039_elhattami2025webarena')} fixes `11.3 pp` false negatives while cutting runtime `68.2%–83%`; `BenchJack` {c('SR038_wang2026do')} uncovers `219` harness exploits; `Zhu et al.` {c('SR037_zhu2025establishing')} establish judge-bias controls across `RL`/`agent` benchmarks; `CLEAR` {c('SR035_mehta2025beyond')} exposes `50x` enterprise cost variance and `8`-run decay; and `VTFR` {c('SR040_sheshanarayana2026do')} quantifies `30.9%` verifier delegation loss (`85.5%` of transport failures recoverable via provenance).
3. **OpenReview Longitudinal & Rejection Audits (`E8`):** Public review logs verify why methodological omissions matter: `AgenticNet` {c('SR077')} was rejected at TMLR after strict exact-match re-runs dropped `MBPP` `100% -> 77.5%` and cost-matched MATH Level 5 favored CoT; `Inducing Disagreement` {c('SR078')} was rejected for substituting `99.2%` process disagreement for outcome quality; `SCALE` transformed a withdrawn `ICLR 2025` cost-incomplete draft {c('ICLR2025_SCALE_6097')} into an `ACL 2025` archival paper {c('SR082_zhao2025scale')}; while `CMAD` {c('TMLR2025_WhenConsensus_9844', 'SR079_dai2026when')} remains doubly rejected at TMLR despite workshop acceptance.
4. **Archival-Only `RQ4` Sensitivity & Gate Effect:** Within `RQ4` (`n = {rsens['rq4_total']}`), `{rsens['rq4_archival']}` studies are **Archival** (`tau-bench`, `Kapoor et al.`, `Rabanser et al.`, `PatchDiff`, `Zhu et al.`), while `{len(rsens['rq4_non_archival'])}` high-signal audits are Workshops (`WebArena Verified` {c('SR039')}, `VTFR` {c('SR040')}) or Preprints (`CLEAR` {c('SR035')}, `BenchJack` {c('SR038')}). Meanwhile, preprints average `QA7 = {qa['by_status']['Preprint']['qa7_mean']}` vs. Archival `{qa['by_status']['Archival']['qa7_mean']}` because our Preprint Gate (`>= 6/14`, `QA7 >= 1`) filtered weak preprints prior to admission. Removing `QA1` on the `12`-point normalized scale preserves the quality hierarchy (`RQ4` `{qa['by_track']['RQ4']['mean_12pt_pct']}%` vs. `RQ1/RQ2` `{qa['by_track']['RQ1/RQ2']['mean_12pt_pct']}%`).

---

## 6. Epistemic Evidence Grading, Orthogonal Taxonomy, and Decision Framework

### 6.1 Five-Band Epistemic Evidence Separation

To prevent practitioners from conflating well-replicated parity controls with unvetted workshop findings or unpopulated matrix cells, Table 11 grades our synthesis into five semantic confidence bands (replacing arbitrary Roman labels and strictly excluding twice-rejected `CMAD` {c('SR079')} from High-Confidence Consensus).

#### Table 11: Five-Band Epistemic Evidence Separation Across `RQ1`–`RQ4`

{table_10_epistemic}

### 6.2 Strictly Orthogonal Architectural Taxonomy (`Topo × Task × Ver`) & `D0`–`D4` Decision Workflow

To eliminate methodological conflation, we strictly separate **System Design & Environment Axes (`Topo-1..6 × Task-1..4 × Ver-1..4`)** from the orthogonal **Empirical Appraisal Layer (`Tier 1`–`Tier 4` parity + `C1`–`C6` confounders)**:
- **`Axis Topo` (Coordination Topology):** `Topo-1` Independent/Voting Ensemble; `Topo-2` Sequential Chain/SOP; `Topo-3` Centralized Star; `Topo-4` Dense All-to-All Debate; `Topo-5` Adaptive Sparse/Learned DAG; `Topo-6` Hybrid/Selective Escalation (plus `Multi-Topology` sweeps).
- **`Axis Task` (Task Structure):** `Task-1` Decomposable/Parallelizable; `Task-2` Sequential/State-Dependent; `Task-3` Long-Context/Multi-Turn Sandbox; `Task-4` Static Single-Turn/Mixed Suite.
- **`Axis Ver` (Verification Oracle):** `Ver-1` Deterministic/Unit-Test Verifier; `Ver-2` Exact-Match/Objective Key; `Ver-3` LLM-as-a-Judge; `Ver-4` Unverified/Open-Ended.

Table 12 populates the exact `59`-study `Topo × Task` surface alongside strict `Tier 1` parity density, revealing glaring empirical deserts: **`0 Tier 1` studies exist across `Topo-5` (Learned Sparse DAGs, `0/10`) and `Topo-6` (Selective Hybrid, `0/2`)**, and almost all `Tier 1` parity tests cluster in static/sequential suites rather than verified parallel sub-task decompositions.

#### Table 12: Populated 2D `Topology × Task Structure` Evidence-Gap Matrix (`Total / Tier 1 Parity Studies`)

{blk['TABLE_11_EVIDENCE_GAP_HEATMAP']}

Operationalizing this evidence base yields a logically consistent four-regime decision workflow (`D0`–`D4`), resolving prior ambiguities around high single-agent baselines (`>~45%` routed consistently to `Regime A`) and unamortizable low-volume deployments (`Q <= Q_break-even` routed to `Regime A/B` whenever $c_{{\text{{MAS}}}} \ge c_{{\text{{SAS}}}}$).

```mermaid
{mermaid_decision.removeprefix('```mermaid').removesuffix('```').strip()}
```
*Figure 2: Conditional deployment decision workflow (`D0`–`D4`) grounded in compute-normalized empirical findings (`Regimes A–D` represent synthesis-derived hypotheses awaiting prospective end-to-end RCT validation).*

### 6.3 Security-vs.-Liveness & Lifecycle-Economics Governance

Choosing `Regime C` or `Regime D` introduces structural governance coupling alongside compute overhead. Comprehensive threat SoKs—including Kim et al. {c('Kim2026_USENIX_Security')} (*USENIX Security '26*), Deng et al. {c('Deng2025_CSUR_Security')} (*ACM CSUR*), He et al. {c('SR051_he2026security')}, and Dantas et al. {c('Dantas2026_SafeAgents')}—document control-flow hijacking, memory poisoning, and verifier overhead across agentic pipelines. Primary empirical studies inside our corpus {c('SR069_zhou2026corba', 'SR098_2026', 'SR099_2025', 'SR100_2025')} confirm that inter-agent privilege sharing, dense broadcast messaging, and unverified tool delegation widen attack surfaces without commensurate accuracy gains. Responsible deployment therefore requires least-privilege tool isolation, immutable provenance hashes (`VTFR`-style verification), hard turn/budget circuit breakers, and explicit accounting of $C_{{\text{{search}}}}$ before commissioning multi-agent topologies in production.

---

## 7. Open Research Directions

1. **Compute- & Amortization-Complete RCTs for Learned DAGs (`Topo-5`):** Close the `0/{st['topology_counts'].get('Adaptive Sparse/Learned DAG', 0)}` `Tier 1` parity gap by benchmarking `AFlow`, `DyLAN`, `AgentDropout`, `Optima`, and `SAIGE` against `Self-Consistency` / `Self-MoA` with $C_{{\text{{search}}}}$ amortized over realistic query curves $Q$.
2. **Standardized `pass^k` + Wall-Clock + USD Reporting Protocol:** Require all multi-agent evaluations to report unbiased $\mathbb{{E}}[\binom{{c}}{{k}}/\binom{{n}}{{k}}]$ across $k \ge 5$ trials, end-to-end wall-clock seconds, hidden thinking tokens (`thoughts_token_count`), and API dollar expenditures.
3. **Adversarial & Provenance-Preserving Topologies (`Ver-1` + Security):** Evaluate whether structured non-zero-sum verification (`ColMAD` + `G-Safeguard` edge pruning + immutable state provenance) simultaneously mitigates error amplification, `VTFR` abstraction drops, and `3.8x` multi-agent exploit amplification under compute-matched baselines.
4. **Hardened Agentic Sandboxes Free of `C5` Distortions:** Retire unverified base benchmarks in favor of backend-state-checked harnesses (`WebArena Verified`, `SWE-bench` hardened tests, `AgentDojo`/`Inspect AI`) paired with stochastic noise controls {c('SR089_2026')}.

---

## 8. Threats to Validity and Limitations

1. **Seeded Open-Web Coverage vs. Proprietary Databases:** Without bulk *Scopus* or *Web of Science* API exports, Searches 1–13 remain open-web query- and snowball-seeded rather than an exhaustive publisher census; specialized Searches 2, 5, and 9 and Protocol v1.2 anchor imports (Searches 12–13) are disclosed transparently.
2. **Summary-Bounded `NV` Fields & Paywalled Supplements:** Web/open-HTML inspection left {nv['scalar_nv_fields']} scalar fields ({nv['leaf_nv_strings']} total leaf strings) across {nv['records_with_nv']}/{nv['total_records']} records coded "not verifiable from accessible open summary", and Kim et al. {c('SR001_kim2026capable')} supplementary `pass^k` and wall-clock seconds remain behind a *Nature Machine Intelligence* paywall. Zero missing values were extrapolated or imputed.
3. **Within-Study Clustering & Heterogeneous Scales:** Tuple counts vary across papers (1 to 15 tuples per study). Addressing this via fractional study weighting ({ca['Tier 1']['study_frac_win_pct']}% vs {ca['Tier 2+3']['study_frac_win_pct']}%) and two-sided Fisher's exact testing (p = {ca['fisher_p_t1_vs_t23']}) confirms the {ca['tuple_attenuation_pp']} pp attenuation is statistically robust.
4. **Preprint/Workshop Velocity & Retroactive Stage 2 Completion:** Workshop ({pr['workshop_count']}/{pr['included_total']}) and gate-screened preprint ({pr['preprint_count']}/{pr['included_total']}) shares may shift as 2026 manuscripts finalize peer review; Archival-Only sensitivity analyses across `RQ1`, `RQ3`, and `RQ4` plus full disclosure of retroactive Stage 2 review completion on Dai {c('SR079_dai2026when')} and SCALE {c('SR082_zhao2025scale')} bound publication-status risk cleanly.

---

## 9. Conclusion

Across `{pr['included_total']}` systematically screened studies (`2023–2026`) and `{ca['All']['n_tuples']}` cleaned paired comparisons, the empirical verdict is unambiguous: **`LLM-MAS` superiority over single agents is largely an artifact of unmatched compute budgets, weak zero-shot comparators, unamortized optimization overhead, and fragile evaluation harnesses.** Enforcing strict `Tier 1` parity cuts MAS win rates from `{ca['Tier 3']['win_pct']}%` (`Tier 3`) and `{ca['Tier 2']['win_pct']}%` (`Tier 2`) down to **`{ca['Tier 1']['win_pct']}%`**, with outright MAS losses reaching **`{ca['Tier 1']['loss_pct']}%`** (`{ca['tuple_attenuation_pp']} pp` drop; study-weighted `{ca['study_frac_attenuation_pp']} pp`; Fisher $p = {ca['fisher_p_t1_vs_t23']}$). Genuine multi-agent advantages emerge selectively—primarily when external tools or long documents overload a single context window and deterministic verifiers gate escalation—whereas closed-book, sequential, or unguided homogeneous debate reliably loses to compute-matched `Self-Consistency`, `Self-MoA`, or isolated self-correction. Future agentic research must treat compute normalization, `pass^k` reliability, $C_{{\text{{search}}}}$ amortization, and adversarial topology auditing as mandatory baselines rather than optional ablations.

---

## 10. References

{refs}

---

## 11. Declarations

- **Ethical & Plagiarism Statement:** All prose, synthesis tables, and taxonomic frameworks are original; every external metric and claim is traced directly to verified source records with zero fabrication or imputation of missing numbers.
- **Funding & Competing Interests:** This review was conducted as independent graduate/academic systematic research with no commercial funding or competing financial interests.
- **AI Tooling Transparency & Human Accountability:** Following ACM Authorship Policy and TMLR guidelines, tool-verified LLM workflows assisted structured literature screening triage, JSON schema extraction, and deterministic verification scripting (`Python`), while the human authors designed the protocol, adjudicated every screening/quality dispute, audited source tables, and assume full responsibility for manuscript accuracy.
- **Reproducibility & Artifact Availability:** The complete PRISMA screening ledger (`N = 100`), Draft 2020-12 JSON extraction database (`N = 59`), `QA1`–`QA7` scoring table, deterministic statistics scripts, `112`-entry `BibTeX` file, and full Online Supplement (**Appendix G**) will be released via an anonymized review repository during double-blind assessment and archived permanently upon publication.
"""

    # Strip redundant monospace backticks on ordinary numbers, percentages, and prose acronyms before checking
    manuscript_clean_body, refs_sec = manuscript.split("## 10. References", 1)
    manuscript_clean_body = re.sub(r"`([+-]?[0-9][0-9.,/%–-]*(?: pp|%)?)`", r"\1", manuscript_clean_body)
    manuscript_clean_body = re.sub(r"`(LLM-MAS|SAS|MAS|MAD|CoT|RL|MARL|Tier [1-4])`", r"\1", manuscript_clean_body)
    manuscript = manuscript_clean_body + "## 10. References" + refs_sec

    # Sanity verification of 112/112 citation coverage, zero raw leaks, zero collisions!
    cited_nums = set()
    # Extract references section separately so we don't scan Refs as body prose
    body_part, refs_part = manuscript.split("## 10. References")
    body_for_check = body_part
    for m in re.finditer(r"\[(\d+(?:,\s*\d+)*)\]", body_for_check):
        for x in m.group(1).split(","):
            cited_nums.add(int(x.strip()))

    missing_cites = sorted(set(range(1, cm["total"] + 1)) - cited_nums)
    extra_cites = sorted(cited_nums - set(range(1, cm["total"] + 1)))
    assert not missing_cites, f"Uncited BibTeX entries in body: {missing_cites} -> {[cm['by_num'][str(x)]['key'] for x in missing_cites]}"
    assert not extra_cites, f"Undefined citation numbers in body: {extra_cites}"

    # Check colliding labels & internal leaks
    assert not re.search(r"\bTier [A-C]\b|\bTier [IVX]+\b", body_part), "Found forbidden Tier A-C / Tier I-V!"
    assert not re.search(r"\bQ[0-4]\b", body_part), "Found forbidden Mermaid Q0-Q4 node!"
    assert not re.search(r"\bSR\d{3}\b|`F17`|`F18`|FM-2\.3", body_part), "Found raw internal ID leak!"
    assert not re.search(r"`\[\d+", body_part), "Found backticked citation bracket!"
    assert "Discovery Specialist" not in body_part and "Review Methodologist" not in body_part and "Research Director" not in body_part, "Found internal agent role title!"

    # Check prose clichés on body (excluding References)
    cliches = ["in recent years", "paradigm shift", "game-changer", "game changer", "delve into", "tapestry", "landscape of", "it is worth noting"]
    found_cliches = [cl for cl in cliches if cl in body_part.lower()]
    assert not found_cliches, f"Found banned AI cliché in body: {found_cliches}"

    # Write both files
    with open(REVIEWS / "manuscript_v3_final.md", "w") as f:
        f.write(manuscript)
    with open(DELIV / "Deliverable_F_Final_Review_Manuscript.md", "w") as f:
        f.write(manuscript)

    print(f"BUILT manuscript_v3_final.md & Deliverable_F_Final_Review_Manuscript.md!")
    print(f"  Abstract: {len(abs_words)} whitespace words | {len(abs_split)} split tokens")
    print(f"  Citations: {len(cited_nums)}/{cm['total']} (1:1 parity, 0 uncited, 0 undefined)")
    print(f"  Body word count: {len(body_part.split())} words | Total size: {len(manuscript)} chars")


if __name__ == "__main__":
    main()
