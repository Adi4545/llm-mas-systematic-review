#!/usr/bin/env python3
"""
Deterministic Citation Renumbering, Clean BibTeX Formatting, Multi-Method Statistical Synthesis,
Sensitivity Matrix, Effect-Size Aggregation, and Table Renderer (Protocol Amendment v1.3, N=59).
Generates:
  - data/cite_map.json
  - data/formatted_references.md
  - data/verified_stats.json
  - data/rendered_tables.md
"""

import csv
import json
import math
import random
import re
from collections import Counter, defaultdict
from math import comb
from pathlib import Path

ROOT = Path("/Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review")
DATA = ROOT / "data"


LATEX_MAP = {
    r"\"a": "ä", r"\"o": "ö", r"\"u": "ü", r"\"A": "Ä", r"\"O": "Ö", r"\"U": "Ü",
    r"\'a": "á", r"\'e": "é", r"\'i": "í", r"\'o": "ó", r"\'u": "ú", r"\'c": "ć", r"\'n": "ń", r"\'y": "ý",
    r"\'A": "Á", r"\'E": "É", r"\'O": "Ó",
    r"\`a": "à", r"\`e": "è", r"\`o": "ò", r"\`u": "ù",
    r"\^a": "â", r"\^e": "ê", r"\^i": "î", r"\^o": "ô", r"\^u": "û",
    r"\v{c}": "č", r"\v{z}": "ž", r"\v{s}": "š", r"\v{C}": "Č", r"\v{Z}": "Ž", r"\v{S}": "Š",
    r"\u{a}": "ă", r"\u{g}": "ğ", r"\u{A}": "Ă",
    r"\c{c}": "ç", r"\c{s}": "ş", r"\c{t}": "ţ", r"\c{C}": "Ç",
    r"\~n": "ñ", r"\~a": "ã", r"\~o": "õ",
    r"\l": "ł", r"\L": "Ł", r"\o": "ø", r"\O": "Ø", r"\ss": "ß",
    r"\&": "&", r"\#": "#", r"\_": "_", r"--": "–", r"---": "—", r"``": '"', r"''": '"',
}


def latex_to_unicode(s: str) -> str:
    if not s:
        return ""
    s = re.sub(r"\\v\{([a-zA-Z])\}", lambda m: LATEX_MAP.get(f"\\v{{{m.group(1)}}}", m.group(1)), s)
    s = re.sub(r"\\u\{([a-zA-Z])\}", lambda m: LATEX_MAP.get(f"\\u{{{m.group(1)}}}", m.group(1)), s)
    s = re.sub(r"\\c\{([a-zA-Z])\}", lambda m: LATEX_MAP.get(f"\\c{{{m.group(1)}}}", m.group(1)), s)
    s = re.sub(r"\\'\{?([a-zA-Z])\}?", lambda m: LATEX_MAP.get(f"\\'{m.group(1)}", m.group(1)), s)
    s = re.sub(r'\\"\{?([a-zA-Z])\}?', lambda m: LATEX_MAP.get(f'\\"{m.group(1)}', m.group(1)), s)
    s = re.sub(r"\\`\{?([a-zA-Z])\}?", lambda m: LATEX_MAP.get(f"\\`{m.group(1)}", m.group(1)), s)
    s = re.sub(r"\\\^\{?([a-zA-Z])\}?", lambda m: LATEX_MAP.get(f"\\^{m.group(1)}", m.group(1)), s)
    s = re.sub(r"\\~\{?([a-zA-Z])\}?", lambda m: LATEX_MAP.get(f"\\~{m.group(1)}", m.group(1)), s)
    s = s.replace("$\\tau$", "τ")
    for k, v in LATEX_MAP.items():
        s = s.replace(k, v)
    s = s.replace("{", "").replace("}", "")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def parse_bib_entries(bib_text: str):
    entries = []
    pos = 0
    while True:
        m = re.search(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", bib_text[pos:])
        if not m:
            break
        entry_type = m.group(1).lower()
        key = m.group(2)
        idx = pos + m.start()
        depth = 0
        opened = False
        while idx < len(bib_text):
            ch = bib_text[idx]
            if ch == "{":
                depth += 1
                opened = True
            elif ch == "}":
                depth -= 1
                if opened and depth == 0:
                    idx += 1
                    break
            idx += 1
        body = bib_text[pos + m.end():idx - 1]
        fields = parse_bib_fields(body)
        entries.append({"type": entry_type, "key": key, "fields": fields})
        pos = idx
    return entries


def parse_bib_fields(body: str):
    fields = {}
    i = 0
    n = len(body)
    while i < n:
        while i < n and body[i] in " \t\r\n,":
            i += 1
        if i >= n:
            break
        m = re.match(r"([a-zA-Z0-9_-]+)\s*=\s*", body[i:])
        if not m:
            break
        fname = m.group(1).lower()
        i += m.end()
        if i >= n:
            break
        if body[i] == "{":
            depth = 0
            start = i + 1
            while i < n:
                if body[i] == "{":
                    depth += 1
                elif body[i] == "}":
                    depth -= 1
                    if depth == 0:
                        val = body[start:i]
                        i += 1
                        break
                i += 1
        elif body[i] == '"':
            i += 1
            start = i
            while i < n and not (body[i] == '"' and body[i - 1] != "\\"):
                i += 1
            val = body[start:i]
            i += 1
        else:
            start = i
            while i < n and body[i] not in ",\r\n}":
                i += 1
            val = body[start:i]
        fields[fname] = val.strip()
    return fields


def split_authors(raw_author: str):
    parts = re.split(r"\s+and\s+", raw_author.strip(), flags=re.I)
    cleaned = []
    for p in parts:
        p = latex_to_unicode(p)
        if "," in p:
            segs = [x.strip() for x in p.split(",", 1)]
            full = f"{segs[1]} {segs[0]}".strip()
            surname = segs[0]
        else:
            full = p
            toks = p.split()
            surname = toks[-1] if toks else p
            if len(toks) >= 2 and toks[-2].lower() in ("el", "van", "von", "de", "la", "al"):
                surname = f"{toks[-2]} {toks[-1]}"
        cleaned.append((full, surname))
    return cleaned


def format_authors_acm(author_pairs):
    names = [a[0] for a in author_pairs]
    if not names:
        return "Anonymous"
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} and {names[1]}"
    return ", ".join(names[:-1]) + f", and {names[-1]}"


def strip_accents_for_sort(s: str) -> str:
    import unicodedata
    nk = unicodedata.normalize("NFKD", s)
    return "".join(c for c in nk if not unicodedata.combining(c)).lower()


def build_citations():
    with open(DATA / "bibliography.bib") as f:
        bib_entries = parse_bib_entries(f.read())

    sortable = []
    for e in bib_entries:
        flds = e["fields"]
        auths = split_authors(flds.get("author", "Anonymous"))
        first_surname = strip_accents_for_sort(auths[0][1]) if auths else "zzz"
        first_full = strip_accents_for_sort(auths[0][0]) if auths else "zzz"
        year = re.sub(r"\D", "", flds.get("year", "9999"))[:4] or "9999"
        title = latex_to_unicode(flds.get("title", ""))
        sortable.append((first_surname, first_full, int(year), strip_accents_for_sort(title), e, auths, title, year))

    sortable.sort(key=lambda x: (x[0], x[1], x[2], x[3]))

    by_num = {}
    by_key = {}
    by_study_id = {}
    ref_lines = []

    for idx, item in enumerate(sortable, 1):
        _, _, _, _, e, auths, title, year = item
        flds = e["fields"]
        key = e["key"]
        by_key[key] = idx
        m_sr = re.match(r"^(SR\d{3})(?:_|$)", key)
        if m_sr:
            by_study_id[m_sr.group(1)] = idx

        auth_str = format_authors_acm(auths)
        venue_parts = []
        if e["type"] == "article":
            j = latex_to_unicode(flds.get("journal", ""))
            v_str = f"*{j}*" if j else ""
            vol = flds.get("volume", "")
            num = flds.get("number", "")
            art = flds.get("articleno", "")
            pgs = latex_to_unicode(flds.get("pages", ""))
            meta = []
            if vol and num:
                meta.append(f"{vol}, {num}")
            elif vol:
                meta.append(f"Vol. {vol}")
            if art:
                meta.append(f"Article {art}")
            if pgs:
                meta.append(f"pp. {pgs}")
            if v_str:
                venue_parts.append(v_str + (f" ({', '.join(meta)})" if meta else ""))
        elif e["type"] in ("inproceedings", "proceedings"):
            bk = latex_to_unicode(flds.get("booktitle", ""))
            pgs = latex_to_unicode(flds.get("pages", ""))
            if bk:
                venue_parts.append(f"In *{bk}*" + (f", pp. {pgs}" if pgs else ""))
        elif e["type"] == "book":
            pub = latex_to_unicode(flds.get("publisher", ""))
            if pub:
                venue_parts.append(pub)
        elif e["type"] == "techreport":
            inst = latex_to_unicode(flds.get("institution", ""))
            num = latex_to_unicode(flds.get("number", ""))
            venue_parts.append(f"Technical Report {num}, {inst}".strip(", "))
        else:
            hp = latex_to_unicode(flds.get("howpublished", ""))
            if hp:
                venue_parts.append(hp)

        pub = latex_to_unicode(flds.get("publisher", ""))
        if pub and e["type"] in ("inproceedings", "article"):
            venue_parts.append(pub)

        doi = latex_to_unicode(flds.get("doi", ""))
        url = latex_to_unicode(flds.get("url", ""))
        eprint = latex_to_unicode(flds.get("eprint", ""))

        loc_parts = []
        if doi:
            doi_url = doi if doi.startswith("http") else f"https://doi.org/{doi}"
            loc_parts.append(doi_url)
        elif url:
            loc_parts.append(url)
        elif eprint and "arxiv" in flds.get("archiveprefix", "").lower():
            loc_parts.append(f"https://arxiv.org/abs/{eprint}")

        if eprint and "arxiv.org/abs/" not in " ".join(loc_parts):
            venue_parts.append(f"arXiv:{eprint}")

        title_clean = title.rstrip(".")
        auth_clean = auth_str.rstrip(".")
        segs = [f"**[{idx}]** {auth_clean}. {year}. {title_clean}."]
        if venue_parts:
            segs.append(". ".join(p.rstrip(".") for p in venue_parts if p) + ".")
        if loc_parts:
            segs.append(" ".join(loc_parts))

        line = " ".join(segs)
        line = re.sub(r"\.\.+", ".", line)
        line = re.sub(r"\s+", " ", line).strip()
        ref_lines.append(line)

        by_num[str(idx)] = {
            "num": idx,
            "key": key,
            "study_id": m_sr.group(1) if m_sr else None,
            "short_cite": f"{auths[0][1]}{' et al.' if len(auths) > 2 else (f' & {auths[1][1]}' if len(auths) == 2 else '')} ({year})",
            "title": title,
            "year": year,
        }

    cite_map = {"total": len(sortable), "by_num": by_num, "by_key": by_key, "by_study_id": by_study_id}
    with open(DATA / "cite_map.json", "w") as f:
        json.dump(cite_map, f, indent=2)
    refs_out = "\n\n".join(ref_lines) + "\n"
    for bad in ["Screening Record", "Action Editor", "Topic T9", "upstream CSV", r"\%", "``"]:
        assert bad not in refs_out, f"Ref formatting leak detected: {bad}"
    with open(DATA / "formatted_references.md", "w") as f:
        f.write(refs_out)
    print(f"Built cite_map.json & formatted_references.md ({len(sortable)} clean entries)")
    return cite_map


def cohen_kappa(pairs):
    n = len(pairs)
    if n == 0:
        return 0.0, 0.0
    agree = sum(1 for a, b in pairs if a == b)
    po = agree / n
    labels = set(a for a, _ in pairs) | set(b for _, b in pairs)
    pe = sum((sum(1 for a, _ in pairs if a == lbl) / n) * (sum(1 for _, b in pairs if b == lbl) / n) for lbl in labels)
    kappa = (po - pe) / (1.0 - pe) if abs(1.0 - pe) > 1e-12 else 1.0
    return po, kappa


def wilson_ci(k: int, n: int, z: float = 1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    denom = 1.0 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = (z * math.sqrt((p * (1 - p) + z * z / (4 * n)) / n)) / denom
    return (max(0.0, center - half), min(1.0, center + half))


def fisher_exact_2sided(a: int, b: int, c: int, d: int) -> float:
    n = a + b + c + d
    r1 = a + b
    c1 = a + c
    def p(x):
        return comb(r1, x) * comb(n - r1, c1 - x) / comb(n, c1)
    p0 = p(a)
    lo = max(0, c1 - (n - r1))
    hi = min(r1, c1)
    return sum(p(x) for x in range(lo, hi + 1) if p(x) <= p0 + 1e-12)


def cluster_bootstrap_group(grp, n_boot=10000, seed=42, use_adj_1pp=False):
    rng = random.Random(seed)
    n_s = len(grp)
    if n_s == 0:
        return {"win_ci": [0.0, 0.0], "loss_ci": [0.0, 0.0], "frac_win_ci": [0.0, 0.0]}
    win_rates = []
    loss_rates = []
    frac_wins = []
    key = "adj_verdicts" if use_adj_1pp else "verdicts"
    for _ in range(n_boot):
        samp = [grp[rng.randrange(n_s)] for _ in range(n_s)]
        vs = [v for s in samp for v in s[key]]
        tot = len(vs)
        win_rates.append(100.0 * sum(1 for v in vs if v == "MAS > SAS") / tot)
        loss_rates.append(100.0 * sum(1 for v in vs if v == "MAS < SAS") / tot)
        frac_wins.append(100.0 * sum(sum(1 for v in s[key] if v == "MAS > SAS") / len(s[key]) for s in samp) / n_s)
    win_rates.sort()
    loss_rates.sort()
    frac_wins.sort()
    lo_idx = int(0.025 * n_boot)
    hi_idx = int(0.975 * n_boot)
    return {
        "win_ci": [round(win_rates[lo_idx], 1), round(win_rates[hi_idx], 1)],
        "loss_ci": [round(loss_rates[lo_idx], 1), round(loss_rates[hi_idx], 1)],
        "frac_win_ci": [round(frac_wins[lo_idx], 1), round(frac_wins[hi_idx], 1)],
    }


def cluster_bootstrap_diff_ci(g1, g2, n_boot=10000, seed=42):
    rng = random.Random(seed)
    if not g1 or not g2:
        return {"tuple_diff_ci": [0.0, 0.0], "frac_diff_ci": [0.0, 0.0]}
    t_diffs = []
    f_diffs = []
    n1, n2 = len(g1), len(g2)
    for _ in range(n_boot):
        s1 = [g1[rng.randrange(n1)] for _ in range(n1)]
        s2 = [g2[rng.randrange(n2)] for _ in range(n2)]
        v1 = [v for s in s1 for v in s["verdicts"]]
        v2 = [v for s in s2 for v in s["verdicts"]]
        t1 = 100.0 * sum(1 for v in v1 if v == "MAS > SAS") / len(v1)
        t2 = 100.0 * sum(1 for v in v2 if v == "MAS > SAS") / len(v2)
        f1 = 100.0 * sum(sum(1 for v in s["verdicts"] if v == "MAS > SAS") / len(s["verdicts"]) for s in s1) / n1
        f2 = 100.0 * sum(sum(1 for v in s["verdicts"] if v == "MAS > SAS") / len(s["verdicts"]) for s in s2) / n2
        t_diffs.append(t1 - t2)
        f_diffs.append(f1 - f2)
    t_diffs.sort()
    f_diffs.sort()
    lo_idx = int(0.025 * n_boot)
    hi_idx = int(0.975 * n_boot)
    return {
        "tuple_diff_ci": [round(t_diffs[lo_idx], 1), round(t_diffs[hi_idx], 1)],
        "frac_diff_ci": [round(f_diffs[lo_idx], 1), round(f_diffs[hi_idx], 1)],
    }


def permutation_test_study_frac(g1, g2, n_perm=20000, seed=42):
    """Two-sided exact randomization test on study-level fractional win rates."""
    if not g1 or not g2:
        return 1.0
    x1 = [sum(1 for v in s["verdicts"] if v == "MAS > SAS") / len(s["verdicts"]) for s in g1]
    x2 = [sum(1 for v in s["verdicts"] if v == "MAS > SAS") / len(s["verdicts"]) for s in g2]
    obs = abs(sum(x1) / len(x1) - sum(x2) / len(x2))
    comb_vals = x1 + x2
    n1 = len(x1)
    rng = random.Random(seed)
    cnt = 0
    for _ in range(n_perm):
        rng.shuffle(comb_vals)
        d = abs(sum(comb_vals[:n1]) / n1 - sum(comb_vals[n1:]) / (len(comb_vals) - n1))
        if d >= obs - 1e-12:
            cnt += 1
    return round((cnt + 1) / (n_perm + 1), 4)


def extract_numeric_pp(tp):
    """
    Returns delta_pp (MAS - SAS on a 0-100 scale) if both MAS and SAS scores are exact numbers on %/0-1 scale,
    excluding 0-10 rating scales like MT-Bench. Returns None if not cleanly numeric.
    """
    ms = tp.get("mas_score")
    ss = tp.get("sas_score")
    if isinstance(ms, (int, float)) and isinstance(ss, (int, float)):
        bench = tp.get("benchmark_and_backbone", "").lower()
        if "mt-bench" in bench:
            return None
        # Normalize 0..1 proportions to 0..100 percentage points when both <= 1.05
        if abs(ms) <= 1.05 and abs(ss) <= 1.05:
            return round((ms - ss) * 100.0, 2)
        return round(ms - ss, 2)
    return None


def classify_task_family(bench_text: str) -> str:
    t = bench_text.lower()
    if any(k in t for k in ["finance-agent", "browsecomp", "agentif", "nl2repo", "deep research", "hotpot", "2wiki", "drop"]):
        if "single-turn" not in t and "table 1" not in t:
            return "Decomposable / Multi-Source & Info-Split"
    if any(k in t for k in ["finance-agent", "browsecomp", "agentif", "nl2repo", "deep research"]):
        return "Decomposable / Multi-Source & Info-Split"
    if any(k in t for k in ["plancraft", "workbench", "terminal-bench", "travelplanner", "swe-bench", "chess", "scienceworld", "crossword", "codenames"]):
        return "Sequential Planning, Embodied & Tool/SWE"
    if any(k in t for k in ["gsm", "math", "arithmetic", "svamp", "aqua", "multiarith", "knight", "logic", "folio"]):
        return "Math & Symbolic Logic"
    return "General QA, Truthfulness & Instruction Following"


def summarize_pp_deltas(items):
    """
    items: list of dicts {"rid": str, "delta_pp": float}.
    Aggregates strictly at the study level (one unweighted mean per study) alongside
    study-level median, IQR, and full study range (Min to Max).
    Does NOT fabricate missing item-level variances or run unweighted pooling across mismatched tasks.
    """
    if not items:
        return {"n_tuples": 0, "n_studies": 0}
    by_st = defaultdict(list)
    for x in items:
        by_st[x["rid"]].append(x["delta_pp"])
    st_means = sorted(sum(v) / len(v) for v in by_st.values())
    n_s = len(st_means)
    q1 = st_means[n_s // 4]
    med = st_means[n_s // 2] if n_s % 2 == 1 else (st_means[n_s // 2 - 1] + st_means[n_s // 2]) / 2.0
    q3 = st_means[(3 * n_s) // 4]

    rng = random.Random(42)
    b_means = []
    for _ in range(5000):
        samp = [st_means[rng.randrange(n_s)] for _ in range(n_s)]
        b_means.append(sum(samp) / n_s)
    b_means.sort()
    ci_lo, ci_hi = round(b_means[int(0.025 * 5000)], 2), round(b_means[int(0.975 * 5000)], 2)

    return {
        "n_tuples": len(items),
        "n_studies": n_s,
        "study_mean_pp": round(sum(st_means) / n_s, 2),
        "study_median_pp": round(med, 2),
        "study_iqr_pp": [round(q1, 2), round(q3, 2)],
        "study_range_pp": [round(min(st_means), 2), round(max(st_means), 2)],
        "study_boot_ci95": [ci_lo, ci_hi],
    }


def count_nv_recursive(obj):
    leaf_nv = 0
    if isinstance(obj, dict):
        for v in obj.values():
            leaf_nv += count_nv_recursive(v)
    elif isinstance(obj, list):
        for v in obj:
            leaf_nv += count_nv_recursive(v)
    elif isinstance(obj, str) and "not verifiable from accessible open summary" in obj.lower():
        leaf_nv += 1
    return leaf_nv


def count_direct_scalar_nv(rec):
    cnt = 0
    for _, val in rec.items():
        if isinstance(val, dict):
            for _, v in val.items():
                if isinstance(v, str) and "not verifiable from accessible open summary" in v.lower():
                    cnt += 1
    return cnt


def compute_binomial_se_pct(p1_pct: float, p2_pct: float, n_items: int):
    p1 = p1_pct / 100.0
    p2 = p2_pct / 100.0
    var_pp = ((p1 * (1.0 - p1) / n_items) + (p2 * (1.0 - p2) / n_items)) * 10000.0
    return round(math.sqrt(var_pp), 2), round(var_pp, 2)


def analyze_cohort(cohort_list, extra_groups=None):
    out = {}
    t1 = [s for s in cohort_list if s["tier"] == 1]
    t2 = [s for s in cohort_list if s["tier"] == 2]
    t2a = [s for s in cohort_list if s["tier"] == 2 and not s.get("has_c6", False)]
    t2b = [s for s in cohort_list if s["tier"] == 2 and s.get("has_c6", False)]
    t3 = [s for s in cohort_list if s["tier"] == 3]
    t23 = [s for s in cohort_list if s["tier"] in (2, 3)]
    groups = [
        ("Tier 1", t1),
        ("Tier 2A", t2a),
        ("Tier 2B", t2b),
        ("Tier 2", t2),
        ("Tier 3", t3),
        ("Tier 2+3", t23),
        ("All", cohort_list),
    ]
    if extra_groups:
        groups.extend(extra_groups)

    for name, grp in groups:
        vs = [v for s in grp for v in s["verdicts"]]
        vs_adj = [v for s in grp for v in s["adj_verdicts"]]
        n_s = len(grp)
        n_t = len(vs)
        w = sum(1 for v in vs if v == "MAS > SAS")
        tie = sum(1 for v in vs if v == "MAS ≈ SAS")
        loss = sum(1 for v in vs if v == "MAS < SAS")
        mix = sum(1 for v in vs if v == "Mixed across budgets/subtasks")
        assert w + tie + loss + mix == n_t, f"Unrecognized verdict in {name}: {vs}"

        w_adj = sum(1 for v in vs_adj if v == "MAS > SAS")
        tie_adj = sum(1 for v in vs_adj if v == "MAS ≈ SAS")
        loss_adj = sum(1 for v in vs_adj if v == "MAS < SAS")
        mix_adj = sum(1 for v in vs_adj if v == "Mixed across budgets/subtasks")

        frac_w = (sum(sum(1 for v in s["verdicts"] if v == "MAS > SAS") / len(s["verdicts"]) for s in grp) / n_s) if n_s else 0.0
        frac_l = (sum(sum(1 for v in s["verdicts"] if v == "MAS < SAS") / len(s["verdicts"]) for s in grp) / n_s) if n_s else 0.0
        maj_w = sum(1 for s in grp if sum(1 for v in s["verdicts"] if v == "MAS > SAS") / len(s["verdicts"]) > 0.5)
        maj_ge50_w = sum(1 for s in grp if sum(1 for v in s["verdicts"] if v == "MAS > SAS") / len(s["verdicts"]) >= 0.5)
        unam_w = sum(1 for s in grp if all(v == "MAS > SAS" for v in s["verdicts"]))
        lo_s, hi_s = wilson_ci(maj_w, n_s)
        lo_w_t, hi_w_t = wilson_ci(w, n_t)
        lo_l_t, hi_l_t = wilson_ci(loss, n_t)
        cboot = cluster_bootstrap_group(grp, n_boot=10000, seed=42)

        out[name] = {
            "n_studies": n_s,
            "n_tuples": n_t,
            "wins": w, "ties": tie, "losses": loss, "mixed": mix,
            "win_pct": round(100 * w / n_t, 1) if n_t else 0.0,
            "tie_pct": round(100 * tie / n_t, 1) if n_t else 0.0,
            "loss_pct": round(100 * loss / n_t, 1) if n_t else 0.0,
            "mixed_pct": round(100 * mix / n_t, 1) if n_t else 0.0,
            "win_wilson_ci95": [round(100 * lo_w_t, 1), round(100 * hi_w_t, 1)],
            "loss_wilson_ci95": [round(100 * lo_l_t, 1), round(100 * hi_l_t, 1)],
            "win_boot_ci95": cboot["win_ci"],
            "loss_boot_ci95": cboot["loss_ci"],
            "adj_1pp_wins": w_adj, "adj_1pp_ties": tie_adj, "adj_1pp_losses": loss_adj, "adj_1pp_mixed": mix_adj,
            "adj_1pp_win_pct": round(100 * w_adj / n_t, 1) if n_t else 0.0,
            "study_frac_win_pct": round(100 * frac_w, 1),
            "study_frac_loss_pct": round(100 * frac_l, 1),
            "study_frac_boot_ci95": cboot["frac_win_ci"],
            "study_maj_wins": maj_w,
            "study_maj_win_pct": round(100 * maj_w / n_s, 1) if n_s else 0.0,
            "study_maj_ci95": [round(100 * lo_s, 1), round(100 * hi_s, 1)],
            "study_maj_ge50_wins": maj_ge50_w,
            "study_maj_ge50_win_pct": round(100 * maj_ge50_w / n_s, 1) if n_s else 0.0,
            "study_unam_wins": unam_w,
            "study_unam_win_pct": round(100 * unam_w / n_s, 1) if n_s else 0.0,
            "study_cites": [s["cite"] for s in grp],
        }
    out["tuple_attenuation_pp"] = round(out["Tier 1"]["win_pct"] - out["Tier 2+3"]["win_pct"], 1)
    out["study_frac_attenuation_pp"] = round(out["Tier 1"]["study_frac_win_pct"] - out["Tier 2+3"]["study_frac_win_pct"], 1)
    out["study_maj_attenuation_pp"] = round(out["Tier 1"]["study_maj_win_pct"] - out["Tier 2+3"]["study_maj_win_pct"], 1)
    diff_boot = cluster_bootstrap_diff_ci(t1, t23, n_boot=10000, seed=42)
    out["tuple_attenuation_ci95"] = diff_boot["tuple_diff_ci"]
    out["study_frac_attenuation_ci95"] = diff_boot["frac_diff_ci"]
    out["perm_p_study_frac_t1_vs_t23"] = permutation_test_study_frac(t1, t23, n_perm=20000, seed=42)
    out["perm_p_study_frac_t1_vs_t3"] = permutation_test_study_frac(t1, t3, n_perm=20000, seed=42)
    out["fisher_p_t1_vs_t23"] = round(fisher_exact_2sided(
        out["Tier 1"]["study_maj_wins"], out["Tier 1"]["n_studies"] - out["Tier 1"]["study_maj_wins"],
        out["Tier 2+3"]["study_maj_wins"], out["Tier 2+3"]["n_studies"] - out["Tier 2+3"]["study_maj_wins"],
    ), 4)
    out["fisher_p_t1_vs_t23_ge50"] = round(fisher_exact_2sided(
        out["Tier 1"]["study_maj_ge50_wins"], out["Tier 1"]["n_studies"] - out["Tier 1"]["study_maj_ge50_wins"],
        out["Tier 2+3"]["study_maj_ge50_wins"], out["Tier 2+3"]["n_studies"] - out["Tier 2+3"]["study_maj_ge50_wins"],
    ), 4)
    out["fisher_p_t1_vs_t3"] = round(fisher_exact_2sided(
        out["Tier 1"]["study_maj_wins"], out["Tier 1"]["n_studies"] - out["Tier 1"]["study_maj_wins"],
        out["Tier 3"]["study_maj_wins"], out["Tier 3"]["n_studies"] - out["Tier 3"]["study_maj_wins"],
    ), 4)
    return out


def compute_all_stats(cite_map):
    with open(DATA / "search_log.json") as f:
        sl = json.load(f)
    with open(DATA / "screening_records.csv") as f:
        sr_rows = list(csv.DictReader(f))
    with open(DATA / "quality_appraisal.csv") as f:
        qa_rows = list(csv.DictReader(f))
    with open(DATA / "evidence_matrix.json") as f:
        em = json.load(f)

    id_to_c = cite_map["by_study_id"]

    # 1. PRISMA & IRR
    w1_rows = [r for r in sr_rows if r["record_id"] <= "SR084"]
    s1_w1_po, s1_w1_k = cohen_kappa([(r["stage1_agent3_decision"], r["stage1_agent6_decision"]) for r in w1_rows])
    s1_all_po, s1_all_k = cohen_kappa([(r["stage1_agent3_decision"], r["stage1_agent6_decision"]) for r in sr_rows])

    s2_all_rows = [r for r in sr_rows if r["stage1_agent3_decision"] == "PASS_TO_STAGE2" or r["stage1_agent6_decision"] == "PASS_TO_STAGE2"]
    s2_3class_po, s2_3class_k = cohen_kappa([(r["stage2_agent3_decision"], r["stage2_agent6_decision"]) for r in s2_all_rows])
    s2_bin_po, s2_bin_k = cohen_kappa([("INC" if r["stage2_agent3_decision"] == "INCLUDE" else "EXC", "INC" if r["stage2_agent6_decision"] == "INCLUDE" else "EXC") for r in s2_all_rows])
    corp_pairs = [
        ("INC" if r["stage2_agent3_decision"] == "INCLUDE" else "EXC",
         "INC" if r["stage2_agent6_decision"] == "INCLUDE" else "EXC")
        for r in sr_rows
    ]
    corp_po, corp_k = cohen_kappa(corp_pairs)
    s1_agree_n = sum(1 for r in sr_rows if r["stage1_agent3_decision"] == r["stage1_agent6_decision"])
    s2_agree_n = sum(1 for r in s2_all_rows if r["stage2_agent3_decision"] == r["stage2_agent6_decision"])
    pooled_judg_po = (s1_agree_n + s2_agree_n) / (len(sr_rows) + len(s2_all_rows))

    s1_excl = Counter(r["final_exclusion_code"] for r in sr_rows if r["final_decision"] == "EXCLUDE" and (r["stage1_agent3_decision"] == "EXCLUDE" and r["stage1_agent6_decision"] == "EXCLUDE"))
    s2_excl = Counter(r["final_exclusion_code"] for r in sr_rows if r["final_decision"] == "EXCLUDE" and not (r["stage1_agent3_decision"] == "EXCLUDE" and r["stage1_agent6_decision"] == "EXCLUDE"))

    pub_counts = Counter(r["publication_status"] for r in em.values())
    archival_cnt = pub_counts["Peer-reviewed journal"] + pub_counts["Peer-reviewed conference"]
    peer_rev_cnt = archival_cnt + pub_counts["Workshop"]

    # 2. Track & Rigor Tier Breakdown
    track_counts = Counter(r["rq_mapping"]["corpus_track"] for r in em.values())
    tier_counts = Counter(r["baselines_and_rigor_tier"]["sas_baseline_rigor_tier"] for r in em.values())

    # 3. Comparative Paired Tuples (with practical ±1.0 pp tie adjustments & task family)
    non_interactive_rids = {"SR009", "SR010", "SR011"}
    comp_studies = []
    for rid, r in sorted(em.items()):
        tstr = r["baselines_and_rigor_tier"]["sas_baseline_rigor_tier"]
        if tstr.startswith("Tier 1"):
            tnum = 1
        elif tstr.startswith("Tier 2"):
            tnum = 2
        elif tstr.startswith("Tier 3"):
            tnum = 3
        elif tstr.startswith("Tier 4"):
            tnum = 4
        else:
            continue
        has_c6 = any(f.startswith("C6") for f in r["limitations_and_validity_threats"]["six_class_confounder_flags"])
        tuples = r["reported_numerical_outcomes"].get("paired_comparisons", [])
        verdicts = []
        adj_verdicts = []
        opt_verdicts = []
        task_fams = []
        deltas_pp = []
        for idx_t, tp in enumerate(tuples):
            v = tp["direction_verdict"]
            dpp = extract_numeric_pp(tp)
            deltas_pp.append(dpp)
            verdicts.append(v)
            # Sensitivity D (Practical +/- 1.0 pp Tie Margin): re-code <=1.0 pp gaps (incl. SR004 Table 17 ~1 pp edge) to Tie
            if (dpp is not None and abs(dpp) <= 1.0 and v in ("MAS > SAS", "MAS < SAS")) or (rid == "SR004" and idx_t == 1):
                adj_verdicts.append("MAS ≈ SAS")
            else:
                adj_verdicts.append(v)
            # Optimistic Tier-1 sensitivity: count Nguyen et al. Table 17 (~1 pp edge over 1-pass Long-CoT) as MAS > SAS
            if rid == "SR004" and idx_t == 1:
                opt_verdicts.append("MAS > SAS")
            else:
                opt_verdicts.append(v)
            task_fams.append(classify_task_family(tp.get("benchmark_and_backbone", "")))
        if verdicts:
            comp_studies.append({
                "rid": rid,
                "cite": id_to_c[rid],
                "short_cite": cite_map["by_num"][str(id_to_c[rid])]["short_cite"],
                "tier": tnum,
                "has_c6": has_c6,
                "wave1": rid <= "SR084",
                "status": r["publication_status"],
                "archival": r["publication_status"] in ("Peer-reviewed journal", "Peer-reviewed conference"),
                "interactive_mas": rid not in non_interactive_rids,
                "topology": r["architecture_and_agent_count"]["topology_class"],
                "tuples": tuples,
                "verdicts": verdicts,
                "adj_verdicts": adj_verdicts,
                "opt_verdicts": opt_verdicts,
                "deltas_pp": deltas_pp,
                "task_fams": task_fams,
                "is_mad": ("Debate" in r["architecture_and_agent_count"]["topology_class"] or "MAD" in " ".join(r["architecture_and_agent_count"]["system_names"]) or "debate" in r["bibliographic_and_identifiers"]["title"].lower()),
            })

    all_comp_stats = analyze_cohort(comp_studies)
    arch_comp_stats = analyze_cohort([s for s in comp_studies if s["archival"]])
    wave1_comp_stats = analyze_cohort([s for s in comp_studies if s["wave1"]])
    wave2_t23_stats = analyze_cohort([s for s in comp_studies if not s["wave1"]])
    inter_comp_stats = analyze_cohort([s for s in comp_studies if s["interactive_mas"]])
    zero_search_comp_stats = analyze_cohort([s for s in comp_studies if not s["has_c6"]])

    adj_list = [dict(s, verdicts=s["adj_verdicts"]) for s in comp_studies]
    adj_comp_stats = analyze_cohort(adj_list)
    opt_list = [dict(s, verdicts=s["opt_verdicts"]) for s in comp_studies]
    opt_comp_stats = analyze_cohort(opt_list)

    # Comparator sub-splits inside Tier 1
    t1_vs_voting = []
    t1_vs_single = []
    t1_moa_boundary = []
    for s in comp_studies:
        if s["tier"] != 1:
            continue
        if s["rid"] in ("SR004", "SR005", "SR007"):
            # Note SR004.1 is vs SC; SR004.2 is vs Long-CoT
            if s["rid"] == "SR004":
                t1_vs_voting.append((s["rid"], s["verdicts"][0]))
                t1_vs_single.append((s["rid"], s["verdicts"][1]))
            else:
                for v in s["verdicts"]:
                    t1_vs_voting.append((s["rid"], v))
        elif s["rid"] == "SR010":
            for v in s["verdicts"]:
                t1_moa_boundary.append((s["rid"], v))
        else:
            for v in s["verdicts"]:
                t1_vs_single.append((s["rid"], v))

    def summarize_sub(pairs):
        w = sum(1 for _, v in pairs if v == "MAS > SAS")
        t = sum(1 for _, v in pairs if v == "MAS ≈ SAS")
        l = sum(1 for _, v in pairs if v == "MAS < SAS")
        m = sum(1 for _, v in pairs if v == "Mixed across budgets/subtasks")
        n_s = len(set(r for r, _ in pairs))
        return {"n_studies": n_s, "n_tuples": len(pairs), "wins": w, "ties": t, "losses": l, "mixed": m,
                "win_pct": round(100 * w / len(pairs), 1) if pairs else 0.0,
                "loss_pct": round(100 * l / len(pairs), 1) if pairs else 0.0}

    # Task-family stratification across all tuples & Tier 1
    tf_all = defaultdict(list)
    tf_t1 = defaultdict(list)
    for s in comp_studies:
        for tf, v in zip(s["task_fams"], s["verdicts"]):
            tf_all[tf].append((s["rid"], v))
            if s["tier"] == 1:
                tf_t1[tf].append((s["rid"], v))

    # Effect-size continuous synthesis (strictly study-level aggregations; no missing-variance pooling)
    es_tier1_numeric = []
    es_strong_all = []
    es_strong_main_qwen = []
    es_unmatched_single = []
    es_optima_or_casc = []
    for s in comp_studies:
        rid = s["rid"]
        for tp, dpp in zip(s["tuples"], s["deltas_pp"]):
            if dpp is None:
                continue
            sas_cmp = tp["sas_comparator"].lower()
            mas_cfg = tp["mas_configuration"].lower()
            bench_lc = tp["benchmark_and_backbone"].lower()
            item = {"rid": rid, "cite": s["cite"], "bench": tp["benchmark_and_backbone"], "delta_pp": dpp}
            if s["tier"] == 1:
                es_tier1_numeric.append(item)
            if s["tier"] == 1 or "majority voting" in sas_cmp or "isolated self-correction" in sas_cmp or ("sc(n=8)" in sas_cmp and "unoptimized" in bench_lc):
                es_strong_all.append(item)
                if rid != "SR089" or "qwen2.5-7b" in bench_lc:
                    es_strong_main_qwen.append(item)
            elif "optima" in mas_cfg or "cascadedebate" in mas_cfg or "cascading" in mas_cfg or "saige" in mas_cfg or "ada-rl" in mas_cfg or "mada-rl" in mas_cfg:
                es_optima_or_casc.append(item)
            else:
                es_unmatched_single.append(item)

    # Exact binomial SE & inverse-variance weighting across Bertalanic & Fortuna [6] 3 documented GSM-Hard splits
    cais_splits = [
        ("Qwen2.5-7B (Primary split, n=1,017)", 58.8, 61.0, 1017),
        ("Llama-3.1-8B (Secondary split, n=100)", 39.3, 41.0, 100),
        ("Ministral-3-8B (Secondary split, n=100)", 20.7, 48.3, 100),
    ]
    cais_rows = []
    tot_w = 0.0
    for nm, p_m, p_s, nn in cais_splits:
        se, var_pp = compute_binomial_se_pct(p_m, p_s, nn)
        w = 1.0 / var_pp
        tot_w += w
        cais_rows.append({"model": nm, "n_items": nn, "mas": p_m, "sas": p_s, "delta_pp": round(p_m - p_s, 1), "se_pp": se, "var_pp": var_pp, "w_raw": w})
    for cr in cais_rows:
        cr["iv_weight_pct"] = round(100.0 * cr["w_raw"] / tot_w, 1)
    cais_iv_mean = round(sum(cr["delta_pp"] * cr["w_raw"] for cr in cais_rows) / tot_w, 2)
    cais_item_mean = round(sum(cr["delta_pp"] * cr["n_items"] for cr in cais_rows) / sum(cr["n_items"] for cr in cais_rows), 2)

    effect_size_meta = {
        "tier1_equal_numeric": summarize_pp_deltas(es_tier1_numeric),
        "strong_controls_all_models": summarize_pp_deltas(es_strong_all),
        "strong_controls_main_qwen": summarize_pp_deltas(es_strong_main_qwen),
        "weak_single_pass": summarize_pp_deltas(es_unmatched_single),
        "posttrained_or_selective_escalation": summarize_pp_deltas(es_optima_or_casc),
        "cais26_variance_audit": {
            "splits": cais_rows,
            "unweighted_mean_pp": round(sum(cr["delta_pp"] for cr in cais_rows) / len(cais_rows), 2),
            "item_weighted_mean_pp": cais_item_mean,
            "iv_weighted_mean_pp": cais_iv_mean,
        },
    }

    # Within-Study Paired Contrasts (Weak vs Strong inside same paper)
    within_study_contrasts = [
        {
            "study": f"Smit et al. [{id_to_c['SR005']}]",
            "benchmarks": "MedQA, PubMedQA, MMLU, CosmosQA, GPQA, Chess",
            "weak_or_unmatched": "Untuned multi-round MAD vs. single-pass baselines (outperforms 1x on specific configs)",
            "strong_or_matched": "Same MAD vs. equal-budget Self-Consistency / Medprompt (out-of-the-box gains disappear; tuned agreement needed)",
        },
        {
            "study": f"Wang et al. [{id_to_c['SR006']}]",
            "benchmarks": "ECQA, GSM8K, FOLIO-wiki",
            "weak_or_unmatched": "MAD / ReConcile / CMD vs. Zero-Shot CoT (no demonstrations -> MAS wins)",
            "strong_or_matched": "Same MAS vs. Strong Few-Shot CoT (same-model prompt parity collapses gap to near tie)",
        },
        {
            "study": f"Zhang et al. [{id_to_c['SR007']}]",
            "benchmarks": "9 benchmarks x 4 models (36 scenarios)",
            "weak_or_unmatched": "Standard homogeneous MAD benchmarks in prior papers at >1x calls",
            "strong_or_matched": "Same 5 MAD methods vs. CoT & compute-matched Self-Consistency (<20% win rate; >80% tie or lose)",
        },
        {
            "study": f"Choi et al. [{id_to_c['SR087']}]",
            "benchmarks": "7 benchmarks incl. GSM8K (Qwen2.5-7B)",
            "weak_or_unmatched": "Decentralized MAD (T=2, N=5) vs. Single-Agent (0.7377 vs. 0.7205 macro avg; drops below SAS by T=3/5)",
            "strong_or_matched": "Same MAD vs. T=0 Majority Voting (N=5: 0.8867 MAD vs. 0.9400 MV = -5.33 pp loss on GSM8K)",
        },
        {
            "study": f"Chen et al. (Optima) [{id_to_c['SR094']}]",
            "benchmarks": "HotpotQA, GSM8K, MATH (Llama-3-8B)",
            "weak_or_unmatched": "Unoptimized MAD appears competitive when tested only against 1-pass CoT (33.8% SC omitted)",
            "strong_or_matched": "Unoptimized MAD loses vs. SC(n=8) (-5.4, -7.8, -5.9 pp); OPTIMA beats SC only after RL/DPO (<12h on 8x A100 for HotpotQA/GSM8K, ~24h for MATH)",
        },
        {
            "study": f"Gao et al. [{id_to_c['SR086']}]",
            "benchmarks": "HumanEval, MBPP, GSM8K",
            "weak_or_unmatched": "MetaGPT / SelfCol / MathDebate vs. older GPT-3.5-era SAS (+8.0 to +20.7 pp gains)",
            "strong_or_matched": "Exact same MAS vs. stronger Gemini-2.0-Flash SAS (margins compress to +0.8 to +3.0 pp)",
        },
    ]

    t1_mad = [s for s in comp_studies if s["tier"] == 1 and s["is_mad"]]
    t1_nonmad = [s for s in comp_studies if s["tier"] == 1 and not s["is_mad"]]

    # 4. Quality Appraisal + 12-pt Normalized Sensitivity + Confounders + pass^k + Latency + USD + NV
    band_counts = Counter(r["rigor_band"] for r in qa_rows)
    pct_vals = [float(r["pct_score"]) for r in qa_rows]
    def norm12(r):
        return 100.0 * sum(int(r[f]) for f in [
            "qa2_cost_latency", "qa3_amortization", "qa4_multirun_stats",
            "qa5_harness_integrity", "qa6_reproducibility", "qa7_claims_parity"
        ]) / 12.0

    track_qa = {}
    for tr_key, tr_lbl in [
        ("Primary Comparative Effectiveness & Topology (RQ1/RQ2)", "RQ1/RQ2"),
        ("Mechanistic Failure & Conformity Analysis (RQ3)", "RQ3"),
        ("Evaluation Validity & Harness Reliability Audit (RQ4)", "RQ4"),
    ]:
        sub = [r for r in qa_rows if r["corpus_track"] == tr_key]
        track_qa[tr_lbl] = {
            "n": len(sub),
            "mean_pct": round(sum(float(r["pct_score"]) for r in sub) / len(sub), 1),
            "mean_12pt_pct": round(sum(norm12(r) for r in sub) / len(sub), 1),
        }

    status_qa = {}
    for st_key, st_lbl in [
        ("Archival", ("Peer-reviewed journal", "Peer-reviewed conference")),
        ("Workshop", ("Workshop",)),
        ("Preprint", ("Preprint (arXiv / Preprints.org)",)),
    ]:
        sub = [r for r in qa_rows if r["publication_status"] in st_lbl]
        status_qa[st_key] = {
            "n": len(sub),
            "mean_pct": round(sum(float(r["pct_score"]) for r in sub) / len(sub), 1),
            "mean_12pt_pct": round(sum(norm12(r) for r in sub) / len(sub), 1),
            "qa7_mean": round(sum(int(r["qa7_claims_parity"]) for r in sub) / len(sub), 2),
        }

    crit_means = {
        "qa1_sas_rigor": round(sum(int(r["qa1_sas_rigor"]) for r in qa_rows if r["qa1_sas_rigor"] != "N/A-Diagnostic") / sum(1 for r in qa_rows if r["qa1_sas_rigor"] != "N/A-Diagnostic"), 2),
        "qa1_n": sum(1 for r in qa_rows if r["qa1_sas_rigor"] != "N/A-Diagnostic"),
    }
    for col in ["qa2_cost_latency", "qa3_amortization", "qa4_multirun_stats", "qa5_harness_integrity", "qa6_reproducibility", "qa7_claims_parity"]:
        crit_means[col] = round(sum(int(r[col]) for r in qa_rows) / len(qa_rows), 2)

    # Confounders C1-C6 across all 59 and strictly 34 comparative studies
    c_all = Counter()
    c_comp = Counter()
    all_comp_track_ids = {rid for rid, r in em.items() if not r["baselines_and_rigor_tier"]["sas_baseline_rigor_tier"].startswith("N/A")}
    assert len(all_comp_track_ids) == len(comp_studies) == 34, f"Comp count mismatch: {len(all_comp_track_ids)} vs {len(comp_studies)}"
    for rid, r in em.items():
        for fl in r["limitations_and_validity_threats"]["six_class_confounder_flags"]:
            code = fl.split(":")[0].strip() if ":" in fl else fl
            c_all[code] += 1
            if rid in all_comp_track_ids:
                c_comp[code] += 1

    # Learned/optimized methods (QA3 == 1 == C6)
    qa3_1_ids = sorted(r["record_id"] for r in qa_rows if int(r["qa3_amortization"]) == 1)
    c6_ids = sorted(rid for rid, r in em.items() if any("C6" in f for f in r["limitations_and_validity_threats"]["six_class_confounder_flags"]))
    assert qa3_1_ids == c6_ids, f"QA3==1 vs C6 mismatch: {qa3_1_ids} vs {c6_ids}"
    qa3_1_comp_ids = [rid for rid in qa3_1_ids if rid in all_comp_track_ids]
    qa3_1_diag_ids = [rid for rid in qa3_1_ids if rid not in all_comp_track_ids]

    # pass^k counts
    pk_comp_true = 0
    pk_comp_false = 0
    pk_comp_nv = []
    pk_all_true = []
    pk_all_nv = []
    for rid, r in sorted(em.items()):
        v = r["variance_cis_and_stats"]["pass_power_k_reported"]
        is_c = rid in all_comp_track_ids
        if v is True:
            pk_all_true.append(rid)
            if is_c:
                pk_comp_true += 1
        elif v is False:
            if is_c:
                pk_comp_false += 1
        else:
            pk_all_nv.append(rid)
            if is_c:
                pk_comp_nv.append(rid)

    # Wall-clock latency & USD classification
    direct_lat_rids = ["SR003", "SR004", "SR005", "SR017", "SR020", "SR025", "SR035", "SR039", "SR090"]
    proxy_lat_rids = ["SR011", "SR069", "SR075"]
    usd_exact_rids = ["SR016", "SR025", "SR032"]
    usd_ratio_rids = ["SR011", "SR018", "SR035", "SR086"]
    usd_explicit_rids = sorted(usd_exact_rids + usd_ratio_rids)
    usd_omitted_or_nv_rids = [rid for rid in sorted(em) if rid not in usd_explicit_rids]

    # Dense Debate Conformity list (excluding SR013 which no longer falsely holds conformity flag)
    dense_debate_rids = sorted(rid for rid, r in em.items() if r["architecture_and_agent_count"]["topology_class"] == "Dense All-to-All Debate")
    dense_conf_rids = sorted(
        rid for rid in dense_debate_rids
        if isinstance(r_fm := em[rid]["reported_successes_and_failures"]["failure_mechanisms_documented"], list)
        and "Conformity/Sycophancy Collapse" in r_fm
    )

    # Archival sensitivity for RQ3 & RQ4
    rq3_rids = sorted(rid for rid, r in em.items() if r["rq_mapping"]["corpus_track"] == "Mechanistic Failure & Conformity Analysis (RQ3)")
    rq4_rids = sorted(rid for rid, r in em.items() if r["rq_mapping"]["corpus_track"] == "Evaluation Validity & Harness Reliability Audit (RQ4)")
    rq3_non_arch = {rid: em[rid]["publication_status"] for rid in rq3_rids if em[rid]["publication_status"] not in ("Peer-reviewed journal", "Peer-reviewed conference")}
    rq4_non_arch = {rid: em[rid]["publication_status"] for rid in rq4_rids if em[rid]["publication_status"] not in ("Peer-reviewed journal", "Peer-reviewed conference")}

    # NV Missingness inventory
    nv_scalar = 0
    nv_leaf = 0
    nv_recs = 0
    nv_by_access = defaultdict(lambda: {"records": 0, "records_with_nv": 0, "scalar_nv": 0, "leaf_nv": 0})
    for rid, r in sorted(em.items()):
        al = r["source_provenance"]["access_level"]
        ds = count_direct_scalar_nv(r)
        lf = count_nv_recursive(r)
        nv_scalar += ds
        nv_leaf += lf
        if ds > 0 or lf > 0:
            nv_recs += 1
            nv_by_access[al]["records_with_nv"] += 1
        nv_by_access[al]["records"] += 1
        nv_by_access[al]["scalar_nv"] += ds
        nv_by_access[al]["leaf_nv"] += lf

    # Topology & Failure Pathway Counts
    topo_counts = Counter(r["architecture_and_agent_count"]["topology_class"] for r in em.values())
    fm_counts = Counter()
    for r in em.values():
        fms = r["reported_successes_and_failures"]["failure_mechanisms_documented"]
        if isinstance(fms, list):
            for m in fms:
                fm_counts[m] += 1

    # Multi-topology evaluation counts (word-boundary regexes so 'decentralized' NEVER matches 'centralized')
    multi_topo_rids = [rid for rid, r in sorted(em.items()) if r["architecture_and_agent_count"]["topology_class"] == "Multiple Topologies Compared"]
    multi_eval_seq = []
    multi_eval_star = []
    multi_eval_debate = []
    multi_eval_indep = []
    for rid in multi_topo_rids:
        txt = json.dumps(em[rid]["architecture_and_agent_count"]["system_names"]).lower()
        if re.search(r"(?<![a-z])(sequential|chain|pipeline|macnet)(?![a-z])", txt):
            multi_eval_seq.append(rid)
        if re.search(r"(?<![a-z])(centralized|star|orchestrator|macnet)(?![a-z])", txt):
            multi_eval_star.append(rid)
        if re.search(r"(?<![a-z])(debate|decentralized|mad|cmd|mesh)(?![a-z])", txt):
            multi_eval_debate.append(rid)
        if re.search(r"(?<![a-z])(independent|ensemble|voting|subtask)(?![a-z])", txt):
            multi_eval_indep.append(rid)

    # 2D Orthogonal Evidence-Gap Grid (Multi-Label Task-Structure Coverage per Study so Multi-Benchmark Suites populate all evaluated cells cleanly!)
    topo_map = {
        "Independent/Voting Ensemble": "Independent / Voting",
        "Sequential Chain/SOP": "Sequential Chain / SOP",
        "Centralized Star/Orchestrator-Worker": "Centralized Star",
        "Dense All-to-All Debate": "Dense All-to-All Debate",
        "Adaptive Sparse/Learned DAG": "Adaptive Sparse / Learned DAG",
        "Hybrid/Selective Escalation": "Hybrid / Selective Escalation",
        "Multiple Topologies Compared": "Multi-Topology Suites",
    }
    def map_tasks_multilabel(rec):
        labels = set()
        for b in rec.get("datasets_and_benchmarks", []):
            ts = b.get("task_structure_type", "")
            if "Decomposable" in ts:
                labels.add("Decomposable / Parallel")
            elif "Sequential" in ts:
                labels.add("Sequential / State-Dep.")
            elif "Context" in ts or "Multi-Turn" in ts:
                labels.add("Long-Context / Sandbox")
            else:
                labels.add("Static Single-Turn / Mixed")
        return sorted(labels) or ["Static Single-Turn / Mixed"]

    grid_all = defaultdict(Counter)
    grid_t1 = defaultdict(Counter)
    grid_row_unique = Counter()
    grid_row_t1_unique = Counter()
    for rid, r in sorted(em.items()):
        tc = r["architecture_and_agent_count"]["topology_class"]
        if tc not in topo_map:
            continue
        t_lbl = topo_map[tc]
        is_t1 = r["baselines_and_rigor_tier"]["sas_baseline_rigor_tier"].startswith("Tier 1")
        grid_row_unique[t_lbl] += 1
        if is_t1:
            grid_row_t1_unique[t_lbl] += 1
        for tk_lbl in map_tasks_multilabel(r):
            grid_all[t_lbl][tk_lbl] += 1
            if is_t1:
                grid_t1[t_lbl][tk_lbl] += 1

    # Export complete itemized 87-comparison dataset & 34-study win-share vector for Section 12C reproducibility
    flat_comparisons = []
    study_shares = []
    cmp_idx = 0
    for s in comp_studies:
        rid = s["rid"]
        tot_k = len(s["verdicts"])
        w_k = sum(1 for v in s["verdicts"] if v == "MAS > SAS")
        t_k = sum(1 for v in s["verdicts"] if v == "MAS ≈ SAS")
        l_k = sum(1 for v in s["verdicts"] if v == "MAS < SAS")
        m_k = sum(1 for v in s["verdicts"] if v == "Mixed across budgets/subtasks")
        st_lbl = "Archival" if s["archival"] else ("Workshop" if s["status"] == "Workshop" else "Preprint")
        w_lbl = "Wave 1" if s["wave1"] else "Wave 2"
        mode_lbl = "Interactive/Hybrid" if s["interactive_mas"] else "Multi-LLM Ensemble"
        t_lbl_full = f"Tier {s['tier']}" + ("B (Search)" if (s["tier"] == 2 and s["has_c6"]) else ("A (Budget)" if s["tier"] == 2 else ""))
        study_shares.append({
            "rid": rid,
            "cite": s["cite"],
            "short_cite": s["short_cite"],
            "status": st_lbl,
            "wave": w_lbl,
            "tier_label": t_lbl_full,
            "tier": s["tier"],
            "has_c6": s["has_c6"],
            "mode": mode_lbl,
            "k": tot_k,
            "wins": w_k, "ties": t_k, "losses": l_k, "mixed": m_k,
            "win_share": round(w_k / tot_k, 4),
            "gt_50": w_k / tot_k > 0.5,
            "ge_50": w_k / tot_k >= 0.5,
        })
        for tp, tf, dpp in zip(s["tuples"], s["task_fams"], s["deltas_pp"]):
            cmp_idx += 1
            flat_comparisons.append({
                "idx": cmp_idx,
                "rid": rid,
                "cite": s["cite"],
                "short_cite": s["short_cite"],
                "wave": w_lbl,
                "tier_label": t_lbl_full,
                "mode": mode_lbl,
                "task_family": tf,
                "benchmark": tp["benchmark_and_backbone"],
                "mas_cfg": tp["mas_configuration"],
                "sas_cmp": tp["sas_comparator"],
                "mas_score": tp["mas_score"],
                "sas_score": tp["sas_score"],
                "delta": tp["delta_mas_minus_sas"],
                "compute_ratio": tp["compute_ratio_mas_over_sas"],
                "verdict": tp["direction_verdict"],
            })

    stats = {
        "prisma": {
            "raw_total": sl["summary"]["total_raw_records_identified"],
            "raw_wave1": 126,
            "raw_wave2": 16,
            "duplicates": sl["summary"]["total_duplicates_merged"],
            "unique_screened": len(sr_rows),
            "stage1_excluded": sum(s1_excl.values()),
            "stage1_excl_by_code": dict(s1_excl),
            "stage2_assessed": len(s2_all_rows),
            "stage2_excluded": sum(s2_excl.values()),
            "stage2_excl_by_code": dict(s2_excl),
            "included_total": len(em),
            "wave1_included": 44,
            "wave2_included": 15,
            "pub_status": dict(pub_counts),
            "archival_count": archival_cnt,
            "archival_pct": round(100 * archival_cnt / len(em), 1),
            "peer_reviewed_count": peer_rev_cnt,
            "peer_reviewed_pct": round(100 * peer_rev_cnt / len(em), 1),
            "workshop_count": pub_counts["Workshop"],
            "workshop_pct": round(100 * pub_counts["Workshop"] / len(em), 1),
            "preprint_count": pub_counts["Preprint (arXiv / Preprints.org)"],
            "preprint_pct": round(100 * pub_counts["Preprint (arXiv / Preprints.org)"] / len(em), 1),
        },
        "irr": {
            "wave1_stage1_po": round(100 * s1_w1_po, 2),
            "wave1_stage1_kappa": round(s1_w1_k, 4),
            "full_stage1_po": round(100 * s1_all_po, 2),
            "full_stage1_kappa": round(s1_all_k, 4),
            "stage2_full_n": len(s2_all_rows),
            "stage2_3class_po": round(100 * s2_3class_po, 2),
            "stage2_3class_kappa": round(s2_3class_k, 4),
            "stage2_bin_po": round(100 * s2_bin_po, 2),
            "stage2_bin_kappa": round(s2_bin_k, 4),
            "corpus_bin_po": round(100 * corp_po, 2),
            "corpus_bin_kappa": round(corp_k, 4),
            "pooled_judg_n": len(sr_rows) + len(s2_all_rows),
            "pooled_judg_agree": s1_agree_n + s2_agree_n,
            "pooled_judg_po": round(100 * pooled_judg_po, 2),
        },
        "tracks": dict(track_counts),
        "tiers": dict(tier_counts),
        "comparative_all": all_comp_stats,
        "comparative_archival": arch_comp_stats,
        "comparative_wave1": wave1_comp_stats,
        "comparative_wave2_t23": wave2_t23_stats,
        "comparative_interactive": inter_comp_stats,
        "comparative_zero_search": zero_search_comp_stats,
        "comparative_adj_1pp": adj_comp_stats,
        "comparative_opt_nguyen": opt_comp_stats,
        "flat_comparisons": flat_comparisons,
        "study_shares": study_shares,
        "tier1_subsplits": {
            "interactive_vs_voting": summarize_sub(t1_vs_voting),
            "interactive_vs_single_or_longcot": summarize_sub(t1_vs_single),
            "mixed_moa_vs_self_moa": summarize_sub(t1_moa_boundary),
        },
        "task_family_all": {k: summarize_sub(v) for k, v in sorted(tf_all.items())},
        "task_family_tier1": {k: summarize_sub(v) for k, v in sorted(tf_t1.items())},
        "effect_size_meta": effect_size_meta,
        "within_study_contrasts": within_study_contrasts,
        "tier1_mad_vs_nonmad": {
            "mad_studies": len(t1_mad),
            "mad_cites": [s["cite"] for s in t1_mad],
            "mad_tuples": sum(len(s["verdicts"]) for s in t1_mad),
            "nonmad_studies": len(t1_nonmad),
            "nonmad_cites": [s["cite"] for s in t1_nonmad],
            "nonmad_tuples": sum(len(s["verdicts"]) for s in t1_nonmad),
        },
        "qa": {
            "bands": dict(band_counts),
            "overall_mean_pct": round(sum(pct_vals) / len(pct_vals), 1),
            "overall_median_pct": round(sorted(pct_vals)[len(pct_vals) // 2], 1),
            "overall_min_pct": round(min(pct_vals), 1),
            "overall_max_pct": round(max(pct_vals), 1),
            "overall_mean_12pt_pct": round(sum(norm12(r) for r in qa_rows) / len(qa_rows), 1),
            "by_track": track_qa,
            "by_status": status_qa,
            "criterion_means": crit_means,
        },
        "confounders": {
            "all_59": dict(c_all),
            "comparative_34": dict(c_comp),
            "comparative_total_studies": len(all_comp_track_ids),
            "qa3_1_count": len(qa3_1_ids),
            "qa3_1_comp_count": len(qa3_1_comp_ids),
            "qa3_1_diag_count": len(qa3_1_diag_ids),
            "c6_count": len(c6_ids),
            "qa3_1_matches_c6_1to1": (qa3_1_ids == c6_ids),
            "qa3_1_cites": [id_to_c[x] for x in qa3_1_ids],
            "learned_optimizers_total": len(qa3_1_ids),
            "static_zero_search_comp": len(all_comp_track_ids) - len(qa3_1_comp_ids),
        },
        "pass_power_k": {
            "comparative_true": pk_comp_true,
            "comparative_false": pk_comp_false,
            "comparative_nv": [id_to_c[x] for x in pk_comp_nv],
            "comparative_total": len(all_comp_track_ids),
            "comparative_verifiable_den": pk_comp_true + pk_comp_false,
            "overall_true": len(pk_all_true),
            "overall_true_cites": [id_to_c[x] for x in pk_all_true],
            "overall_nv": len(pk_all_nv),
            "overall_verifiable_den": len(em) - len(pk_all_nv),
        },
        "latency_and_usd": {
            "direct_latency_count": len(direct_lat_rids),
            "direct_latency_pct": round(100 * len(direct_lat_rids) / len(em), 1),
            "direct_latency_cites": sorted(id_to_c[x] for x in direct_lat_rids),
            "proxy_latency_count": len(proxy_lat_rids),
            "proxy_latency_cites": sorted(id_to_c[x] for x in proxy_lat_rids),
            "omit_or_nv_latency_count": len(em) - len(direct_lat_rids) - len(proxy_lat_rids),
            "omit_or_nv_latency_pct": round(100 * (len(em) - len(direct_lat_rids) - len(proxy_lat_rids)) / len(em), 1),
            "usd_exact_count": len(usd_exact_rids),
            "usd_exact_cites": sorted(id_to_c[x] for x in usd_exact_rids),
            "usd_ratio_count": len(usd_ratio_rids),
            "usd_ratio_cites": sorted(id_to_c[x] for x in usd_ratio_rids),
            "usd_verified_count": len(usd_explicit_rids),
            "usd_verified_pct": round(100 * len(usd_explicit_rids) / len(em), 1),
            "usd_verified_cites": sorted(id_to_c[x] for x in usd_explicit_rids),
            "usd_omit_or_nv_count": len(usd_omitted_or_nv_rids),
            "usd_omit_or_nv_pct": round(100 * len(usd_omitted_or_nv_rids) / len(em), 1),
        },
        "dense_debate_conformity": {
            "dense_debate_total": len(dense_debate_rids),
            "conformity_count": len(dense_conf_rids),
            "conformity_pct": round(100 * len(dense_conf_rids) / len(dense_debate_rids), 1),
            "conformity_cites": sorted(id_to_c[x] for x in dense_conf_rids),
            "non_conformity_rids": [x for x in dense_debate_rids if x not in dense_conf_rids],
            "non_conformity_cites": [id_to_c[x] for x in dense_debate_rids if x not in dense_conf_rids],
        },
        "rq3_rq4_archival_sensitivity": {
            "rq3_total": len(rq3_rids),
            "rq3_archival": len(rq3_rids) - len(rq3_non_arch),
            "rq3_non_archival": {id_to_c[k]: v for k, v in rq3_non_arch.items()},
            "rq4_total": len(rq4_rids),
            "rq4_archival": len(rq4_rids) - len(rq4_non_arch),
            "rq4_non_archival": {id_to_c[k]: v for k, v in rq4_non_arch.items()},
        },
        "nv_inventory": {
            "scalar_nv_fields": nv_scalar,
            "leaf_nv_strings": nv_leaf,
            "records_with_nv": nv_recs,
            "total_records": len(em),
            "by_access_level": dict(nv_by_access),
        },
        "topology_counts": dict(topo_counts),
        "multi_topology_subeval": {
            "seq": len(multi_eval_seq), "seq_rids": multi_eval_seq,
            "star": len(multi_eval_star), "star_rids": multi_eval_star,
            "debate": len(multi_eval_debate), "debate_rids": multi_eval_debate,
            "indep": len(multi_eval_indep), "indep_rids": multi_eval_indep,
        },
        "failure_mechanism_counts": dict(fm_counts),
        "evidence_gap_grid_all": {k: dict(v) for k, v in grid_all.items()},
        "evidence_gap_grid_tier1": {k: dict(v) for k, v in grid_t1.items()},
        "evidence_gap_row_unique": dict(grid_row_unique),
        "evidence_gap_row_t1_unique": dict(grid_row_t1_unique),
    }

    with open(DATA / "verified_stats.json", "w") as f:
        json.dump(stats, f, indent=2)
    print("Wrote verified_stats.json cleanly!")
    return stats, em, qa_rows, sr_rows


def render_tables(stats, cite_map, em, qa_rows):
    id_to_c = cite_map["by_study_id"]
    key_to_c = cite_map["by_key"]
    c_all = stats["comparative_all"]
    c_arch = stats["comparative_archival"]
    c_w1 = stats["comparative_wave1"]
    c_w2 = stats["comparative_wave2_t23"]
    c_int = stats["comparative_interactive"]
    c_zs = stats["comparative_zero_search"]
    c_adj = stats["comparative_adj_1pp"]
    c_opt = stats["comparative_opt_nguyen"]
    qa = stats["qa"]
    pr = stats["prisma"]
    irr = stats["irr"]
    topo_counts = stats["topology_counts"]
    mt = stats["multi_topology_subeval"]

    def ck(k):
        return f"[{key_to_c[k]}]"

    def rids_to_cites(rids):
        return ", ".join(f"[{id_to_c[r]}]" for r in rids)

    out = []

    t1 = f"""| Prior Survey / Group | Venue & Year | Main Topic Covered | Overlap and Complementarity With This Review |
| :--- | :--- | :--- | :--- |
| Li et al. {ck('SR047_li2026efficiency')} | Preprints.org (2026) | Conceptual efficiency taxonomy ("Collaboration Boundary"), matched baselines, and lifecycle cost amortization | Conceptual foundation: Li et al. formulate matched-baseline and lifecycle principles qualitatively. This review tests those principles across {c_all['All']['n_tuples']} cleaned comparisons, measuring a {c_all['tuple_attenuation_pp']} pp drop under equal compute and {stats['confounders']['qa3_1_comp_count']}/{stats['confounders']['qa3_1_comp_count']} unamortized comparative optimizers. |
| Motger et al. {ck('SR041_motger2026mad')} | arXiv (2026) | Systematic review of 141 multi-agent debate (MAD) papers; compares debate against majority voting | Overlaps on debate ({stats['tier1_mad_vs_nonmad']['mad_studies']}/{c_all['Tier 1']['n_studies']} of our equal-compute Tier 1 studies test debate). We extend beyond debate to sequential pipelines, orchestrator-workers, learned graphs, selective escalation, and benchmark harness validity. |
| Yue et al. {ck('SR045_yue2026static')} | Findings of EMNLP 2026 | Static vs. dynamic agent workflow graphs (AFlow, GPTSwarm, G-Designer) and graph efficiency | Surveys graph optimization without stratifying by equal-budget single-agent parity or pricing upfront MCTS/RL/VGAE search costs (0 learned-graph studies meet Tier 1 parity). |
| Wang et al. {ck('SR043_wang2026trajectory')} | IEEE TSE 52(11) (2026) | Survey of trajectory failure attribution across 55 LLM multi-agent reliability papers | Maps execution trace datasets (overlapping 7 of our diagnostic studies); we connect these failure pathways to multi-agent vs. single-agent accuracy drops and security multiplication. |
| Mallampati & Nagoriya {ck('Mallampati2026_Reliability')} | Preprint (2026) | 62 papers on coordination reliability, stopping rules, and deadlock recovery | Complements our stopping and blocking analysis without equal-budget win-rate stratification or benchmark harness audits. |
| Dantas et al. {ck('Dantas2026_SafeAgents')} | Preprint (2026) | 38-study PRISMA review of formal safety specification and verification tax in AI agents | Focuses on formal safety verification rather than equal-compute accuracy comparisons or multi-agent vs. single-agent trade-offs. |
| Kim et al. {ck('Kim2026_USENIX_Security')} & Deng et al. {ck('Deng2025_CSUR_Security')} | USENIX Security '26 & ACM CSUR 57(7) (2025) | Threat landscapes covering prompt hijacking, memory poisoning, and agentic defense | Comprehensive security overviews; complement our topological security analysis across NetSafe, CORBA, G-Safeguard, and Hagag et al. |
| Wei et al. {ck('Wei2026_TMLR_AgenticReasoning')}, Huang et al. {ck('Huang2026_TMLR_AgentMemory')}, Moslem & Kelleher {ck('SR048_moslem2026dynamic')} | TMLR (2025–2026) | Agentic reasoning, long-horizon agent memory, and single-query dynamic model routing | Broad reasoning, memory, and single-query routing reviews {ck('SR055_gao2026selfevolving')}, {ck('SR056_zhang2026generalist')}, {ck('Ke2025_TMLR_LLMReasoning')}, {ck('Zhang2026_TMLR_AgenticRL')}; none audits equal-compute multi-agent vs. single-agent outcomes. |
| Yehudai et al. {ck('SR044_yehudai2026evaluation')} & Mohammadi et al. {ck('Mohammadi2025_KDD')} | Findings of ACL '26 & KDD '25 | General agent evaluation metrics, pass-power-k reliability, and judge bias | Survey agentic evaluation broadly without measuring how baseline compute mismatches inflate published multi-agent gains. |
| ACM CSUR & Broad Reviews {ck('SR052_du2026optimization')}, {ck('SR050_geng2026scaling')}, {ck('SR051_he2026security')}, {ck('Hu2024_CSUR_GameAgents')}, {ck('Zhang2026_CSUR_Generalizability')} | ACM CSUR, AIRE, JAIR, IJCAI, Preprints (2024–2026) | Agent optimization, classical reinforcement learning teams, game agents, and classical-to-LLM boundaries {ck('AbouAli2026_AIRE')}, {ck('SR049_alaanzy2026autonomous')}, {ck('Chowa2026_AIRE')}, {ck('Guo2024_IJCAI')}, {ck('Plaat2025_JAIR')}, {ck('Tran2025_MAS')}, {ck('Zhu2026_FutureInternet')}, {ck('Khan2026_Preprints_MASEvolution')}, {ck('LaMalfa2025')}, {ck('Wang2026_arXiv_ClassicalToFoundationMAS')}, {ck('Badica2025_arXiv_ContemporaryAgentTech')}, {ck('Rahman2025_arXiv_LLMPoweredSwarms')}, {ck('SR042_tillmann2025mad')}, {ck('SR046_yan2026beyond')}, {ck('SR053_wang2024autonomous')} | Establish architectures and classical MARL/swarm distinctions; leave open an empirical compute-normalized audit of when multi-agent teams help vs. hurt. |"""
    out.append("### TABLE_1_SURVEY_COMPARISON\n" + t1)

    pub_tbl = f"""| Grouping Axis | Category | Studies (n) | Share (%) | Role in This Review |
| :--- | :--- | :---: | :---: | :--- |
| Publication Status | Peer-reviewed journal or conference | {pr['archival_count']} ({pr['pub_status']['Peer-reviewed journal']} J + {pr['pub_status']['Peer-reviewed conference']} C) | {pr['archival_pct']}% | Core archival anchor tested separately in Archival-Only sensitivity checks. |
| Publication Status | Peer-reviewed workshop | {pr['workshop_count']} | {pr['workshop_pct']}% | Includes ColMAD {ck('SR012_chen2026when')} (ICML Wkshp), WebArena Verified {ck('SR039_elhattami2025webarena')}, Verifier Transport {ck('SR040_sheshanarayana2026do')}, and CMAD {ck('SR079_dai2026when')}; excluded in Archival-Only sensitivity checks. |
| Publication Status | Open preprint (arXiv / Preprints.org) | {pr['preprint_count']} | {pr['preprint_pct']}% | Admitted only after clearing >=6/14 (or /12) quality and claims-parity checks; isolated in Archival-Only checks. |
| Research Track | Comparative Effectiveness & Topology | {stats['tracks']['Primary Comparative Effectiveness & Topology (RQ1/RQ2)']} | {100*stats['tracks']['Primary Comparative Effectiveness & Topology (RQ1/RQ2)']/pr['included_total']:.1f}% | 33 primary comparative studies (+1 comparative sycophancy study in Mechanistic Failure track = {c_all['All']['n_studies']} total comparative studies across {c_all['All']['n_tuples']} comparisons). |
| Research Track | Mechanistic Failure & Security | {stats['tracks']['Mechanistic Failure & Conformity Analysis (RQ3)']} | {100*stats['tracks']['Mechanistic Failure & Conformity Analysis (RQ3)']/pr['included_total']:.1f}% | Error localization (MAST, Who&When, TraceElephant, TRIAGE), conformity, embodied observation, and multi-agent attack studies (incl. 1 comparative mitigation study). |
| Research Track | Evaluation Validity & Harness Audits | {stats['tracks']['Evaluation Validity & Harness Reliability Audit (RQ4)']} | {100*stats['tracks']['Evaluation Validity & Harness Reliability Audit (RQ4)']/pr['included_total']:.1f}% | Cost-accuracy audits, multi-run consistency (pass^k), Agent Forest solo-voting C3 boundary case, SWE/WebArena harness exploits, and OpenReview rejection cases. |"""
    out.append("### TABLE_PUB_STATUS\n" + pub_tbl)

    def fmt_row(lbl, grp_d):
        return (
            f"| {lbl} | {grp_d['n_studies']} | {grp_d['n_tuples']} | "
            f"{grp_d['wins']}/{grp_d['n_tuples']} ({grp_d['win_pct']}%) "
            f"[Boot {grp_d['win_boot_ci95'][0]}–{grp_d['win_boot_ci95'][1]}%; Wilson {grp_d['win_wilson_ci95'][0]}–{grp_d['win_wilson_ci95'][1]}%] | "
            f"{grp_d['ties']} ({grp_d['tie_pct']}%) | "
            f"{grp_d['losses']} ({grp_d['loss_pct']}%) | "
            f"{grp_d['mixed']} ({grp_d['mixed_pct']}%) | "
            f"{grp_d['study_frac_win_pct']}% [{grp_d['study_frac_boot_ci95'][0]}–{grp_d['study_frac_boot_ci95'][1]}%] | "
            f"{grp_d['study_maj_wins']}/{grp_d['n_studies']} ({grp_d['study_maj_win_pct']}%) | "
            f"{grp_d['study_maj_ge50_wins']}/{grp_d['n_studies']} ({grp_d['study_maj_ge50_win_pct']}%) |"
        )

    t4 = (
        "| Baseline Quality Tier / Sensitivity Slice | Studies (n) | Comparisons (k) | MAS Wins [95% Boot CI; 95% Wilson CI] | Ties (%) | MAS Losses (%) | Mixed (%) | Study-Weighted Win % [Boot CI] | Study Maj (>50%) | Study >=50% |\n"
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n"
        + fmt_row("Tier 1: Equal-Compute Strong Single Agent", c_all["Tier 1"]) + "\n"
        + fmt_row("Tier 2A: Strong Solo, Unmatched Inference Budget (Zero Search)", c_all["Tier 2A"]) + "\n"
        + fmt_row("Tier 2B: Strong Solo, Unamortized Training/Search (C6)", c_all["Tier 2B"]) + "\n"
        + fmt_row("Tier 2 (All): Strong Solo, Unmatched Cost or Search", c_all["Tier 2"]) + "\n"
        + fmt_row("Tier 3: Weak Single-Pass Single Agent Only", c_all["Tier 3"]) + "\n"
        + fmt_row("Tier 2+3 Combined: All Non-Parity Controls", c_all["Tier 2+3"]) + "\n"
        + f"| Parity Gap (Tier 2+3 to Tier 1, Full Corpus) | {c_all['All']['n_studies']} total | {c_all['All']['n_tuples']} | {c_all['tuple_attenuation_pp']} pp [Boot {c_all['tuple_attenuation_ci95'][0]} to {c_all['tuple_attenuation_ci95'][1]} pp] | — | +{round(c_all['Tier 1']['loss_pct']-c_all['Tier 2+3']['loss_pct'],1)} pp | — | {c_all['study_frac_attenuation_pp']} pp (perm p={c_all['perm_p_study_frac_t1_vs_t23']}) | {c_all['study_maj_attenuation_pp']} pp (Fisher p={c_all['fisher_p_t1_vs_t23']}) | Fisher p={c_all['fisher_p_t1_vs_t23_ge50']} |\n"
        + fmt_row("Sensitivity A: Archival-Only Tier 1 (No Preprints/Wkshps)", c_arch["Tier 1"]) + "\n"
        + fmt_row("Sensitivity A: Archival-Only Tier 2+3 (Fisher p=" + str(c_arch["fisher_p_t1_vs_t23"]) + ")", c_arch["Tier 2+3"]) + "\n"
        + fmt_row("Sensitivity B: Wave 1 Baseline Tier 2+3 (S01-S11, Fisher p=" + str(c_w1["fisher_p_t1_vs_t23"]) + ")", c_w1["Tier 2+3"]) + "\n"
        + fmt_row("Sensitivity B: Wave 2 Gap Imports Tier 2+3 Only (S12-S13)", c_w2["Tier 2+3"]) + "\n"
        + fmt_row("Sensitivity C: Interactive Teams Only Tier 1 (Excl. Ensembles)", c_int["Tier 1"]) + "\n"
        + fmt_row("Sensitivity C: Interactive Teams Only Tier 2+3 (Fisher p=" + str(c_int["fisher_p_t1_vs_t23"]) + ")", c_int["Tier 2+3"]) + "\n"
        + fmt_row("Sensitivity D: Practical ±1.0 pp Tie Margin Tier 1", c_adj["Tier 1"]) + "\n"
        + fmt_row("Sensitivity D: Practical ±1.0 pp Tie Margin Tier 2+3", c_adj["Tier 2+3"]) + "\n"
        + fmt_row("Sensitivity E: Zero-Search Static Only Tier 2A+3 (No C6)", c_zs["Tier 2+3"]) + "\n"
        + fmt_row("Sensitivity F: Optimistic Tier 1 (Nguyen Table 17 as Win)", c_opt["Tier 1"])
    )
    out.append("### TABLE_4_QUANTITATIVE_SYNTHESIS\n" + t4)

    t1_rows = []
    for rid in sorted(em):
        r = em[rid]
        if not r["baselines_and_rigor_tier"]["sas_baseline_rigor_tier"].startswith("Tier 1"):
            continue
        c_num = id_to_c[rid]
        short_au = cite_map["by_num"][str(c_num)]["short_cite"]
        ps = "Archival" if r["publication_status"] in ("Peer-reviewed journal", "Peer-reviewed conference") else ("Workshop" if r["publication_status"] == "Workshop" else "Preprint")
        for tp in r["reported_numerical_outcomes"]["paired_comparisons"]:
            bench = tp["benchmark_and_backbone"]
            mas_cfg = tp["mas_configuration"]
            sas_cmp = tp["sas_comparator"]
            delta = tp["delta_mas_minus_sas"]
            comp_r = str(tp["compute_ratio_mas_over_sas"])
            verd = tp["direction_verdict"]
            t1_rows.append(
                f"| {short_au} [{c_num}] | {ps} | {bench} | {mas_cfg} vs. {sas_cmp} | {delta} | {comp_r} | **{verd}** |"
            )
    t5 = (
        "| Study | Status | Benchmark & Model Family | Comparison Pair | Accuracy Difference (MAS minus SAS) | Compute Ratio | Verdict |\n"
        "| :--- | :---: | :--- | :--- | :--- | :--- | :---: |\n" + "\n".join(t1_rows)
    )
    out.append("### TABLE_5_TIER1_CORPUS\n" + t5)

    wsc_lines = [
        "| Study | Benchmarks Held Constant | Result vs. Weak or Unmatched Baseline | Result vs. Strong or Equal-Compute Baseline (Same Authors/Tasks) |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for row in stats["within_study_contrasts"]:
        wsc_lines.append(f"| {row['study']} | {row['benchmarks']} | {row['weak_or_unmatched']} | {row['strong_or_matched']} |")
    out.append("### TABLE_WITHIN_STUDY_CONTRASTS\n" + "\n".join(wsc_lines))

    es = stats["effect_size_meta"]
    cv = es["cais26_variance_audit"]
    es_lines = [
        "Panel A — Unweighted Study-Level Descriptive Accuracy Differences (Percentage Points: MAS minus Solo Agent; Strictly Single Aggregation Level)",
        "",
        "| Control Regime (Numeric 0–100% Scale Pairs Only) | Studies (n) | Comparisons (k) | Unweighted Study Mean (pp) | Study Median [IQR] (pp) | Full Study Range [Min to Max] (pp) |",
        "| :--- | :---: | :---: | :---: | :---: | :---: |",
    ]
    for lbl, key in [
        ("Tier 1 Equal-Compute Numeric Subset ([78], [53])", "tier1_equal_numeric"),
        ("Strong Voting or Self-Correction Controls — All 3 CAIS '26 Models ([78], [53], [16], [14], [6])", "strong_controls_all_models"),
        ("Strong Controls — Main Large-N Model Only for CAIS '26 (Qwen2.5-7B, n=1,017, -2.2 pp)", "strong_controls_main_qwen"),
        ("Weak Single-Pass Solo Controls (Untrained MAS vs. 1x Solo)", "weak_single_pass"),
        ("Post-Trained (RL/DPO) or Selective Escalation Systems", "posttrained_or_selective_escalation"),
    ]:
        d = es[key]
        es_lines.append(
            f"| {lbl} | {d['n_studies']} | {d['n_tuples']} | {d['study_mean_pp']:+.2f} | {d['study_median_pp']:+.2f} [{d['study_iqr_pp'][0]:+.2f} to {d['study_iqr_pp'][1]:+.2f}] | {d['study_range_pp'][0]:+.2f} to {d['study_range_pp'][1]:+.2f} |"
        )
    es_lines.extend([
        "",
        "Panel B — Binomial Variance & Inverse-Variance Reweighting Across Bertalanič & Fortuna (CAIS '26) [6] GSM-Hard Splits (Why One Small-N Model Split Inflates Unweighted Averages)",
        "",
        "| Model Split in CAIS '26 [6] | Test Items (N) | Debate vs. Isolated Self (%) | Gap (pp) | Binomial SE (pp) | Variance | Inverse-Variance Weight (%) |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: |",
    ])
    for sp in cv["splits"]:
        es_lines.append(
            f"| {sp['model']} | {sp['n_items']} | {sp['mas']}% vs. {sp['sas']}% | {sp['delta_pp']:+.1f} | {sp['se_pp']:.2f} | {sp['var_pp']:.2f} | {sp['iv_weight_pct']:.1f}% |"
        )
    es_lines.append(
        f"| Summary Across All 3 CAIS '26 Models | 1,217 total | Unweighted study mean = {cv['unweighted_mean_pp']:+.2f} pp | Item-weighted = {cv['item_weighted_mean_pp']:+.2f} pp | IV-weighted = {cv['iv_weighted_mean_pp']:+.2f} pp | — | Exact DerSimonian-Laird cross-study pooling omitted because 4/5 studies lack complete per-item SEs |"
    )
    out.append("### TABLE_EFFECT_SIZE_META\n" + "\n".join(es_lines))

    tf_lines = [
        "| Task Family | Studies Testing Family (n) | Comparisons (k) | All-Corpus Wins / k (%) [Wilson 95% CI] | Tier 1 Wins / k (%) [Wilson 95% CI] | Pattern Summary |",
        "| :--- | :---: | :---: | :---: | :---: | :--- |",
    ]
    tf_notes = {
        "Decomposable / Multi-Source & Info-Split": "Partitioned information & splittable sub-tasks; Tier 1 wins (2/2) come solely from Kim et al. [46] (Finance-Agent, BrowseComp-Plus).",
        "General QA, Truthfulness & Instruction Following": "Most Tier 1 debate/polling studies tie or lose once sampling/prompt quality is matched.",
        "Math & Symbolic Logic": "Majority voting (Self-Consistency) matches or beats iterative debate at equal token budgets.",
        "Sequential Planning, Embodied & Tool/SWE": "Tightly coupled step dependencies incur up to -39% to -70% degradation (PlanCraft) and coordination deadlocks.",
    }
    for tf_name, d_all in stats["task_family_all"].items():
        d_t1 = stats["task_family_tier1"].get(tf_name, {"wins": 0, "n_tuples": 0, "n_studies": 0})
        lo_a, hi_a = wilson_ci(d_all["wins"], d_all["n_tuples"])
        all_str = f"{d_all['wins']}/{d_all['n_tuples']} ({d_all['win_pct']}%) [{100*lo_a:.1f}–{100*hi_a:.1f}%]"
        if d_t1["n_tuples"]:
            lo_t, hi_t = wilson_ci(d_t1["wins"], d_t1["n_tuples"])
            t1_str = f"{d_t1['wins']}/{d_t1['n_tuples']} ({100*d_t1['wins']/d_t1['n_tuples']:.1f}%) [{100*lo_t:.1f}–{100*hi_t:.1f}%]"
        else:
            t1_str = "0/0 (—)"
        tf_lines.append(
            f"| {tf_name} | {d_all['n_studies']} | {d_all['n_tuples']} | {all_str} | {t1_str} | {tf_notes.get(tf_name, '')} |"
        )
    out.append("### TABLE_TASK_FAMILY\n" + "\n".join(tf_lines))

    def cites_for_topo(tc):
        return ", ".join(f"[{id_to_c[rid]}]" for rid in sorted(em) if em[rid]["architecture_and_agent_count"]["topology_class"] == tc)

    diag_count_t6 = topo_counts.get("Diagnostic/Benchmark Audit (N/A)", 0)
    topo_sum_t6 = sum(topo_counts.get(k, 0) for k in [
        "Independent/Voting Ensemble", "Sequential Chain/SOP", "Centralized Star/Orchestrator-Worker",
        "Dense All-to-All Debate", "Adaptive Sparse/Learned DAG", "Hybrid/Selective Escalation", "Multiple Topologies Compared"
    ])
    t6_groups = [
        ("Non-Interactive Multi-LLM Ensemble", topo_counts.get("Independent/Voting Ensemble", 0), mt["indep"], cites_for_topo("Independent/Voting Ensemble"),
         "Parallel independent candidates aggregated by majority vote or final synthesizer across models (single-LLM voting treated as solo baseline per Sec. 3.4).",
         "Single-best repetition (Self-MoA) beat mixed-model ensembles by +6.6 pp (+10.0% rel.) on AlpacaEval 2.0 under equal sampling."),
        ("Sequential Pipeline / SOP", topo_counts.get("Sequential Chain/SOP", 0), mt["seq"], f"Tested inside Multi-Topo Suites: {rids_to_cites(mt['seq_rids'])}",
         "Fixed ordered steps passing text summaries downstream without revisiting raw context.",
         "Findings derive from multi-topology suites: step-by-step handoffs lose information in closed-book reasoning and multiply latency."),
        ("Centralized Orchestrator-Worker", topo_counts.get("Centralized Star/Orchestrator-Worker", 0), mt["star"], f"Tested inside Multi-Topo Suites: {rids_to_cites(mt['star_rids'])}",
         "One central coordinator assigns sub-tasks to isolated workers and checks final output.",
         "Findings derive from multi-topology suites: wins on splittable multi-source tasks (+80.8% rel. on Finance-Agent, +285% overhead) while capping error growth at 4.4x vs. 17.2x."),
        ("Dense All-to-All Debate", topo_counts.get("Dense All-to-All Debate", 0), mt["debate"], cites_for_topo("Dense All-to-All Debate"),
         "Every agent reads peers' answers across multiple critique rounds on shared prompts.",
         f"{stats['dense_debate_conformity']['conformity_count']}/{stats['dense_debate_conformity']['dense_debate_total']} ({stats['dense_debate_conformity']['conformity_pct']}%) document peer conformity collapse (up to 85.5% modal adoption); loses to Self-Consistency and isolated self-correction at strong controls."),
        ("Adaptive / Learned Sparse Graph", topo_counts.get("Adaptive Sparse/Learned DAG", 0), 0, cites_for_topo("Adaptive Sparse/Learned DAG"),
         "Pruning, MCTS, RL, or evolutionary search shapes agent workflows automatically.",
         "0/10 learned-graph comparative studies pass Tier 1 parity because headline test-time tables omit hours of upfront search or RL training."),
        ("Selective Escalation & Multi-Topology Suites", topo_counts.get("Hybrid/Selective Escalation", 0) + topo_counts.get("Multiple Topologies Compared", 0), 0,
         f"Hybrid: {cites_for_topo('Hybrid/Selective Escalation')}; Multi-Topo: {cites_for_topo('Multiple Topologies Compared')}",
         "Try a fast single agent first, calling a team only on uncertain items; plus factorial sweeps across topologies.",
         "Selective escalation cuts deployment cost ~20% vs. always-on MAS while avoiding needless sequential penalties."),
        ("Non-Topological Diagnostic & Validity Studies", diag_count_t6, 0, f"{diag_count_t6} trace, conformity, embodied, security, & C3 boundary studies (incl. [51])",
         "Trace localization, sycophancy probes, embodied partner checks, benchmark audits, and solo-voting boundary checks.",
         f"No comparative MAS-vs-SAS arm; unique primary study assignments = {topo_sum_t6} + {diag_count_t6} = {topo_sum_t6 + diag_count_t6}."),
    ]
    t6_lines = [
        "| Coordination Structure | Single-Topology Studies (n) | Evaluated in Multi-Topo Suites | Citations | How It Works | Key Parity Finding |",
        "| :--- | :---: | :---: | :--- | :--- | :--- |",
    ]
    for label, cnt, also_n, rep, mech, finding in t6_groups:
        also_s = f"+{also_n} suites" if also_n else "—"
        t6_lines.append(f"| {label} | {cnt} | {also_s} | {rep} | {mech} | {finding} |")
    out.append("### TABLE_6_TOPOLOGY_SUMMARY\n" + "\n".join(t6_lines))

    def fm_cites(fm_name):
        return ", ".join(
            f"[{id_to_c[rid]}]" for rid in sorted(em)
            if isinstance(em[rid]["reported_successes_and_failures"]["failure_mechanisms_documented"], list)
            and fm_name in em[rid]["reported_successes_and_failures"]["failure_mechanisms_documented"]
        )

    fm_rows = [
        ("Error Amplification & Cascading Mistakes", "Error Amplification", "Multiplies initial mistakes 4.4x (Centralized) to 5.1x (Hybrid), 7.8x (Decentralized), and 17.2x (Independent) without central checks."),
        ("Conformity, Sycophancy & Debate Hacking", "Conformity/Sycophancy Collapse", f"Agents cave to a loud majority ({stats['dense_debate_conformity']['conformity_count']}/{stats['dense_debate_conformity']['dense_debate_total']} [{stats['dense_debate_conformity']['conformity_pct']}%] Debate studies, up to 85.5% modal adoption); competitive debate cheap-talk drops -15% to -19% below single agents before collaborative ColMAD recovers up to +10 pp."),
        ("Information Loss Across Text Summaries", "Handoff Information Loss (DPI)", "Passing compressed summaries along sequential closed-book chains discards subtle details (0.379 vs 0.418 at 1k tokens); peer reading also steals context window room in 93% of 980 settings."),
        ("Role Confusion & Fault Attribution Gaps", "Specification/Role Failure", "Persona prompts offer little real specialization; human single-step bug labels show 59.3% LLM-council disagreement in TRIAGE [86] and 14.2% step-level accuracy ceiling (53.5% agent-level) in Who&When [116], alongside 41%–86.7% trace failure in MAST [9]."),
        ("Verification & Stopping Breakdowns", "Termination/Verification Failure", "Verifier summary abstraction drops 30.9% of initially correct answers (85.5% recoverable via full trace links); weak stopping rules cause 18%–47% calibration miscoverage."),
        ("Inter-Agent Attack Spread", "Prompt-Injection/Collusion Vulnerability", "Multi-agent tool wiring shows up to 3.8x higher attack success than single agents (Hagag et al.); CORBA recursive blocking disables ~92%–100% of broadcast agents in 1.6–1.9 turns unless pruned."),
    ]
    t7_lines = [
        "| Failure Pathway | Studies (n / 59) | Citations | Observed Quantitative Evidence & Remedies |",
        "| :--- | :---: | :--- | :--- |",
    ]
    for pname, raw_fm, sig in fm_rows:
        t7_lines.append(f"| {pname} | {stats['failure_mechanism_counts'].get(raw_fm, 0)} | {fm_cites(raw_fm)} | {sig} |")
    out.append("### TABLE_7_FAILURE_SUMMARY\n" + "\n".join(t7_lines))

    cf = stats["confounders"]
    n_c34 = cf["comparative_total_studies"]
    cf_rows = [
        ("Unequal Compute / Token Budgets (C1)", cf["all_59"].get("C1", 0), cf["comparative_34"].get("C1", 0), "Multi-agent pipelines spend 2x to 25x more tokens or API calls without equal-token Self-Consistency or Best-of-N single-agent controls."),
        ("Hidden Reasoning Token Leaks (C2)", cf["all_59"].get("C2", 0), cf["comparative_34"].get("C2", 0), "Hidden thinking tokens inside reasoning APIs distort nominal token matching unless internal reasoning tokens are explicitly metered."),
        ("Voting Labeled as Deliberation (C3)", cf["all_59"].get("C3", 0), cf["comparative_34"].get("C3", 0), "Parallel independent candidate voting/polling attributed to interactive multi-agent communication or persuasion (incl. [51])."),
        ("Prompt or Tool Asymmetry (C4)", cf["all_59"].get("C4", 0), cf["comparative_34"].get("C4", 0), "Extra system hints, code execution loops, or human/tool feedback given to teams while withheld from the single-agent baseline."),
        ("Fragile / Leaky Test Harnesses (C5)", cf["all_59"].get("C5", 0), cf["comparative_34"].get("C5", 0), "Weak unit tests (PatchDiff 6.2–6.4 pp inflation) or buggy substring checks (WebArena 11.3 pp false negatives) dwarf typical MAS deltas."),
        ("Omitted Upfront Search/Training Costs (C6)", cf["all_59"].get("C6", 0), cf["comparative_34"].get("C6", 0), f"All {cf['qa3_1_comp_count']}/{cf['qa3_1_comp_count']} comparative systems using upfront graph search, prompt search, or RL/DPO training (0% amortized; vs. {cf['static_zero_search_comp']}/{n_c34} static zero-search comparative papers) omit training GPU/token costs from headline efficiency tables."),
        ("Clean of Flagged Confounders (None Observed)", cf["all_59"].get("None Observed", 0), cf["comparative_34"].get("None Observed", 0), "Controlled multi-topology/debate parity studies and clean diagnostic/benchmark audits."),
    ]
    t8 = (
        f"Panel A — Quality Scores (QA1–QA7 Raw Scale vs. 12-Pt Scale Across QA2–QA7; N = {pr['included_total']})\n\n"
        "| Subgroup | Studies (n) | Raw Mean (%) | 12-Pt Normalized Mean (%) | Key Score Drivers (0–2 Scale) |\n"
        "| :--- | :---: | :---: | :---: | :--- |\n"
        f"| Full Corpus | {pr['included_total']} | {qa['overall_mean_pct']}% (Med {qa['overall_median_pct']}%) | {qa['overall_mean_12pt_pct']}% | Single-agent rigor = {qa['criterion_means']['qa1_sas_rigor']} (n={qa['criterion_means']['qa1_n']}); Cost/latency = {qa['criterion_means']['qa2_cost_latency']}; Amortization = {qa['criterion_means']['qa3_amortization']}; Stats = {qa['criterion_means']['qa4_multirun_stats']}; Reproducibility = {qa['criterion_means']['qa6_reproducibility']} |\n"
        f"| Comparative Track (RQ1/RQ2) | {qa['by_track']['RQ1/RQ2']['n']} | {qa['by_track']['RQ1/RQ2']['mean_pct']}% | {qa['by_track']['RQ1/RQ2']['mean_12pt_pct']}% | Pulled down by single-run tables, omitted latency, and unamortized search costs. |\n"
        f"| Mechanistic & Security Track (RQ3) | {qa['by_track']['RQ3']['n']} | {qa['by_track']['RQ3']['mean_pct']}% | {qa['by_track']['RQ3']['mean_12pt_pct']}% | 15/16 studies use the 12-pt diagnostic scale; CONSENSAGENT carries QA1=1 on 14-pt scale, explaining the minor raw-vs-12pt difference. |\n"
        f"| Evaluation Validity Track (RQ4) | {qa['by_track']['RQ4']['n']} | {qa['by_track']['RQ4']['mean_pct']}% | {qa['by_track']['RQ4']['mean_12pt_pct']}% | All 10/10 use 12-pt diagnostic scale (0.0 pp difference); includes [51] as C3 boundary audit alongside harness studies. |\n"
        f"| Archival vs. Preprints | {qa['by_status']['Archival']['n']} vs. {qa['by_status']['Preprint']['n']} | {qa['by_status']['Archival']['mean_pct']}% vs. {qa['by_status']['Preprint']['mean_pct']}% | {qa['by_status']['Archival']['mean_12pt_pct']}% vs. {qa['by_status']['Preprint']['mean_12pt_pct']}% | Preprints passed a strict >=6/14 (12) quality screen before admission (QA7 = {qa['by_status']['Preprint']['qa7_mean']} vs. {qa['by_status']['Archival']['qa7_mean']}). |\n\n"
        f"Panel B — Confounder Prevalence & Missing Reporting (N = {pr['included_total']}; Comparative Studies = {cf['comparative_total_studies']})\n\n"
        f"| Methodological Confounder or Reporting Gap | All 59 Studies (%) | Comparative {cf['comparative_total_studies']} Studies (%) | Practical Effect on Claims |\n"
        "| :--- | :---: | :---: | :--- |\n"
        + "\n".join(
            f"| {nm} | {cnt59}/{pr['included_total']} ({100*cnt59/pr['included_total']:.1f}%) | {cntc}/{n_c34} ({100*cntc/n_c34:.1f}%) | {desc} |"
            for nm, cnt59, cntc, desc in cf_rows
        )
        + f"\n| Missing Multi-Trial Consistency (pass^k) | {len(em) - stats['pass_power_k']['overall_true']}/{len(em)} ({100*(len(em)-stats['pass_power_k']['overall_true'])/len(em):.1f}%) | {stats['pass_power_k']['comparative_false']}/{stats['pass_power_k']['comparative_verifiable_den']} (100.0%) | Only {stats['pass_power_k']['overall_true']}/{stats['pass_power_k']['overall_verifiable_den']} studies overall ({', '.join(f'[{x}]' for x in stats['pass_power_k']['overall_true_cites'])}) measure whether systems pass consistently across k runs. |"
        + f"\n| Missing Direct Wall-Clock Latency | {stats['latency_and_usd']['omit_or_nv_latency_count']}/{pr['included_total']} ({stats['latency_and_usd']['omit_or_nv_latency_pct']}%) | — | Only {stats['latency_and_usd']['direct_latency_count']} studies ({', '.join(f'[{x}]' for x in stats['latency_and_usd']['direct_latency_cites'])}) report direct seconds/minutes (+{stats['latency_and_usd']['proxy_latency_count']} proxy step/TFLOP studies). |"
        + f"\n| Missing Dollar (USD) Cost Totals/Ratios | {stats['latency_and_usd']['usd_omit_or_nv_count']}/{pr['included_total']} ({stats['latency_and_usd']['usd_omit_or_nv_pct']}%) | — | Only {stats['latency_and_usd']['usd_verified_count']}/{pr['included_total']} ({stats['latency_and_usd']['usd_verified_pct']}%) report exact USD spend ({', '.join(f'[{x}]' for x in stats['latency_and_usd']['usd_exact_cites'])}) or numeric USD ratios ({', '.join(f'[{x}]' for x in stats['latency_and_usd']['usd_ratio_cites'])}). |"
    )
    out.append("### TABLE_8_QA_CONFOUNDERS\n" + t8)

    t_rows_order = [
        "Independent / Voting",
        "Sequential Chain / SOP",
        "Centralized Star",
        "Dense All-to-All Debate",
        "Adaptive Sparse / Learned DAG",
        "Hybrid / Selective Escalation",
        "Multi-Topology Suites",
    ]
    k_cols_order = [
        "Decomposable / Parallel",
        "Sequential / State-Dep.",
        "Long-Context / Sandbox",
        "Static Single-Turn / Mixed",
    ]
    g_all = stats["evidence_gap_grid_all"]
    g_t1 = stats["evidence_gap_grid_tier1"]
    ru = stats["evidence_gap_row_unique"]
    rt1 = stats["evidence_gap_row_t1_unique"]
    t11_lines = [
        "| Primary Topology Row | Decomposable / Parallel (Tot / Tier 1) | Sequential / State-Dep. (Tot / Tier 1) | Long-Context / Sandbox (Tot / Tier 1) | Static Single-Turn / Mixed (Tot / Tier 1) | Unique Studies in Row (Tot / Tier 1) |",
        "| :--- | :---: | :---: | :---: | :---: | :---: |",
    ]
    tot_u_all = 0
    tot_u_t1 = 0
    for tl in t_rows_order:
        cells = []
        for kl in k_cols_order:
            a = g_all.get(tl, {}).get(kl, 0)
            b = g_t1.get(tl, {}).get(kl, 0)
            cells.append(f"{a} / {b}" if a > 0 else "0 / 0 (Gap)")
        ua = ru.get(tl, 0)
        ub = rt1.get(tl, 0)
        tot_u_all += ua
        tot_u_t1 += ub
        t11_lines.append(f"| {tl} | " + " | ".join(cells) + f" | {ua} / {ub} |")
    diag_n = stats["topology_counts"].get("Diagnostic/Benchmark Audit (N/A)", 0)
    t11_lines.append(f"| Non-Topological Diagnostic / Validity Studies (N/A) | — | — | — | — | {diag_n} / 0 |")
    t11_lines.append(
        f"| Total Corpus Studies | Multi-label coverage above | Multi-label coverage above | Multi-label coverage above | Multi-label coverage above | {tot_u_all + diag_n} / {tot_u_t1} |"
    )
    out.append("### TABLE_11_EVIDENCE_GAP_HEATMAP\n" + "\n".join(t11_lines))

    def clean_cell(s):
        return str(s).replace("|", ";").replace("\n", " ").strip()

    fc_lines = [
        "| # | Study | Wave | Tier Stratum | Task Family | Benchmark & Setup | MAS vs. SAS Pair | MAS / SAS Scores | Delta | Compute Ratio | Verdict |",
        "| :---: | :--- | :---: | :--- | :--- | :--- | :--- | :---: | :--- | :--- | :---: |",
    ]
    for row in stats["flat_comparisons"]:
        ms_s = f"{row['mas_score']}"
        ss_s = f"{row['sas_score']}"
        fc_lines.append(
            f"| {row['idx']} | {row['short_cite']} [{row['cite']}] | {row['wave']} | {row['tier_label']} | {row['task_family']} | "
            f"{clean_cell(row['benchmark'])} | {clean_cell(row['mas_cfg'])} vs. {clean_cell(row['sas_cmp'])} | "
            f"{clean_cell(ms_s)} vs. {clean_cell(ss_s)} | {clean_cell(row['delta'])} | {clean_cell(row['compute_ratio'])} | **{row['verdict']}** |"
        )
    out.append("### TABLE_APP_C_COMPARISONS\n" + "\n".join(fc_lines))

    ss_lines = [
        "| Study | Status | Wave | Tier Stratum | Mode | k | Wins | Ties | Losses | Mixed | Win Share | >50% Maj | >=50% |",
        "| :--- | :---: | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]
    for row in stats["study_shares"]:
        ss_lines.append(
            f"| {row['short_cite']} [{row['cite']}] | {row['status']} | {row['wave']} | {row['tier_label']} | {row['mode']} | "
            f"{row['k']} | {row['wins']} | {row['ties']} | {row['losses']} | {row['mixed']} | {row['win_share']:.4f} | "
            f"{'Yes' if row['gt_50'] else 'No'} | {'Yes' if row['ge_50'] else 'No'} |"
        )
    out.append("### TABLE_APP_C_STUDY_SHARES\n" + "\n".join(ss_lines))

    rendered = "\n\n".join(out) + "\n"
    with open(DATA / "rendered_tables.md", "w") as f:
        f.write(rendered)
    print("Wrote rendered_tables.md cleanly!")


def main():
    cite_map = build_citations()
    stats, em, qa_rows, sr_rows = compute_all_stats(cite_map)
    render_tables(stats, cite_map, em, qa_rows)
    ca = stats["comparative_all"]
    cr = stats["comparative_archival"]
    cw = stats["comparative_wave1"]
    ci = stats["comparative_interactive"]
    cadj = stats["comparative_adj_1pp"]
    es = stats["effect_size_meta"]
    print("COMPUTE_STATS SUMMARY (v1.4):")
    print(f"  Total studies={stats['prisma']['included_total']} | Comp studies={ca['All']['n_studies']} ({ca['All']['n_tuples']} tuples)")
    print(f"  Full: T3={ca['Tier 3']['win_pct']}% -> T2={ca['Tier 2']['win_pct']}% (T2A={ca['Tier 2A']['win_pct']}%, T2B={ca['Tier 2B']['win_pct']}%) -> T1={ca['Tier 1']['win_pct']}% (Wilson={ca['Tier 1']['win_wilson_ci95']}, Boot={ca['Tier 1']['win_boot_ci95']}, losses={ca['Tier 1']['loss_pct']}%)")
    print(f"  Attenuation T1 vs T2+3: tuple={ca['tuple_attenuation_pp']}pp {ca['tuple_attenuation_ci95']}, study_frac={ca['study_frac_attenuation_pp']}pp (perm p={ca['perm_p_study_frac_t1_vs_t23']}), Fisher p={ca['fisher_p_t1_vs_t23']} (ge50={ca['fisher_p_t1_vs_t23_ge50']}, ge50_t23={ca['Tier 2+3']['study_maj_ge50_wins']}/{ca['Tier 2+3']['n_studies']})")
    print(f"  Archival: T1={cr['Tier 1']['win_pct']}% ({cr['Tier 1']['wins']}/{cr['Tier 1']['n_tuples']}, n={cr['Tier 1']['n_studies']}) vs T2+3={cr['Tier 2+3']['win_pct']}% ({cr['tuple_attenuation_pp']}pp, study_frac p={cr['perm_p_study_frac_t1_vs_t23']}, Fisher p={cr['fisher_p_t1_vs_t23']})")
    print(f"  Wave 1 T2+3={cw['Tier 2+3']['win_pct']}% ({cw['tuple_attenuation_pp']}pp, Fisher p={cw['fisher_p_t1_vs_t23']}) | Wave 2 T2+3={stats['comparative_wave2_t23']['Tier 2+3']['win_pct']}%")
    print(f"  Interactive-Only: T1={ci['Tier 1']['win_pct']}% vs T2+3={ci['Tier 2+3']['win_pct']}% (Fisher p={ci['fisher_p_t1_vs_t23']})")
    print(f"  Sens D (±1pp Tie): T1={cadj['Tier 1']['wins']}/{cadj['Tier 1']['n_tuples']} wins, {cadj['Tier 1']['ties']} ties | T2+3={cadj['Tier 2+3']['wins']}/{cadj['Tier 2+3']['n_tuples']} ({cadj['Tier 2+3']['win_pct']}%)")
    print(f"  Sens F (Opt Nguyen T1): T1={stats['comparative_opt_nguyen']['Tier 1']['win_pct']}% ({stats['comparative_opt_nguyen']['Tier 1']['wins']}/{stats['comparative_opt_nguyen']['Tier 1']['n_tuples']})")
    print(f"  Effect Size: Tier1_num={es['tier1_equal_numeric']['study_mean_pp']}pp | StrongAll={es['strong_controls_all_models']['study_mean_pp']}pp | StrongMainQwen={es['strong_controls_main_qwen']['study_mean_pp']}pp | Weak={es['weak_single_pass']['study_mean_pp']}pp | Post/Casc={es['posttrained_or_selective_escalation']['study_mean_pp']}pp")
    print(f"  IRR Pooled Judgments: {stats['irr']['pooled_judg_agree']}/{stats['irr']['pooled_judg_n']} ({stats['irr']['pooled_judg_po']}%) | End-to-end: {stats['irr']['corpus_bin_po']}%")
    print(f"  QA mean={stats['qa']['overall_mean_pct']}% (12pt={stats['qa']['overall_mean_12pt_pct']}%) | RQ3={stats['qa']['by_track']['RQ3']} | RQ4={stats['qa']['by_track']['RQ4']}")
    print(f"  C6 comparative optimizers={stats['confounders']['qa3_1_comp_count']} / static={stats['confounders']['static_zero_search_comp']} | MultiTopo={stats['multi_topology_subeval']}")


if __name__ == "__main__":
    main()
