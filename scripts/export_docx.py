#!/usr/bin/env python3
"""
Publication-Grade Word (.docx) Exporter for Deliverables F, G, and H (Protocol Amendment v1.3).
Generates 4 crisp 300-DPI PNG figures:
  - Figure 1: Two-Column PRISMA 2020 Selection Flow (Database Queries vs. Citation Chaining)
  - Figure 2: Stratified Multi-Agent Win / Tie / Mixed / Loss Breakdown & Sensitivity with 95% CIs
  - Figure 3: Paired Accuracy Difference Forest Plot (Delta pp: Multi-Agent minus Solo Agent)
  - Figure 4: Conditional 5-Step Single-Agent vs. Multi-Agent Deployment Guide (D0-D4)
Converts Markdown + LaTeX math + tables + hanging-indent References cleanly into styled Word
documents with zero raw markup, zero literal backticks, and full programmatic verification.
"""

import json
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

import docx
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Inches, Pt, RGBColor

ROOT = Path("/Users/adityasharma/.gemini/antigravity/scratch/llm-mas-systematic-review")
DATA = ROOT / "data"
DELIV = ROOT / "deliverables"


def render_prisma_png(st: dict, out_path: Path):
    pr = st["prisma"]
    irr = st["irr"]
    fig, ax = plt.subplots(figsize=(10.2, 8.2), dpi=300)
    ax.set_xlim(0, 10.6)
    ax.set_ylim(0, 10.4)
    ax.axis("off")

    def box(cx, cy, w, h, text, fc="#F0F4F8", ec="#1B365D", lw=1.35, fs=8.0, bold=False):
        p = FancyBboxPatch(
            (cx - w / 2, cy - h / 2), w, h,
            boxstyle="round,pad=0.07,rounding_size=0.12",
            facecolor=fc, edgecolor=ec, linewidth=lw,
        )
        ax.add_patch(p)
        ax.text(cx, cy, text, ha="center", va="center", fontsize=fs,
                fontweight=("bold" if bold else "normal"),
                fontfamily="DejaVu Sans", color="#111111", linespacing=1.30)

    def arrow(x1, y1, x2, y2):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="-|>,head_width=0.20,head_length=0.32",
                                    color="#1B365D", lw=1.35))

    ax.text(5.3, 10.12, "PRISMA 2020 Two-Column Systematic Selection Flow (Searches 1–13)",
            ha="center", va="center", fontsize=11.2, fontweight="bold", color="#1B365D")

    # Section banners on far left
    for cy, lbl, col in [(8.95, "IDENTIFICATION", "#1B365D"),
                         (5.75, "SCREENING", "#2B4C7E"),
                         (1.25, "INCLUDED", "#1E6B38")]:
        box(0.55, cy, 0.85, 1.35 if cy > 3 else 1.55, lbl, fc=col, ec=col, lw=1.0, fs=7.0, bold=True)
        # Re-color text white on banners
        ax.texts[-1].set_color("white")
        ax.texts[-1].set_rotation(90)

    # Top Identification Row: Two Columns (DB Queries vs Citation Chaining/Other)
    box(3.35, 9.10, 4.15, 1.15,
        "Database & Repository Searches (S01–S09, S12)\n"
        "arXiv, OpenReview, ACL Anthology, PMLR, ACM DL, Springer/Nature\n"
        "n = 96 raw records (84 baseline + 12 targeted import)",
        fc="#E8EEF5", fs=7.7)
    box(8.15, 9.10, 4.15, 1.15,
        "Citation Chaining & Targeted Checks (S10–S11, S13)\n"
        "Backward/forward snowballing + anchor recovery\n"
        "n = 46 records (42 snowballing + 4 gap anchors)",
        fc="#EBF3EC", ec="#2D6A4F", fs=7.7)

    # Merged Deduplication Box
    box(4.65, 7.55, 5.4, 0.92,
        f"Combined Identified: n = {pr['raw_total']} raw hits\n"
        f"Duplicates & version links merged: n = {pr['duplicates']} removed -> {pr['unique_screened']} unique records",
        fc="#F7F9FB", fs=8.0)

    # Stage 1 Screening & Exclusion
    box(3.55, 6.00, 4.35, 1.05,
        f"Stage 1: Title, Abstract & Venue Screening\n"
        f"n = {pr['unique_screened']} unique records screened\n"
        f"Dual-pass agree: {irr['full_stage1_po']}% (98/100, kappa = {irr['full_stage1_kappa']})",
        fc="#E8EEF5", fs=7.7)
    box(8.25, 6.00, 3.85, 1.05,
        f"Excluded at Stage 1 (n = {pr['stage1_excluded']})\n"
        f"E4 Surveys: {pr['stage1_excl_by_code'].get('E4', 0)} | E8 Rejected/Withdrawn: {pr['stage1_excl_by_code'].get('E8', 0)}\n"
        f"E3 Single-Agent/Router: {pr['stage1_excl_by_code'].get('E3', 0)} | E7 Scope: {pr['stage1_excl_by_code'].get('E7', 0)}",
        fc="#FDF2F2", ec="#9B2C2C", fs=7.6)

    # Reports Sought / Retrieval Box + Reports Not Retrieved Side Box
    box(3.55, 4.45, 4.35, 0.85,
        "Reports Sought for Open-Text / Summary Retrieval\n"
        "n = 70 records advancing (67 open full PDF/HTML + 3 abstract-only)",
        fc="#F7F9FB", fs=7.6)
    box(8.25, 4.45, 3.85, 0.85,
        "Reports Not Retrieved: n = 0\n"
        "(3 paywalled abstracts advanced & coded E5 at Stage 2;\n"
        "1 paywalled ICSE item verified via open arXiv mirror)",
        fc="#FFF8E6", ec="#9C6500", fs=7.4)

    # Stage 2 Eligibility & Exclusion
    box(3.55, 2.95, 4.35, 1.08,
        f"Stage 2: Open Full-Text & Open-Summary Eligibility\n"
        f"n = {pr['stage2_assessed']} dual-assessed (3-class: {irr['stage2_3class_po']}%, kappa={irr['stage2_3class_kappa']})\n"
        f"Pooled judgments: {irr['pooled_judg_agree']}/{irr['pooled_judg_n']} ({round(irr['pooled_judg_po'], 1)}%) | Record agree: {irr['corpus_bin_po']}%",
        fc="#E8EEF5", fs=7.3)
    box(8.25, 2.95, 3.85, 1.08,
        f"Excluded at Stage 2 (n = {pr['stage2_excluded']})\n"
        f"E5 Paywall/Abstract Only: {pr['stage2_excl_by_code'].get('E5', 0)} | E3 Single-Agent: {pr['stage2_excl_by_code'].get('E3', 0)}\n"
        f"E2 Non-Empirical: {pr['stage2_excl_by_code'].get('E2', 0)} | E7 Scope: {pr['stage2_excl_by_code'].get('E7', 0)} | E4: {pr['stage2_excl_by_code'].get('E4', 0)}",
        fc="#FDF2F2", ec="#9B2C2C", fs=7.5)

    # Final Included Corpus
    box(5.65, 1.15, 8.75, 1.48,
        f"Final Included Corpus: N = {pr['included_total']} Studies\n"
        f"Archival (Journal + Conference): {pr['archival_count']} ({pr['archival_pct']}%) | "
        f"Workshop: {pr['workshop_count']} ({pr['workshop_pct']}%) | Preprint: {pr['preprint_count']} ({pr['preprint_pct']}%)\n"
        f"Tracks: {st['comparative_all']['All']['n_studies']} Comparative Studies ({st['comparative_all']['All']['n_tuples']} Cleaned Comparisons) + 25 Mechanistic / Security / Validity Studies",
        fc="#E6F4EA", ec="#1E6B38", lw=1.7, fs=8.0)

    # Arrows
    arrow(3.35, 8.45, 3.85, 8.08)
    arrow(8.15, 8.45, 5.75, 8.08)
    arrow(4.10, 7.02, 3.65, 6.60)
    arrow(5.80, 6.00, 6.25, 6.00)
    arrow(3.55, 5.40, 3.55, 4.95)
    arrow(5.80, 4.45, 6.25, 4.45)
    arrow(3.55, 3.95, 3.55, 3.56)
    arrow(5.80, 2.95, 6.25, 2.95)
    arrow(3.55, 2.34, 4.45, 1.96)

    plt.tight_layout(pad=0.2)
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def render_winrates_png(st: dict, out_path: Path):
    ca = st["comparative_all"]
    cr = st["comparative_archival"]

    labels = [
        f"Tier 3: Weak 1-Pass\n(n={ca['Tier 3']['n_studies']}, k={ca['Tier 3']['n_tuples']})",
        f"Tier 2B: Search / Train C6\n(n={ca['Tier 2B']['n_studies']}, k={ca['Tier 2B']['n_tuples']})",
        f"Tier 2A: Unmatched Budget\n(n={ca['Tier 2A']['n_studies']}, k={ca['Tier 2A']['n_tuples']})",
        f"Tier 1: Equal Compute\n(n={ca['Tier 1']['n_studies']}, k={ca['Tier 1']['n_tuples']})",
        f"Archival-Only Tier 1\n(n={cr['Tier 1']['n_studies']}, k={cr['Tier 1']['n_tuples']})",
    ]
    slices = [ca["Tier 3"], ca["Tier 2B"], ca["Tier 2A"], ca["Tier 1"], cr["Tier 1"]]
    wins = [s["win_pct"] for s in slices]
    ties = [s["tie_pct"] for s in slices]
    mixed = [s["mixed_pct"] for s in slices]
    losses = [s["loss_pct"] for s in slices]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.8, 4.7), dpi=300, gridspec_kw={"width_ratios": [1.22, 1.05]})

    y = list(range(len(labels)))[::-1]
    h = 0.56
    ax1.barh(y, wins, height=h, color="#1E6B38", label="MAS Wins")
    ax1.barh(y, ties, left=wins, height=h, color="#94A3B8", label="Ties")
    l_mix = [w + t for w, t in zip(wins, ties)]
    ax1.barh(y, mixed, left=l_mix, height=h, color="#D97706", label="Mixed")
    l_loss = [lm + m for lm, m in zip(l_mix, mixed)]
    ax1.barh(y, losses, left=l_loss, height=h, color="#B91C1C", label="MAS Losses")

    for yi, w, l in zip(y, wins, losses):
        if w >= 12:
            ax1.text(w / 2, yi, f"{w:.1f}%", ha="center", va="center", color="white", fontsize=7.8, fontweight="bold")
        if l >= 12:
            ax1.text(100 - l / 2, yi, f"{l:.1f}%", ha="center", va="center", color="white", fontsize=7.8, fontweight="bold")

    ax1.set_yticks(y)
    ax1.set_yticklabels(labels, fontsize=8.0)
    ax1.set_xlim(0, 100)
    ax1.set_xlabel("Share of Paired Comparisons (%)", fontsize=8.8)
    ax1.set_title("A. Verdict Breakdown by Baseline Fairness Tier", fontsize=9.8, fontweight="bold", color="#1B365D")
    ax1.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=4, fontsize=7.6, frameon=False)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    # Right panel: Win rates + 95% cluster-bootstrap CIs
    ci_labels = [
        "Tier 3\n(Tuples)",
        "Tier 2B\n(Tuples)",
        "Tier 2A\n(Tuples)",
        "Tier 2+3\n(Tuples)",
        "Tier 1\n(Tuples)",
        "Tier 2+3\n(Study)",
        "Tier 1\n(Study)",
    ]
    vals = [
        ca["Tier 3"]["win_pct"],
        ca["Tier 2B"]["win_pct"],
        ca["Tier 2A"]["win_pct"],
        ca["Tier 2+3"]["win_pct"],
        ca["Tier 1"]["win_pct"],
        ca["Tier 2+3"]["study_frac_win_pct"],
        ca["Tier 1"]["study_frac_win_pct"],
    ]
    cis = [
        ca["Tier 3"]["win_boot_ci95"],
        ca["Tier 2B"]["win_boot_ci95"],
        ca["Tier 2A"]["win_boot_ci95"],
        ca["Tier 2+3"]["win_boot_ci95"],
        ca["Tier 1"]["win_boot_ci95"],
        ca["Tier 2+3"]["study_frac_boot_ci95"],
        ca["Tier 1"]["study_frac_boot_ci95"],
    ]
    x = list(range(len(ci_labels)))
    cols = ["#2D6A4F", "#2563EB", "#60A5FA", "#1D4ED8", "#B91C1C", "#64748B", "#991B1B"]
    yerr_lo = [max(0.0, v - c[0]) for v, c in zip(vals, cis)]
    yerr_hi = [max(0.0, c[1] - v) for v, c in zip(vals, cis)]

    ax2.bar(x, vals, width=0.56, color=cols, alpha=0.92,
            yerr=[yerr_lo, yerr_hi], capsize=3.2, error_kw={"elinewidth": 1.15, "ecolor": "#111827"})
    for xi, v, hi in zip(x, vals, yerr_hi):
        ax2.text(xi, v + hi + 2.2, f"{v:.1f}%", ha="center", va="bottom", fontsize=7.0, fontweight="bold", color="#111827")

    ax2.annotate(f"{ca['tuple_attenuation_pp']} pp\n(perm p={ca['perm_p_study_frac_t1_vs_t23']})",
                 xy=(4.0, ca["Tier 1"]["win_pct"] + yerr_hi[4] + 8), xytext=(4.85, 102),
                 ha="center", va="center", fontsize=7.4, fontweight="bold", color="#991B1B",
                 bbox=dict(boxstyle="round,pad=0.18", fc="#FEF2F2", ec="#991B1B", lw=0.8),
                 arrowprops=dict(arrowstyle="-|>", color="#991B1B", lw=1.15))

    ax2.set_xticks(x)
    ax2.set_xticklabels(ci_labels, fontsize=7.0)
    ax2.set_ylim(0, 120)
    ax2.set_ylabel("Multi-Agent Win Rate (% with 95% Boot CI)", fontsize=8.6)
    ax2.set_title("B. Parity Drop & Cluster-Bootstrap CIs", fontsize=9.8, fontweight="bold", color="#1B365D")
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    plt.tight_layout(pad=0.8)
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def render_forest_png(st: dict, out_path: Path):
    es = st["effect_size_meta"]
    entries = [
        ("CAIS '26: Ministral-3-8B vs. Isolated Self (n=100)", -27.6, None, None, "#B91C1C", False),
        ("Optima (Raw): Unoptimized MAD vs. SC (GSM8K)", -7.8, None, None, "#B91C1C", False),
        ("Self-MoA: Mixed-MoA vs. Single-Best (AlpacaEval 2.0)", -6.6, None, None, "#B91C1C", False),
        ("Optima (Raw): Unoptimized MAD vs. SC (MATH)", -5.9, None, None, "#B91C1C", False),
        ("Debate or Vote: MAD vs. Majority Vote (Arithmetics)", -5.4, None, None, "#B91C1C", False),
        ("Debate or Vote: MAD vs. Majority Vote (GSM8K)", -5.33, None, None, "#B91C1C", False),
        ("Tran & Kiela: Teams vs. Solo (5k tok, 4-hop QA)", -4.1, None, None, "#B91C1C", False),
        ("CAIS '26: Qwen2.5-7B Primary vs. Isolated Self (n=1,017)", -2.2, None, None, "#B91C1C", False),
        ("CAIS '26: Llama-3.1-8B vs. Isolated Self (n=100)", -1.7, None, None, "#B91C1C", False),
        ("Strong Controls Mean — All 3 CAIS Models (n=5, k=9)",
         es["strong_controls_all_models"]["study_mean_pp"],
         es["strong_controls_all_models"]["study_boot_ci95"][0],
         es["strong_controls_all_models"]["study_boot_ci95"][1], "#7F1D1D", True),
        ("Strong Controls Mean — Main Qwen2.5-7B (n=5, k=7)",
         es["strong_controls_main_qwen"]["study_mean_pp"],
         es["strong_controls_main_qwen"]["study_boot_ci95"][0],
         es["strong_controls_main_qwen"]["study_boot_ci95"][1], "#991B1B", True),
        ("Weak Single-Pass Solo Controls Mean (n=8, k=34)",
         es["weak_single_pass"]["study_mean_pp"],
         es["weak_single_pass"]["study_boot_ci95"][0],
         es["weak_single_pass"]["study_boot_ci95"][1], "#1D4ED8", True),
        ("Gao et al.: Same MAS vs. Stronger Gemini-2.0-Flash", 1.67, 0.8, 3.0, "#1E6B38", False),
        ("Optima (Trained <12h 8xA100): GSM8K vs. SC(n=8)", 3.7, None, None, "#1E6B38", False),
        ("SAIGE Sparse Escalation vs. Solo (AgentIF-OneDay)", 18.23, None, None, "#1E6B38", False),
        ("Optima (Trained <12h 8xA100): HotpotQA vs. SC(n=8)", 21.8, None, None, "#1E6B38", False),
        ("CascadeDebate Escalation vs. Cascade (MedQA)", 22.52, None, None, "#1E6B38", False),
        ("Post-Trained / Selective Escalation Mean (n=4, k=6)",
         es["posttrained_or_selective_escalation"]["study_mean_pp"],
         es["posttrained_or_selective_escalation"]["study_boot_ci95"][0],
         es["posttrained_or_selective_escalation"]["study_boot_ci95"][1], "#14532D", True),
    ]

    fig, ax = plt.subplots(figsize=(10.2, 6.4), dpi=300)
    y = list(range(len(entries)))[::-1]
    ax.axvline(0.0, color="#334155", linestyle="--", linewidth=1.2, zorder=1)
    ax.axvspan(-33, 0, color="#FEF2F2", alpha=0.45, zorder=0)
    ax.axvspan(0, 29, color="#ECFDF5", alpha=0.45, zorder=0)

    for yi, (lbl, val, lo, hi, col, is_sum) in zip(y, entries):
        marker = "D" if is_sum else "o"
        ms = 8.0 if is_sum else 5.8
        if lo is not None and hi is not None:
            ax.errorbar(val, yi, xerr=[[val - lo], [hi - val]], fmt=marker, color=col,
                        markersize=ms, capsize=3.5, elinewidth=1.7 if is_sum else 1.1, zorder=3)
        else:
            ax.plot(val, yi, marker=marker, color=col, markersize=ms, zorder=3)
        txt = f"{val:+.2f} pp" if abs(val) < 10 and not is_sum else f"{val:+.1f} pp"
        if is_sum:
            txt = f"{val:+.2f} [{lo:+.1f}, {hi:+.1f}]"
        offset = 1.2 if val >= 0 else -1.2
        ha = "left" if val >= 0 else "right"
        # Prevent left-edge clipping for -27.6
        if val < -20:
            offset, ha = 1.2, "left"
        ax.text((hi if hi is not None and val >= 0 else (lo if lo is not None and val < 0 else val)) + offset,
                yi, txt, va="center", ha=ha, fontsize=7.6,
                fontweight=("bold" if is_sum else "normal"), color=col)

    ax.set_yticks(y)
    ax.set_yticklabels([e[0] for e in entries], fontsize=7.9)
    for tick, e in zip(ax.get_yticklabels(), entries):
        if e[5]:
            tick.set_fontweight("bold")
    ax.set_xlim(-33, 30)
    ax.set_xlabel("Accuracy Difference (Percentage Points: Multi-Agent minus Solo Agent)", fontsize=8.8)
    ax.set_title("Paired Accuracy Effect Sizes Across Control Rigor Regimes (Within-Study Numeric Comparisons)",
                 fontsize=9.8, fontweight="bold", color="#1B365D")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout(pad=0.5)
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def render_decision_png(out_path: Path):
    fig, ax = plt.subplots(figsize=(10.0, 7.2), dpi=300)
    ax.set_xlim(0, 10.2)
    ax.set_ylim(0, 10.2)
    ax.axis("off")

    def node(cx, cy, w, h, text, fc="#EEF3F8", ec="#1B365D", fs=8.0, lw=1.35):
        p = FancyBboxPatch(
            (cx - w / 2, cy - h / 2), w, h,
            boxstyle="round,pad=0.07,rounding_size=0.14",
            facecolor=fc, edgecolor=ec, linewidth=lw,
        )
        ax.add_patch(p)
        ax.text(cx, cy, text, ha="center", va="center", fontsize=fs,
                fontfamily="DejaVu Sans", color="#111111", linespacing=1.28)

    def arrow(x1, y1, x2, y2, lbl="", lx=None, ly=None):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="-|>,head_width=0.20,head_length=0.32",
                                    color="#1B365D", lw=1.3))
        if lbl:
            mx = lx if lx is not None else (x1 + x2) / 2
            my = ly if ly is not None else (y1 + y2) / 2
            ax.text(mx, my, lbl, ha="center", va="center", fontsize=7.4,
                    fontweight="bold", color="#1B365D",
                    bbox=dict(boxstyle="round,pad=0.14", fc="white", ec="none"))

    ax.text(5.1, 9.85, "5-Step Conditional Single-Agent vs. Multi-Agent Deployment Guide",
            ha="center", va="center", fontsize=11.0, fontweight="bold", color="#1B365D")
    ax.text(5.1, 9.48, "(Synthesis-Derived Checklist — Requires Prospective Controlled Validation)",
            ha="center", va="center", fontsize=8.5, style="italic", color="#475569")

    node(2.70, 8.55, 4.75, 0.88,
         "Step 1: Reliable automatic check (unit test, DB state)\nOR context too large for one solo AI's memory?",
         fc="#E8EEF5")
    node(2.70, 6.80, 4.75, 0.88,
         "Step 2: Does one modern solo AI already score high\non this task (diminishing-return zone, e.g., ~45%+)?",
         fc="#E8EEF5")
    node(2.70, 5.05, 4.75, 0.88,
         "Step 3: Tightly ordered steps OR closed-book logic\nwhere written summaries risk losing clues?",
         fc="#E8EEF5")
    node(2.70, 3.30, 4.75, 0.88,
         "Step 4: Mixed easy/hard traffic with a reliable\nconfidence or test-check trigger to escalate?",
         fc="#E8EEF5")
    node(2.70, 1.45, 4.75, 0.94,
         "Step 5: At matched accuracy, is c_MAS < c_SAS AND\nvolume Q > C_search / (c_SAS - c_MAS)? (or +v $/pt/q)",
         fc="#E8EEF5")

    node(7.90, 7.68, 3.35, 1.25,
         "Regime A: Keep Equal-Budget Solo AI\nUse compute-matched single agent;\navoid +58% to +285% token tax &\n-39% to -70% sequential drops.",
         fc="#FDF2F2", ec="#9B2C2C", fs=7.8)
    node(7.90, 5.05, 3.35, 1.15,
         "Regime B: Solo Repeated Voting\nRun Self-Consistency, Self-MoA,\nor isolated self-checks on top\nmodel (no peer conformity).",
         fc="#FFF8E6", ec="#9C6500", fs=7.8)
    node(7.90, 3.30, 3.35, 1.05,
         "Regime C: Selective Escalation\nSolve easy items with Solo AI first;\ncall team only when checks fail.",
         fc="#EBF5FF", ec="#1D4ED8", fs=7.8)
    node(7.90, 1.45, 3.35, 1.32,
         "Regime D: Controlled Static Team\nCentralized workers / pruned DAG\n(0/10 learned graphs Tier 1 verified)\n+ hashes, turn caps & sandbox.",
         fc="#E6F4EA", ec="#1E6B38", fs=7.5)

    arrow(5.15, 8.55, 6.15, 8.05, "No (open-ended)", 5.72, 8.72)
    arrow(2.70, 8.04, 2.70, 7.31, "Yes", 2.35, 7.68)
    arrow(5.15, 6.80, 6.15, 7.28, "Yes (strong solo)", 5.75, 6.72)
    arrow(2.70, 6.29, 2.70, 5.56, "No (headroom)", 2.18, 5.92)
    arrow(5.15, 5.05, 6.15, 5.05, "Yes", 5.65, 5.26)
    arrow(2.70, 4.54, 2.70, 3.81, "No (splittable)", 2.18, 4.18)
    arrow(5.15, 3.30, 6.15, 3.30, "Yes", 5.65, 3.51)
    arrow(2.70, 2.79, 2.70, 1.99, "No (uniform)", 2.18, 2.39)
    arrow(5.15, 1.45, 6.15, 1.45, "Yes", 5.65, 1.66)

    # Outer dashed fallback from Step 5 No -> Regime B
    ax.plot([2.70, 2.70, 9.85, 9.85], [0.91, 0.35, 0.35, 5.05], color="#1B365D", lw=1.25, ls="--")
    ax.annotate("", xy=(9.65, 5.05), xytext=(9.85, 5.05),
                arrowprops=dict(arrowstyle="-|>,head_width=0.20,head_length=0.32",
                                color="#1B365D", lw=1.25))
    ax.text(6.25, 0.35, "No (c_MAS >= c_SAS or low volume -> use Regime B)", ha="center", va="center",
            fontsize=7.5, fontweight="bold", color="#1B365D",
            bbox=dict(boxstyle="round,pad=0.14", fc="white", ec="none"))

    plt.tight_layout(pad=0.2)
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def read_brace_group(s: str, start: int):
    if start >= len(s) or s[start] != "{":
        return None, start
    depth = 0
    i = start
    while i < len(s):
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return s[start + 1:i], i + 1
        i += 1
    return None, start


def replace_cmd_1arg(s: str, cmd: str, fn):
    while True:
        idx = s.find(cmd + "{")
        if idx == -1:
            break
        arg1, p1 = read_brace_group(s, idx + len(cmd))
        if arg1 is None:
            break
        s = s[:idx] + fn(arg1) + s[p1:]
    return s


def replace_cmd_2arg(s: str, cmd: str, fn):
    while True:
        idx = s.find(cmd + "{")
        if idx == -1:
            break
        arg1, p1 = read_brace_group(s, idx + len(cmd))
        while p1 < len(s) and s[p1] == " ":
            p1 += 1
        arg2, p2 = read_brace_group(s, p1)
        if arg1 is None or arg2 is None:
            break
        s = s[:idx] + fn(arg1, arg2) + s[p2:]
    return s


def wrap_atom(txt: str) -> str:
    t = txt.strip()
    if any(op in t for op in ["+", " - ", " / ", " × ", " · "]):
        return f"({t})"
    return t


def clean_math_expr(expr: str) -> str:
    s = expr.strip()
    s = s.replace(r"\mathbb{E}_{\text{task}}", "E_task")
    s = s.replace(r"\mathbb{E}", "E")
    s = s.replace(r"\Delta", "Δ").replace(r"\bar{p}", "p̄").replace(r"\hat{p}", "p̂").replace(r"\hat{Z}", "Ẑ")
    s = replace_cmd_1arg(s, r"\text", lambda a: a)
    s = replace_cmd_1arg(s, r"\mathrm", lambda a: a)
    s = replace_cmd_2arg(s, r"\binom", lambda a, b: f"C({a}, {b})")
    s = replace_cmd_2arg(s, r"\frac", lambda a, b: f"{wrap_atom(a)} / {wrap_atom(b)}")
    # Longer arrows BEFORE prefix commands (\leftrightarrow before \le and \rightarrow!)
    s = s.replace(r"\leftrightarrow", " ↔ ").replace(r"\rightarrow", " → ").replace(r"\leftarrow", " ← ")
    s = s.replace(r"\left[", "[").replace(r"\right]", "]")
    s = s.replace(r"\left(", "(").replace(r"\right)", ")")
    s = s.replace(r"\ge", "≥").replace(r"\le", "≤").replace(r"\approx", "≈").replace(r"\to", " → ")
    s = s.replace(r"\times", "×").replace(r"\cdot", "·").replace(r"\quad", "   ").replace(r"\infty", "∞")
    s = s.replace(r"\sum_i", "Σ_i").replace(r"\sum", "Σ")
    s = s.replace(r"\kappa", "κ").replace(r"\beta", "β").replace(r"\rho", "ρ").replace(r"\tau", "τ")
    s = s.replace("^*", "*").replace(r"\%", "%").replace("{", "").replace("}", "")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def preprocess_markdown_math(text: str) -> str:
    text = re.sub(r"\$\$(.*?)\$\$", lambda m: "\n> " + clean_math_expr(m.group(1)) + "\n", text, flags=re.S)
    text = re.sub(r"\$([^$\n]+)\$", lambda m: clean_math_expr(m.group(1)), text)
    text = re.sub(r"\[([^\]]+)\]\(file:///[^)]+\)", r"\1", text)
    return text


def set_cell_shading(cell, fill_hex: str):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)


def set_cell_margins(cell, top=55, bottom=55, left=80, right=80):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement("w:tcMar")
    for m, val in [("top", top), ("bottom", bottom), ("left", left), ("right", right)]:
        node = OxmlElement(f"w:{m}")
        node.set(qn("w:w"), str(val))
        node.set(qn("w:type"), "dxa")
        tcMar.append(node)
    tcPr.append(tcMar)


def set_table_borders(table, color="CBD5E1"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="6" w:space="0" w:color="1B365D"/>'
        f'<w:bottom w:val="single" w:sz="8" w:space="0" w:color="1B365D"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="none"/><w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)


def add_formatted_runs(p, text: str, base_size=10.5, base_color=RGBColor(0x1F, 0x29, 0x37), force_bold=False, font_name="Times New Roman"):
    # Strip any stray backticks cleanly so typography stays completely uniform (no Consolas jumps)
    clean_text = text.replace("`", "")
    pattern = re.compile(r"(\*\*[^*]+\*\*|\*[^*\n]+\*)")
    pos = 0
    for m in pattern.finditer(clean_text):
        if m.start() > pos:
            r = p.add_run(clean_text[pos:m.start()])
            r.font.name = font_name
            r.font.size = Pt(base_size)
            r.font.color.rgb = base_color
            if force_bold:
                r.bold = True
        tok = m.group(0)
        if tok.startswith("**") and tok.endswith("**"):
            inner = tok[2:-2]
            r = p.add_run(inner)
            r.font.name = font_name
            r.font.size = Pt(base_size)
            r.font.color.rgb = base_color
            r.bold = True
        elif tok.startswith("*") and tok.endswith("*"):
            inner = tok[1:-1]
            r = p.add_run(inner)
            r.font.name = font_name
            r.font.size = Pt(base_size)
            r.font.color.rgb = base_color
            r.italic = True
            if force_bold:
                r.bold = True
        pos = m.end()
    if pos < len(clean_text):
        r = p.add_run(clean_text[pos:])
        r.font.name = font_name
        r.font.size = Pt(base_size)
        r.font.color.rgb = base_color
        if force_bold:
            r.bold = True


def add_page_number_field(run):
    fldChar1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls("w"))
    instrText = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls("w"))
    fldChar2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls("w"))
    fldChar3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls("w"))
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    run._r.append(fldChar3)


def configure_doc(header_title: str) -> Document:
    doc = Document()
    for sec in doc.sections:
        sec.top_margin = Inches(0.85)
        sec.bottom_margin = Inches(0.85)
        sec.left_margin = Inches(0.85)
        sec.right_margin = Inches(0.85)
        sec.different_first_page_header_footer = True

        hdr = sec.header.paragraphs[0]
        hdr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hr = hdr.add_run(header_title)
        hr.font.name = "Times New Roman"
        hr.font.size = Pt(8.5)
        hr.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)
        hr.italic = True

        ftr = sec.footer.paragraphs[0]
        ftr.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fr1 = ftr.add_run("Page ")
        fr1.font.name = "Times New Roman"
        fr1.font.size = Pt(8.5)
        fr1.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)
        fr_num = ftr.add_run()
        fr_num.font.name = "Times New Roman"
        fr_num.font.size = Pt(8.5)
        fr_num.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)
        add_page_number_field(fr_num)

    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(10.5)
    normal.paragraph_format.line_spacing = 1.15
    normal.paragraph_format.space_after = Pt(5)
    return doc


def render_md_table(doc: Document, table_lines: list[str]):
    rows = []
    for i, line in enumerate(table_lines):
        if i == 1 and re.match(r"^\|\s*:?-{2,}", line.strip()):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append(cells)
    if not rows:
        return
    ncols = max(len(r) for r in rows)
    tbl = doc.add_table(rows=len(rows), cols=ncols)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl)
    font_sz = 8.0 if ncols >= 7 else (8.5 if ncols >= 5 else 9.5)

    for r_idx, row_vals in enumerate(rows):
        trPr = tbl.rows[r_idx]._tr.get_or_add_trPr()
        trPr.append(OxmlElement("w:cantSplit"))
        if r_idx == 0:
            trPr.append(OxmlElement("w:tblHeader"))
        for c_idx in range(ncols):
            val = row_vals[c_idx] if c_idx < len(row_vals) else ""
            cell = tbl.cell(r_idx, c_idx)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell, top=55, bottom=55, left=70, right=70)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.08
            if r_idx == 0:
                set_cell_shading(cell, "1B365D")
                add_formatted_runs(p, val, base_size=font_sz, base_color=RGBColor(0xFF, 0xFF, 0xFF), force_bold=True, font_name="Calibri")
            else:
                if r_idx % 2 == 0:
                    set_cell_shading(cell, "F4F7FA")
                add_formatted_runs(p, val, base_size=font_sz, base_color=RGBColor(0x1F, 0x29, 0x37), font_name="Calibri")

    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_before = Pt(0)
    spacer.paragraph_format.space_after = Pt(4)


def convert_markdown_to_docx(md_path: Path, docx_path: Path, header_title: str, fig_map: dict = None):
    raw_txt = md_path.read_text()
    txt = preprocess_markdown_math(raw_txt)
    lines = txt.splitlines()

    doc = configure_doc(header_title)
    fig_map = fig_map or {}
    in_refs = False
    in_abstract = False
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        s = line.strip()

        if not s or s == "---" or s.startswith("!["):
            i += 1
            continue

        if s.startswith("```mermaid"):
            block = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1
            btxt = "\n".join(block)
            img_path = None
            for kw, pth in fig_map.items():
                if kw in btxt:
                    img_path = pth
                    break
            if img_path and Path(img_path).exists():
                p_img = doc.add_paragraph()
                p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_img.paragraph_format.space_before = Pt(6)
                p_img.paragraph_format.space_after = Pt(2)
                p_img.add_run().add_picture(str(img_path), width=Inches(6.55))
            continue

        if s.startswith("```"):
            block = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1
            p_code = doc.add_paragraph()
            p_code.paragraph_format.left_indent = Inches(0.25)
            r = p_code.add_run("\n".join(block))
            r.font.name = "Times New Roman"
            r.font.size = Pt(9.5)
            continue

        if s.startswith("|"):
            tlines = []
            while i < n and lines[i].strip().startswith("|"):
                tlines.append(lines[i])
                i += 1
            render_md_table(doc, tlines)
            continue

        if s.startswith("# "):
            title_txt = s[2:].strip()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(8)
            add_formatted_runs(p, title_txt, base_size=15.5, base_color=RGBColor(0x1B, 0x36, 0x5D), force_bold=True)
            i += 1
            continue

        if s.startswith("## "):
            h_txt = s[3:].strip()
            in_refs = h_txt.startswith("10. References") or h_txt == "References"
            in_abstract = (h_txt == "Abstract")
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            add_formatted_runs(p, h_txt, base_size=13.0, base_color=RGBColor(0x1B, 0x36, 0x5D), force_bold=True)
            pPr = p._p.get_or_add_pPr()
            pPr.append(parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:space="2" w:color="CBD5E1"/></w:pBdr>'))
            i += 1
            continue

        if s.startswith("### "):
            h_txt = s[4:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(9)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.keep_with_next = True
            add_formatted_runs(p, h_txt, base_size=11.5, base_color=RGBColor(0x1E, 0x3A, 0x5F), force_bold=True)
            i += 1
            continue

        if s.startswith("#### "):
            h_txt = s[5:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.keep_with_next = True
            add_formatted_runs(p, h_txt, base_size=10.0, base_color=RGBColor(0x1B, 0x36, 0x5D), force_bold=True, font_name="Calibri")
            i += 1
            continue

        if in_abstract:
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.25)
            p.paragraph_format.right_indent = Inches(0.25)
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(8)
            pPr = p._p.get_or_add_pPr()
            pPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="F4F7FA"/>'))
            pPr.append(parse_xml(f'<w:pBdr {nsdecls("w")}><w:left w:val="single" w:sz="18" w:space="8" w:color="1B365D"/></w:pBdr>'))
            add_formatted_runs(p, s, base_size=10.0, base_color=RGBColor(0x11, 0x18, 0x27))
            in_abstract = False
            i += 1
            continue

        if s.startswith("> "):
            q_txt = s[2:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.45)
            p.paragraph_format.right_indent = Inches(0.35)
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(5)
            pPr = p._p.get_or_add_pPr()
            pPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8FAFC"/>'))
            add_formatted_runs(p, q_txt, base_size=10.0, base_color=RGBColor(0x0F, 0x17, 0x2A))
            i += 1
            continue

        if in_refs and re.match(r"^\*\*\[\d+\]\*\*", s):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.35)
            p.paragraph_format.first_line_indent = Inches(-0.35)
            p.paragraph_format.space_after = Pt(3.5)
            p.paragraph_format.line_spacing = 1.08
            add_formatted_runs(p, s, base_size=9.0, base_color=RGBColor(0x1F, 0x29, 0x37))
            i += 1
            continue

        m_num = re.match(r"^(\d+)\.\s+(.*)$", s)
        if s.startswith("- ") or (s.startswith("* ") and not s.startswith("*Note:") and not s.startswith("*Figure ") and not s.startswith("*Target Journal:")):
            b_txt = s[2:].strip()
            p = doc.add_paragraph(style="List Bullet")
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.12
            add_formatted_runs(p, b_txt, base_size=10.0)
            i += 1
            continue
        elif m_num:
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.28)
            p.paragraph_format.first_line_indent = Inches(-0.2)
            p.paragraph_format.space_after = Pt(3.5)
            add_formatted_runs(p, f"**{m_num.group(1)}.** {m_num.group(2)}", base_size=10.5)
            i += 1
            continue

        if (s.startswith("*Figure ") or s.startswith("*Note:")) and s.endswith("*"):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if s.startswith("*Figure ") else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(7)
            add_formatted_runs(p, s, base_size=9.0, base_color=RGBColor(0x47, 0x55, 0x69))
            i += 1
            continue

        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(5.5)
        add_formatted_runs(p, s, base_size=10.5)
        i += 1

    doc.save(str(docx_path))
    print(f"Saved {docx_path.name}: {docx_path.stat().st_size:,} bytes")


def verify_docx(path: Path, min_tables=0, check_refs=False, expected_figs=0, total_refs=124):
    d = docx.Document(str(path))
    all_text = "\n".join(p.text for p in d.paragraphs)
    for t in d.tables:
        for row in t.rows:
            for cell in row.cells:
                all_text += "\n" + cell.text
    assert len(d.tables) >= min_tables, f"{path.name}: expected >= {min_tables} tables, got {len(d.tables)}"
    if expected_figs > 0:
        assert len(d.inline_shapes) == expected_figs, f"{path.name}: expected {expected_figs} figures, got {len(d.inline_shapes)}"
    bad_tokens = ["```mermaid", "\\binom{", "\\frac{", "\\text{", "\\mathrm{", "\\mathbb", "≤ftrightarrow", "\\%", "`", "## 1."]
    for bad in bad_tokens:
        assert bad not in all_text, f"{path.name}: raw/corrupted markup leaked: {bad}"
    if check_refs:
        for k in range(1, total_refs + 1):
            assert f"[{k}]" in all_text, f"{path.name}: missing ref [{k}]"
    print(f"Verified {path.name}: paragraphs={len(d.paragraphs)}, tables={len(d.tables)}, figs={len(d.inline_shapes)}, clean=True")


def main():
    with open(DATA / "verified_stats.json") as f:
        st = json.load(f)
    with open(DATA / "cite_map.json") as f:
        cm = json.load(f)

    fig1 = DATA / "fig1_prisma.png"
    fig2 = DATA / "fig2_win_rates.png"
    fig3 = DATA / "fig3_forest_effects.png"
    fig4 = DATA / "fig4_decision_workflow.png"
    render_prisma_png(st, fig1)
    render_winrates_png(st, fig2)
    render_forest_png(st, fig3)
    render_decision_png(fig4)

    fig_map = {
        "S_ID": fig1,
        "FIG2_BAR": fig2,
        "FIG3_FOREST": fig3,
        "D0": fig4,
    }

    f_docx = DELIV / "Deliverable_F_Final_Review_Manuscript.docx"
    g_docx = DELIV / "Deliverable_G_Evidence_and_Reproducibility_Appendix.docx"
    h_docx = DELIV / "Deliverable_H_Oral_Defense_and_Submission_Pack.docx"

    convert_markdown_to_docx(
        DELIV / "Deliverable_F_Final_Review_Manuscript.md",
        f_docx,
        "When Do LLM Multi-Agent Systems Outperform Single Agents? — Systematic Review",
        fig_map=fig_map,
    )
    convert_markdown_to_docx(
        DELIV / "Deliverable_G_Evidence_and_Reproducibility_Appendix.md",
        g_docx,
        "Online Supplement & Reproducibility Appendix (Deliverable G)",
    )
    convert_markdown_to_docx(
        DELIV / "Deliverable_H_Oral_Defense_and_Submission_Pack.md",
        h_docx,
        "Submission Cover Letters, Checklists & Oral Defense Guide (Deliverable H)",
    )

    verify_docx(f_docx, min_tables=18, check_refs=True, expected_figs=4, total_refs=cm["total"])
    verify_docx(g_docx, min_tables=5, check_refs=False)
    verify_docx(h_docx, min_tables=0, check_refs=False)
    print("DOCX EXPORT & VERIFICATION COMPLETE")


if __name__ == "__main__":
    main()
