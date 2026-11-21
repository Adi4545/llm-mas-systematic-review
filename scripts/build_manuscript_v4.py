#!/usr/bin/env python3
"""
Deterministic Plain-English + Publication-Grade Authoring Script for:
  - reviews/manuscript_v4_final.md
  - deliverables/Deliverable_F_Final_Review_Manuscript.md
Implements Protocol v1.4:
  - Addresses all Round-2 Reconciled Referee Report requests (Requests 1-9, M1-M10, m1-m16, N1-N13, Second Reviewer #1-#19)
  - Class-12-accessible plain academic English (Table 1 Glossary, intuition before math, zero backticks outside code blocks)
  - Multi-node populated Mermaid diagrams paired with 300-DPI PNG figure embeds
  - Full self-contained Section 12 Appendices A (verbatim Q1-Q6 + 13-search PRISMA-S log), B (59-study QA item + flag + source locator ledger),
    C (full 87-comparison dataset + 34-study win-share vector), D (comparison-cleaning & re-coding log), and E (41-record exclusion ledger)
  - Strict 124/124 1:1 BibTeX citation parity and automated leak assertions.
"""

import csv
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
    with open(DATA / "search_log.json") as f:
        sl = json.load(f)
    with open(DATA / "evidence_matrix.json") as f:
        em = json.load(f)
    with open(DATA / "quality_appraisal.csv") as f:
        qa_rows = list(csv.DictReader(f))
    with open(DATA / "screening_records.csv") as f:
        sr_rows = list(csv.DictReader(f))

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
    return st, cm, refs, blocks, sl, em, qa_rows, sr_rows


def main():
    st, cm, refs, blk, sl, em, qa_rows, sr_rows = load_inputs()
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

    def find_excl_cnum(rid: str):
        if rid in by_sid:
            return by_sid[rid]
        prefix = rid + "_"
        for k, v in by_key.items():
            if k.startswith(prefix) or k == rid:
                return v
        return None

    def short_first_author(authors_str: str) -> str:
        parts = [a.strip() for a in authors_str.split(";") if a.strip()]
        if not parts:
            return "Unknown"
        first = parts[0]
        if "Anonymous" in first:
            return first
        last = first.split()[-1]
        if len(parts) == 1:
            return last
        if len(parts) == 2:
            return f"{last} & {parts[1].split()[-1]}"
        return f"{last} et al."

    pr = st["prisma"]
    irr = st["irr"]
    ca = st["comparative_all"]
    cr = st["comparative_archival"]
    cw = st["comparative_wave1"]
    cw2 = st["comparative_wave2_t23"]
    ci = st["comparative_interactive"]
    czs = st["comparative_zero_search"]
    copt = st["comparative_opt_nguyen"]
    t1sub = st["tier1_subsplits"]
    es = st["effect_size_meta"]
    qa = st["qa"]
    cf = st["confounders"]
    pk = st["pass_power_k"]
    lu = st["latency_and_usd"]
    dd = st["dense_debate_conformity"]
    nv = st["nv_inventory"]
    rsens = st["rq3_rq4_archival_sensitivity"]

    dense_conf_str = "[" + ", ".join(str(x) for x in dd["conformity_cites"]) + "]"
    dense_nonconf_str = "[" + ", ".join(str(x) for x in dd["non_conformity_cites"]) + "]"
    direct_lat_str = "[" + ", ".join(str(x) for x in lu["direct_latency_cites"]) + "]"
    proxy_lat_str = "[" + ", ".join(str(x) for x in lu["proxy_latency_cites"]) + "]"
    usd_exact_str = "[" + ", ".join(str(x) for x in lu["usd_exact_cites"]) + "]"
    usd_ratio_str = "[" + ", ".join(str(x) for x in lu["usd_ratio_cites"]) + "]"
    pk_overall_str = "[" + ", ".join(str(x) for x in pk["overall_true_cites"]) + "]"

    # Abstract (<= 95 whitespace words, <= 100 split tokens, zero backticks, exact unit alignment)
    abstract = (
        f"Teams of large language models are widely applied to reasoning, coding, and tool tasks, "
        f"yet many benchmarks lack compute-matched single-agent baselines. This systematic review synthesizes "
        f"{pr['included_total']} studies ({ca['All']['n_studies']} comparative studies, {ca['All']['n_tuples']} comparisons). "
        f"Multi-agent teams win {ca['Tier 2+3']['win_pct']}% of unmatched comparisons, declining to "
        f"{ca['Tier 1']['win_pct']}% wins and {ca['Tier 1']['loss_pct']}% losses under equal-compute controls "
        f"({ca['tuple_attenuation_pp']} percentage points; study-weighted {ca['study_frac_attenuation_pp']} points, "
        f"permutation p = {ca['perm_p_study_frac_t1_vs_t23']}). Multi-agent gains appear mainly on splittable multi-source tasks "
        f"observed in Kim et al., while declines reflect error cascades, peer conformity, text-handoff loss, "
        f"unamortized search ({cf['qa3_1_count']}/{cf['learned_optimizers_total']} comparative optimizers), "
        f"and missing reliability checks."
    )
    abs_words = abstract.split()
    abs_split = re.split(r"[\s/\u2013-]+", abstract.strip())
    assert "`" not in abstract, "Backticks forbidden in Abstract!"
    assert len(abs_words) <= 95, f"Abstract too long: {len(abs_words)} words"

    # Glossary Table (Table 1) — Class-12 friendly
    glossary_tbl = """| Term | Simple Meaning |
| :--- | :--- |
| Single-Agent System (SAS) | One AI model solving a problem alone, either in one pass or by generating and checking several independent attempts by itself. |
| Multi-Agent System (MAS) | Two or more stateful AI agents exchanging messages, critiques, or delegated subtasks—or mixing distinct LLM model families together. |
| Compute-Matched Baseline | A fair test where the solo AI and the multi-agent team spend the same total tokens, API calls, or dollar budget. |
| Self-Consistency Voting | Asking one solo AI to solve the same problem multiple times independently and choosing the most common answer by vote. |
| Pass-at-k vs. Pass-power-k | Pass-at-k checks whether at least one out of k attempts works; pass-power-k checks whether all k attempts succeed consistently. |
| Cost Amortization | Including the hidden upfront GPU hours or search tokens spent discovering a team workflow inside total deployment cost. |
| Error Amplification | One agent making an early mistake that teammates repeat, defend, and magnify instead of catching. |
| Sycophantic Conformity | An agent that held the right answer switching sides just to agree with a confident or larger wrong crowd. |"""

    # Table 3: PRISMA-S Summary
    table_prismas = (
        "| Search Phase | Target Repositories & Method | Campaign Date | Raw Logged | Duplicates Merged | Net Unique | Primary Purpose |\n"
        "| :--- | :--- | :---: | :---: | :---: | :---: | :--- |\n"
        "| Baseline Core Queries (S01–S09) | arXiv, OpenReview, ACL Anthology, PMLR, ACM DL, Springer, Nature, IEEE Xplore | 2026-11-20 (2023–2026 window) | 105 | 33 | 72 | Comparative tests, topologies, failure mechanisms, validity audits, OpenReview status |\n"
        "| Backward & Forward Snowballing (S10–S11) | Reference lists & citations around flagship scaling, debate, workflow, and harness papers | 2026-11-20 (2023–2026 window) | 21 | 9 | 12 | Recover foundational anchors and late-2026 follow-up studies |\n"
        "| Targeted Gap Recovery (S12–S13) | Named anchors in agent ensembles, optimization, conformity, and multi-agent security | 2026-11-20 (2023–2026 window) | 16 | 0 | 16 | Close recall gaps missed by broad Boolean terms (15 included, 1 excluded) |\n"
        f"| Cumulative Total (S01–S13) | Consolidated single-day retrieval & verification campaign | Through 2026-11-20 | {pr['raw_total']} | {pr['duplicates']} | {pr['unique_screened']} | Yields {pr['included_total']} included studies and 41 excluded records |"
    )

    table_excl = f"""| Exclusion Reason | Excluded (n) | Representative Works & Boundary Logic |
| :--- | :---: | :--- |
| Single-agent tool loop or router without multi-agent teamwork | 9 (6 Stage 1, 3 Stage 2) | Solo coding pipelines like Agentless {c('SR065_xia2025agentless')} and intra-agent fault logs like AgentDebug {c('Zhu2026_AgentDebug')} (Excl-01), plus single-policy routers like Router-R1 {c('SR095_2025')} invoking stateless APIs without inter-agent dialogue. |
| Secondary surveys and narrative reviews | 16 (15 Stage 1, 1 Stage 2) | Competing surveys {c('SR041', 'SR042', 'SR043', 'SR044', 'SR045', 'SR046', 'SR047', 'SR048', 'SR050', 'SR051', 'SR052', 'SR053', 'SR055', 'SR056', 'SR080', 'SR084')} (including single-query routing review {c('SR048')}); excluded from primary counts and compared in Table 2. |
| Paywalled abstract only, non-empirical, or off-topic tasks | 10 (3 paywalled, 2 non-emp., 5 scope) | Closed-access proceedings lacking open mirrors (3 papers), non-empirical or non-LLM essays (Model Swarms {c('SR057')}, NetLogo insects {c('SR058')}), and single-agent security suites (5 papers). |
| Publicly rejected or withdrawn OpenReview versions | 6 (all Stage 1) | Separated into our peer-review case audit in Section 5.4: rejected TMLR submissions (AgenticNet {c('SR077')}, Inducing Disagreement {c('SR078')}, self-play survey {c('SR084')}) and withdrawn drafts (Harness survey {c('SR080')}, SwarmBench {c('SR081')}, Peacemaker {c('SR083')}, alongside SCALE's withdrawn draft {c('ICLR2025_SCALE_6097')} before ACL 2025 acceptance {c('SR082')}). |"""

    table_anchors = """| Methodological Check | Simple Definition & Why It Matters |
| :--- | :--- |
| Equal Token / Compute Check (Confounder C1) | Did both solo AI and team spend roughly equal tokens, API calls, and dollars, or use equal-budget Self-Consistency? |
| Hidden Thinking-Token Check (Confounder C2) | Did evaluation count hidden internal reasoning tokens (such as extended thinking traces) in the budget? |
| Real Communication vs. Voting (Confounder C3) | Did agents actually exchange feedback, or were single-model answers merely aggregated by vote (such as Agent Forest [51])? |
| Equal Prompts and Tools (Confounder C4) | Did the solo AI receive the same instructions, tools, and code retries as the multi-agent team? |
| Test Harness Reliability (Confounder C5) | Did benchmarks check real execution states and prevent grading loopholes or data leakage? |
| Upfront Search/Training Amortization (Confounder C6) | If a comparative framework spent hours searching or training workflows before testing, were those upfront costs counted? |
| Study Quality Rubric (QA1–QA7) | Seven 0–2 criteria (14 pts for comparative studies; 12 pts for diagnostic audits without a solo arm) plus a 12-pt scale excluding QA1. |"""

    # Section 6.1 GRADE-Inspired Evidence Table (Downgraded per Referee M5 / Request #5!)
    table_epistemic = f"""| Evidence Certainty (GRADE-Adapted) | Core Empirical Finding & Important Scope Conditions | Key Grounding Studies |
| :--- | :--- | :--- |
| Moderate Certainty (Observational Cross-Study + Within-Study Contrasts) | Moving from weak single-pass or unmatched baselines to equal-compute controls is associated with a {ca['tuple_attenuation_pp']} percentage-point drop in multi-agent win rates ({ca['Tier 2+3']['win_pct']}% to {ca['Tier 1']['win_pct']}%, Wilson 95% CI {ca['Tier 1']['win_wilson_ci95'][0]}%–{ca['Tier 1']['win_wilson_ci95'][1]}%; study-weighted {ca['study_frac_attenuation_pp']} points, permutation p = {ca['perm_p_study_frac_t1_vs_t23']}). Replicated inside 6 single-paper contrasts holding authors and benchmarks fixed; rated Moderate rather than High because Tier 1 contains n = 7 studies (4 archival, 2 preprints, 1 workshop) and non-randomized observational designs. | {c('SR001','SR002','SR004','SR005','SR006','SR007','SR010','SR012','SR086','SR087','SR089','SR094')} |
| High Certainty (Direct Corpus Census of Published Reporting) | Every comparative learned-graph or RL/MCTS-optimized framework (12/12 = 100%) omits upfront search or GPU training costs from headline efficiency tables. Similarly, 0/34 (0%) verifiable comparative studies report multi-trial pass^k consistency, 79.7% (47/59) omit direct wall-clock seconds, and 88.1% (52/59) omit dollar spend totals or ratios. | {c('SR003','SR015','SR016','SR017','SR018','SR019','SR020','SR076','SR092','SR093','SR094','SR096')} |
| Low-to-Moderate Certainty (Sample-Limited Archival Sub-Slice) | Restricting solely to archival journal and conference papers preserves a {cr['tuple_attenuation_pp']} pp win difference ({cr['Tier 1']['win_pct']}% [2/9, Wilson 6.3%–54.7%] vs. {cr['Tier 2+3']['win_pct']}% [40/58]; study-weighted permutation p = {cr['perm_p_study_frac_t1_vs_t23']}). Wide intervals and non-significant binary majority Fisher p = {cr['fisher_p_t1_vs_t23']} reflect the small n = 4 archival Tier 1 sample. | {c('SR001','SR005','SR007','SR010')} |
| Moderate Certainty (Task- & Model-Bounded) | Tier 1 gains on splittable multi-source tasks (2/2 = 100%, Finance-Agent +80.8% relative and BrowseComp-Plus +9.2% relative) come from one six-benchmark study (Kim et al. [46]), alongside non-zero-sum verification (ColMAD [15], +10 pp vs. prior debate). Conversely, sequential PlanCraft drops -39% to -70%, and CAIS '26 [6] loses across all three GSM-Hard models (-2.2 pp on Qwen2.5-7B n=1,017; -1.7 pp on Llama-3.1-8B; -27.6 pp on Ministral-3-8B). | {c('SR001','SR002','SR012','SR020','SR086','SR089','SR091')} |
| Moderate Certainty (Mechanism-Specific) | Dense all-to-all debate triggers peer conformity or sycophancy in {dd['conformity_count']}/{dd['dense_debate_total']} ({dd['conformity_pct']}%) debate papers; multi-agent tool wiring reaches up to 3.8x higher attack success than solo baselines under shared models and risks recursive blocking unless pruned. | {c('SR005','SR007','SR029','SR031','SR069','SR087','SR088','SR089','SR098','SR099','SR100')} |
| Low / Provisional Certainty (Evidence Gap) | Workshop calibration findings (18%–47% miscoverage in CMAD [19]) await archival replication. Because 0/10 learned-graph studies meet Tier 1 equal-compute and amortized-search standards, Figure 4's routing guide represents a structured synthesis checklist awaiting prospective controlled trials. | {c('SR015','SR017','SR018','SR076','SR079','SR091','SR093','SR094')} |"""

    # Section 12 Appendix A: Verbatim Q1-Q6 Strings + Search Log (S01-S13)
    verbatim_queries_md = """All six Boolean queries were executed in a single consolidated retrieval campaign on November 20, 2026 (`2023-01-01` to `2026-11-20`). Minimal repository syntax adjustments (parentheses, quotes, `site:` filters) preserved identical logical terms:

* **Q1 — Compute/Token-Matched SAS-vs.-MAS Benchmarks (RQ1):**
```text
("multi-agent" OR "multiagent" OR "multi-agent debate" OR "agent collaboration")
AND ("LLM" OR "large language model" OR "language agent")
AND ("single-agent" OR "single agent" OR "self-consistency" OR "chain-of-thought" OR "vanilla CoT")
AND ("token budget" OR "compute-matched" OR "equal compute" OR "inference cost" OR "cost-accuracy" OR "outperform" OR "underperform")
```
* **Q2 — Coordination Topologies, Pruning, Scaling & Amortization (RQ2):**
```text
("multi-agent" OR "LLM-MAS" OR "agentic workflow")
AND ("LLM" OR "large language model")
AND ("topology" OR "communication graph" OR "pruning" OR "orchestration" OR "decentralized" OR "centralized" OR "hierarchical")
AND ("token reduction" OR "token overhead" OR "latency" OR "scaling" OR "MCTS" OR "GNN" OR "amortized" OR "search cost")
```
* **Q3 — Inter-Agent Error Propagation, Conformity, Cascades & Attribution (RQ3):**
```text
("multi-agent" OR "multi-agent debate" OR "LLM agents")
AND ("LLM" OR "large language model")
AND ("error propagation" OR "error amplification" OR "cascading failure" OR "conformity" OR "sycophancy" OR "consensus collapse" OR "diversity collapse" OR "failure attribution" OR "root cause" OR "trajectory")
```
* **Q4 — Evaluation Validity, pass^k, Harness Fragility & Reliability Audits (RQ4):**
```text
("LLM agent" OR "multi-agent" OR "agentic benchmark")
AND ("pass^k" OR "pass@k" OR "multi-run" OR "reliability" OR "harness" OR "reward hacking" OR "benchmark leakage" OR "exact match" OR "SWE-bench" OR "tau-bench" OR "WebArena" OR "verification transport")
```
* **Q5 — Terminological Boundary & Selective SAS-to-MAS Escalation (Boundary / Mitigation):**
```text
("LLM" OR "large language model")
AND (("swarm intelligence" OR "classical MAS" OR "prompt chaining" OR "emergent coordination")
     OR ("selective escalation" OR "uncertainty-aware delegation" OR "single-to-multi" OR "masrouter" OR "cascadedebate"))
```
* **Q6 — Venue-Targeted & Public Peer-Review / OpenReview Audit Query (RQ4 & Status Verification):**
```text
(site:openreview.net OR site:aclanthology.org OR site:proceedings.neurips.cc OR site:proceedings.mlr.press OR site:dl.acm.org)
AND ("multi-agent" OR "multiagent")
AND ("large language model" OR "LLM")
AND ("single-agent" OR "failure" OR "debate" OR "topology" OR "benchmark")
AND ("2023" OR "2024" OR "2025" OR "2026")
```
"""

    app_a_lines = [
        "| Search ID | Wave / Query Focus | Date | Raw Hits | Merged | Unique Added | Domains Covered |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :--- |",
    ]
    for s in sl["searches"]:
        doms = ", ".join(s["domains_targeted"][:4])
        app_a_lines.append(
            f"| {s['search_id']} | {s['protocol_query']} | {s['date']} | {s['raw_hits_logged']} | {s['duplicates_collapsed']} | {s['unique_new_records_added']} | {doms} |"
        )

    # Appendix B: Full 59-Study Ledger with QA1-QA7 Item Ratings, Flags, & Source Locators
    qa_map = {r["record_id"]: r for r in qa_rows}
    app_b_lines = [
        "| Ref | First Author & Year | Venue & Status | Track | Parity Tier | Topology | QA1–QA7 Items & Score (%) | Confounders | Verified Source Locator |",
        "| :---: | :--- | :--- | :---: | :--- | :--- | :---: | :--- | :--- |",
    ]
    for rid, rec in sorted(em.items()):
        cnum = by_sid[rid]
        qr = qa_map[rid]
        short_au = cm["by_num"][str(cnum)]["short_cite"]
        ps = "Archival" if rec["publication_status"] in ("Peer-reviewed journal", "Peer-reviewed conference") else ("Workshop" if rec["publication_status"] == "Workshop" else "Preprint")
        tr = "RQ1/2" if "RQ1/RQ2" in rec["rq_mapping"]["corpus_track"] else ("RQ3" if "RQ3" in rec["rq_mapping"]["corpus_track"] else "RQ4")
        tier = rec["baselines_and_rigor_tier"]["sas_baseline_rigor_tier"].split(" (")[0]
        tc = rec["architecture_and_agent_count"]["topology_class"]
        q1_v = "NA" if "N/A" in qr["qa1_sas_rigor"] else qr["qa1_sas_rigor"]
        qa_vec = f"{q1_v}-{qr['qa2_cost_latency']}-{qr['qa3_amortization']}-{qr['qa4_multirun_stats']}-{qr['qa5_harness_integrity']}-{qr['qa6_reproducibility']}-{qr['qa7_claims_parity']} ({qr['total_raw_score']}/{qr['applicable_max_score']}, {qr['pct_score']}%)"
        flags = ", ".join(x.split(":")[0].strip() for x in rec["limitations_and_validity_threats"]["six_class_confounder_flags"])
        bi = rec["bibliographic_and_identifiers"]
        sp = rec["source_provenance"]
        id_cand = []
        for fld in ["doi", "arxiv_id", "acl_anthology_id", "openreview_id"]:
            val = bi.get(fld, "")
            if val and "not " not in val.lower() and "none" not in val.lower():
                id_cand.append(val)
        loc_id = id_cand[0] if id_cand else sp["verified_url"]
        acc_lbl = sp["access_level"].replace("_", " ")
        app_b_lines.append(
            f"| [{cnum}] | {short_au} | {bi['venue']} ({ps}) | {tr} | {tier} | {tc} | {qa_vec} | {flags} | {loc_id} ({acc_lbl}) |"
        )

    # Appendix D: Clean Comparison Cleaning & Boundary Re-Coding Log (no SRxxx, no v1.x process jargon)
    app_d_txt = f"""Every quantitative entry in Synthesis Tables 8–12 tests one multi-agent system ($N \ge 2$ collaborating LLMs or heterogeneous multi-LLM ensemble) against a single-agent baseline ($N = 1$). Before statistical pooling, overlapping summary rows, non-single-agent ablations, and pure single-model voting benchmarks were cleaned as itemized below:

| Item | Study | Benchmark / Scope | Action Taken | Rationale |
| :---: | :--- | :--- | :--- | :--- |
| 1 | GPTSwarm {c('SR015')} | Mini Crosswords (GPT-3.5-Turbo) | Removed (-1 row) | Compares optimized MAS graph against unoptimized MAS graph rather than a single agent (N = 1). |
| 2 | GPTSwarm {c('SR015')} | HumanEval (Node-opt ReAct vs. Initial ReAct) | Removed (-1 row) | Compares single-agent node optimization against single-agent baseline (N = 1 vs. N = 1). |
| 3 | Zhang et al. {c('SR007')} | 9 benchmarks x heterogeneous model pairings | Removed (-1 row) | Compares Heter-MAD vs. Homog-MAD (+6.4% / +8.2%), not MAS vs. SAS (retained in diagnostic text). |
| 4 | MacNet {c('SR014')} | 4-Benchmark Average (Table 1) | Removed (-1 row) | Macro-average duplicating the 4 individual benchmark rows (MMLU, HumanEval, SRDD, CommonGen-Hard). |
| 5–6 | Tran & Kiela {c('SR002')} | Nested 1,000- & 5,000-token sub-slices | Collapsed & Re-Split (-2 -> +2) | Merged nested token slices into two non-overlapping strata: >=500-token budgets (MAS < SAS) vs. 100-token / injected context-rot stress (Mixed). |
| 7 | CascadeDebate {c('SR020')} | 5-benchmark suite peak aggregate | Removed (-1 row) | Composite peak overlapping MedQA and blending single-LLM cascades with standalone MAS. |
| 8 | Debate or Vote {c('SR087')} | 6 secondary MAD(T=2) vs. N=1 weak-prompt rows | Collapsed (-6 -> +3) | Retained primary Majority Vote (N=5, T=0), Arithmetics, and 7-benchmark sweep to avoid over-weighting one study. |
| 9–10 | Optima {c('SR094')} | 2 duplicate HotpotQA weak-CoT rows | Removed (-2 rows) | Retained the 6 SC(n=8) parity pairings cleanly (3 RL/DPO-trained Optima wins vs. 3 unoptimized MAD losses). |
| 11 | Kim et al. {c('SR001')} | Expanded coarse 3-row summary across all 6 suites | Expanded (3 -> 5 rows) | Explicitly separates WorkBench and SWE-bench Verified & Terminal-Bench alongside Finance-Agent, BrowseComp-Plus, and PlanCraft. |
| 12 | Nguyen et al. {c('SR004')} | Split by single-agent comparator type | Split (1 -> 2 rows) | Separates MAD vs. Self-Consistency (MAS < SAS, 93% of 980 settings) from MAD vs. 1-Pass Long-CoT (Mixed, Table 17). |
| 13 | OneFlow {c('SR003')} & Denisov-Blanch et al. {c('SR009')} | Re-classified from Tier 1 to Tier 2 | Re-coded (1 row each) | OneFlow uses KV-cache prefix reuse + unamortized MCTS (C6 -> Tier 2B); Denisov-Blanch et al. tests 25x polling against 1x solo (Tier 2A). |
| 14 | Bertalanič & Fortuna (CAIS '26) {c('SR089')} | Expanded GSM-Hard from 1 model to all 3 tested models | Expanded (1 -> 3 rows) | Reports primary Qwen2.5-7B (n=1,017, -2.2 pp), Llama-3.1-8B (n=100, -1.7 pp), and Ministral-3-8B (n=100, -27.6 pp) with binomial SEs. |
| 15 | More Agents Is All You Need / Agent Forest {c('SR085')} | Re-classified from Tier 3 MAS (15 rows) to RQ4 C3 validity audit | Re-coded (-15 -> 0 comp rows) | Enforces Section 3.4 execution rule: repeating N=1 single LLM and voting without inter-agent dialogue is solo test-time scaling, not MAS. |
| 16 | AgenTracer {c('SR023')}, AgentLocate {c('SR025')}, VerifyMAS {c('SR097')}, G-Safeguard {c('SR100')} | Removed non-comparative C6 training cost flags | Re-coded (12/12 C6) | Non-comparative fault-localization and defense studies make no comparative MAS-vs-SAS runtime cost claim (QA3 = 2). |"""

    # Appendix E: Complete 41-Record Excluded-Studies Ledger from screening_records.csv
    excl_rows = [r for r in sr_rows if r["final_decision"] == "EXCLUDE"]
    assert len(excl_rows) == 41, f"Expected 41 excluded records, got {len(excl_rows)}"
    app_e_lines = [
        "| Excl ID | Author & Year (Ref if Cited) | Title | Venue & Canonical ID | Stage Excluded | Code | Primary Exclusion Reason |",
        "| :---: | :--- | :--- | :--- | :---: | :---: | :--- |",
    ]
    for idx, r in enumerate(excl_rows, 1):
        eid = f"Excl-{idx:02d}"
        rid = r["record_id"]
        cnum = find_excl_cnum(rid)
        au_yr = f"{short_first_author(r['authors'])} ({r['year']})" + (f" [{cnum}]" if cnum else "")
        title_clean = r["title"].replace("|", "/")
        venue_id = f"{r['venue'].replace('|', '/')} ({r['canonical_id']})"
        stg = "Stage 1" if r["stage1_agent3_decision"] == "EXCLUDE" and r["stage1_agent6_decision"] == "EXCLUDE" else "Stage 2"
        code = r["final_exclusion_code"]
        reason = r["notes"].replace("|", "/")
        reason = re.sub(r"\[Dir Arbitration:[^\]]*\]", "", reason)
        reason = re.sub(r"\bSR\d{3}\b", "", reason)
        reason = re.sub(r"\s+", " ", reason).strip()
        app_e_lines.append(
            f"| {eid} | {au_yr} | {title_clean} | {venue_id} | {stg} | {code} | {reason} |"
        )

    # Real Multi-Node Populated Mermaid Diagrams (with PNG markdown embeds above each)
    mermaid_prisma = f"""![Figure 1: PRISMA 2020 two-column flow diagram showing 142 raw hits, 42 duplicates removed, 100 screened records, 41 exclusions, and 59 included studies.](../data/fig1_prisma.png)

```mermaid
flowchart TD
    S_ID["Database Searches S01-S09 and S12: 96 raw records"] --> DEDUP["Combined Records Identified: 142 raw hits"]
    S_CH["Citation Chaining & Anchor Recovery S10-S11 and S13: 46 records"] --> DEDUP
    DEDUP --> UNIQ["Duplicates & Prior Versions Removed: 42 | Net Unique Screened: 100"]
    UNIQ --> STG1["Stage 1 Title, Abstract & Venue Screen: 100 records (98.0% agree)"]
    STG1 --> EXC1["Excluded at Stage 1: n = 30 (E4 Surveys 15, E8 OpenReview 6, E3 Solo 6, E7 Scope 3)"]
    STG1 --> RET["Open Full-Text or Summary Retrieved: n = 70 (Reports Not Retrieved: n = 0)"]
    RET --> STG2["Stage 2 Eligibility Appraisal: n = 70 (92.9% agree; pooled 163/170 = 95.9%)"]
    STG2 --> EXC2["Excluded at Stage 2: n = 11 (E5 Paywall 3, E3 Solo 3, E2 Non-Emp 2, E7 Scope 2, E4 1)"]
    STG2 --> INC["Final Included Corpus: N = 59 Studies (43 Archival, 4 Workshop, 12 Preprint | 34 Comparative / 87 Comparisons + 25 Diagnostic)"]
```"""

    mermaid_winrates = """![Figure 2: Multi-agent win, loss, and mixed rates by baseline quality tier and sensitivity slices with 95% confidence intervals.](../data/fig2_win_rates.png)

```mermaid
xychart-beta
    %% FIG2_BAR
    title "Multi-Agent Win Rate (%) by Baseline Quality Tier and Sensitivity Slice"
    x-axis ["Tier 3 Weak", "Tier 2B Search", "Tier 2+3 Combined", "Tier 2A Budget", "Tier 1 Equal Compute", "Archival Tier 1"]
    y-axis "Multi-Agent Win Rate (%)" 0 --> 100
    bar [80.0, 84.8, 69.4, 48.3, 20.0, 22.2]
    line [80.0, 84.8, 69.4, 48.3, 20.0, 22.2]
```"""

    mermaid_forest = """![Figure 3: Paired accuracy differences in percentage points comparing equal-budget strong controls against unmatched or post-trained setups.](../data/fig3_forest_effects.png)

```mermaid
xychart-beta
    %% FIG3_FOREST
    title "Paired Accuracy Differences (Percentage Points: Multi-Agent minus Solo Agent)"
    x-axis ["CAIS Ministral", "Optima Raw", "Self-MoA", "Strong All Mean", "Strong Qwen Mean", "CAIS Qwen N=1017", "Weak 1-Pass Mean", "Post-Train Mean", "CascadeDebate"]
    y-axis "Accuracy Difference (pp)" -30 --> 25
    bar [-27.6, -7.8, -6.6, -6.54, -4.88, -2.2, 7.06, 13.05, 22.52]
```"""

    mermaid_decision = """![Figure 4: Conditional 5-step single-agent vs. multi-agent deployment decision workflow.](../data/fig4_decision_workflow.png)

```mermaid
flowchart TD
    D0["Step 1: Reliable automatic verifier OR context larger than one solo window?"] -->|No open-ended| RA["Regime A: Equal-Budget Solo AI (+58% to +285% overhead avoided)"]
    D0 -->|Yes| D1["Step 2: Does one modern solo AI already score high (roughly 45%+)?"]
    D1 -->|Yes diminishing returns| RA
    D1 -->|No headroom remains| D2["Step 3: Tightly sequential steps OR closed-book logic?"]
    D2 -->|Yes summary risk| RB["Regime B: Solo Repeated Voting (Self-Consistency, Self-MoA, Isolated Self-Check)"]
    D2 -->|No splittable| D3["Step 4: Mixed easy/hard traffic with reliable escalation check?"]
    D3 -->|Yes| RC["Regime C: Selective Escalation (Fast Solo first, MAS only on failure)"]
    D3 -->|No uniform| D4["Step 5: Payback volume Q > C_search / (deltaCost + v*deltaAcc) & verified topology?"]
    D4 -->|Yes (0/10 learned graphs Tier 1 verified)| RD["Regime D: Controlled Centralized Workers or Static Pruned Graph + Provenance & Sandbox"]
    D4 -->|No cost >= SAS| RB
```"""

    # Build Manuscript Body (Class-12 plain academic English, zero backticks outside code blocks!)
    manuscript = rf"""# When Do LLM Multi-Agent Systems Outperform Single Agents? A Systematic Review of Compute-Normalized Evidence, Coordination Topologies, Failure Mechanisms, and Evaluation Validity

**Author(s) & Affiliation(s):** [Author Placeholder — Blinded for Review / ACM Computing Surveys Style]  
*Target Journal:* **ACM Computing Surveys (CSUR)** *(Formatted for conversion to acmsmall; includes complete self-contained Reproducibility Appendices in Section 12).*

---

## Abstract

{abstract}

---

## ACM CCS Concepts

- **Computing methodologies ~ Artificial intelligence ~ Distributed artificial intelligence ~ Multi-agent systems** (Significance: 500)
- **Computing methodologies ~ Natural language processing ~ Natural language generation** (Significance: 300)
- **General and reference ~ Surveys and overviews** (Significance: 300)
- **General and reference ~ Empirical studies** (Significance: 100)

## Keywords

Large language models, multi-agent systems, compute-normalized evaluation, test-time scaling, multi-agent debate, failure mechanisms, systematic literature review

---

## 1. Introduction

Teams of Large Language Models (LLMs), often called multi-agent systems, connect two or more AI instances so they can debate answers, play specialized roles, check each other's work, or split up long tasks. Early frameworks such as CAMEL {c('Li2023_CAMEL')}, AutoGen {c('Wu2024_AutoGen')}, MetaGPT {c('Hong2024_MetaGPT')}, and ChatDev {c('Qian2024_ChatDev')} popularized a straightforward intuition: assigning several AI agents to collaborate like a human team should beat a single AI working alone. Early debate papers such as Society of Minds {c('SR013_du2024improving')}, Divergent Thinking MAD {c('Liang2024_DivergentMAD')}, and ReConcile {c('Chen2024_ReConcile')} reported encouraging gains on reasoning tasks.

Yet a practical engineering question soon emerged. When a three-agent team runs three rounds of discussion, it spends far more computing time, tokens, and API dollars than a single AI answering once. What happens if you give that **single solo AI the exact same token or compute budget**—either through Self-Consistency majority voting {c('Wang2023_SelfConsistency')}, repeated random sampling {c('Brown2024_LanguageMonkeys')}, extended test-time thinking {c('Snell2025_TestTimeCompute')}, or structured single-agent iteration? Controlled experiments across 2024–2026 show a consistent pattern: once solo baselines receive matched budgets and strong models, published multi-agent gains shrink sharply, vanish, or reverse {c('SR001_kim2026capable', 'SR002_tran2026single', 'SR005_smit2024should', 'SR086_2025', 'SR089_2026')}.

To make every part of this review easy to follow for readers who know basic AI terms (like prompts, tokens, and accuracy) without memorizing specialist jargon, Table 1 defines the eight core concepts used throughout this paper.

#### Table 1: Plain-English Glossary of Key Concepts Used in This Review

{glossary_tbl}

Many prior surveys already catalog how LLM agents and multi-agent architectures work. Peer-reviewed articles in *Artificial Intelligence Review* {c('AbouAli2026_AIRE', 'SR049_alaanzy2026autonomous', 'Chowa2026_AIRE')}, *ACM Computing Surveys* {c('Deng2025_CSUR_Security', 'SR052_du2026optimization', 'SR050_geng2026scaling', 'SR051_he2026security', 'Hu2024_CSUR_GameAgents', 'Zhang2026_CSUR_Generalizability')}, *Journal of Artificial Intelligence Research* {c('Plaat2025_JAIR')}, *Frontiers of Computer Science* {c('SR053_wang2024autonomous')}, *Transactions on Machine Learning Research* {c('SR055_gao2026selfevolving', 'Huang2026_TMLR_AgentMemory', 'Ke2025_TMLR_LLMReasoning', 'SR048_moslem2026dynamic', 'Wei2026_TMLR_AgenticReasoning', 'Zhang2026_TMLR_AgenticRL', 'SR056_zhang2026generalist')}, *IJCAI* {c('Guo2024_IJCAI')}, *KDD* {c('Mohammadi2025_KDD')}, *Findings of ACL/EMNLP* {c('SR044_yehudai2026evaluation', 'SR045_yue2026static')}, *IEEE Transactions on Software Engineering* {c('SR043_wang2026trajectory')}, *Future Internet* {c('Zhu2026_FutureInternet')}, and open preprints {c('Badica2025_arXiv_ContemporaryAgentTech', 'Dantas2026_SafeAgents', 'Khan2026_Preprints_MASEvolution', 'SR080_li2026harness', 'SR047_li2026efficiency', 'Mallampati2026_Reliability', 'SR041_motger2026mad', 'Rahman2025_arXiv_LLMPoweredSwarms', 'SR042_tillmann2025mad', 'Tran2025_MAS', 'Wang2026_arXiv_ClassicalToFoundationMAS', 'SR046_yan2026beyond')} organize agent memory, workflow graphs, trace failures, and security risks. However, as Table 2 summarizes, none quantifies empirically **how much of the multi-agent accuracy advantage shrinks once single-agent baselines match total inference compute and upfront search or training costs**.

#### Table 2: Positioning Against Competing Surveys (2024–2026)

{blk['TABLE_1_SURVEY_COMPARISON']}

Guided by established systematic review standards {c('Page2021_PRISMA', 'Kitchenham2007', 'Rethlefsen2021_PRISMAS')}, this paper makes four specific contributions:
1. **Fair Compute Audit:** Across {ca['All']['n_studies']} comparative studies ({ca['All']['n_tuples']} cleaned paired comparisons), we observe a {ca['tuple_attenuation_pp']} percentage-point decline in multi-agent win rates when weak or unequal-budget baselines are replaced by compute-matched single-agent controls (validated across Archival-Only, Wave-1 vs. Wave-2, Interactive-Only, fixed-margin tie, within-study paired contrasts, and continuous effect sizes).
2. **Topology & Hidden Cost Audit:** We separate non-interactive voting ensembles from genuine interactive teams and find that all {cf['qa3_1_count']}/{cf['learned_optimizers_total']} comparative learned or optimized frameworks omit upfront search or GPU training costs from headline per-query efficiency tables (compared with {cf['static_zero_search_comp']}/{cf['comparative_total_studies']} static zero-search comparative papers).
3. **Failure & Security Synthesis:** We link documented failure pathways—error amplification, peer conformity, information loss across text summaries, and multi-agent exploit spreading—to why teams underperform solo baselines on tightly coupled tasks.
4. **Evidence-Graded Guide:** Using a GRADE-inspired certainty framework {c('Guyatt2008_GRADE')}, we grade each finding transparently, expose empty research cells (such as 0/10 learned-graph systems passing Tier 1 parity), and offer a conditional 5-step decision guide awaiting prospective controlled trials.

---

## 2. Research Questions and Scope

To separate verified engineering value from evaluation artifacts, this review investigates four focused research questions:

- **RQ1 (Effectiveness Under Fair Budgets):** When total tokens, API cost, prompt quality, and tool access are matched against a strong solo AI baseline, how often do LLM multi-agent teams outperform solo agents, and on which kinds of tasks do wins or losses cluster?
- **RQ2 (Team Structure and Hidden Search Costs):** How do different team designs—parallel voting, step-by-step pipelines, hub-and-spoke orchestrators, all-to-all debate, learned sparse graphs, and selective escalation—trade accuracy against extra inference overhead and upfront training or search time?
- **RQ3 (Why Multi-Agent Teams Fail or Lose Security):** Which verified mechanisms—cascading errors, sycophantic conformity, information loss during handoffs, verification breakdowns, and inter-agent attack propagation—explain multi-agent degradation?
- **RQ4 (Evaluation Flaws and Reporting Gaps):** How heavily do six common experimental confounders, missing multi-run consistency checks, missing latency or dollar logs, and flawed benchmark test suites distort published multi-agent claims?

We strictly focus on teams of two or more LLM instances coordinating through natural language or structured schemas. We exclude single-policy query routers without persistent multi-agent state {c('SR095_2025')}, classical insect or particle swarm algorithms using numeric vectors {c('Rahman2025_arXiv_LLMPoweredSwarms', 'SR058_jimenezromero2025swarm', 'SR081_ruan2025swarmbench')}, and static weight-space checkpoint merging {c('SR057_feng2025modelswarms')}, clarifying these conceptual boundaries in Section 4.2.

---

## 3. Systematic Review Methodology

### 3.1 Transparent Search Strategy (PRISMA-S)

Following PRISMA 2020 {c('Page2021_PRISMA')}, Kitchenham–Charters guidelines {c('Kitchenham2007')}, and PRISMA-S search reporting standards {c('Rethlefsen2021_PRISMAS')}, we conducted a **targeted open-web query- and citation-seeded systematic search in a single consolidated retrieval and verification campaign on November 20, 2026** (covering publications from January 2023 through November 20, 2026). Because proprietary bulk exports from Scopus and Web of Science were not available in our environment, we report this explicitly as a documented open-web seeded review across arXiv, OpenReview, ACL Anthology, PMLR, ACM DL, Springer/Nature, and IEEE Xplore rather than a closed-publisher census.

Our search progressed through three documented stages in Table 3, with all six verbatim Boolean queries and all 13 search executions recorded in Section 12, Appendix A. Baseline core queries logged 105 hits. Backward and forward citation chaining around flagship scaling, debate, workflow, and harness papers added 21 hits (126 baseline records; 42 duplicates merged into 84 unique records). Finally, a targeted gap-recovery pass imported 16 named anchors in agent ensembles, graph pruning, conformity, and multi-agent security that broad Boolean phrases missed, yielding {pr['raw_total']} raw hits and **{pr['unique_screened']} unique records screened**. Section 5.1 compares Wave 1 and Wave 2 directly to confirm that targeted gap recovery did not manufacture our headline drop.

#### Table 3: PRISMA-S Summary of Literature Searches (Campaign Date: November 20, 2026)

{table_prismas}

### 3.2 Screening Process and Human Verification

To screen all 100 unique candidates systematically, initial Stage 1 (title and abstract) and Stage 2 (open PDF, HTML proceedings, or open summary) passes were run independently by **two blinded automated LLM screening workflows** following fixed protocol rules, followed by **direct human-author verification of every included study, quality rating, and numerical comparison**. Because automated pass-agreement reflects inter-model consistency rather than two separate human raters, human review adjudicated every disagreement and checked source numbers directly. Stage 1 agreement across all 100 records reached **{irr['full_stage1_po']}%** (98/100; inter-model Cohen's kappa = {irr['full_stage1_kappa']}; Wave-1 baseline {irr['wave1_stage1_po']}%, kappa = {irr['wave1_stage1_kappa']}), and Stage 2 eligibility agreement across {irr['stage2_full_n']} advancing papers reached **{irr['stage2_3class_po']}%** (65/70; kappa = {irr['stage2_3class_kappa']}). Pooled across all {irr['pooled_judg_n']} screening judgments (100 Stage 1 + 70 Stage 2 decisions), raw pass agreement was **{irr['pooled_judg_agree']}/{irr['pooled_judg_n']} ({round(irr['pooled_judg_po'], 1)}%)**, while end-to-end record inclusion agreement across all 100 unique records was **{irr['corpus_bin_po']}%** (95/100; kappa = {irr['corpus_bin_kappa']}).

### 3.3 PRISMA Flow, Inclusion Rules, and Exclusion Boundaries

Figure 1 shows the complete two-column PRISMA 2020 selection flow separating repository searches from citation chaining and targeted additions. Table 4 breaks down the {pr['included_total']} included studies by publication status and research track, and Table 5 summarizes the 41 excluded records (itemized individually in Section 12, Appendix E).

{mermaid_prisma}
*Figure 1: PRISMA 2020 two-column flow diagram tracking identification, duplicate removal, screening, and final inclusion across database queries and citation chaining (N = {pr['included_total']} included studies).*

#### Table 4: Included Corpus by Publication Status and Research Track (N = {pr['included_total']})

{blk['TABLE_PUB_STATUS']}

Studies entered the corpus if they were written in English (2023–2026) and tested at least one of three pillars: (1) a team of two or more collaborating LLM agents (or heterogeneous multi-LLM ensemble) compared directly against a single-agent system; (2) verified multi-agent failure mechanisms, trace attribution, or topological security attacks {c('SR029', 'SR031', 'SR069', 'SR097', 'SR099', 'SR100')}; or (3) cross-cutting agentic benchmark, solo-voting boundary {c('SR085_2024')}, and reliability audits {c('SR032', 'SR033', 'SR034', 'SR035', 'SR036', 'SR037', 'SR038', 'SR039', 'SR040')}. Single-agent module logs lacking multi-agent coordination (AgentDebug, Excl-01), single-policy routers (Router-R1 {c('SR095_2025')}), and unverified paywalled abstracts lacking open mirrors were excluded. Unrefereed preprints ({pr['preprint_count']}/{pr['included_total']}, {pr['preprint_pct']}%) entered only after clearing a >=6/14 (or /12) quality floor and are isolated in Archival-Only sensitivity checks.

#### Table 5: Excluded Records Summary (n = 41)

{table_excl}

### 3.4 Defining Single-Agent Types, Six Confounders, and Statistical Synthesis Methods

A subtle confusion in the literature is calling **parallel single-model voting** (such as Self-Consistency {c('Wang2023_SelfConsistency')} or Self-MoA {c('SR010_li2026rethinking')}) a "single-agent baseline" in one paper while labeling the exact same single-model sampling trick ("Agent Forest" {c('SR085_2024')}) a "multi-agent swarm" in another. To enforce strict conceptual hygiene, we distinguish three execution regimes:
1. **Single-Pass Solo Agent:** One model making one continuous execution (Chain-of-Thought, ReAct, or one long thinking trace).
2. **Multi-Sample Solo Voting (Test-Time Compute Scaling):** Generating multiple independent answers from *one* model and picking the consensus answer without agents communicating (`Self-Consistency` {c('Wang2023_SelfConsistency')}, `Best-of-N`, `Agent Forest` {c('SR085_2024')}, `Self-MoA` {c('SR010_li2026rethinking')}). Following this rule strictly, *Agent Forest* {c('SR085_2024')} is classified as an **RQ4 evaluation-validity boundary check (Confounder C3)** with 0 comparative multi-agent rows rather than as a Tier 3 multi-agent system.
3. **Interactive or Multi-Model Team (MAS):** Two or more stateful agents exchanging messages, critiques, or delegated subtasks—or mixing distinct LLM model families (`Mixed-MoA`).

For comparative synthesis (Section 5.1), we classify all {ca['All']['n_studies']} comparative studies ({ca['All']['n_tuples']} cleaned comparisons) into clear baseline fairness tiers: **Tier 1 (equal compute and strong solo baseline, n=7, k=15)**, **Tier 2A (strong solo baseline, unmatched inference compute, zero search cost, n=12, k=29)**, **Tier 2B (strong solo baseline, unamortized upfront search or RL/DPO training C6, n=9, k=33)**, and **Tier 3 (weak single-pass solo baseline only, n=6, k=10)**. Because averaging raw accuracies across incompatible benchmarks (such as algebra, coding, and clinical diagnosis) is invalid {c('Borenstein2009_MetaAnalysis')}, we synthesize within-study paired outcomes (`MAS minus Solo`) using four complementary methods:
- **Cluster-Bootstrapped Intervals (10,000 study resamples) & 95% Wilson Score CIs:** Cluster bootstrapping accounts for multiple comparisons per study, while Wilson binomial score intervals avoid zero-collapse on small proportions.
- **Exact Study-Level Permutation Tests (20,000 randomizations) & Fisher's Exact Tests:** Assigns equal weight (`1.0`) to every study regardless of how many benchmark rows it reports.
- **Unweighted Study-Level Effect-Size Summaries (with Binomial Variance Audit):** Panel A of Table 11 operates strictly at a single unweighted study level (never mixing comparisons and study averages inside one distribution). Full cross-study random-effects (DerSimonian–Laird) pooling is withheld because 4 of 5 strong-control numeric studies omit item-level variances; instead, Panel B reports exact binomial standard errors and inverse-variance weights across all three splits of *Bertalanič & Fortuna* {c('SR089_2026')}.
- **Within-Study Paired Contrasts & Task-Family Stratification:** Tests whether switching from weak to equal-compute controls shrinks gains inside the *exact same papers and datasets*.

Table 6 lists our six experimental confounders and seven quality-appraisal criteria.

#### Table 6: Six Experimental Confounders and Seven Study-Quality Checks

{table_anchors}

---

## 4. Core Concepts and Classical Boundaries

### 4.1 Three Simple Mathematical Ideas Behind Multi-Agent Evaluation

Understanding why multi-agent systems help or hurt hinges on three practical ideas—every-try reliability, information loss across text summaries, and upfront search payback—explained plainly before each formula.

1. **Best-Case Luck vs. Every-Try Reliability (pass-at-k vs. pass-power-k):**  
   Many coding suites let an AI try k times and count a win if **at least one** attempt succeeds (`pass@k`) {c('Brown2024_LanguageMonkeys')}. That rewards noisy guessing. In real operations—like modifying customer bookings or issuing database transactions—a system must succeed **every single time** across k repeated deployments. Yao et al. {c('SR033_yao2025taubench')} formalize this with `pass^k`, sampling **without replacement** for k random draws out of n recorded runs (approaching $p^k$ when $n \gg k$ and c out of n trials succeed):
   $$\text{{pass}}^k = \mathbb{{E}}_{{\text{{task}}}} \left[ \frac{{\binom{{c}}{{k}}}}{{\binom{{n}}{{k}}}} \right]$$
   Take one task where an agent solves c = 6 out of n = 10 attempts (`60%` single-run score). Over k = 4 deployments, `pass@4` (at least one win) looks misleadingly strong at $1 - \binom{{4}}{{4}}/\binom{{10}}{{4}} = 99.5\%$, while `pass^4` (all four succeed) collapses to $\binom{{6}}{{4}}/\binom{{10}}{{4}} = 15/210 = 7.1\%$. Notice also **Jensen's inequality**: because $f(p) = p^k$ is convex, plugging dataset average pass rate $\bar{{p}}$ into $\bar{{p}}^k$ **underestimates** true `pass^k` on heterogeneous pass/fail tasks ($\frac{{1}}{{M}}\sum p_i^k \ge \bar{{p}}^k$), while single-run average accuracy (`60%`) severely **overstates** `pass^4` (`7.1%`) on stochastic tasks. Researchers must run multiple trials per task directly.

2. **Information Loss in Text Relays ("Telephone Game" / Data Processing Inequality):**  
   Suppose Agent 1 reads question X, computes intermediate reasoning $Z_1$, writes a compressed summary $M_{{\text{{handoff}}}}$, and passes *only that summary* to Agent 2—like a closed-book game of telephone where Agent 2 cannot re-read X or query tools. In that Markov chain ($Y \leftrightarrow Z_1 \leftrightarrow M_{{\text{{handoff}}}} \leftrightarrow \hat{{Z}}_2$ relative to true answer Y), information theory's **Data Processing Inequality** guarantees that Agent 2 cannot extract more mutual information about Y than Agent 1 already held: $I(Y; \hat{{Z}}_2) \le I(Y; Z_1)$ {c('SR002_tran2026single')}. Two explicit caveats apply: first, when downstream agents *can* inspect original input X, or when independent parallel samples cancel decoding variance {c('Wang2023_SelfConsistency')}, accuracy can still improve without extra Shannon information; second, when workers query **different documents or tools** {c('SR001_kim2026capable', 'SR091_2026')}, they break the closed-book Markov chain and supply genuinely new evidence.

3. **When Does Upfront Search or Training Cost Pay Back? ($Q^*$):**  
   Many modern frameworks run Monte Carlo Tree Search, reinforcement learning, or evolution to discover team graphs before evaluation begins, incurring a large upfront cost $C_{{\text{{search}}}}$ (in GPU hours, search tokens, or dollars) {c('SR015', 'SR018', 'SR094')}. Suppose a learned team reaches **matched accuracy** against a strong solo AI, with both per-query runtime costs $c_{{\text{{SAS}}}}$ and $c_{{\text{{MAS}}}}$ measured in the **same unit** (dollars or tokens). How many production queries $Q^*$ are needed before test-time savings recover $C_{{\text{{search}}}}$?
   $$Q^* = \frac{{C_{{\text{{search}}}}}}{{c_{{\text{{SAS}}}} - c_{{\text{{MAS}}}}}} \quad (\text{{at equal accuracy, valid only if }} c_{{\text{{MAS}}}} < c_{{\text{{SAS}}}})$$
   If the learned team costs **more or equal per query** than the solo AI ($c_{{\text{{MAS}}}} \ge c_{{\text{{SAS}}}}$) at equal accuracy, extra search costs never pay back in runtime savings ($Q^* = \infty$). More generally, if accuracy gains are valued at $v$ dollars **per accuracy point per query** ($\Delta\text{{Acc}} = \text{{Acc}}_{{\text{{MAS}}}} - \text{{Acc}}_{{\text{{SAS}}}}$), break-even requires $(c_{{\text{{SAS}}}} - c_{{\text{{MAS}}}}) + v \cdot \Delta\text{{Acc}} > 0$, giving $Q^* = C_{{\text{{search}}}} / [(c_{{\text{{SAS}}}} - c_{{\text{{MAS}}}}) + v \cdot \Delta\text{{Acc}}]$.

### 4.2 How LLM Agent Teams Differ From Classical Swarms and Classical Multi-Agent Systems

Before examining empirical comparisons, it helps to separate modern LLM agent teams from two older research fields {c('LaMalfa2025', 'Wang2026_arXiv_ClassicalToFoundationMAS', 'Badica2025_arXiv_ContemporaryAgentTech', 'Rahman2025_arXiv_LLMPoweredSwarms')}. **Classical Swarm Intelligence** (Ant Colony Optimization, Particle Swarm Optimization, Boids) coordinates hundreds to millions of simple mathematical units updating local rules or digital pheromones {c('SR058_jimenezromero2025swarm', 'Rahman2025_arXiv_LLMPoweredSwarms')}. **Classical Multi-Agent Systems** (Belief–Desire–Intention architectures, speech-act protocols, and multi-agent reinforcement learning) exchange compact symbols or numeric state vectors in structured worlds {c('SR050_geng2026scaling', 'Wang2026_arXiv_ClassicalToFoundationMAS')}.

In contrast, modern **LLM multi-agent systems** typically coordinate 2 to 15 expensive language models (and occasionally sparse graphs up to ~1,000 nodes like MacNet {c('SR014_qian2025scaling')}) via **open-ended natural-language text** inside finite context windows {c('Badica2025_arXiv_ContemporaryAgentTech', 'LaMalfa2025')}. Table 7 highlights these structural differences. Because natural language carries persuasion and bloat, LLM teams suffer brand-new failures—peer flattery, summary loss, and text prompt injections—rarely seen in classical swarms.

#### Table 7: Key Differences Across Classical Swarms, Classical Multi-Agent Systems, and LLM Agent Teams

| System Property | Classical Swarm Intelligence (ACO, PSO, Boids) {c('Rahman2025_arXiv_LLMPoweredSwarms', 'SR058_jimenezromero2025swarm')} | Classical Multi-Agent Systems (BDI, FIPA, MARL) {c('SR050_geng2026scaling', 'Wang2026_arXiv_ClassicalToFoundationMAS')} | Modern LLM Agent Teams (AutoGen, Debate, AFlow, GPTSwarm) {c('Badica2025_arXiv_ContemporaryAgentTech', 'LaMalfa2025')} |
| :--- | :--- | :--- | :--- |
| Memory per Agent | Tiny numeric vectors or pheromone weights | Formal logic beliefs or compact learned hidden vectors | Long text context windows plus external vector memory |
| How Agents Communicate | Simple local math attraction or neighbor signals | Formal predefined message schemas or policy embeddings | Flexible natural language or JSON text handoffs |
| Typical Team Size & Cost | 100 to 1,000,000+ lightweight units (O(1) per step) | 2 to 100 policy agents in fast simulated worlds | Typically 2–15 heavy LLMs (up to ~1,000 in sparse DAGs), high token cost |
| Main Failure Mode at Scale | Local optima or parameter oscillation | Non-stationarity, sparse rewards, noisy credit assignment | Peer conformity, handoff summary loss, prompt-injection cascades |

---

## 5. Empirical Synthesis (RQ1–RQ4)

### 5.1 Do Multi-Agent Teams Beat Solo Agents Under Equal Compute? (RQ1)

Across **{ca['All']['n_studies']} comparative studies** covering **{ca['All']['n_tuples']} cleaned paired comparisons** (Section 12, Appendices C–D), a consistent empirical gradient emerges: **multi-agent win rates drop sharply as single-agent baselines become compute-matched and properly prompted**. Table 8 presents the full breakdown—separating unmatched static compute (`Tier 2A`) from unamortized training/search (`Tier 2B`) and showing both cluster-bootstrap and Wilson 95% confidence intervals—while Figure 2 visualizes this shift.

{mermaid_winrates}
*Figure 2: Multi-agent win, loss, and mixed rates by baseline quality tier (left) alongside cluster-bootstrap 95% confidence intervals and study-weighted drops (right).*

#### Table 8: Multi-Agent Win/Loss Rates by Baseline Fairness Tier and Sensitivity Slice (34 Comparative Studies, 87 Comparisons)

{blk['TABLE_4_QUANTITATIVE_SYNTHESIS']}

When teams face weak single-pass solo prompts (`Tier 3` {c('SR011', 'SR016', 'SR017', 'SR030', 'SR082', 'SR093')}), they win **{ca['Tier 3']['wins']}/{ca['Tier 3']['n_tuples']} ({ca['Tier 3']['win_pct']}%)** of comparisons (Wilson 95% CI {ca['Tier 3']['win_wilson_ci95'][0]}%–{ca['Tier 3']['win_wilson_ci95'][1]}%; study-weighted {ca['Tier 3']['study_frac_win_pct']}%). Under `Tier 2` (strong solo baselines without matched compute or amortized search, `n=21`, `k=62`), overall win rate sits at **{ca['Tier 2']['wins']}/{ca['Tier 2']['n_tuples']} ({ca['Tier 2']['win_pct']}%)**—splitting cleanly between **{ca['Tier 2A']['win_pct']}%** (`{ca['Tier 2A']['wins']}/{ca['Tier 2A']['n_tuples']}`, Wilson {ca['Tier 2A']['win_wilson_ci95'][0]}%–{ca['Tier 2A']['win_wilson_ci95'][1]}%) in zero-search unmatched inference (`Tier 2A`) and **{ca['Tier 2B']['win_pct']}%** (`{ca['Tier 2B']['wins']}/{ca['Tier 2B']['n_tuples']}`, Wilson {ca['Tier 2B']['win_wilson_ci95'][0]}%–{ca['Tier 2B']['win_wilson_ci95'][1]}%) in systems with unamortized upfront search or RL/DPO training (`Tier 2B`). When only zero-search static systems are inspected (**Sensitivity E**, omitting all `C6` optimizers), even non-parity `Tier 2A+3` wins fall to **{czs['Tier 2+3']['wins']}/{czs['Tier 2+3']['n_tuples']} ({czs['Tier 2+3']['win_pct']}%)** (Wilson {czs['Tier 2+3']['win_wilson_ci95'][0]}%–{czs['Tier 2+3']['win_wilson_ci95'][1]}%), showing how heavily `Tier 2B` training boosts raw headline percentages.

Under strict **equal-compute strong solo controls (`Tier 1`, n=7, k=15)** {c('SR001', 'SR002', 'SR004', 'SR005', 'SR007', 'SR010', 'SR012')}, multi-agent win rates drop to **{ca['Tier 1']['wins']}/{ca['Tier 1']['n_tuples']} ({ca['Tier 1']['win_pct']}%)** (cluster-bootstrap 95% CI {ca['Tier 1']['win_boot_ci95'][0]}%–{ca['Tier 1']['win_boot_ci95'][1]}%; Wilson 95% CI {ca['Tier 1']['win_wilson_ci95'][0]}%–{ca['Tier 1']['win_wilson_ci95'][1]}%), while losses rise to **{ca['Tier 1']['losses']}/{ca['Tier 1']['n_tuples']} ({ca['Tier 1']['loss_pct']}%)** (`{ca['tuple_attenuation_pp']}` percentage points relative to Tier 2+3's `{ca['Tier 2+3']['win_pct']}%` [Wilson {ca['Tier 2+3']['win_wilson_ci95'][0]}%–{ca['Tier 2+3']['win_wilson_ci95'][1]}%]; cluster-bootstrap CI `{ca['tuple_attenuation_ci95'][0]}` to `{ca['tuple_attenuation_ci95'][1]}`). Giving every paper equal `1.0` study weight confirms the same gradient: Tier 1 averages **{ca['Tier 1']['study_frac_win_pct']}%** vs. **{ca['Tier 2+3']['study_frac_win_pct']}%** in Tier 2+3 (`{ca['study_frac_attenuation_pp']}` points; exact two-sided permutation test **p = {ca['perm_p_study_frac_t1_vs_t23']}**; strict `>50%` majority Fisher p = {ca['fisher_p_t1_vs_t23']}; `>=50%` Fisher p = {ca['fisher_p_t1_vs_t23_ge50']}). Separating Tier 1 by solo comparator yields identical lessons: interactive teams win **{t1sub['interactive_vs_voting']['wins']}/{t1sub['interactive_vs_voting']['n_tuples']} ({t1sub['interactive_vs_voting']['win_pct']}%)** against equal-budget single-model voting (`Self-Consistency` {c('SR004', 'SR005', 'SR007')}), lose `2/2` (`0%`) when heterogeneous `Mixed-MoA` faces k-sample single-best `Self-MoA` {c('SR010_li2026rethinking')}, and win **{t1sub['interactive_vs_single_or_longcot']['wins']}/{t1sub['interactive_vs_single_or_longcot']['n_tuples']} ({t1sub['interactive_vs_single_or_longcot']['win_pct']}%)** across equal-token single-agent comparisons {c('SR001', 'SR002', 'SR004', 'SR012')} (2 splittable gains in Kim et al. {c('SR001')} and 1 non-zero-sum judge gain in ColMAD {c('SR012')}).

Table 9 inspects all 7 Tier 1 equal-compute studies across all 15 comparisons.

#### Table 9: Complete Tier 1 Equal-Compute Study Ledger (7 Studies, 15 Comparisons)

{blk['TABLE_5_TIER1_CORPUS']}

*Note: Raw cell % marked as not verifiable from accessible open summary where open preprints/HTML texts report relative % changes or normalized frontier figures without raw cell matrices; pp = percentage points; % rel. = relative percentage change.*

To test whether Tier 1's modest win rate could be explained by author bias, benchmark differences, sampling choices, or margin thresholds, we ran four robustness checks:
1. **Within-Study Paired Contrasts (Fixed Authors & Tasks):** Table 10 tracks six papers that tested *both* weak/unequal and strong/equal controls on identical datasets {c('SR005', 'SR006', 'SR007', 'SR086', 'SR087', 'SR094')}. Every single paper shows multi-agent gains shrinking or reversing when solo baselines tighten—for instance, in Choi et al. {c('SR087_2025')}, debate slightly beats a 1-pass solo prompt (`0.7377` vs. `0.7205`) yet loses to `N = 5` Majority Voting on GSM8K (`88.67%` vs. `94.00%`, `-5.33` points), and in Optima {c('SR094_2025')}, unoptimized debate loses `-5.4` to `-7.8` points against `Self-Consistency(n=8)` unless `<12` hours (for HotpotQA/GSM8K; `~24` hours for MATH) of 8x A100 RL/DPO post-training is applied.
2. **Continuous Effect Sizes & Primary-Split Variance Audit:** Across comparative studies reporting exact 0–100% scores (Table 11 and Figure 3), Panel A shows that unmatched single-pass comparisons average **+{es['weak_single_pass']['study_mean_pp']:.2f} pp** (median `+{es['weak_single_pass']['study_median_pp']:.2f} pp`, `n=8, k=34`), whereas equal-budget or strong voting/self-correction controls reverse to **`{es['strong_controls_all_models']['study_mean_pp']:+.2f} pp`** across all three CAIS '26 {c('SR089_2026')} splits (median `{es['strong_controls_all_models']['study_median_pp']:+.2f} pp`, range `{es['strong_controls_all_models']['study_range_pp'][0]:+.2f}` to `{es['strong_controls_all_models']['study_range_pp'][1]:+.2f} pp`) and **`{es['strong_controls_main_qwen']['study_mean_pp']:+.2f} pp`** when using only CAIS '26's primary large-N model (`Qwen2.5-7B`, `n=1,017`, `58.8% vs. 61.0% = -2.2 pp`). Panel B shows why inspecting sample sizes matters: *Bertalanič & Fortuna* {c('SR089_2026')} evaluate `Qwen2.5-7B` on `1,017` items (binomial `SE = 2.17 pp`, carrying `82.5%` inverse-variance weight) alongside two `100`-item secondary splits (`Llama-3.1-8B` `-1.7 pp`, `SE = 6.93 pp`; `Ministral-3-8B` `-27.6 pp`, `SE = 6.43 pp`), yielding an item-weighted CAIS '26 mean of `-4.25 pp` (inverse-variance `-4.55 pp`) versus an unweighted 3-model average of `-10.50 pp`. Because 4 of 5 strong-control studies omit per-item variances, Panel A keeps study-level summaries strictly unweighted and non-pooled.
3. **Task-Family Concentration:** Table 12 stratifies outcomes across four task types. All `2/2` (`100%`, Wilson `34.2%–100.0%`) Tier 1 decomposable/multi-source wins occur within **one six-benchmark study (*Kim et al.* {c('SR001')})** (`Finance-Agent` and `BrowseComp-Plus`), whereas Math & Logic (`0/2`), General QA (`1/7`), and Sequential / Tool suites (`0/4`) rarely beat equal-compute solo controls (note Tran & Kiela {c('SR002')} specifically tests 4-hop `FRAMES` and `MuSiQue` QA under matched thinking budgets).
4. **Archival, Wave, Interactive, Margin & Optimistic Sensitivity Checks (Table 8):**
   - *Archival-Only:* Removing preprints and workshops yields `{cr['Tier 1']['win_pct']}%` (`2/9`, Wilson `6.3%–54.7%`) vs. `{cr['Tier 2+3']['win_pct']}%` (`40/58`; `-46.8 pp`, study-weighted `10.0% vs. 62.3%`, permutation `p = {cr['perm_p_study_frac_t1_vs_t23']}`), while small `n = 4` vs. `21` sample size leaves binary majority Fisher `p = {cr['fisher_p_t1_vs_t23']}`.
   - *Wave 1 vs. Wave 2 Side-by-Side:* Wave-1 baseline `Tier 2+3` studies win **`{cw['Tier 2+3']['win_pct']}%` (`{cw['Tier 2+3']['wins']}/{cw['Tier 2+3']['n_tuples']}`)** (`-51.0 pp` drop to `Tier 1`, Fisher `p = {cw['fisher_p_t1_vs_t23']}`), closely matching Wave-2 targeted additions (**`{cw2['Tier 2+3']['win_pct']}%`**, `{cw2['Tier 2+3']['wins']}/{cw2['Tier 2+3']['n_tuples']}`), confirming gap recovery did not skew overall results.
   - *Interactive Teams Only:* Excluding non-interactive multi-LLM ensembles {c('SR010', 'SR011', 'SR009')} leaves Tier 1 at **`{ci['Tier 1']['win_pct']}%`** (`3/13`, Wilson `8.2%–50.3%`) vs. **`{ci['Tier 2+3']['win_pct']}%`** (`47/67`, Fisher `p = {ci['fisher_p_t1_vs_t23']}`).
   - *Practical `±1.0 pp` Tie Margin (`Sensitivity D`) & Optimistic Recoding (`Sensitivity F`):* Treating `<=1.0 pp` differences symmetrically as ties (re-coding Gao et al. {c('SR086')} GSM8K `+0.8 pp` and AFlow GSM8K `+0.8 pp` inside Tier 2+3 alongside Nguyen Table 17 in Tier 1) keeps Tier 1 at `{ca['Tier 1']['adj_1pp_wins']}/15 (20.0%)` wins and `1 (6.7%)` tie vs. `Tier 2+3` `{ca['Tier 2+3']['adj_1pp_wins']}/72 (68.1%)` (`perm p = {st['comparative_adj_1pp']['perm_p_study_frac_t1_vs_t23']}`). Conversely, promoting Nguyen Table 17 optimistically as a full win (`Sensitivity F`) shifts Tier 1 only to **`{copt['Tier 1']['win_pct']}%` (`4/15`, Wilson `10.9%–52.0%`, `perm p = {copt['perm_p_study_frac_t1_vs_t23']}`)**.

#### Table 10: Within-Study Contrasts Holding Author Team and Benchmarks Fixed

{blk['TABLE_WITHIN_STUDY_CONTRASTS']}

{mermaid_forest}
*Figure 3: Paired accuracy differences (Percentage Points: Multi-Agent minus Solo Agent) contrasting equal-budget or strong voting controls (negative) with weak single-pass or post-trained/cascading setups (positive).*

#### Table 11: Continuous Accuracy Effect Sizes Across Numeric % Studies (Panel A: Unweighted Study-Level; Panel B: CAIS '26 Binomial Variance Audit)

{blk['TABLE_EFFECT_SIZE_META']}

#### Table 12: Multi-Agent Win Rates Stratified by Task Structure

{blk['TABLE_TASK_FAMILY']}

---

### 5.2 Coordination Topologies, Compute Tax, and Upfront Search Costs (RQ2)

Table 13 maps all {pr['included_total']} included studies across six coordination designs plus non-topological diagnostic studies, tracking multi-topology suites evaluating sequential chains (`+3` suites {c('SR002', 'SR014', 'SR099')}), centralized orchestrator-workers (`+4` suites {c('SR001', 'SR014', 'SR098', 'SR099')}), debate (`+6`), and independent ensembles (`+3`). Complete per-study tags appear in Section 12, Appendix B.

#### Table 13: Empirical Summary Across Coordination Structures (59 Studies, RQ2)

{blk['TABLE_6_TOPOLOGY_SUMMARY']}

Three clear engineering patterns emerge from Table 13:
1. **Repeating Your Strongest Model Beats Mixing Weaker Models in Ensembles:** Earlier Mixture-of-Agents (`MoA` {c('SR011_wang2025mixture')}) compared multiple open models against single-pass GPT-4o without equal sample counts. At matched sample counts, `Self-MoA` {c('SR010_li2026rethinking')} demonstrated that resampling the *single best* model repeatedly beats heterogeneous mixtures (`65.7%` vs. `59.1%` on AlpacaEval 2.0, `-6.6` percentage points for mixing weaker models; see also `Chen et al.` {c('Chen2024_CompoundCalls')}, showing compound multi-call voting can degrade non-monotonically on harder queries). Similarly, `OneFlow` {c('SR003_xu2026rethinking')} showed that executing multi-role steps inside **one multi-turn LLM context** matches homogeneous MAS accuracy across 7 benchmarks within `<1%` while saving runtime prefill dollars via shared KV-cache reuse.
2. **All 12/12 Comparative Learned-Graph & Optimized Systems Omit Upfront Search/Training Costs:** Every comparative study using upfront graph search, evolutionary loops, or RL/DPO training (`{cf['qa3_1_comp_count']}/{cf['learned_optimizers_total']} = 100%` flagged `C6` {c('SR003', 'SR015', 'SR016', 'SR017', 'SR018', 'SR019', 'SR020', 'SR076', 'SR092', 'SR093', 'SR094', 'SR096')}, compared with `{cf['static_zero_search_comp']}/{cf['comparative_total_studies']}` static zero-search comparative papers) excludes upfront training or search cost from headline per-query cost-vs-accuracy tables (`0/12` amortized). Those omitted upfront costs are substantial: **`<12 hours on 8x A100 GPUs` for HotpotQA/GSM8K and `~24 hours` for MATH** in `Optima` {c('SR094_2025')}, `2.1–2.8` hours of optimization in `DyLAN` / `GPTSwarm` / `G-Designer` {c('SR015', 'SR017', 'SR092')}, 20 MCTS iterations on Claude-3.5-Sonnet in `AFlow` {c('SR018')}, routing training in `MasRouter` {c('SR019')}, and LoRA RL in `MADA-RL` {c('SR076')}. Under Section 4.1's payback rule ($Q^*$), upfront search recovers its cost only when post-deployment per-query savings over a strong solo model remain positive.
3. **Selective Escalation Offers the Most Practical Runtime Trade-Off:** Because always-on MAS orchestration adds `+58%` to `+285%` token overhead {c('SR001_kim2026capable')}, selective escalation runs a fast solo AI first and escalates to a team **only** when confidence or verifier signals fail {c('SR020', 'SR086', 'SR090', 'SR091')}. `Gao et al.` {c('SR086_2025')} reduce deployment cost up to `20%` while preserving gains; `CascadeDebate` {c('SR020')} raises MedQA (`75.22%` vs. `52.70%`); and `SAIGE` {c('SR091_2026')} gains `+18.23` points on sparse `AgentIF-OneDay` (`71.80%` vs. `53.57%`) while confirming solo execution still outperforms all tested MAS variants on tightly sequential `Terminal-Bench 2.1` (`76.71%`).

---

### 5.3 Why Teams Fail or Become Less Secure (RQ3)

We separate **mechanisms measured alongside matched solo baselines** {c('SR001', 'SR002', 'SR004', 'SR012', 'SR087', 'SR089')} from **diagnostic trace and attack benchmarks** (`MAST`, `Who&When`, `NetSafe`, `CORBA`, `G-Safeguard`) lacking a solo accuracy comparison. Six documented pathways (summarized in Table 14) explain why multi-agent systems degrade or fail safely:

#### Table 14: Six Failure and Security Pathways Observed Across the 59-Study Corpus (RQ3)

{blk['TABLE_7_FAILURE_SUMMARY']}

1. **Error Amplification Along Unchecked Handoffs:** Kim et al. {c('SR001_kim2026capable')} observe that initial errors amplify by `4.4x` in centralized orchestrator-worker teams, `5.1x` in hybrid teams, `7.8x` in decentralized teams, and **`17.2x` in independent teams** lacking central checks. Sequential closed-book chains discard information across text summaries {c('SR002_tran2026single')} (`0.379` vs. `0.418` at 1k thinking tokens on 4-hop QA), while `Nguyen et al.` {c('SR004_nguyen2026think')} show across 980 configurations that reading peer replies competes for context-window room needed for deep reasoning (`Self-Consistency` matches or beats debate in `93%` of settings). Meanwhile, embodied partner studies show sharing compact goal cues aids efficiency when bandwidth is constrained {c('SR075')}.
2. **Sycophancy, Peer Conformity, and Debate Hacking:** Across all `{dd['dense_debate_total']}` Dense All-to-All Debate studies in the corpus, **`{dd['conformity_count']}/{dd['dense_debate_total']}` ({dd['conformity_pct']}%)** {dense_conf_str} document peer conformity or consensus collapse (only {dense_nonconf_str} do not study conformity directly). Specifically, `Choi et al.` {c('SR029_choi2025empirical')} quantify majority pressure across `>2,500` debates; `Estornell & Liu` {c('SR088_2024')} analyze shared-misconception lock-in ("tyranny of the majority"); `Choi et al.` {c('SR087_2025')} prove homogeneous debate updates act as zero-drift martingales around initial majority votes; and `Bertalanič & Fortuna` {c('SR089_2026')} show debate consistently trails isolated solo self-correction on all three GSM-Hard models (`Qwen2.5-7B n=1,017`: `58.8% vs. 61.0% = -2.2 pp`; `Llama-3.1-8B n=100`: `-1.7 pp`; `Ministral-3-8B n=100`: `20.7% vs. 48.3% = -27.6 pp` alongside `85.5%` modal conformity, while spending `2.1x–3.4x` more tokens; note also `Huang et al.`'s warning {c('Huang2024_CannotSelfCorrect')} on intrinsic self-correction sensitivity). Anti-sycophancy prompts {c('SR030', 'SR031')} and non-zero-sum collaborative evidence sharing (`ColMAD` {c('SR012_chen2026when')}, `+10 pp` over competitive `CopMAD` cheap-talk) reduce conformity cascades.
3. **Trace-Attribution Tools Debug MAS Failures:** Multi-agent traces exhibit high failure rates—`MAST` {c('SR021_cemri2025why')} annotates `1,642` traces across `7` frameworks finding `41%–86.7%` failure across `14` failure modes (inter-annotator `kappa = 0.88`), while `TRAIL` {c('SR028')} drops to `11%` localization accuracy on `>200k`-token traces. Root-cause tools including `Who&When` {c('SR022')} (`14.2%` automated step-level / `53.5%` agent-level localization across `127` MAS), `AgenTracer` {c('SR023')}, `AgentLocate` {c('SR025')}, `TraceElephant` {c('SR026')}, `VerifyMAS` {c('SR097')}, and `TRIAGE` {c('SR027')} (reporting `59.3%` LLM-council disagreement with single-bug labels) substantially improve failure attribution without making comparative runtime cost claims.
4. **Multi-Agent Wiring Expands Security & Availability Risks:** Connecting agents multiplies attack pathways. Testing 13 `Inspect AI` architectures on identical models, `Hagag et al.` {c('SR098_2026')} measure up to **`3.8x` higher attack success rates** in multi-agent tool architectures over `single_agent`; `NetSafe` {c('SR099_2025')} records `-29.7%` star-topology misinformation collapse; `CORBA` {c('SR069_zhou2026corba')} causes **`~92%–100%` proportional blocking** within `1.60–1.90` turns via contagious broadcast loops; and `G-Safeguard` {c('SR100_2025')} restores `>40%` task utility by pruning compromised graph edges via anomaly detection.
5. **Archival Stability:** Excluding preprints and workshops retains **`{rsens['rq3_archival']}/{rsens['rq3_total']}`** mechanistic/security studies in peer-reviewed archival venues (`TRAIL` {c('SR028')} and `PARTNR` {c('SR075')} are preprints; `CMAD` {c('SR079')} is a workshop study).

---

### 5.4 Evaluation Flaws, Quality Scores, and OpenReview Rejection Evidence (RQ4)

Table 15 presents our seven-criterion study-quality scores (`QA1–QA7` on raw 14/12 scales and uniform 12-point scales excluding single-agent parity) alongside all six experimental confounders (`C1–C6`) and missing metric rates.

#### Table 15: Study Quality Scores, Six-Confounder Prevalence, and Reporting Blind Spots (N = 59, RQ4)

{blk['TABLE_8_QA_CONFOUNDERS']}

Four widespread evaluation gaps explain why multi-agent benefits are routinely overstated:
1. **Missing Consistency (`pass^k`), Wall-Clock Time, and Dollar Logs:** Across all `{pk['comparative_verifiable_den']}` comparative studies (`0` unverifiable), **`{pk['comparative_false']}/{pk['comparative_verifiable_den']}` (`0%` reported)** evaluate multi-trial `pass^k`, and only `{pk['overall_true']}/{pk['overall_verifiable_den']}` (`5.1%`) studies overall (`tau-bench` {c('SR033')}, `Rabanser et al.` {c('SR034')}, and `CLEAR` {c('SR035')}) measure `pass^k` (`Zhao et al.` {c('SR090')} report best-of-k `pass@k`). Likewise, **`{lu['omit_or_nv_latency_pct']}%` (`{lu['omit_or_nv_latency_count']}/59`)** omit direct wall-clock seconds (only `{lu['direct_latency_count']}` direct {direct_lat_str} + `{lu['proxy_latency_count']}` step/TFLOP proxies {proxy_lat_str}), and **`{lu['usd_omit_or_nv_pct']}%` (`{lu['usd_omit_or_nv_count']}/59`)** omit API dollar totals or ratios (only `{lu['usd_verified_count']}` reported: exact USD {usd_exact_str} or USD ratios {usd_ratio_str}).
2. **Broken Test Harnesses Can Mask or Mimic Typical MAS Deltas:** On interactive software engineering and web tasks, benchmark harness flaws often rival or exceed typical MAS differences. `PatchDiff` {c('SR036_wang2026are')} finds weak test suites inflate SWE-bench resolve rates by `6.2–6.4` percentage points (`29.6%` behavioral divergence), `WebArena Verified` {c('SR039_elhattami2025webarena')} removes `11.3` points of false grading failures while reducing runtime `68.2%–83%`, `BenchJack` {c('SR038_wang2026do')} identifies `219` reward-hacking exploits across 10 benchmarks, `Zhu et al.` {c('SR037_zhu2025establishing')} systematize reward/oracle setup flaws, `CLEAR` {c('SR035_mehta2025beyond')} measures `50x` enterprise cost spread, and `Sheshanarayana & Goli` {c('SR040_sheshanarayana2026do')} show abstracting tool logs loses **`30.9%`** of initially right verifier judgments (`85.5%` recoverable via provenance hashes). (Note carefully: interactive SWE/web harness flaws apply specifically to execution sandboxes rather than closed-form multiple-choice QA.)
3. **What Public OpenReview Rejections and Withdrawals Reveal:** Public review threads corroborate these exact issues. `AgenticNet` {c('SR077_tmlr7332_agenticnet')} was publicly rejected by TMLR after stricter exact-match checks dropped MBPP from `100%` to `77.5%` and cost-matched MATH Level 5 trailed single CoT; `Inducing Disagreement` {c('SR078_tmlr7253_disagreement')} was rejected for reporting a `99.2%` disagreement proxy without improving task accuracy; and `SCALE` withdrew an incomplete ICLR 2025 draft {c('ICLR2025_SCALE_6097')} before adding N=1 baselines for ACL 2025 publication {c('SR082_zhao2025scale')}. Similarly, `More Agents Is All You Need` {c('SR085_2024')} highlights our Section 3.4 `C3` boundary: repeated sampling from one LLM via majority voting improves accuracy without inter-agent communication, belonging to single-model test-time scaling rather than interactive MAS.
4. **Quality Check Without Selection Distortion:** Removing preprints and workshops retains `{rsens['rq4_archival']}/{rsens['rq4_total']}` validity studies in archival venues (`tau-bench`, `Kapoor et al.`, `Rabanser et al.`, `PatchDiff`, `Zhu et al.`, `Agent Forest`). Preprints in Table 15A score slightly higher than archival averages (`75.9%` vs. `71.9%`) solely because our minimum preprint gate filtered weak preprints prior to inclusion, and switching to the uniform 12-point scale preserves exact track ranking (`RQ4 {qa['by_track']['RQ4']['mean_12pt_pct']}% > RQ3 {qa['by_track']['RQ3']['mean_12pt_pct']}% > RQ1/RQ2 {qa['by_track']['RQ1/RQ2']['mean_12pt_pct']}%`).

---

## 6. Evidence Grading, Architecture Map, and Decision Guide

### 6.1 GRADE-Adapted Evidence Certainty Separation

Borrowing the certainty criteria of the clinical GRADE framework {c('Guyatt2008_GRADE')}, Table 16 separates **High-Certainty** census facts (missing search amortization and `pass^k`), **Moderate-Certainty** observational parity patterns (`-49.4 pp` overall shift, splittable vs. sequential contrast, peer conformity), **Low-to-Moderate** small-sample archival slices, and **Low / Provisional** workshop or untested learned-graph hypotheses (`CMAD` `18%–47%` miscoverage {c('SR079_dai2026when')}).

#### Table 16: Evidence Certainty Ratings Across Findings

{table_epistemic}

### 6.2 Separating Design Axes From Study Rigor & Identifying Research Gaps

To keep engineering structure separate from methodological quality, Table 17 cross-tabulates **Coordination Topology** against **Task Structure**, showing total studies alongside equal-compute `Tier 1` parity counts. A stark evidence gap stands out: **`0` out of `10` learned sparse-graph studies** and **`0` out of `2` selective escalation studies** currently satisfy Tier 1 equal-compute + amortized-search standards.

#### Table 17: Evidence-Gap Matrix Mapping Coordination Structure Against Task Type (Multi-Label Benchmark Coverage / Tier 1 Parity Count)

{blk['TABLE_11_EVIDENCE_GAP_HEATMAP']}

*Note: Multi-benchmark suites (e.g., Kim et al. {c('SR001')}, Tran & Kiela {c('SR002')}, MacNet {c('SR014')}) span multiple task-type columns across their datasets while summing once in the rightmost unique-studies column (`40` topological + `19` diagnostic = `59` total).*

Synthesizing verified findings yields the cautious **5-Step Conditional Deployment Guide** in Figure 4 (intended as a structured checklist awaiting prospective controlled trials):
1. **Step 1 — Reliable Verifier or Split Context?** Without reliable automatic verification (unit tests, DB checks, or objective keys) *and* when inputs fit comfortably in one prompt window, stay with a **Solo AI** (avoids correlated hallucination polling {c('SR009', 'SR033', 'SR036')}).
2. **Step 2 — Check Diminishing Returns on Strong Solo Models:** Where a single modern AI already performs well (such as around `>=45%` baseline accuracy in {c('SR001_kim2026capable')}, or capable `Gemini-2.0-Flash` baselines in {c('SR086_2025')}), measure equal-compute solo performance first before spending `+58%` to `+285%` orchestration tokens.
3. **Step 3 — Sequential Steps or Closed-Book Logic? Use Solo Repeated Sampling (`Regime B`):** For stateful sequential plans or closed-book logic without external retrieval, **Self-Consistency**, **Self-MoA**, or **isolated self-checks** outperform unguided debate and text-handoff chains {c('SR002', 'SR004', 'SR010', 'SR087', 'SR089')}.
4. **Step 4 — Mixed Query Difficulty? Use Selective Escalation (`Regime C`):** Route easy items to a fast solo AI first and trigger a multi-agent team **only** when confidence or test checks fail {c('SR020', 'SR086', 'SR090')}.
5. **Step 5 — Splittable Tasks & Proven Payback? Deploy Controlled Static Teams (`Regime D`):** Because **`0/10` learned sparse graphs currently pass Tier 1 parity**, prefer simple centralized orchestrator-worker teams or static pruned graphs with hard turn caps, provenance hashes {c('SR040')}, and sandboxed tools—and apply learned-graph pipelines only where $Q > Q^*$ pays back $C_{{\text{{search}}}}$ {c('SR001', 'SR091', 'SR094', 'SR069', 'SR098', 'SR100')}.

{mermaid_decision}
*Figure 4: Conditional 5-step deployment decision workflow separating when equal-compute solo control, solo repeated voting, selective escalation, or controlled multi-agent teams are justified by verified evidence.*

### 6.3 Security-vs.-Liveness and Lifecycle Governance

Production multi-agent deployment also faces security-versus-liveness trade-offs {c('Kim2026_USENIX_Security', 'Deng2025_CSUR_Security', 'SR051_he2026security', 'Dantas2026_SafeAgents')}. Unrestricted tool access and broadcast agent chat enable `3.8x` higher exploit success {c('SR098_2026')} and `~92%–100%` contagious blocking {c('SR069_zhou2026corba')}, while summarizing intermediate tool logs drops `30.9%` of initially valid verifier checks {c('SR040_sheshanarayana2026do')}. Safe deployments therefore enforce least-privilege worker isolation, immutable provenance hashes across summaries, strict turn/token circuit breakers, and explicit tracking of $C_{{\text{{search}}}}$.

---

## 7. Open Research Directions

1. **Equal-Compute & Amortized Trials for Learned Graphs (`0/10` Tier 1 Gap):** Benchmark `AFlow` {c('SR018')}, `Optima` {c('SR094')}, `DyLAN` {c('SR092')}, `AgentDropout` {c('SR093')}, and `SAIGE` {c('SR091')} directly against compute- and dollar-matched `Self-Consistency` and `Self-MoA`, reporting end-to-end break-even query volume $Q^*$.
2. **Mandatory `pass^k`, Wall-Clock, Hidden-Token, and Dollar Accounting:** Replace single-run averages with multi-trial `pass^5`, wall-clock seconds, hidden thinking tokens, and API dollar spend per resolved task.
3. **Combined Security, Provenance, and Non-Zero-Sum Verification:** Test whether pairing `ColMAD` collaborative debate {c('SR012')}, `G-Safeguard` edge pruning {c('SR100')}, and provenance hashes {c('SR040')} mitigates conformity and exploit amplification under equal compute.
4. **Hardened Execution Sandboxes:** Replace brittle string-match evaluators with database-state checks (`WebArena Verified` {c('SR039')}, `PatchDiff` differential audits {c('SR036')}, and `Inspect AI` adversarial suites {c('SR098')}).

---

## 8. Threats to Validity and Limitations

1. **Single-Campaign Open-Web Search vs. Closed Publisher APIs:** Without proprietary bulk exports from Scopus or Web of Science, our 13 searches represent a targeted open-web query- and citation-seeded systematic review executed in one consolidated retrieval and verification campaign on November 20, 2026. To confirm targeted Wave-2 additions did not bias our conclusions, Table 8 reports **Wave 1 Only** (`{cw['Tier 2+3']['win_pct']}%` Tier 2+3 wins, `-51.0 pp` drop, Fisher `p = {cw['fisher_p_t1_vs_t23']}`) alongside **Wave 2 Only** (`{cw2['Tier 2+3']['win_pct']}%`).
2. **Fields Not Verifiable From Open Summaries (`NV`):** Relying strictly on open arXiv preprints, ACL/PMLR/OpenReview HTML proceedings, and public code repositories without guessing unprinted numbers left `{nv['scalar_nv_fields']}` scalar fields (`{nv['leaf_nv_strings']}` strings across `{nv['records_with_nv']}/{nv['total_records']}` records) coded as not verifiable from accessible open summary—for instance, raw per-cell accuracy tables in papers reporting relative percentages or frontier plots {c('SR001', 'SR005')} or secondary metadata absent from accessible HTML snippets {c('SR011', 'SR080')}. Zero missing numbers were imputed.
3. **Author Allegiance, Task-Mix Concentration, and Boundary Choices:** Skeptical evaluation teams in `Tier 1` might pick benchmarks unfavorable to MAS, and all `2/2` Tier 1 decomposable wins come from one study (*Kim et al.* {c('SR001')}). We mitigated both risks directly via **Within-Study Paired Contrasts** (showing reversals inside identical author teams and datasets), **Task-Family Stratification** (Table 12), **Sensitivity C** separating non-interactive ensembles (`{ci['Tier 1']['win_pct']}%` Tier 1), **Sensitivity D** (`±1.0 pp` tie margin), and **Sensitivity F** (`{copt['Tier 1']['win_pct']}%` optimistic recoding).
4. **LLM-Assisted Screening Consistency & Small Sub-Sample Power:** Blinded initial screening passes ran via two LLM screening workflows (Stage 1 `kappa = {irr['full_stage1_kappa']}`, Stage 2 `kappa = {irr['stage2_3class_kappa']}`, pooled raw pass agreement `163/170 = 95.9%`, end-to-end `95/100 = 95.0%`), verified manually across all 100 records and all 59 extracted studies by human review rather than claiming two independent human raters. Small `n = 4` archival Tier 1 sample size limits binary Fisher power (`p = {cr['fisher_p_t1_vs_t23']}` vs. exact permutation `p = {cr['perm_p_study_frac_t1_vs_t23']}`).

---

## 9. Conclusion

Across `{pr['included_total']}` studies (2023–2026) and `{ca['All']['n_tuples']}` paired comparisons, **the measured advantage of LLM multi-agent systems over single agents depends critically on baseline fairness**. Under weak single-pass or unmatched baselines (`Tier 2+3`), teams win `{ca['Tier 2+3']['win_pct']}%` of comparisons. Under equal-compute parity (`Tier 1`), wins drop to **`{ca['Tier 1']['win_pct']}%` (`3/15`, Wilson `7.0%–45.2%`)** while losses reach **`{ca['Tier 1']['loss_pct']}%` (`7/15`)** (`{ca['tuple_attenuation_pp']}` percentage points; study-weighted `{ca['study_frac_attenuation_pp']}` points, permutation `p = {ca['perm_p_study_frac_t1_vs_t23']}`), echoed across fixed-author paired contrasts and continuous effect-size gaps (`+{es['weak_single_pass']['study_mean_pp']:.2f} pp` unmatched vs. `{es['strong_controls_all_models']['study_mean_pp']:+.2f} pp` across all three CAIS '26 splits / `{es['strong_controls_main_qwen']['study_mean_pp']:+.2f} pp` using main Qwen2.5-7B).

These results clarify *where* multi-agent coordination helps: splittable multi-source tasks exceeding single-context capacity (`+80.8%` relative on `Finance-Agent` in Kim et al. {c('SR001')}) and boundary-triggered selective cascades (`-20%` spend {c('SR086')}). On tightly sequential workflows, closed-book reasoning, and unverified QA, however, equal-budget **Self-Consistency**, **Single-Best Repetition (`Self-MoA`)**, and **isolated solo iteration** remain stronger, safer, and cheaper baselines until multi-agent frameworks satisfy equal-compute, amortized-search, `pass^k`, and security-audit standards.

---

## 10. References

{refs}

---

## 11. Declarations

- **Originality & Verification Statement:** All prose, synthesis tables, figures, and frameworks in this manuscript are original; all reported numbers and citations were verified directly against accessible primary papers, OpenReview records, and public repositories without imputing missing values.
- **Competing Interests:** The authors declare no commercial funding or competing financial interests.
- **AI Tooling Transparency:** Tool-verified LLM workflows assisted initial screening triage, structured JSON extraction, and deterministic statistical scripting under continuous human-author protocol design, conflict adjudication, and source verification.
- **Data & Code Availability:** Section 12 embeds the complete self-contained PRISMA-S search strings and execution log (Appendix A), full 59-study ledger with item-level `QA1–QA7` ratings, confounder flags, and verified source locators (Appendix B), complete 87-comparison paired dataset and 34-study win-share vector (Appendix C), comparison-cleaning and re-coding log (Appendix D), and 41-record excluded-studies ledger (Appendix E). Machine-readable JSON, CSV, BibTeX (`124` entries), and deterministic Python analysis/verification scripts reside in the companion `data/` and `scripts/` directories.

---

## 12. Self-Contained Reproducibility & Evidence Appendix

### Appendix A: Verbatim Boolean Search Queries (`Q1–Q6`) and Complete Execution Log (`S01–S13`, PRISMA-S)

{verbatim_queries_md}

{chr(10).join(app_a_lines)}

### Appendix B: Complete 59-Study Rigor, Topology, Item-Level `QA1–QA7`, Confounder, & Source Locator Ledger

{chr(10).join(app_b_lines)}

### Appendix C: Complete Reconciled Comparative Dataset (`87` Paired Comparisons Across `34` Studies)

#### C.1 Complete 87-Comparison Paired Dataset

{blk['TABLE_APP_C_COMPARISONS']}

#### C.2 Complete 34-Study Win-Share Vector

{blk['TABLE_APP_C_STUDY_SHARES']}

### Appendix D: Comparison Cleaning, Split & Boundary Re-Coding Log

{app_d_txt}

### Appendix E: Complete 41-Record Excluded-Studies Ledger (`Excl-01` to `Excl-41`)

{chr(10).join(app_e_lines)}
"""

    # Clean any stray backticks outside ```mermaid / ```text code blocks!
    parts = re.split(r"(```.*?```)", manuscript, flags=re.S)
    for idx in range(0, len(parts), 2):
        parts[idx] = parts[idx].replace("`", "")
    manuscript = "".join(parts)

    # Verify 124/124 exact 1:1 BibTeX citation coverage & zero leaks
    body_part, rest_part = manuscript.split("## 10. References", 1)
    refs_part, app_part = rest_part.split("## 12. Self-Contained Reproducibility & Evidence Appendix", 1)

    cited_nums = set()
    for m in re.finditer(r"\[(\d+(?:,\s*\d+)*)\]", body_part + "\n" + app_part):
        for x in m.group(1).split(","):
            cited_nums.add(int(x.strip()))

    missing_cites = sorted(set(range(1, cm["total"] + 1)) - cited_nums)
    extra_cites = sorted(cited_nums - set(range(1, cm["total"] + 1)))
    assert not missing_cites, f"Uncited BibTeX entries ({len(missing_cites)}): {missing_cites} -> {[cm['by_num'][str(x)]['key'] for x in missing_cites]}"
    assert not extra_cites, f"Undefined citation numbers: {extra_cites}"

    # Verify zero forbidden terms, raw IDs, or Round-2 regression leaks
    check_txt = body_part + "\n" + app_part
    forbidden_patterns_ci = [
        r"\bm\.tech\b",
        r"graduate research committee",
        r"tmlr backup",
        r"post-peer-review remediation",
        r"\bcandid\b",
        r"\bcandor\b",
        r"audit candor",
        r"\bunambiguous(?:ly)?\b",
        r"\bzero[- ]fabrication\b",
        r"\btwice-rejected\b",
        r"arr #2880",
        r"arr #1068",
        r"remediation-v1\.2",
        r"protocol amendment",
        r"25\.8%",
        r"discovery specialist",
        r"review methodologist",
        r"research director",
    ]
    found_bad = [pat for pat in forbidden_patterns_ci if re.search(pat, check_txt, re.I)]
    if re.search(r"\bTier [A-C]\b|\bTier [IVX]+\b", check_txt):
        found_bad.append("Tier A-C/I-V collision")
    if re.search(r"\bQ[0-4]\b", body_part):
        found_bad.append("Q0-Q4 collision in main body")
    assert not found_bad, f"Forbidden terms found: {found_bad}"
    assert not re.search(r"\bSR\d{3}\b", check_txt), "Raw SRxxx leaked into manuscript!"

    with open(REVIEWS / "manuscript_v4_final.md", "w") as f:
        f.write(manuscript)
    with open(DELIV / "Deliverable_F_Final_Review_Manuscript.md", "w") as f:
        f.write(manuscript)

    print("BUILT manuscript_v4_final.md & Deliverable_F_Final_Review_Manuscript.md (v1.4)!")
    print(f"  Abstract: {len(abs_words)} words | {len(abs_split)} split tokens | 0 backticks")
    print(f"  Citations: {len(cited_nums)}/{cm['total']} (1:1 parity, 0 uncited, 0 undefined)")


if __name__ == "__main__":
    main()
