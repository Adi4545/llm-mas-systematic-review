# LLM Multi-Agent Systems vs. Single-Agent Baselines: A Systematic Review

[![Audit Status](https://img.shields.io/badge/Audit%20Checks-15%2F15%20Passed-brightgreen)](scripts/verify_audit.py)
[![PRISMA 2020](https://img.shields.io/badge/PRISMA-2020%20Compliant-blue)](data/fig1_prisma.png)
[![Protocol](https://img.shields.io/badge/Protocol-v1.4-orange)](deliverables/Deliverable_C_Systematic_Review_Protocol.md)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An exhaustive, audit-verified systematic literature review evaluating the empirical performance, cost dynamics, latency scaling, and error topology of **LLM Multi-Agent Systems (MAS)** relative to rigorously tuned **Single-Agent Baselines** across 59 peer-reviewed and pre-print studies (34 comparative studies with 87 matched experimental pairs).

Conducted under **PRISMA 2020** guidelines and **Open Science Framework (OSF)** registration protocol standards (Protocol v1.4).

---

## 📌 Key Findings at a Glance

* **Overall Empirical Win-Rate:** Multi-agent architectures outperform single-agent baselines in **63.2%** (55/87) of head-to-head task evaluations (95% Wilson CI: [52.8%, 72.6%]).
* **Task-Family Disparities:**
  - **Code Generation & Software Engineering:** Multi-agent systems exhibit their strongest performance advantage (**72.4%** win-rate, 21/29 comparisons, Wilson CI: [54.3%, 85.3%]).
  - **Reasoning & Planning:** Moderate advantage (**60.0%** win-rate, 18/30 comparisons, Wilson CI: [42.3%, 75.4%]).
  - **Open-Ended Dialogue & Creative Generation:** Highly parity-dominated / ambiguous advantage (**57.1%** win-rate, 16/28 comparisons, Wilson CI: [39.1%, 73.5%]).
* **Resource & Cost Overhead:**
  - **Token Consumption Multiplier:** Multi-agent systems consume between **3.2× to 15.8×** more tokens than matched single-agent baselines (median token multiplier: **4.6×**).
  - **End-to-End Latency Overhead:** Multi-agent orchestration incurs a **2.8× to 8.4×** latency increase due to sequential inter-agent message exchanges and round-robin validation loops.
* **Failure Modes & Cascades:** Cascading hallucinations, infinite conversational loops, and majority-voting groupthink account for over **68%** of multi-agent execution failures on complex reasoning tasks.

---

## 📁 Repository Structure

```
├── README.md                                  # Repository overview and reproduction guide
├── LICENSE                                    # MIT License
├── deliverables/                              # Final submission deliverables & manuscripts
│   ├── Deliverable_A_Journal_Intelligence_Report.md
│   ├── Deliverable_B_Topic_and_Novelty_Report.md
│   ├── Deliverable_C_Systematic_Review_Protocol.md
│   ├── Deliverable_D_Literature_Evidence_Register.md
│   ├── Deliverable_E_Critical_Synthesis_Report.md
│   ├── Deliverable_F_Final_Review_Manuscript.md     # Full Journal Manuscript (v4 Final)
│   ├── Deliverable_F_Final_Review_Manuscript.docx   # Submission-ready Word format
│   ├── Deliverable_G_Evidence_and_Reproducibility_Appendix.md
│   ├── Deliverable_G_Evidence_and_Reproducibility_Appendix.docx
│   ├── Deliverable_H_Oral_Defense_and_Submission_Pack.md
│   └── Deliverable_H_Oral_Defense_and_Submission_Pack.docx
├── data/                                      # Complete empirical datasets, PRISMA logs, and figures
│   ├── bibliography.bib                       # 121 verified reference citations in BibTeX
│   ├── cite_map.json                          # Citation keys mapped to numbered indices [1]-[121]
│   ├── evidence_matrix.json                   # Detailed extraction of all 59 included studies
│   ├── included_studies.csv                   # Tabular list of 59 included studies & metadata
│   ├── screening_records.csv                  # PRISMA dual-screener inclusion/exclusion logs
│   ├── quality_appraisal.csv                  # Newcastle-Ottawa / CASP quality scores
│   ├── search_log.json                        # Query string strings, date ranges, hit counts
│   ├── verified_stats.json                    # Exact statistical figures & confidence intervals
│   ├── fig1_prisma.png                        # PRISMA flow diagram (300 DPI)
│   ├── fig2_win_rates.png                     # Task-family win rates with Wilson 95% CIs (300 DPI)
│   ├── fig3_forest_effects.png                # Forest plot of performance deltas (300 DPI)
│   └── fig4_decision_workflow.png             # Architecture selection decision flowchart (300 DPI)
├── scripts/                                   # Audit and data-processing pipelines
│   ├── verify_audit.py                        # 15-point automated data integrity audit script
│   ├── compute_stats.py                       # Statistical calculation engine (Wilson CIs, p-values)
│   ├── build_manuscript_v4.py                 # Manuscript generator incorporating referee remediations
│   ├── build_deliverables_deg.py              # Deliverables D, E, G build pipeline
│   └── export_docx.py                         # Pandoc/docx conversion utility
├── reviews/                                   # Referee peer review rounds & rebuttal packages
│   ├── external_referee_response.md           # Formal Round-1 and Round-2 referee response letter
│   ├── manuscript_v4_final.md                 # Certified final manuscript text
│   └── reviewer_response_matrix.md            # Point-by-point reviewer comment resolution matrix
├── phase_logs/                                # Verification gates for Phases 1 through 10
└── agents/                                    # Specialized autonomous research agent extraction records
```

---

## 🛠 Reproduction & Verification

To verify that all numbers, statistics, table rows, and citations in the manuscripts and deliverables match the source data with 100% mathematical precision:

```bash
# Clone the repository
git clone https://github.com/Adi4545/llm-mas-systematic-review.git
cd llm-mas-systematic-review

# Run the 15-point automated verification audit
python3 scripts/verify_audit.py
```

### Expected Output:
```json
{
  "status": "ALL AUDIT CHECKS PASSED",
  "passed": "15/15",
  "checks": {
    "studies_count": "PASS (59 == 59)",
    "comparative_count": "PASS (34 == 34)",
    "comparisons_count": "PASS (87 == 87)",
    "total_citations": "PASS (121 == 121)",
    "win_rate_math": "PASS (63.2% == 55/87)",
    "task_family_sums": "PASS (29 + 30 + 28 == 87; 21 + 18 + 16 == 55)",
    "manuscript_stats_alignment": "PASS (all 14 tested numbers match exactly)",
    "referee_claims_alignment": "PASS",
    "bibtex_keys_present": "PASS (all 121 cite_map keys in bibliography.bib)",
    "quality_appraisal_sync": "PASS (59 rows match 59 studies)",
    "screening_records_sync": "PASS (matches PRISMA flow totals)",
    "docx_deliverables_present": "PASS (Deliverables F, G, H docx exist)",
    "figures_present": "PASS (fig1, fig2, fig3, fig4 exist and valid)",
    "evidence_matrix_integrity": "PASS (59 valid schema records)",
    "zero_broken_citation_tags": "PASS (no unresolved placeholders found)"
  }
}
```

---

## 📊 Deliverables Summary

| Deliverable | Format | Description |
|---|---|---|
| **Deliverable F** | `.md`, `.docx` | **Full Systematic Review Manuscript** formatted for IEEE/ACM / Elsevier standards. |
| **Deliverable G** | `.md`, `.docx` | **Evidence & Reproducibility Appendix**, including raw extraction tables, quality appraisals, and prompt definitions. |
| **Deliverable H** | `.md`, `.docx` | **Oral Defense & Submission Pack**, with executive slide deck outlines, examiner Q&A defense briefs, and rebuttal scripts. |
| **Deliverables A–E** | `.md` | Journal intelligence, topic novelty reports, OSF protocol specification, and literature evidence registers. |

---

## 📜 Citation

```bibtex
@article{sharma2026systematic,
  title={When Do Multiple Agents Outperform One? A Systematic Review and Meta-Analysis of LLM Multi-Agent Systems vs. Single-Agent Baselines},
  author={Sharma, Aditya and Contributors},
  journal={Systematic Literature Review Repository},
  year={2026},
  url={https://github.com/Adi4545/llm-mas-systematic-review}
}
```

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
