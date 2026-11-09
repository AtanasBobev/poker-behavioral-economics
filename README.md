# Dynamic Risk Preferences, Loss Chasing, and Reference-Dependent Stopping in Repeated Contests: Field Evidence from Online Poker

This repository contains the replication code, high-throughput TypeScript streaming pipeline, econometric estimation suite, and working paper manuscript for the empirical study on dynamic risk preferences, the house money effect, and reference-dependent stopping rules in online poker.

* **Working Paper:** [paper/Dynamic_Risk_Preferences_Poker_Economics.pdf](paper/Dynamic_Risk_Preferences_Poker_Economics.pdf)
* **Author:** Atanas Bobev
* **JEL Classification:** D81, D91, C93, G41

---

## Abstract

We examine how dynamic within-session wealth fluctuations alter risk-taking and session termination decisions in repeated contests. Analyzing 4,070,556 hand-level decisions across 119,584 completed sessions from the University of Alberta Computer Poker Research Group archive (1995-1997), we exploit continuous bankroll tracking within an environment where objective probabilities are governed by invariant combinatorial rules. Controlling for player fixed effects, table stakes, position, and time-on-task, we identify two distinct behavioral regimes. In the gain domain, competitors exhibit a house money effect: accumulated profits increase voluntary pot entry (VPIP, +0.59 percentage points, p < 0.001), preflop raising (+0.27 percentage points, p = 0.003), and absolute wager sizes (+0.57 chips per 100 chips gained, p < 0.001). In the loss domain, increasing cumulative deficits trigger systematic loss chasing: holding current stack size constant, each 100 chips of deficit increases absolute bet sizes by +0.99 chips (p < 0.001) and escalates the bet-to-stack ratio (t = 15.52, p < 10^-50). At the session level, termination choices exhibit sharp reference dependence. Players display an acute "never quit on a win" asymmetry: the per-hand exit hazard is 0.36% immediately following a winning hand, compared to 2.48% after a loss and 5.02% after uncontested folds. Furthermore, 1,340 sessions terminate at exact net break-even (W = 0), with active round-trip clawbacks accounting for 54.9% of these exits. While capital constraints truncate losing sessions on average, surviving losing sessions display pronounced right-tail persistence, consistent with selective sunk-cost chasing. Our results provide empirical support for dynamic mental accounting and dual-account prospect theory.

We document five empirical findings:
1. **The House Money Effect:** In the gain domain, accumulating prior profits increases voluntary pot entry (VPIP, +0.59 percentage points, t = 4.16, p < 0.0001), preflop aggressive raising (+0.27 percentage points, t = 2.99, p = 0.0028), and absolute wager sizes (+0.57 chips per 100 chips won, t = 5.25, p < 0.0001) under within-player fixed effects.
2. **Loss Chasing Escalation:** In the loss domain, increasing cumulative deficits trigger systematic risk escalation: holding current stack size constant, each 100 chips of deficit increases absolute bet sizes by +0.99 chips (t = 6.58, p < 0.0001) and escalates the bet-to-stack ratio (t = 15.52, p < 10^-50).
3. **The "Never Quit on a Win" Asymmetry:** Examining 4,070,556 hand decisions reveals that the per-hand termination hazard is only 0.36% immediately following a winning hand, compared to 2.48% after a loss and 5.02% after uncontested folds (chi2 = 14,210, p < 10^-300).
4. **Break-Even Reference Point Bunching:** A total of 1,340 completed sessions terminate at exact net break-even (W = 0). Active round-trip clawbacks (recovering from deficits back to zero and immediately stopping) account for 54.9% of these exits, exhibiting an excess mass ratio of b = +0.284 (p < 0.001).
5. **Session Duration and Sunk-Cost Persistence:** While capital constraints and buy-in bust-outs truncate losing sessions on average (30.2 hands vs 37.8 hands for winning sessions), surviving losing sessions display a pronounced right-tail persistence, reflecting selective sunk-cost chasing among trailing competitors.

---

## Empirical Findings Summary

| Question | Mechanism | Sample Size | Primary Estimate | Standard Error | Test Statistic | p-value |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| Q1: House Money (VPIP) | In Gain Domain 1(W > 0) | 3,999,153 | beta = +0.0059 | 0.0014 | t = 4.16 | < 0.0001 |
| Q1: House Money (PFR) | In Gain Domain 1(W > 0) | 3,999,153 | beta = +0.0027 | 0.0009 | t = 2.99 | 0.0028 |
| Q1: House Money (Stakes) | Gain Magnitude W+ / 100 | 3,999,153 | beta = +0.5712 | 0.1088 | t = 5.25 | < 0.0001 |
| Q2: Loss Chasing (Stakes) | Loss Magnitude W- / 100 | 3,999,153 | beta = +0.9896 | 0.1505 | t = 6.58 | < 0.0001 |
| Q2: Loss Chasing (Relative) | Bet / Stack Ratio (Log Stack ctrl) | 3,999,153 | beta = +0.0035 | 0.0002 | t = 15.52 | < 10^-50 |
| Q3: Break-Even Bunching | Exact W = 0 Terminal Mass | 119,584 | excess mass b = +0.284 | - | Polynomial CF | < 0.001 |
| Q3: Active Clawbacks | Deficit Recovery Exits | 1,340 | share = 54.85% | - | Exact Binomial | < 10^-300 |
| Q4: Quitting Asymmetry | Exit Hazard: Win vs Loss | 2,674,468 | 0.36% vs 2.48% | - | Chi-square | < 10^-300 |

---

## Repository Structure

```text
├── analysis/                              # Python econometric replication scripts
│   ├── run_robust_regressions.py          # Player FE panel regressions with log stack controls
│   ├── 01_house_money_panel.py            # Baseline panel regressions (VPIP, PFR, Aggression)
│   ├── 02_bunching_hazard_stopping.py     # McCrary density bunching and discrete-time hazard models
│   ├── 03_summary_statistics.py           # Descriptive statistics generator (Table 1)
│   ├── audit_referee_concerns.py          # Micro-level audit of clawbacks, givebacks, and bust-outs
│   ├── generate_figures.py                # Script to reproduce publication figures
│   ├── build_paper_docx.py                # Formatted Word manuscript compiler
│   └── build_paper_pdf.py                 # Headless Chromium PDF compiler
├── figures/                               # High-resolution (300 DPI) publication figures
│   ├── fig1_house_money_curve.png         # House money curve & absolute wager sizing
│   ├── fig2_breakeven_bunching.png        # Terminal wealth density bunching at W = 0
│   ├── fig3_stopping_hazard.png           # Discrete-time termination hazard rate
│   └── fig4_duration_escalation.png       # Duration CDF and session length distributions
├── paper/                                 # Working paper manuscript and compiled PDF
│   ├── Dynamic_Risk_Preferences_Poker_Economics.pdf
│   ├── Dynamic_Risk_Preferences_Poker_Economics.docx
│   └── manuscript.md
├── src/                                   # High-throughput TypeScript streaming engine
│   ├── irc-parser.ts                      # Space-delimited pdb parser and action tokenizer
│   ├── session-tracker.ts                 # Session reconstruction and running bankroll manager
│   ├── stream-pipeline.ts                 # In-stream pipeline coupled to compressed archives
│   ├── types.ts                           # TypeScript interfaces and econometric data models
│   └── index.ts                           # CLI pipeline entry point
├── package.json                           # Node.js and TypeScript project dependencies
├── tsconfig.json                          # TypeScript compiler configuration
└── README.md
```

---

## Prerequisites and Installation

### 1. TypeScript Streaming Pipeline

Requires Node.js (>= v18.0.0).

```bash
# Clone the repository
git clone https://github.com/AtanasBobev/poker-behavioral-economics.git
cd poker-behavioral-economics

# Install dependencies and build TypeScript
npm install
npm run build
```

### 2. Python Econometric Environment

Requires Python (>= 3.9) with standard scientific libraries:

```bash
pip install pandas numpy scipy statsmodels matplotlib python-docx
```

---

## Data Pipeline and Replication

### Streaming Raw CPRG IRC Dumps

The pipeline processes compressed monthly archives from the [University of Alberta Computer Poker Research Group](https://poker.cs.ualberta.ca/irc_poker_database.html):

```bash
# Compile TypeScript to dist/
npm run build

# Run pipeline over uncompressed/extracted directory
node dist/index.js
```

The pipeline outputs structured CSV datasets:
1. `data/q2_house_money_risk.csv`: Hand-level observations with running bankroll, gain/loss domains, and betting choices.
2. `data/q4_session_stopping.csv`: Completed session records with initial/final stacks, durations, and break-even indicators.
3. `data/q4_hazard_panel.csv`: Discrete-time survival panel tracking termination opportunities per hand.

### Running Econometric Estimations

To reproduce the regression tables and statistical tests reported in the paper:

```bash
# Table 2: Player Fixed Effects regressions with log stack controls
python analysis/run_robust_regressions.py

# Table 3 & Table 4: Bunching estimation and discrete-time hazard survival models
python analysis/02_bunching_hazard_stopping.py

# Table 1: Summary statistics of hand decisions and completed sessions
python analysis/03_summary_statistics.py

# Figures 1-4: Generate high-resolution publication figures
python analysis/generate_figures.py

# Recompile Word (.docx) and PDF manuscripts
python analysis/build_paper_docx.py
python analysis/build_paper_pdf.py
```

---

## Citation

```bibtex
@article{bobev2026dynamicpoker,
  title={Dynamic Risk Preferences, Loss Chasing, and Reference-Dependent Stopping in Repeated Contests: Field Evidence from Online Poker},
  author={Bobev, Atanas},
  journal={Working Paper Series},
  year={2026}
}
```

---

## License

* Code: [MIT License](LICENSE)
* Working Paper: Creative Commons Attribution 4.0 International (CC BY 4.0)
