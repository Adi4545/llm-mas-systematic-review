#!/usr/bin/env python3
"""
Deterministic Final Audit & Integrity Verifier (scripts/verify_audit.py, Protocol Amendment v1.3).
Verifies all 13 programmatic gates across Deliverables A-H (.md and .docx), evidence_matrix.json,
screening_records.csv, quality_appraisal.csv, search_log.json, bibliography.bib, cite_map.json,
and verified_stats.json, emitting data/verification_report.json and exiting 0 only on full pass.
"""

import csv
import json
import re
import sys
from pathlib import Path
import docx
import jsonschema

ROOT = Path("/Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review")
DATA = ROOT / "data"
DELIV = ROOT / "deliverables"


def main():
    checks = {}
    all_passed = True

    def record(name: str, passed: bool, details):
        nonlocal all_passed
        checks[name] = {"passed": bool(passed), "details": details}
        if not passed:
            all_passed = False

    # 1. All 8 Deliverables exist and are non-empty
    expected_delivs = [
        "Deliverable_A_Journal_Intelligence_Report.md",
        "Deliverable_B_Topic_and_Novelty_Report.md",
        "Deliverable_C_Systematic_Review_Protocol.md",
        "Deliverable_D_Literature_Evidence_Register.md",
        "Deliverable_E_Critical_Synthesis_Report.md",
        "Deliverable_F_Final_Review_Manuscript.md",
        "Deliverable_G_Evidence_and_Reproducibility_Appendix.md",
        "Deliverable_H_Oral_Defense_and_Submission_Pack.md",
    ]
    sizes = {}
    missing = []
    for fn in expected_delivs:
        p = DELIV / fn
        if not p.exists() or p.stat().st_size < 2000:
            missing.append(fn)
        else:
            sizes[fn] = p.stat().st_size
    record("1_all_8_deliverables_exist_nonempty", len(missing) == 0, {"sizes_bytes": sizes, "missing": missing})

    # 2. evidence_matrix.json vs extraction_schema.json (Draft 2020-12)
    with open(DATA / "extraction_schema.json") as f:
        schema = json.load(f)
    with open(DATA / "evidence_matrix.json") as f:
        em = json.load(f)
    validator = jsonschema.Draft202012Validator(schema)
    schema_errs = []
    for rid, rec in sorted(em.items()):
        for e in validator.iter_errors(rec):
            schema_errs.append(f"{rid}:{list(e.path)}:{e.message}")
    record("2_evidence_matrix_jsonschema_valid", len(em) == 59 and len(schema_errs) == 0, {"records": len(em), "errors": schema_errs})

    # 3. PRISMA & CSV arithmetic consistency
    with open(DATA / "search_log.json") as f:
        sl = json.load(f)
    with open(DATA / "screening_records.csv") as f:
        sr = list(csv.DictReader(f))
    with open(DATA / "included_studies.csv") as f:
        inc = list(csv.DictReader(f))
    with open(DATA / "quality_appraisal.csv") as f:
        qa = list(csv.DictReader(f))
    with open(DATA / "verified_stats.json") as f:
        st = json.load(f)
    with open(DATA / "cite_map.json") as f:
        cm = json.load(f)

    sum_raw = sum(s["raw_hits_logged"] for s in sl["searches"])
    sum_dup = sum(s["duplicates_collapsed"] for s in sl["searches"])
    sum_uniq = sum(s["unique_new_records_added"] for s in sl["searches"])
    n_inc_sr = sum(1 for r in sr if r["final_decision"] == "INCLUDE")
    n_exc_sr = sum(1 for r in sr if r["final_decision"] == "EXCLUDE")
    prisma_ok = (
        sum_raw - sum_dup == sum_uniq == len(sr) == 100
        and n_inc_sr == len(inc) == len(qa) == len(em) == 59
        and n_exc_sr == 41
        and st["prisma"]["included_total"] == 59
        and st["comparative_all"]["All"]["n_studies"] == 34
        and st["comparative_all"]["All"]["n_tuples"] == 87
        and st["confounders"]["qa3_1_matches_c6_1to1"] is True
    )
    record("3_prisma_arithmetic_consistent", prisma_ok, {
        "raw": sum_raw, "dup": sum_dup, "uniq": sum_uniq,
        "sr_rows": len(sr), "inc_rows": len(inc), "qa_rows": len(qa), "em_rows": len(em),
        "comp_studies": st["comparative_all"]["All"]["n_studies"],
        "comp_tuples": st["comparative_all"]["All"]["n_tuples"],
        "qa3_1_eq_c6": st["confounders"]["qa3_1_matches_c6_1to1"],
    })

    # Parse Deliverable F
    df_txt = (DELIV / "Deliverable_F_Final_Review_Manuscript.md").read_text()
    m_abs = re.search(r"## Abstract\s+(.*?)\s+---", df_txt, re.S)
    abs_txt = m_abs.group(1).strip() if m_abs else ""
    abs_ws = len(abs_txt.split())
    abs_sp = len(re.split(r"[\s/\u2013-]+", abs_txt))
    abs_bt = "`" not in abs_txt
    record("4_deliverable_f_abstract_compliance", bool(abs_txt) and abs_ws <= 95 and abs_sp <= 100 and abs_bt, {
        "whitespace_words": abs_ws, "split_tokens": abs_sp, "zero_backticks": abs_bt
    })

    # 5. Deliverable F heading hierarchy (12 self-contained sections)
    headings = [line.strip() for line in df_txt.splitlines() if re.match(r"^## \d+\.", line.strip())]
    expected_h = [
        "## 1. Introduction",
        "## 2. Research Questions and Scope",
        "## 3. Systematic Review Methodology",
        "## 4. Core Concepts and Classical Boundaries",
        "## 5. Empirical Synthesis (RQ1–RQ4)",
        "## 6. Evidence Grading, Architecture Map, and Decision Guide",
        "## 7. Open Research Directions",
        "## 8. Threats to Validity and Limitations",
        "## 9. Conclusion",
        "## 10. References",
        "## 11. Declarations",
        "## 12. Self-Contained Reproducibility & Evidence Appendix",
    ]
    record("5_deliverable_f_heading_hierarchy", headings == expected_h and "## 2. Abstract" not in df_txt, {
        "headings_found": headings
    })

    # 6. 1:1 citation-to-Reference-to-BibTeX parity + clean BibTeX hygiene
    total_refs = cm["total"]
    body_part, rest_part = df_txt.split("## 10. References", 1)
    refs_part, rest2 = rest_part.split("## 11. Declarations", 1)
    decl_part, app_part = rest2.split("## 12. Self-Contained Reproducibility & Evidence Appendix", 1)

    cited_nums = set()
    for m in re.finditer(r"\[(\d+(?:,\s*\d+)*)\]", body_part + "\n" + app_part):
        for x in m.group(1).split(","):
            cited_nums.add(int(x.strip()))
    ref_nums = set(int(x) for x in re.findall(r"^\*\*\[(\d+)\]\*\*", refs_part, re.M))
    bib_txt = (DATA / "bibliography.bib").read_text()
    bib_keys = re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib_txt)
    bt_cites = re.findall(r"`\[\d+", body_part + app_part)
    df_no_fence = re.sub(r"```.*?```", "", df_txt, flags=re.S)
    stray_bt = "`" in df_no_fence
    bib_leaks = [s for s in ["Screening Record", "Action Editor", "note =", "note=", "\\%"] if s.lower() in bib_txt.lower()]

    cite_ok = (
        len(bib_keys) == len(set(bib_keys)) == len(ref_nums) == len(cited_nums) == total_refs == 124
        and cited_nums == ref_nums == set(range(1, total_refs + 1))
        and len(bt_cites) == 0
        and not stray_bt
        and len(bib_leaks) == 0
        and bib_txt.count("{") == bib_txt.count("}")
    )
    record("6_citation_reference_bibtex_1to1", cite_ok, {
        "bib_entries": len(bib_keys), "unique_bib_keys": len(set(bib_keys)),
        "ref_entries": len(ref_nums), "cited_nums": len(cited_nums),
        "backticked_citations": len(bt_cites), "stray_backticks_in_md": stray_bt,
        "bib_leaks": bib_leaks, "braces_balanced": bib_txt.count("{") == bib_txt.count("}"),
    })

    # 7. Zero raw internal ID leaks in Deliverable F prose
    raw_leaks = re.findall(r"\bSR\d{3}\b|`F17`|`F18`|FM-2\.3", body_part + decl_part + app_part)
    record("7_zero_raw_internal_id_leaks", len(raw_leaks) == 0, {"leaks": raw_leaks})

    # 8. Zero colliding Tier A-C / Tier I-V / Q0-Q4 (outside App A query labels) or forbidden audience/tone terms in Deliverable F
    collisions = (
        re.findall(r"\bTier [A-C]\b|\bTier [IVX]+\b", body_part + decl_part + app_part)
        + re.findall(r"\bQ[0-4]\b", body_part + decl_part)
    )
    bad_tone_pats = [
        r"\bm\.tech\b", r"graduate research committee", r"tmlr backup",
        r"post-peer-review remediation", r"\bcandid\b", r"\bcandor\b",
        r"\bunambiguous(?:ly)?\b", r"\bzero[- ]fabrication\b", r"\btwice-rejected\b",
    ]
    bad_tone_hits = [p for p in bad_tone_pats if re.search(p, body_part + decl_part + app_part, re.I)]
    record("8_zero_colliding_labels_or_audience_slips", len(collisions) == 0 and len(bad_tone_hits) == 0, {
        "collisions": collisions, "bad_tone_hits": bad_tone_hits
    })

    # 9. Zero banned AI cliches in Deliverable F prose (excluding Reference titles)
    cliches = ["in recent years", "paradigm shift", "game-changer", "game changer", "delve into", "tapestry", "landscape of", "it is worth noting"]
    prose_lc = (body_part + decl_part).lower()
    cliche_hits = [c for c in cliches if c in prose_lc]
    record("9_zero_prose_ai_cliches", len(cliche_hits) == 0, {"cliche_hits": cliche_hits})

    # 10. Zero fabricated similarity % or acceptance probability claims across Deliverables A-H
    fab_hits = {}
    fab_pat = re.compile(r"(\b\d+(?:\.\d+)?%\s*(?:similarity|plagiarism|turnitin|ithenticate|acceptance\s+(?:rate|chance|probability))|(?:turnitin|ithenticate)\s*[:=]?\s*\d+(?:\.\d+)?%)", re.I)
    for fn in expected_delivs:
        txt = (DELIV / fn).read_text()
        matches = fab_pat.findall(txt)
        if matches:
            fab_hits[fn] = matches
    record("10_zero_fabricated_similarity_or_acceptance_pct", len(fab_hits) == 0, {"hits": fab_hits})

    # 11. Headline numerical alignment between Deliverable F and verified_stats.json (v1.4)
    ca = st["comparative_all"]
    cr = st["comparative_archival"]
    es = st["effect_size_meta"]
    cf = st["confounders"]
    pk = st["pass_power_k"]
    dd = st["dense_debate_conformity"]
    nv = st["nv_inventory"]
    req_tokens = [
        f"{st['prisma']['included_total']} studies",
        f"{ca['All']['n_tuples']} cleaned paired comparisons",
        f"{ca['Tier 1']['win_pct']}%",
        f"{ca['Tier 1']['loss_pct']}%",
        "7.0%–45.2%",
        f"{ca['Tier 2+3']['win_pct']}%",
        f"{ca['tuple_attenuation_pp']} percentage points",
        f"{cr['tuple_attenuation_pp']} pp",
        f"{ca['study_frac_attenuation_pp']}",
        f"{ca['perm_p_study_frac_t1_vs_t23']}",
        f"{ca['fisher_p_t1_vs_t23']}",
        f"{cf['qa3_1_count']}/{cf['learned_optimizers_total']}",
        f"{pk['comparative_true']}/{pk['comparative_verifiable_den']}",
        f"{dd['conformity_count']}/{dd['dense_debate_total']}",
        f"{nv['scalar_nv_fields']}",
        f"{nv['leaf_nv_strings']}",
        "163/170",
        f"{es['strong_controls_all_models']['study_mean_pp']:+.2f} pp",
        f"{es['strong_controls_main_qwen']['study_mean_pp']:+.2f} pp",
        "Moderate Certainty",
    ]
    missing_tokens = [t for t in req_tokens if t not in df_txt]
    record("11_deliverable_f_matches_verified_stats", len(missing_tokens) == 0, {
        "checked_tokens": req_tokens, "missing_tokens": missing_tokens
    })

    # 12. Zero corrupted ASCII control bytes across Deliverables E-H & Table 17 totals
    ctrl_hits = {}
    for fn in expected_delivs[4:]:
        raw = (DELIV / fn).read_text()
        bad = [f"L{ln}:0x{ord(ch):02x}" for ln, line in enumerate(raw.splitlines(), 1) for ch in line if ord(ch) < 32]
        if bad:
            ctrl_hits[fn] = bad
    t17_ok = (
        "| Total Corpus Studies |" in df_txt
        and "| 59 / 7 |" in df_txt
        and "| Non-Topological Diagnostic / Validity Studies (N/A) |" in df_txt
    )
    record("12_zero_ctrl_chars_and_table17_totals", len(ctrl_hits) == 0 and t17_ok, {
        "control_char_hits": ctrl_hits, "table17_59_7_total_present": t17_ok
    })

    # 13. DOCX cleanliness, 4 embedded figures, Section 12 Appendix & 124 refs
    docx_targets = [
        ("Deliverable_F_Final_Review_Manuscript.docx", 18, 4, True),
        ("Deliverable_G_Evidence_and_Reproducibility_Appendix.docx", 5, 0, False),
        ("Deliverable_H_Oral_Defense_and_Submission_Pack.docx", 0, 0, False),
    ]
    docx_details = {}
    docx_ok = True
    bad_docx_tokens = ["```mermaid", "![Figure", "xychart-beta", "\\binom{", "\\frac{", "\\text{", "\\mathrm{", "\\mathbb", "≤ftrightarrow", "\\%", "`", "## 1."]
    for fname, min_tbl, exp_fig, chk_refs in docx_targets:
        dp = DELIV / fname
        if not dp.exists():
            docx_ok = False
            docx_details[fname] = {"exists": False}
            continue
        d = docx.Document(str(dp))
        all_txt = "\n".join(p.text for p in d.paragraphs)
        for tbl in d.tables:
            for row in tbl.rows:
                for cell in row.cells:
                    all_txt += "\n" + cell.text
        found_bad = [bt for bt in bad_docx_tokens if bt in all_txt]
        miss_refs = []
        if chk_refs:
            miss_refs = [k for k in range(1, 125) if f"[{k}]" not in all_txt]
        has_app = ("Self-Contained Reproducibility & Evidence Appendix" in all_txt) if chk_refs else True
        item_ok = (
            len(d.tables) >= min_tbl
            and (exp_fig == 0 or len(d.inline_shapes) == exp_fig)
            and len(found_bad) == 0
            and len(miss_refs) == 0
            and has_app
        )
        if not item_ok:
            docx_ok = False
        docx_details[fname] = {
            "paragraphs": len(d.paragraphs),
            "tables": len(d.tables),
            "inline_shapes": len(d.inline_shapes),
            "bad_tokens": found_bad,
            "missing_refs": miss_refs,
            "has_section12_appendix": has_app,
            "ok": item_ok,
        }
    record("13_docx_cleanliness_figures_and_parity", docx_ok, docx_details)

    # 14. Section 12 self-contained completeness & multi-node Mermaid + PNG embeds (Protocol v1.4)
    fig_embeds = len(re.findall(r"^!\[Figure [1-4]:", df_txt, re.M))
    mermaid_blocks = re.findall(r"```mermaid\n(.*?)\n```", df_txt, re.S)
    mermaid_min_lines = min((len(b.splitlines()) for b in mermaid_blocks), default=0)

    def count_section_rows(sec_header_pat: str, next_header_pat: str | None) -> int:
        m = re.search(sec_header_pat, app_part)
        if not m:
            return 0
        sub = app_part[m.end():]
        if next_header_pat:
            m2 = re.search(next_header_pat, sub)
            if m2:
                sub = sub[:m2.start()]
        rows = [ln for ln in sub.splitlines() if ln.strip().startswith("|") and not re.match(r"^\|\s*:?-{2,}", ln.strip())]
        return max(0, len(rows) - 1)

    q_bool_ok = all(f"**{q}" in app_part for q in ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"]) and '("multi-agent"' in app_part
    app_b_rows = count_section_rows(r"### Appendix B:[^\n]+\n", r"\n### Appendix C:")
    app_c1_rows = count_section_rows(r"#### C\.1[^\n]+\n", r"\n#### C\.2")
    app_c2_rows = count_section_rows(r"#### C\.2[^\n]+\n", r"\n### Appendix D:")
    app_e_rows = len(re.findall(r"^\| Excl-\d{2} \|", app_part, re.M))
    sec12_ok = (
        fig_embeds == 4
        and len(mermaid_blocks) == 4
        and mermaid_min_lines >= 6
        and q_bool_ok
        and app_b_rows == 59
        and app_c1_rows == 87
        and app_c2_rows == 34
        and app_e_rows == 41
    )
    record("14_section12_completeness_and_real_mermaid", sec12_ok, {
        "fig_embeds": fig_embeds, "mermaid_blocks": len(mermaid_blocks), "mermaid_min_lines": mermaid_min_lines,
        "q1_q6_present": q_bool_ok, "app_b_rows": app_b_rows, "app_c1_rows": app_c1_rows,
        "app_c2_rows": app_c2_rows, "app_e_rows": app_e_rows,
    })

    # 15. Round-2 Referee factual, BibTeX & process-leak checks
    sr_raw = (DATA / "screening_records.csv").read_text()
    leak_files = {}
    ban_pats = [r"25\.8%", r"ARR #1068", r"Remediation-v1\.2"]
    for fn in expected_delivs[3:]:
        txt = (DELIV / fn).read_text()
        hits = [p for p in ban_pats if re.search(p, txt, re.I)]
        if fn != "Deliverable_H_Oral_Defense_and_Submission_Pack.md" and re.search(r"protocol amendment", txt, re.I):
            hits.append("protocol amendment")
        if hits:
            leak_files[fn] = hits
    df_no_paywall = ("paywalled NV on" not in df_txt) and ("paywalled NMI" not in df_txt)
    grade_ok = "| Moderate Certainty (Observational Cross-Study + Within-Study Contrasts) |" in df_txt
    bib_v14_ok = (
        "Towards Scaling Laws" in bib_txt
        and "Toward Scaling Laws" not in bib_txt
        and "311--329" in bib_txt
        and "376--397" in bib_txt
        and "ARR Submission" not in bib_txt
        and "ARR #1068" not in sr_raw
    )
    record("15_round2_referee_regression_and_bibtex_fixes", len(leak_files) == 0 and df_no_paywall and grade_ok and bib_v14_ok, {
        "leak_files": leak_files, "df_no_kim_paywall_claim": df_no_paywall,
        "grade_parity_downgraded_moderate": grade_ok, "bib_and_csv_fixes_ok": bib_v14_ok,
    })

    report = {
        "status": "ALL AUDIT CHECKS PASSED" if all_passed else "AUDIT CHECKS FAILED",
        "passed_count": sum(1 for v in checks.values() if v["passed"]),
        "total_checks": len(checks),
        "checks": checks,
    }
    with open(DATA / "verification_report.json", "w") as f:
        json.dump(report, f, indent=2)

    print(json.dumps({"status": report["status"], "passed": f"{report['passed_count']}/{report['total_checks']}"}, indent=2))
    for k, v in checks.items():
        if not v["passed"]:
            print("FAIL:", k, v["details"])
    if not all_passed:
        sys.exit(1)
    print("ALL AUDIT CHECKS PASSED")


if __name__ == "__main__":
    main()
