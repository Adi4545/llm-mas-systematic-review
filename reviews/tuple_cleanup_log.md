# Comparison Cleaning, Split & Re-Coding Log (`Protocol v1.4`)

**Date:** 2026-11-20  
**Final Reconciled Comparative Pool:** **`34` comparative studies across `87` cleaned paired comparisons** (`+ 25` non-comparative diagnostic, security, and validity-audit studies = **`59` included studies**).

Every comparison included in synthesis Tables 8–12 tests one multi-agent system ($N \ge 2$ collaborating LLMs or heterogeneous multi-LLM ensemble) against a single-agent baseline ($N = 1$), with double-counted summaries, invalid non-SAS comparators, and pure single-model voting benchmarks reconciled as itemized below:

## 1. Invalid, Non-SAS, Nested, & Redundant Rows Removed or Collapsed (`10` Items)

| Item # | Study | Benchmark / Slice | Action Taken | Rationale |
| :---: | :--- | :--- | :--- | :--- |
| `1` | `SR015` (*GPTSwarm*) | Mini Crosswords (GPT-3.5-Turbo) | **Removed (`-1`)** | Optimized graph compared against unoptimized MAS graph rather than a single agent (`N=1`). |
| `2` | `SR015` (*GPTSwarm*) | HumanEval (Node-opt ReAct vs. Initial ReAct) | **Removed (`-1`)** | Single-agent node optimization vs. single-agent baseline (`N=1` vs. `N=1`). |
| `3` | `SR007` (*Zhang et al.*) | 9 benchmarks x heterogeneous model pairings | **Removed (`-1`)** | Compares Heter-MAD vs. Homog-MAD (`+6.4%` / `+8.2%`), not MAS vs. SAS (preserved in diagnostic text). |
| `4` | `SR014` (*MacNet*) | 4-Benchmark Average (Table 1) | **Removed (`-1`)** | Macro-average duplicating the 4 individual benchmark rows (`MMLU`, `HumanEval`, `SRDD`, `CommonGen-Hard`). |
| `5`–`6` | `SR002` (*Tran & Kiela*) | Nested `1,000`-token & `5,000`-token sub-slices | **Collapsed & Re-Split (`-2 -> +2`)** | Merged nested token sub-slices into two non-overlapping strata: `>=500-token` matched budgets (`MAS < SAS`) vs. `100-token / injected context-rot` (`Mixed`). |
| `7` | `SR020` (*CascadeDebate*) | 5-benchmark suite peak aggregate | **Removed (`-1`)** | Composite peak overlapping MedQA and mixing single-model cascades with standalone MAS. |
| `8` | `SR087` (*Debate or Vote*) | 6 secondary `MAD(T=2)` vs `N=1` weak-prompt rows | **Collapsed (`-6 -> +3`)** | Retained primary Majority Vote (`N=5, T=0`), Arithmetics, and multi-round sweep so one paper cannot inflate unweighted counts. |
| `9`–`10` | `SR094` (*Optima*) | 2 duplicate HotpotQA weak-CoT rows | **Removed (`-2`)** | Kept cleanly the 6 `SC(n=8)` parity pairings (3 RL/DPO-trained Optima wins vs. 3 unoptimized MAD losses). |

## 2. Granularity Expansions, Model Disaggregations, & Boundary Re-Codings (`16` Items)

| Item # | Study | Change Made | Resulting Rows in Final Dataset | Rationale |
| :---: | :--- | :--- | :---: | :--- |
| `11` | `SR001` (*Kim et al.*, NMI '26) | Expanded coarse 3-row summary to cover all 6 evaluated suites | **5 rows** | Added `WorkBench` and `SWE-bench Verified & Terminal-Bench` alongside `Finance-Agent`, `BrowseComp-Plus`, and `PlanCraft` (all 4 MAS topologies). |
| `12` | `SR004` (*Nguyen et al.*) | Split by single-agent comparator type | **2 rows** | Separated `MAD vs. Self-Consistency` (`MAS < SAS`, `93%` of `980` settings) from `MAD vs. 1-Pass Long-CoT` (`Mixed`, Table 17). |
| `13` | `SR003` (*OneFlow*) & `SR009` (*Denisov-Blanch et al.*) | Re-coded `Tier 1 -> Tier 2` (`SR003` -> `Tier 2B`, `SR009` -> `Tier 2A`) | **1 row each (`Tier 2`)** | *OneFlow* uses shared KV-cache prefix reuse + unamortized MCTS (`C6`); *Denisov-Blanch et al.* runs `25x` polling calls against `1x` solo baseline. |
| `14` | `SR089` (*Bertalanič & Fortuna*, CAIS '26) | Expanded from 1 model (`Ministral-3-8B` `-27.6 pp`) to all 3 GSM-Hard models | **3 rows (`+2`)** | Reports primary `Qwen2.5-7B` (`n=1,017`, `-2.2 pp`), `Llama-3.1-8B` (`n=100`, `-1.7 pp`), and `Ministral-3-8B` (`n=100`, `-27.6 pp`) with exact `N` and binomial SEs. |
| `15` | `SR085` (*More Agents Is All You Need* / *Agent Forest*) | Re-coded from `Tier 3` comparative MAS (`15` rows) to `RQ4` `C3` validity benchmark (`0` comparative rows) | **0 comparative rows (`-15`)** | Enforces Section 3.4 definition: single-LLM repeated sampling + voting (`N=1` model, no inter-agent dialogue) is single-agent test-time scaling, not a multi-agent team. |
| `16` | `SR023`, `SR025`, `SR097`, `SR100` | Removed non-comparative `C6` cost flags | **`12/12` comparative optimizers flagged `C6`** | Non-comparative fault-localization / defense tools make no comparative MAS-vs-SAS runtime cost claim (`QA3 = 2`). |
