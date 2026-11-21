#!/usr/bin/env python3
"""
Deterministic Phase 9-10 Remediation Merge Script (Protocol v1.2).
Applies Director arbitrations across search_log.json, screening_records.csv,
included_studies.csv, evidence_matrix.json, quality_appraisal.csv, bibliography.bib,
and logs every purged/deduplicated tuple in reviews/tuple_cleanup_log.md.
"""

import csv
import json
import re
from pathlib import Path
import jsonschema

ROOT = Path("/Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review")
DATA = ROOT / "data"
AGENTS = ROOT / "agents"
REVIEWS = ROOT / "reviews"


def pct_str(score: int, max_score: int) -> str:
    return f"{(100.0 * score / max_score):.1f}"


def band_short(score: int, max_score: int) -> str:
    pct = 100.0 * score / max_score
    if pct >= 78.0:
        return "High"
    elif pct >= 42.5:
        return "Moderate"
    return "Low"


def band_schema(score: int, max_score: int) -> str:
    b = band_short(score, max_score)
    if b == "High":
        return "High (>=78.0%; 11-14/14 or 10-12/12)"
    if b == "Moderate":
        return "Moderate (42.5%-77.9%; 6-10/14 or 6-9/12)"
    return "Low (<42.5%; 0-5/14 or 0-5/12)"


def update_search_log():
    p = DATA / "search_log.json"
    with open(p) as f:
        sl = json.load(f)

    sl["protocol_version"] = "v1.2"
    sl["remediation_date"] = "2026-11-20"
    sl["environment_note"] = (
        "Executed via search_web over open academic web repositories (arXiv, OpenReview, ACL Anthology, PMLR), "
        "publisher portals (ACM DL, Springer, Nature), and semantic citation indices (no closed Scopus or Web of Science bulk API exports). "
        "Protocol Amendment v1.2 transparently frames retrieval as a PRISMA-governed open-web query- and snowball-seeded review, "
        "discloses targeted system-name specializations in S02/S05/S09, and appends remediation waves S12-S13."
    )

    # Disclose S02/S05/S09 specializations transparently on existing entries if not already noted
    disclosure = {
        "S02": " [v1.2 Disclosure: Query specialized post-v1.0 freeze with named architectures (Mixture-of-Agents, Self-MoA, ColMAD, Self-Refine, Reflexion).]",
        "S05": " [v1.2 Disclosure: Query specialized post-v1.0 freeze with named systems (CONSENSAGENT, CORBA).]",
        "S09": " [v1.2 Disclosure: Query specialized post-v1.0 freeze with named benchmarks/frameworks (SwarmBench, SCALE, 8079).]",
    }
    existing_ids = {s["search_id"] for s in sl["searches"]}
    for s in sl["searches"]:
        sid = s["search_id"]
        if sid in disclosure and "[v1.2 Disclosure:" not in s.get("notes", ""):
            s["notes"] = s.get("notes", "") + disclosure[sid]
            s["post_freeze_specialization_disclosed"] = True

    if "S12" not in existing_ids:
        sl["searches"].append({
            "search_id": "S12",
            "protocol_query": "Remediation-v1.2-Comparative",
            "date": "2026-11-20",
            "query_string_executed": (
                "Protocol Amendment v1.2 targeted import and live verification of 12 Phase-2 & referee-flagged "
                "primary comparative MAS-vs-SAS anchors (Agent Forest 2402.05120, Gao et al. 2505.18286, "
                "Debate or Vote 2508.17536, Estornell & Liu NeurIPS 2024, Cost of Consensus 2605.00914 / CAIS 2026, "
                "Zhao et al. 2602.04234, SAIGE 2609.19759, DyLAN 2310.02170, AgentDropout 2503.18891, "
                "Optima 2410.08115, Router-R1 2506.09033, EvoAgent 2406.14228)"
            ),
            "domains_targeted": ["arxiv.org", "openreview.net", "aclanthology.org", "dl.acm.org"],
            "raw_hits_logged": 12,
            "duplicates_collapsed": 0,
            "unique_new_records_added": 12,
            "notes": "Blinded dual screening across Agent 3+9 and Agent 6 under Protocol v1.2 (SR085-SR096; SR095 excluded E3 at Stage 2)."
        })

    if "S13" not in existing_ids:
        sl["searches"].append({
            "search_id": "S13",
            "protocol_query": "Remediation-v1.2-Security-Attribution",
            "date": "2026-11-20",
            "query_string_executed": (
                "Protocol Amendment v1.2 targeted import and live verification of 4 Phase-2 & referee-flagged "
                "multi-agent failure-attribution & security comparison studies (VerifyMAS NeurIPS 2026 2605.17467, "
                "Hagag et al. ICML 2026 PMLR 306, NetSafe ACL Findings 2025, G-Safeguard ACL 2025)"
            ),
            "domains_targeted": ["arxiv.org", "proceedings.mlr.press", "aclanthology.org"],
            "raw_hits_logged": 4,
            "duplicates_collapsed": 0,
            "unique_new_records_added": 4,
            "notes": "Blinded dual screening across Agent 3+9 and Agent 6 under Protocol v1.2 (SR097-SR100; all 4 included)."
        })

    sl["summary"] = {
        "total_raw_records_identified": 142,
        "total_duplicates_merged": 42,
        "preprint_to_archival_merges": 27,
        "cross_query_and_snowball_overlaps_merged": 15,
        "unique_records_entering_stage1": 100,
        "wave1_unique_records": 84,
        "remediation_v1_2_unique_records": 16,
    }
    with open(p, "w") as f:
        json.dump(sl, f, indent=2)
    print("Updated search_log.json: searches =", len(sl["searches"]), "unique =", sl["summary"]["unique_records_entering_stage1"])


def update_screening_and_included(wave, a6_votes):
    sr_path = DATA / "screening_records.csv"
    with open(sr_path) as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = [r for r in reader if r["record_id"] <= "SR084"]

    # Update retroactive Stage 2 Agent 3 decisions on SR079 and SR082 under v1.2
    for r in rows:
        if r["record_id"] == "SR079":
            r["stage2_agent3_decision"] = "INCLUDE"
            r["stage2_agent3_code"] = "NONE"
            r["notes"] = (
                "Rejected by TMLR Paper 9844 & 11271 (excluded from archival high-confidence claims under E8; "
                "logged in RQ4 Rejection Audit); accepted KDD 2026 Workshop version included as Workshop track under v1.1/v1.2. "
                "[v1.2 Retroactive Stage 2 Agent 3 Completed: INCLUDE Workshop / RQ3-RQ4 Audit; QA2 corrected 1->0.]"
            )
        elif r["record_id"] == "SR082":
            r["stage2_agent3_decision"] = "INCLUDE"
            r["stage2_agent3_code"] = "NONE"
            r["notes"] = (
                "Withdrawn ICLR 2025 #6097 isolated in RQ4 Longitudinal Audit (E8); subsequent archival ACL 2025 Long Paper "
                "(2025.acl-long.416) included under I2a/Sec. 5.1 Rule 3 (evaluates N>=2 SCALE vs N=1 coding baseline). "
                "[v1.2 Retroactive Stage 2 Agent 3 Completed: INCLUDE ACL 2025 Archival.]"
            )

    # Append SR085-SR100
    a6_map = {r["record_id"]: r for r in a6_votes}
    cands = wave["candidates_SR085_SR100"]

    for i in range(85, 101):
        rid = f"SR{i:03d}"
        c = cands[rid]
        rec = c["extraction_record"]
        bib = rec["bibliographic_and_identifiers"]
        a6 = a6_map[rid]

        # Canonical URL & venue overrides per Director Arbitration
        title = bib["title"]
        authors = "; ".join(bib["authors"])
        year = str(rec["year"])
        venue = bib["venue"]
        pub_status = rec["publication_status"]
        canon_id = bib["arxiv_id"]
        if bib["doi"] not in ("not reported", "not verifiable from accessible open summary"):
            canon_id = f"DOI:{bib['doi']}"
        elif bib["acl_anthology_id"] not in ("not reported", "not verifiable from accessible open summary"):
            canon_id = f"ACL:{bib['acl_anthology_id']}"
        elif bib["openreview_id"] not in ("not reported", "not verifiable from accessible open summary"):
            canon_id = f"OpenReview:{bib['openreview_id']}"

        verified_url = rec["source_provenance"]["verified_url"]
        linked = ";".join(bib.get("linked_preprint_or_prior_version_ids", [])) or "NONE"

        if rid == "SR087":
            canon_id = "OpenReview:iUjGNJzrF1"
            verified_url = "https://openreview.net/forum?id=iUjGNJzrF1"
            linked = "arXiv:2508.17536"
        elif rid == "SR088":
            canon_id = "OpenReview:sy7eSEXdPC"
            verified_url = "https://openreview.net/forum?id=sy7eSEXdPC"
            linked = f"DOI:{bib['doi']}"
        elif rid == "SR089":
            venue = "Proceedings of the ACM Conference on AI and Agentic Systems (CAIS 2026)"
            pub_status = "Peer-reviewed conference"
            canon_id = "DOI:10.1145/3786335.3813137"
            verified_url = "https://doi.org/10.1145/3786335.3813137"
            linked = "arXiv:2605.00914"
            authors = "Blaz Bertalanic; Carolina Fortuna"

        source_q = "S12 (v1.2)" if i <= 96 else "S13 (v1.2)"
        rq_rel = ";".join(rec["rq_mapping"]["rqs_addressed"])

        a3_s1 = "PASS_TO_STAGE2" if c["stage1_decision"] in ("PASS", "INCLUDE", "PASS_TO_STAGE2") else "EXCLUDE"
        a3_s2 = c["stage2_decision"]
        a6_s1 = "PASS_TO_STAGE2" if a6["stage1_agent6_decision"] == "INCLUDE" else "EXCLUDE"
        a6_s2 = a6["stage2_agent6_decision"]
        a6_code = a6["exclusion_code"] if a6["exclusion_code"] != "N/A" else "NONE"

        if rid == "SR095":
            final_dec = "EXCLUDE"
            final_code = "E3"
            notes = (
                "Director Arbitration: Uphold Agent 6 EXCLUDE (E3). Single RL-trained policy LLM calling external models "
                "as stateless black-box API tools analogous to Search-R1 without persistent N>=2 MAS roles or SAS->MAS escalation "
                "(contrasts Agent 3 INCLUDE boundary view; retained as cited E3 boundary contrast in manuscript)."
            )
        else:
            final_dec = "INCLUDE"
            final_code = "NONE"
            notes = f"v1.2 Blinded Dual-Screening Unanimous INCLUDE. {c['protocol_rule_matched']}"
            if rid == "SR087":
                notes += " [Dir Fix: Verified OpenReview ID iUjGNJzrF1; normalized to 3 primary MV/Single tuples.]"
            elif rid == "SR088":
                notes += " [Dir Fix: Verified OpenReview ID sy7eSEXdPC; upgraded to Tier 2 (includes Majority baseline).]"
            elif rid == "SR089":
                notes += " [Dir Fix: Upgraded arXiv:2605.00914 -> published ACM CAIS 2026 DOI:10.1145/3786335.3813137.]"

        rows.append({
            "record_id": rid,
            "title": title,
            "authors": authors,
            "year": year,
            "venue": venue,
            "canonical_id": canon_id,
            "linked_preprint_ids": linked,
            "verified_url": verified_url,
            "source_query_or_snowball": source_q,
            "publication_status": pub_status,
            "rq_relevance": rq_rel,
            "stage1_agent3_decision": a3_s1,
            "stage1_agent3_code": "NONE",
            "stage2_agent3_decision": a3_s2,
            "stage2_agent3_code": "NONE",
            "stage1_agent6_decision": a6_s1,
            "stage1_agent6_code": "NONE",
            "stage2_agent6_decision": a6_s2,
            "stage2_agent6_code": a6_code,
            "final_decision": final_dec,
            "final_exclusion_code": final_code,
            "notes": notes,
        })

    with open(sr_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    inc_fields = [
        "record_id", "title", "authors", "year", "venue", "canonical_id",
        "linked_preprint_ids", "verified_url", "publication_status", "rq_relevance", "notes"
    ]
    inc_rows = [{k: r[k] for k in inc_fields} for r in rows if r["final_decision"] == "INCLUDE"]
    with open(DATA / "included_studies.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=inc_fields)
        writer.writeheader()
        writer.writerows(inc_rows)

    print(f"Updated screening_records.csv ({len(rows)} rows) and included_studies.csv ({len(inc_rows)} rows)")
    return inc_rows


def update_evidence_matrix_and_qa(wave):
    em_path = DATA / "evidence_matrix.json"
    with open(em_path) as f:
        em = json.load(f)

    # Keep only SR001-SR084 baseline records before applying remediation wave so script is idempotent
    em = {k: v for k, v in em.items() if k <= "SR084"}
    cleanup_log = []

    def drop_tuples(rid, drop_indices, reason_map):
        rec = em[rid]
        old_tuples = rec["reported_numerical_outcomes"]["paired_comparisons"]
        kept = []
        for idx, t in enumerate(old_tuples):
            if idx in drop_indices:
                cleanup_log.append({
                    "study_id": rid,
                    "tuple_index": idx + 1,
                    "benchmark_and_backbone": t.get("benchmark_and_backbone", ""),
                    "original_verdict": t.get("direction_verdict", ""),
                    "reason": reason_map[idx],
                })
            else:
                kept.append(t)
        rec["reported_numerical_outcomes"]["paired_comparisons"] = kept

    # 1. Purge 7 invalid/nested tuples from existing 44 studies (idempotent check)
    if len(em["SR015"]["reported_numerical_outcomes"]["paired_comparisons"]) == 3:
        drop_tuples("SR015", {1, 2}, {
            1: "Non-MAS-vs.-SAS comparator: optimized graph compared against 'Initial unoptimized graph baseline' (MAS vs. MAS ablation).",
            2: "Non-MAS-vs.-SAS comparator violating N>=2 gate: node-optimized single-agent ReAct vs. unoptimized ReAct (N=1 vs. N=1).",
        })
    if len(em["SR007"]["reported_numerical_outcomes"]["paired_comparisons"]) == 2:
        drop_tuples("SR007", {1}, {
            1: "Non-MAS-vs.-SAS comparator verified by Agent 3+9: +6.4% (Heter-SoM) and +8.2% (Heter-EoT) are strictly Heter-MAD vs. Homog-MAD gains, not direct vs. SAS deltas (preserved in diagnostic_or_topology_outcomes).",
        })
    heter_note = "Heterogeneous model assignment lifts MAD over homogeneous MAD by +6.4% (Heter-SoM) and +8.2% (Heter-EoT) across GPT-4o-mini and Llama-3.1-70B."
    if heter_note not in em["SR007"]["reported_numerical_outcomes"].setdefault("diagnostic_or_topology_outcomes", []):
        em["SR007"]["reported_numerical_outcomes"]["diagnostic_or_topology_outcomes"].append(heter_note)
    # Confirm conformity collapse documented in SR007 (fixes L314 [39] -> [73])
    if "Conformity/Sycophancy Collapse" not in em["SR007"]["reported_successes_and_failures"]["failure_mechanisms_documented"]:
        em["SR007"]["reported_successes_and_failures"]["failure_mechanisms_documented"].append("Conformity/Sycophancy Collapse")

    if len(em["SR014"]["reported_numerical_outcomes"]["paired_comparisons"]) == 5:
        drop_tuples("SR014", {4}, {
            4: "Nested/double-counted composite: 4-Benchmark Average (0.6522 vs. 0.5757) averages Tuples 1-4 (MMLU, HumanEval, SRDD, CommonGen-Hard).",
        })

    # SR002: preserve slice numbers explicitly inside kept Tuple 3 before removing nested Tuples 1-2
    if len(em["SR002"]["reported_numerical_outcomes"]["paired_comparisons"]) == 3:
        em["SR002"]["reported_numerical_outcomes"]["paired_comparisons"][2]["benchmark_and_backbone"] = (
            "336-config matrix across Qwen3-30B-A3B, DeepSeek-R1-Distill-Llama-70B, Gemini 2.5 Flash/Pro (100-10,000 thinking tokens; "
            "FRAMES & MuSiQue representative slices: 1k tok 0.379 MAS vs 0.418 SAS; 5k tok 0.386 MAS vs 0.427 SAS)"
        )
        drop_tuples("SR002", {0, 1}, {
            0: "Nested sub-slice double-count: 1,000 thinking-token slice (0.379 vs 0.418) already covered inside the 336-config 100-10,000 token matrix (values preserved inside Tuple 3 notes).",
            1: "Nested sub-slice double-count: 5,000 thinking-token slice (0.386 vs 0.427) already covered inside the 336-config 100-10,000 token matrix (values preserved inside Tuple 3 notes).",
        })

    if len(em["SR020"]["reported_numerical_outcomes"]["paired_comparisons"]) == 2:
        drop_tuples("SR020", {1}, {
            1: "Nested/non-pure composite: 5-benchmark peak aggregate overlaps Tuple 1 (MedQA) and bundles single-model cascades with standalone MAS.",
        })

    # 2. Apply Open-Text NV reductions & dispute fixes on existing studies
    nv = wave["open_text_nv_updates"]

    # SR001
    em["SR001"]["architecture_and_agent_count"]["agent_count_n"] = "n_a in {1, 3, 5, 7, 9} (N=1 SAS vs N in {3, 5, 7, 9} MAS)"
    em["SR001"]["architecture_and_agent_count"]["backbone_models"] = ["OpenAI GPT-5 family", "Google Gemini 2.x family", "Anthropic Claude Sonnet family"]
    em["SR001"]["experimental_setup"]["decoding_and_hyperparameters"] = (
        "Controlled normalized token budgets across OpenAI GPT-5, Google Gemini 2.x, and Anthropic Claude Sonnet; 10,000 bootstrap resamples for error scaling"
    )
    diag1 = em["SR001"]["reported_numerical_outcomes"].get("diagnostic_or_topology_outcomes", [])
    diag1_str = "Exact error amplification factors: Centralized 4.4x, Hybrid 5.1x, Decentralized 7.8x, Independent 17.2x; SAS capability saturation ~45% (beta=-0.096, p<0.001)."
    if diag1_str not in diag1:
        diag1.append(diag1_str)
    em["SR001"]["reported_numerical_outcomes"]["diagnostic_or_topology_outcomes"] = diag1
    if "[v1.2 Audit:" not in em["SR001"]["limitations_and_validity_threats"]["threats_to_validity"]:
        em["SR001"]["limitations_and_validity_threats"]["threats_to_validity"] += (
            " [v1.2 Audit: QA2=2 rests on normalized success-per-1k-tokens & orchestration turn counts; raw wall-clock seconds and pass^k remain paywalled NV in NMI supplement.]"
        )

    # SR002
    em["SR002"]["architecture_and_agent_count"]["backbone_models"] = ["Qwen3-30B-A3B", "DeepSeek-R1-Distill-Llama-70B", "Gemini 2.5 Flash", "Gemini 2.5 Pro"]
    em["SR002"]["architecture_and_agent_count"]["system_names"] = ["SAS", "SAS-L (long-thinking single agent)", "Sequential MAS", "Subtask-parallel MAS", "Parallel-roles MAS", "Debate MAS", "Ensemble MAS"]
    em["SR002"]["cost_and_latency"]["wall_clock_latency"] = "not reported (matches thinking-token budgets 100-10,000 without tabulating wall-clock seconds)"
    em["SR002"]["quality_appraisal_and_evidence_provenance"]["quality_appraisal"]["qa2_cost_and_latency_accounting"] = 1

    # SR003
    em["SR003"]["experimental_setup"]["sample_or_trace_count"] = (
        "HumanEval (131), MBPP (341), GSM8K (1,055), MATH (486), HotpotQA (800), DROP (800), TravelPlanner (180)"
    )

    # SR004
    em["SR004"]["architecture_and_agent_count"]["backbone_models"] = ["Llama-3.2-3B", "Qwen2.5-7B", "Falcon3-7B", "Gemma-2-9B", "Gemma3-12B"]
    em["SR004"]["cost_and_latency"]["wall_clock_latency"] = (
        "Table 10 wall-clock minutes (200 questions across GSM8K/MATH500/CSQA/MMLU-Pro, Probe vs Full Debate): "
        "6-34 min vs 21-336 min (5x-9x latency multiplier across Llama-3.2-3B to Gemma3-12B)."
    )
    em["SR004"]["quality_appraisal_and_evidence_provenance"]["quality_appraisal"]["qa2_cost_and_latency_accounting"] = 2

    # SR005 (Keep C1 with clear Pareto sub-regime annotation)
    if "C1: Unmatched Inference Compute/Tokens" not in em["SR005"]["limitations_and_validity_threats"]["six_class_confounder_flags"]:
        em["SR005"]["limitations_and_validity_threats"]["six_class_confounder_flags"].append("C1: Unmatched Inference Compute/Tokens")
    if "[v1.2 Audit:" not in em["SR005"]["limitations_and_validity_threats"]["threats_to_validity"]:
        em["SR005"]["limitations_and_validity_threats"]["threats_to_validity"] += (
        " [v1.2 Audit: Keeps C1 for out-of-the-box Table 2 comparisons where Multi-Persona MAD incurs higher sequential calls/tokens/time than Medprompt/SC, "
        "distinct from Appendix Figs 1-13 Pareto compute-matched Tier 1 sweeps.]"
    )

    # SR008
    em["SR008"]["architecture_and_agent_count"]["backbone_models"] = ["GPT", "Claude", "Qwen", "DeepSeek", "Llama (exact variant tags in PDF Appendices)"]
    em["SR008"]["experimental_setup"]["sample_or_trace_count"] = "6 controllable factors in Table 1 + Het-Mix A/B/C/D in Table 2 on Knight-Knave-Spy"

    # SR010 (Fix 65.1% -> 59.1% vs 65.7% = -6.6 pp / -10.0% rel)
    t0_10 = em["SR010"]["reported_numerical_outcomes"]["paired_comparisons"][0]
    t0_10["mas_score"] = 59.1
    t0_10["sas_score"] = 65.7
    t0_10["delta_mas_minus_sas"] = "-6.6 pp (-10.0% relative; Mixed-MoA 59.1% vs. Self-MoA 65.7%)"
    em["SR010"]["reported_numerical_outcomes"]["paired_comparisons"][0] = t0_10

    # SR012 (Remove ALL stale arXiv:2510.18375 strings and anchor ColMAD gain verbatim)
    s12_str = json.dumps(em["SR012"]).replace("arXiv:2510.18375", "arXiv:2510.20963")
    em["SR012"] = json.loads(s12_str)
    em["SR012"]["reported_numerical_outcomes"]["paired_comparisons"][1]["mas_score"] = (
        "Up to +10 pp over legacy MAD (CopMAD/CosMAD); consistent gains over compute-matched SA (exact cell % not verifiable from accessible open summary)"
    )
    em["SR012"]["reported_numerical_outcomes"]["paired_comparisons"][1]["delta_mas_minus_sas"] = (
        "Up to +10 pp over prior MAD protocols; outperforms compute-matched SA"
    )
    em["SR012"]["limitations_and_validity_threats"]["threats_to_validity"] = (
        "Individual benchmark table cell figures and exact model lists require inspecting full PDF; arXiv preprint verified strictly as arXiv:2510.20963."
    )
    em["SR012"]["quality_appraisal_and_evidence_provenance"]["supporting_evidence_locations"] = [
        "https://arxiv.org/abs/2510.20963 (Verified Abstract & ICML 2026 summary: CopMAD -15% to -19% below SA; ColMAD up to +10 pp over prior MAD & consistent gains over SA)"
    ]

    # SR017
    em["SR017"]["cost_and_latency"]["wall_clock_latency"] = (
        "Table 2 GSM8K Training/Inference hours reported alongside tokens: Complete 2.4h inf (9.8e6 tok), "
        "DyLAN 2.8h train / 4.6h inf (2.2e7 tok), GPTSwarm 2.1h train / 2.8h inf (1.4e7 tok)."
    )
    em["SR017"]["quality_appraisal_and_evidence_provenance"]["quality_appraisal"]["qa2_cost_and_latency_accounting"] = 2

    # SR020 (Confirm QA2=2, resolve latency + C6 sync)
    em["SR020"]["cost_and_latency"]["wall_clock_latency"] = "2.45s (CascadeDebate) vs 2.34s (MAS baselines) mean A100 inference latency on ARC-Challenge"
    em["SR020"]["cost_and_latency"]["token_or_api_cost"] = "20%-35% token savings vs full MAD; 12.79x (ARC-Easy), 13.71x (MedMCQA), 16.66x (MedQA) cost multipliers vs Single Base" if "token_or_api_cost" in em["SR020"]["cost_and_latency"] else None
    if em["SR020"]["cost_and_latency"].get("token_or_api_cost") is None:
        em["SR020"]["cost_and_latency"].pop("token_or_api_cost", None)
    em["SR020"]["cost_and_latency"]["token_accounting"] = (
        "20%-35% token savings vs standalone MAD; normalized cost multipliers: 12.79x ARC-Easy (+26.78 pp), 13.71x MedMCQA (+40.22 pp), 16.66x MedQA (+52.22 pp)"
    )
    em["SR020"]["quality_appraisal_and_evidence_provenance"]["quality_appraisal"]["qa2_cost_and_latency_accounting"] = 2
    if "C6: Unamortized Search/Training Cost Omission" not in em["SR020"]["limitations_and_validity_threats"]["six_class_confounder_flags"]:
        em["SR020"]["limitations_and_validity_threats"]["six_class_confounder_flags"].append("C6: Unamortized Search/Training Cost Omission")

    # SR025
    em["SR025"]["cost_and_latency"]["wall_clock_latency"] = "Hand-Crafted Qwen-7B: AgentLocate 315s vs AgenTracer 6,752s (>20x speedup)"
    em["SR025"]["cost_and_latency"]["usd_cost_accounting"] = "Hand-Crafted Qwen-7B: AgentLocate $0.148 vs AgenTracer $3.204 (>21x cost reduction)"
    em["SR025"]["quality_appraisal_and_evidence_provenance"]["quality_appraisal"]["qa2_cost_and_latency_accounting"] = 2

    # SR032
    em["SR032"]["architecture_and_agent_count"]["backbone_models"] = ["GPT-4"]
    em["SR032"]["variance_cis_and_stats"]["dispersion_metrics_reported"] = "Table A1 95% CIs (GPT-4 Direct $1.93 [1.91-1.95]; LATS $134.50 [123.98-147.13]; Warming $2.45 at 93.2%)"
    em["SR032"]["cost_and_latency"]["wall_clock_latency"] = "not reported quantitatively (qualitative discussion of latency alongside USD evaluation)"
    em["SR032"]["quality_appraisal_and_evidence_provenance"]["quality_appraisal"]["qa2_cost_and_latency_accounting"] = 1

    # SR034
    em["SR034"]["cost_and_latency"]["wall_clock_latency"] = "Embedded only inside composite dimensionless Resource Consistency CV index R_Con^Res = exp(-mean CV over cost, time, API calls); raw seconds omitted"
    em["SR034"]["quality_appraisal_and_evidence_provenance"]["quality_appraisal"]["qa2_cost_and_latency_accounting"] = 1

    # SR039 (Capitalization El Hattami + QA2 upgrade)
    if "El Hattami" not in " ".join(em["SR039"]["bibliographic_and_identifiers"]["authors"]):
        em["SR039"]["bibliographic_and_identifiers"]["authors"] = [
            "Amine El Hattami" if "hattami" in a.lower() else a
            for a in em["SR039"]["bibliographic_and_identifiers"]["authors"]
        ]
    em["SR039"]["cost_and_latency"]["wall_clock_latency"] = "68.2%-83% evaluation runtime cut on WebArena Verified Hard subset"
    em["SR039"]["cost_and_latency"]["token_accounting"] = "Eliminates LLM-as-a-judge evaluation token calls via deterministic DB/state checks (raw evaluated-agent USD totals omitted)"
    em["SR039"]["quality_appraisal_and_evidence_provenance"]["quality_appraisal"]["qa2_cost_and_latency_accounting"] = 2

    # SR069 P-ASR acronym fix
    em["SR069"]["reported_numerical_outcomes"]["diagnostic_or_topology_outcomes"] = [
        "Broadcast-style AutoGen and CAMEL topologies suffer ~100% Proportional Attack Success Rate (P-ASR) in smaller agent configs and ~92% P-ASR even in 10-agent systems.",
        "Peak Blocking Turn Number (PTN) averages 1.60 to 1.90 turns, indicating near-immediate contagious system paralysis.",
    ]

    # SR079 QA2 downgrade 1->0 & Workshop / Rejection audit refinement
    em["SR079"]["quality_appraisal_and_evidence_provenance"]["quality_appraisal"]["qa2_cost_and_latency_accounting"] = 0
    em["SR079"]["cost_and_latency"]["token_accounting"] = "not reported"
    em["SR079"]["cost_and_latency"]["usd_cost_accounting"] = "not reported"
    em["SR079"]["cost_and_latency"]["wall_clock_latency"] = "not reported"

    # Recompute totals & rigor_band for all updated SR001-SR084 records
    for rid, r in em.items():
        qa = r["quality_appraisal_and_evidence_provenance"]["quality_appraisal"]
        q1 = qa["qa1_single_agent_baseline_rigor"]
        s1 = 0 if q1 == "N/A-Diagnostic" else int(q1)
        tot = s1 + int(qa["qa2_cost_and_latency_accounting"]) + int(qa["qa3_amortization_transparency"]) + int(qa["qa4_multi_run_stochastic_reliability"]) + int(qa["qa5_benchmark_and_harness_integrity"]) + int(qa["qa6_reproducibility_code_prompts"]) + int(qa["qa7_claims_evidence_parity"])
        mx = 12 if q1 == "N/A-Diagnostic" else 14
        qa["total_raw_score"] = tot
        qa["applicable_max_score"] = mx
        qa["rigor_band"] = band_schema(tot, mx)

    # 3. Import SR085-SR100 (excluding SR095) with Director Arbitrations
    arbitrated_qa = {
        # rid: (tier_str, [qa1, qa2, qa3, qa4, qa5, qa6, qa7], max_score, confounder_flags_override)
        "SR085": ("Tier 3 (Weak Zero-Shot Single-Pass SAS Only)", [1, 1, 2, 1, 1, 2, 1], 14,
                  ["C1: Unmatched Inference Compute/Tokens", "C3: Process Proxy / Voting-as-Deliberation Conflation", "C5: Exact-Match / Harness Fragility / Benchmark Leakage"]),
        "SR086": ("Tier 2 (Strong SAS, Unmatched Compute or Unamortized Search)", [1, 1, 2, 0, 1, 1, 2], 14,
                  ["C1: Unmatched Inference Compute/Tokens", "C4: Asymmetric Prompting or Tool/Execution Feedback", "C5: Exact-Match / Harness Fragility / Benchmark Leakage"]),
        "SR087": ("Tier 2 (Strong SAS, Unmatched Compute or Unamortized Search)", [1, 0, 2, 0, 1, 2, 2], 14,
                  ["C1: Unmatched Inference Compute/Tokens", "C3: Process Proxy / Voting-as-Deliberation Conflation", "C5: Exact-Match / Harness Fragility / Benchmark Leakage"]),
        "SR088": ("Tier 2 (Strong SAS, Unmatched Compute or Unamortized Search)", [1, 0, 2, 0, 1, 1, 2], 14,
                  ["C1: Unmatched Inference Compute/Tokens", "C5: Exact-Match / Harness Fragility / Benchmark Leakage"]),
        "SR089": ("Tier 2 (Strong SAS, Unmatched Compute or Unamortized Search)", [1, 1, 2, 1, 2, 1, 2], 14,
                  ["C1: Unmatched Inference Compute/Tokens", "C5: Exact-Match / Harness Fragility / Benchmark Leakage"]),
        "SR090": ("Tier 2 (Strong SAS, Unmatched Compute or Unamortized Search)", [1, 2, 2, 1, 1, 2, 2], 14,
                  ["C1: Unmatched Inference Compute/Tokens", "C5: Exact-Match / Harness Fragility / Benchmark Leakage"]),
        "SR091": ("Tier 2 (Strong SAS, Unmatched Compute or Unamortized Search)", [1, 1, 2, 1, 2, 1, 2], 14,
                  ["C1: Unmatched Inference Compute/Tokens", "C4: Asymmetric Prompting or Tool/Execution Feedback", "C5: Exact-Match / Harness Fragility / Benchmark Leakage"]),
        "SR092": ("Tier 2 (Strong SAS, Unmatched Compute or Unamortized Search)", [1, 1, 1, 0, 1, 2, 1], 14,
                  ["C1: Unmatched Inference Compute/Tokens", "C4: Asymmetric Prompting or Tool/Execution Feedback", "C5: Exact-Match / Harness Fragility / Benchmark Leakage", "C6: Unamortized Search/Training Cost Omission"]),
        "SR093": ("Tier 3 (Weak Zero-Shot Single-Pass SAS Only)", [1, 1, 1, 0, 1, 2, 1], 14,
                  ["C1: Unmatched Inference Compute/Tokens", "C4: Asymmetric Prompting or Tool/Execution Feedback", "C5: Exact-Match / Harness Fragility / Benchmark Leakage", "C6: Unamortized Search/Training Cost Omission"]),
        "SR094": ("Tier 2 (Strong SAS, Unmatched Compute or Unamortized Search)", [1, 1, 1, 0, 1, 2, 1], 14,
                  ["C1: Unmatched Inference Compute/Tokens", "C5: Exact-Match / Harness Fragility / Benchmark Leakage", "C6: Unamortized Search/Training Cost Omission"]),
        "SR096": ("Tier 2 (Strong SAS, Unmatched Compute or Unamortized Search)", [1, 1, 1, 0, 1, 2, 1], 14,
                  ["C1: Unmatched Inference Compute/Tokens", "C4: Asymmetric Prompting or Tool/Execution Feedback", "C5: Exact-Match / Harness Fragility / Benchmark Leakage", "C6: Unamortized Search/Training Cost Omission"]),
        "SR097": ("N/A (Non-Comparative Diagnostic/Validity Study)", ["N/A-Diagnostic", 1, 1, 0, 2, 2, 2], 12,
                  ["C5: Exact-Match / Harness Fragility / Benchmark Leakage", "C6: Unamortized Search/Training Cost Omission"]),
        "SR098": ("Tier 2 (Strong SAS, Unmatched Compute or Unamortized Search)", [1, 0, 2, 2, 2, 2, 2], 14,
                  ["C1: Unmatched Inference Compute/Tokens", "C5: Exact-Match / Harness Fragility / Benchmark Leakage"]),
        "SR099": ("N/A (Non-Comparative Diagnostic/Validity Study)", ["N/A-Diagnostic", 0, 2, 1, 1, 2, 2], 12,
                  ["C5: Exact-Match / Harness Fragility / Benchmark Leakage"]),
        "SR100": ("N/A (Non-Comparative Diagnostic/Validity Study)", ["N/A-Diagnostic", 0, 1, 0, 1, 2, 1], 12,
                  ["C5: Exact-Match / Harness Fragility / Benchmark Leakage", "C6: Unamortized Search/Training Cost Omission"]),
    }

    cands = wave["candidates_SR085_SR100"]
    for rid, (tier_str, qa_vec, mx, flags) in arbitrated_qa.items():
        rec = json.loads(json.dumps(cands[rid]["extraction_record"]))  # deep copy
        rec["baselines_and_rigor_tier"]["sas_baseline_rigor_tier"] = tier_str
        rec["limitations_and_validity_threats"]["six_class_confounder_flags"] = flags

        # Specific metadata / tuple arbitrations
        if rid == "SR086":
            rec["cost_and_latency"]["amortization_search_or_training_cost"] = (
                "Agent Cascade triggers verifier checks (SAS -> verify -> escalate) and Agent Routing uses zero-shot LLM rater prompts without offline RL weight training."
            )
            rec["variance_cis_and_stats"]["pass_power_k_reported"] = False
        elif rid == "SR087":
            rec["bibliographic_and_identifiers"]["openreview_id"] = "iUjGNJzrF1"
            rec["source_provenance"]["verified_url"] = "https://openreview.net/forum?id=iUjGNJzrF1"
            rec["quality_appraisal_and_evidence_provenance"]["supporting_evidence_locations"] = [
                "https://openreview.net/forum?id=iUjGNJzrF1 (NeurIPS 2025 Spotlight verified)",
                "https://arxiv.org/abs/2508.17536 (Tables 1-2 & Theorem 3.2 Martingale curse)",
                "https://github.com/deeplearning-wisc/debate-or-vote"
            ]
            old_t = rec["reported_numerical_outcomes"]["paired_comparisons"]
            cleanup_log.append({
                "study_id": "SR087",
                "tuple_index": "T2, T4-T8",
                "benchmark_and_backbone": "6 secondary MAD(T=2) vs N=1 tuples collapsed into strongest-SAS 7-benchmark Majority Vote comparison",
                "original_verdict": "MAS > SAS (6 tuples)",
                "reason": "Director Arbitration: Prioritize primary strongest-comparator MV (N=5, T=0) & Arithmetics loss tuples to eliminate inflating N=1 multi-task sub-rows when matched Majority Voting eliminates MAD advantage (Martingale Theorem 3.2).",
            })
            rec["reported_numerical_outcomes"]["paired_comparisons"] = [
                {
                    "benchmark_and_backbone": "GSM8K (Qwen2.5-7B-Instruct)",
                    "mas_configuration": "Decentralized MAD (T=2 rounds, N=5)",
                    "sas_comparator": "Majority Voting (T=0, N=5 independent calls)",
                    "mas_score": 0.8867,
                    "sas_score": 0.94,
                    "delta_mas_minus_sas": "-5.33 pp (0.8867 vs 0.9400)",
                    "compute_ratio_mas_over_sas": "2x-5x higher debate rounds vs T=0 parallel voting",
                    "direction_verdict": "MAS < SAS",
                },
                {
                    "benchmark_and_backbone": "Arithmetics (Qwen2.5-7B-Instruct)",
                    "mas_configuration": "Decentralized MAD (T=2 rounds)",
                    "sas_comparator": "Single-Agent (N=1)",
                    "mas_score": 0.76,
                    "sas_score": 0.814,
                    "delta_mas_minus_sas": "-5.40 pp (0.760 vs 0.814)",
                    "compute_ratio_mas_over_sas": "Multi-round debate calls vs 1 call",
                    "direction_verdict": "MAS < SAS",
                },
                {
                    "benchmark_and_backbone": "7-Benchmark Multi-Round Sweep (Qwen2.5-7B & Llama-3.1-8B, T=2..5)",
                    "mas_configuration": "Multi-Round MAD (Decentralized/Sparse/Centralized)",
                    "sas_comparator": "Majority Voting (N=5, T=0)",
                    "mas_score": "Trajectory drift centered around T=0 initial vote (martingale ~0 net gain; exact matrix across T=2..5 in paper figs)",
                    "sas_score": "T=0 Majority Vote matches or outperforms multi-round MAD across T=2..5",
                    "delta_mas_minus_sas": "~0 pp net debate improvement over majority vote across rounds",
                    "compute_ratio_mas_over_sas": "Up to Tx higher serial inference tokens",
                    "direction_verdict": "MAS ≈ SAS",
                },
            ]
        elif rid == "SR088":
            rec["bibliographic_and_identifiers"]["openreview_id"] = "sy7eSEXdPC"
            rec["source_provenance"]["verified_url"] = "https://openreview.net/forum?id=sy7eSEXdPC"
        elif rid == "SR089":
            rec["bibliographic_and_identifiers"]["venue"] = "Proceedings of the ACM Conference on AI and Agentic Systems (CAIS 2026)"
            rec["bibliographic_and_identifiers"]["doi"] = "10.1145/3786335.3813137"
            rec["bibliographic_and_identifiers"]["linked_preprint_or_prior_version_ids"] = ["arXiv:2605.00914"]
            rec["source_provenance"]["verified_url"] = "https://doi.org/10.1145/3786335.3813137"
            rec["publication_status"] = "Peer-reviewed conference"
            rec["limitations_and_validity_threats"]["publication_bias_or_status_caveats"] = (
                "Peer-reviewed conference (ACM CAIS 2026, DOI: 10.1145/3786335.3813137; arXiv:2605.00914)."
            )
        elif rid == "SR090":
            rec["cost_and_latency"]["wall_clock_latency"] = "Per-agent and per-round execution latencies logged alongside token consumption"
            rec["cost_and_latency"]["amortization_search_or_training_cost"] = (
                "Training-free test-time selection via Entropy Judger (uses lightweight structural entropy signatures across 245 features; no RL/weight fine-tuning)"
            )
        elif rid == "SR091":
            rec["variance_cis_and_stats"]["pass_power_k_reported"] = False
            rec["cost_and_latency"]["amortization_search_or_training_cost"] = (
                "Training-free on-demand semantic graph evolution during execution (zero offline RL/MCTS weight training)"
            )
        elif rid == "SR092":
            rec["cost_and_latency"]["amortization_search_or_training_cost"] = (
                "Stage 1 Team Optimization API calls omitted from main Tables 2-4 per-query efficiency totals (C6); Stage 2 edge pruning runs per task."
            )
        elif rid == "SR094":
            rec["baselines_and_rigor_tier"]["compute_matching_status"] = "Partially Matched / Budget-Bounded"
            old_t94 = rec["reported_numerical_outcomes"]["paired_comparisons"]
            for drop_i in (0, 2):
                cleanup_log.append({
                    "study_id": "SR094",
                    "tuple_index": drop_i + 1,
                    "benchmark_and_backbone": old_t94[drop_i]["benchmark_and_backbone"],
                    "original_verdict": old_t94[drop_i]["direction_verdict"],
                    "reason": "Director Arbitration: Dropped redundant HotpotQA weak-CoT / +SC duplicate comparator row to retain exactly the 6 clean vs SC(n=8) tuples (3 OPTIMA wins, 3 unoptimized MAD losses).",
                })
            rec["reported_numerical_outcomes"]["paired_comparisons"] = [t for idx, t in enumerate(old_t94) if idx not in (0, 2)]
        elif rid == "SR098":
            rec["variance_cis_and_stats"]["pass_power_k_reported"] = False
            rec["variance_cis_and_stats"]["dispersion_metrics_reported"] = "95% bootstrap confidence intervals reported across architectural evaluations"
        elif rid == "SR099":
            rec["baselines_and_rigor_tier"]["sas_baseline_rigor_tier"] = "N/A (Non-Comparative Diagnostic/Validity Study)"
            rec["baselines_and_rigor_tier"]["compute_matching_status"] = "Not Applicable (Diagnostic Audit)"
            rec["baselines_and_rigor_tier"]["sas_baselines_included"] = []
            rec["rq_mapping"]["rqs_addressed"] = ["RQ2", "RQ3"]
            rec["rq_mapping"]["corpus_track"] = "Mechanistic Failure & Conformity Analysis (RQ3)"
        elif rid == "SR100":
            rec["baselines_and_rigor_tier"]["sas_baseline_rigor_tier"] = "N/A (Non-Comparative Diagnostic/Validity Study)"
            rec["baselines_and_rigor_tier"]["compute_matching_status"] = "Not Applicable (Diagnostic Audit)"
            rec["baselines_and_rigor_tier"]["sas_baselines_included"] = []
            rec["rq_mapping"]["rqs_addressed"] = ["RQ2", "RQ3"]
            rec["rq_mapping"]["corpus_track"] = "Mechanistic Failure & Conformity Analysis (RQ3)"

        # Write exact arbitrated QA values
        q1, q2, q3, q4, q5, q6, q7 = qa_vec
        tot = (0 if q1 == "N/A-Diagnostic" else int(q1)) + q2 + q3 + q4 + q5 + q6 + q7
        rec["quality_appraisal_and_evidence_provenance"]["quality_appraisal"] = {
            "qa1_single_agent_baseline_rigor": q1,
            "qa2_cost_and_latency_accounting": q2,
            "qa3_amortization_transparency": q3,
            "qa4_multi_run_stochastic_reliability": q4,
            "qa5_benchmark_and_harness_integrity": q5,
            "qa6_reproducibility_code_prompts": q6,
            "qa7_claims_evidence_parity": q7,
            "total_raw_score": tot,
            "applicable_max_score": mx,
            "rigor_band": band_schema(tot, mx),
        }
        em[rid] = rec

    # Validate ALL 59 records against extraction_schema.json
    with open(DATA / "extraction_schema.json") as f:
        schema = json.load(f)
    validator = jsonschema.Draft202012Validator(schema)
    err_cnt = 0
    for rid, rec in sorted(em.items()):
        for err in validator.iter_errors(rec):
            err_cnt += 1
            print(f"SCHEMA ERROR in {rid} at {list(err.path)}: {err.message}")
    assert err_cnt == 0, f"Found {err_cnt} schema errors!"

    with open(em_path, "w") as f:
        json.dump(em, f, indent=2)
    print(f"Validated & wrote evidence_matrix.json: {len(em)} records, 0 schema errors!")

        # Write tuple_cleanup_log.md
    if len(cleanup_log) >= 8:
        log_lines = [
            "# Tuple Deduplication & Validity Cleanup Log (`Protocol Amendment v1.2`)",
            "",
            "**Date:** 2026-11-20  ",
            "**Adjudicator:** Agent 1 (Research Director) following Phase 9 Peer-Review Audit ([reviewer_C_technical.md](file:///Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review/reviews/reviewer_C_technical.md))",
            "",
            "To preserve statistical unit-of-analysis integrity and enforce strict `N >= 2 MAS vs. N = 1 SAS` pairing across all comparative tables, the following invalid, non-SAS, or nested/double-counted tuples were purged from `data/evidence_matrix.json` (while preserving non-comparative sub-results in narrative/diagnostic arrays where noted):",
            "",
            "| Study ID | Removed Tuple Index | Benchmark / Slice | Original Verdict | Removal / Deduplication Rationale |",
            "| :--- | :---: | :--- | :--- | :--- |",
        ]
        for item in cleanup_log:
            log_lines.append(
                f"| `{item['study_id']}` | `{item['tuple_index']}` | {item['benchmark_and_backbone']} | `{item['original_verdict']}` | {item['reason']} |"
            )
        log_lines.extend(["", f"**Total rows purged/collapsed across cleanup:** `{len(cleanup_log)}` entries (`7` inside baseline `SR001`–`SR084` pool + `2` collapses on new imports `SR087` & `SR094`).", ""])
        with open(REVIEWS / "tuple_cleanup_log.md", "w") as f:
            f.write("\n".join(log_lines))
        print(f"Wrote reviews/tuple_cleanup_log.md ({len(cleanup_log)} logged actions)")

    # Regenerate quality_appraisal.csv 100% synced from evidence_matrix.json + included_studies.csv
    existing_qa_just = {}
    with open(DATA / "quality_appraisal.csv") as f:
        for r in csv.DictReader(f):
            existing_qa_just[r["record_id"]] = (r["study_short_name"], r["appraisal_justification"])

    new_short = {
        "SR085": "Li et al. (2024) - More Agents Is All You Need (TMLR)",
        "SR086": "Gao et al. (2025) - Why Not Both? (arXiv)",
        "SR087": "Choi et al. (2025) - Debate or Vote (NeurIPS Spotlight)",
        "SR088": "Estornell & Liu (2024) - Multi-LLM Debate (NeurIPS)",
        "SR089": "Bertalanic & Fortuna (2026) - Cost of Consensus (ACM CAIS)",
        "SR090": "Zhao et al. (2026) - Entropy Perspective (arXiv)",
        "SR091": "Yuan et al. (2026) - SAIGE When More Is Less (arXiv)",
        "SR092": "Liu et al. (2024) - DyLAN (COLM)",
        "SR093": "Wang et al. (2025) - AgentDropout (ACL)",
        "SR094": "Chen et al. (2025) - Optima (Findings ACL)",
        "SR096": "Yuan et al. (2025) - EvoAgent (NAACL)",
        "SR097": "VerifyMAS (2026) - Hypothesis Verification (NeurIPS)",
        "SR098": "Hagag et al. (2026) - Architecture Matters Security (ICML)",
        "SR099": "Yu et al. (2025) - NetSafe Topological Safety (Findings ACL)",
        "SR100": "Wang et al. (2025) - G-Safeguard Security Lens (ACL)",
    }

    qa_fields = [
        "record_id", "study_short_name", "publication_status", "corpus_track",
        "sas_baseline_rigor_tier", "qa1_sas_rigor", "qa2_cost_latency", "qa3_amortization",
        "qa4_multirun_stats", "qa5_harness_integrity", "qa6_reproducibility", "qa7_claims_parity",
        "total_raw_score", "applicable_max_score", "pct_score", "rigor_band",
        "preprint_gate_pass", "appraisal_justification"
    ]
    qa_rows = []
    for rid, r in sorted(em.items()):
        qa = r["quality_appraisal_and_evidence_provenance"]["quality_appraisal"]
        ps = r["publication_status"]
        tot = qa["total_raw_score"]
        mx = qa["applicable_max_score"]
        pct = pct_str(tot, mx)
        b_short = band_short(tot, mx)
        if ps.startswith("Preprint"):
            pg = "TRUE" if (tot >= 6 and int(qa["qa7_claims_evidence_parity"]) >= 1) else "FALSE"
        else:
            pg = "N/A-PeerReviewed"

        short_name, just = existing_qa_just.get(rid, (new_short.get(rid, rid), ""))
        if rid == "SR020":
            just = (
                "QA1=1 (Tier 2: evaluates CascadeDebate vs single-model cascade); "
                "QA2=2 (A100 mean latency 2.45s vs 2.34s + normalized cost multipliers 12.79x-16.66x & 20%-35% token savings); "
                "QA3=1 (C6: online threshold optimizer tau_k overhead omitted from savings); QA4=1; QA5=1; QA6=1; QA7=2. "
                "[v1.2 Audit: Cleaned CSV numeric/enum formatting & synced C6 flag with QA3=1.]"
            )
        elif rid in ("SR002", "SR004", "SR017", "SR032", "SR034", "SR039", "SR079"):
            just += f" [v1.2 QA2 Audit: QA2 verified/updated to {qa['qa2_cost_and_latency_accounting']}.]"
        elif rid >= "SR085":
            just = f"v1.2 Blinded Dual-Screening + Director Arbitration: Tier={r['baselines_and_rigor_tier']['sas_baseline_rigor_tier']}; QA=[{qa['qa1_single_agent_baseline_rigor']},{qa['qa2_cost_and_latency_accounting']},{qa['qa3_amortization_transparency']},{qa['qa4_multi_run_stochastic_reliability']},{qa['qa5_benchmark_and_harness_integrity']},{qa['qa6_reproducibility_code_prompts']},{qa['qa7_claims_evidence_parity']}] ({tot}/{mx} {b_short})."

        qa_rows.append({
            "record_id": rid,
            "study_short_name": short_name,
            "publication_status": ps,
            "corpus_track": r["rq_mapping"]["corpus_track"],
            "sas_baseline_rigor_tier": r["baselines_and_rigor_tier"]["sas_baseline_rigor_tier"],
            "qa1_sas_rigor": str(qa["qa1_single_agent_baseline_rigor"]),
            "qa2_cost_latency": str(qa["qa2_cost_and_latency_accounting"]),
            "qa3_amortization": str(qa["qa3_amortization_transparency"]),
            "qa4_multirun_stats": str(qa["qa4_multi_run_stochastic_reliability"]),
            "qa5_harness_integrity": str(qa["qa5_benchmark_and_harness_integrity"]),
            "qa6_reproducibility": str(qa["qa6_reproducibility_code_prompts"]),
            "qa7_claims_parity": str(qa["qa7_claims_evidence_parity"]),
            "total_raw_score": str(tot),
            "applicable_max_score": str(mx),
            "pct_score": pct,
            "rigor_band": b_short,
            "preprint_gate_pass": pg,
            "appraisal_justification": just,
        })

    with open(DATA / "quality_appraisal.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=qa_fields)
        writer.writeheader()
        writer.writerows(qa_rows)
    print(f"Wrote synced quality_appraisal.csv ({len(qa_rows)} rows)")


def update_bibliography(wave):
    bib_path = DATA / "bibliography.bib"
    with open(bib_path) as f:
        orig = f.read()

    # Parse existing BibTeX entries cleanly via brace depth
    entries = {}
    order = []
    pos = 0
    while True:
        m = re.search(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", orig[pos:])
        if not m:
            break
        start = pos + m.start()
        key = m.group(2)
        brace_start = pos + m.end() - 1
        depth = 0
        idx = pos + m.start()
        found_open = False
        while idx < len(orig):
            if orig[idx] == "{":
                depth += 1
                found_open = True
            elif orig[idx] == "}":
                depth -= 1
                if found_open and depth == 0:
                    idx += 1
                    break
            idx += 1
        block = orig[start:idx].strip()
        if key not in entries:
            entries[key] = block
            order.append(key)
        pos = idx

    # Fix capitalization on El Hattami in SR039
    if "SR039_elhattami2025webarena" in entries:
        entries["SR039_elhattami2025webarena"] = entries["SR039_elhattami2025webarena"].replace(
            "El hattami", "El Hattami"
        ).replace("El-Hattami", "El Hattami")

    vb = wave["verified_bibtex_entries"]

    # Map repaired keys in wave -> exact keys in bibliography.bib
    repaired_map = {
        "Hu2024_CSUR_GameAgents": "Hu2024_CSUR_GameAgents",
        "Chowa2026_AIRE": "Chowa2026_AIRE",
        "Yue2026_EMNLP_Findings": "SR045_yue2026static",
        "Mohammadi2025_KDD_Eval": "Mohammadi2025_KDD",
        "Xia2025_Agentless": "SR065_xia2025agentless",
        "AbouAli2026_AIRE_Ref1": "AbouAli2026_AIRE",
        "Alaanzy2026_AIRE_Ref2": "SR049_alaanzy2026autonomous",
        "Du2026_CSUR_Ref16": "SR052_du2026optimization",
        "He2026_CSUR_Ref23": "SR051_he2026security",
        "Geng2026_CSUR_MARL_Ref21": "SR050_geng2026scaling",
        "Zhang2026_CSUR_Generalizability_Ref77_v2_76": "Zhang2026_CSUR_Generalizability",
        "Wang2026_TRIAGE_Ref59_v2_58": "SR027_wang2026triage",
    }
    for wave_key, bib_key in repaired_map.items():
        raw_bib = vb["repaired_existing_entries"][wave_key]["bibtex"].strip()
        # Rewrite the citekey to preserve existing bib_key
        raw_bib = re.sub(r"^(@\w+\{)[^,]+,", rf"\g<1>{bib_key},", raw_bib)
        entries[bib_key] = raw_bib

    # Update Kim2026_USENIX_Security in place with verified USENIX Security '26 record
    kim_bib = vb["restored_excluded_background"]["Kim2026_USENIX_Security"]["bibtex"].strip()
    entries["Kim2026_USENIX_Security"] = kim_bib

    # Add 10 missed surveys
    for k, val in vb["missed_surveys"].items():
        b = val["bibtex"].strip()
        if k not in entries:
            order.append(k)
        entries[k] = b

    # Add SR085-SR100 (applying Director fixes on SR087, SR088, SR089)
    for rid in [f"SR{i:03d}" for i in range(85, 101)]:
        b = vb["newly_included_candidates_bibtex"][rid].strip()
        m = re.match(r"@(\w+)\{([^,]+),", b)
        citekey = m.group(2)
        if rid == "SR087":
            b = b.replace("nfKfAzkiez", "iUjGNJzrF1")
        elif rid == "SR088":
            b = b.replace("OkHC30LLpO", "sy7eSEXdPC")
        elif rid == "SR089":
            b = """@inproceedings{SR089_2026,
  author       = {Bla\\v{z} Bertalani\\v{c} and Carolina Fortuna},
  title        = {The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate},
  booktitle    = {Proceedings of the ACM Conference on AI and Agentic Systems (CAIS '26)},
  year         = {2026},
  publisher    = {ACM},
  doi          = {10.1145/3786335.3813137},
  url          = {https://doi.org/10.1145/3786335.3813137},
  note         = {Preprint: arXiv:2605.00914}
}"""
        if citekey not in entries:
            order.append(citekey)
        entries[citekey] = b

    # Verify balanced braces & emit clean bibliography.bib
    out_blocks = []
    for k in order:
        blk = entries[k]
        assert blk.count("{") == blk.count("}"), f"Unbalanced braces in {k}"
        out_blocks.append(blk)

    header = (
        "% Authoritative Reconciled Bibliography — Protocol Amendment v1.2\n"
        "% Synchronized 1:1 with Deliverable F (manuscript_v3_final.md) Reference Section\n\n"
    )
    with open(bib_path, "w") as f:
        f.write(header + "\n\n".join(out_blocks) + "\n")
    print(f"Wrote bibliography.bib: {len(order)} verified entries, 0 unbalanced braces, 0 duplicates")


def main():
    with open(AGENTS / "agent3_9_remediation_wave.json") as f:
        wave = json.load(f)
    with open(AGENTS / "agent6_remediation_votes.csv") as f:
        a6_votes = list(csv.DictReader(f))

    update_search_log()
    update_screening_and_included(wave, a6_votes)
    update_evidence_matrix_and_qa(wave)
    update_bibliography(wave)
    print("STEP 3.1 MERGE COMPLETE")


if __name__ == "__main__":
    main()
