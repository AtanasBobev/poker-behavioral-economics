# Dynamic Risk Preferences, Loss Chasing, and Reference-Dependent Stopping in Repeated Contests: Field Evidence from Online Poker

**Author:** Atanas Bobev  
**Working Paper / Replication Repository**

---

## Abstract

We examine how dynamic within-session wealth fluctuations alter risk-taking and session termination decisions in repeated contests. Analyzing 4,070,556 hand-level decisions across 119,584 completed sessions from the University of Alberta Computer Poker Research Group archive (1995-1997), we exploit continuous bankroll tracking within an environment where objective probabilities are governed by invariant combinatorial rules. Controlling for player fixed effects, table stakes, position, and time-on-task, we identify two distinct behavioral regimes. In the gain domain, competitors exhibit a house money effect: accumulated profits increase voluntary pot entry (VPIP, $+0.59$ percentage points, $p < 0.001$), preflop raising ($+0.27$ percentage points, $p = 0.003$), and absolute wager sizes ($+0.57$ chips per 100 chips gained, $p < 0.001$). In the loss domain, increasing cumulative deficits trigger systematic loss chasing: holding current stack size constant, each 100 chips of deficit increases absolute bet sizes by $+0.99$ chips ($p < 0.001$) and escalates the bet-to-stack ratio ($t = 15.52, p < 10^{-50}$). At the session level, termination choices exhibit sharp reference dependence. Players display an acute "never quit on a win" asymmetry: the per-hand exit hazard is 0.36% immediately following a winning hand, compared to 2.48% after a loss and 5.02% after uncontested folds. Furthermore, 1,340 sessions terminate at exact net break-even ($W = 0$), with active round-trip clawbacks accounting for 54.9% of these exits. While capital constraints truncate losing sessions on average, surviving losing sessions display pronounced right-tail persistence, consistent with selective sunk-cost chasing. Our results provide empirical support for dynamic mental accounting and dual-account prospect theory.

---

## Empirical Findings Summary

| Phenomenon | Empirical Metric | Econometric Estimate | Statistical Significance |
| :--- | :--- | :--- | :--- |
| **House Money (VPIP)** | Voluntary Pot Entry in Gain Domain | $+0.587$ pp | $t = 4.16, p = 3.25 \times 10^{-5}$ |
| **House Money (PFR)** | Preflop Raise in Gain Domain | $+0.269$ pp | $t = 2.99, p = 2.81 \times 10^{-3}$ |
| **House Money (Stakes)** | Absolute Bet Sizing with Gain Magnitude | $+0.571$ chips / 100 chips | $t = 5.25, p = 1.53 \times 10^{-7}$ |
| **Loss Chasing (Stakes)** | Absolute Bet Sizing with Loss Magnitude | $+0.990$ chips / 100 chips | $t = 6.58, p = 4.79 \times 10^{-11}$ |
| **Loss Chasing (Relative)** | Bet / Stack Ratio (controlling for $\ln(\text{Stack})$) | $+0.00352$ / 100 chips | $t = 15.52, p = 2.65 \times 10^{-54}$ |
| **Break-Even Bunching** | Sessions Ending at Exact $W = 0$ | $1,340$ sessions ($\hat{b} = +0.284$) | $p < 0.001$ |
| **Active Clawbacks** | Quits after Recovering from Deficit to 0 | $735$ sessions ($54.9\%$ of $W=0$) | $p < 0.001$ |
| **"Never Quit on Win"** | Exit Hazard after Win vs. Loss vs. Fold | $0.36\%$ vs. $2.48\%$ vs. $5.02\%$ | $\chi^2 = 14,210, p < 10^{-300}$ |

---

## Repository Structure

```
poker-behavioral-economics/
├── src/                               # TypeScript Data Pipeline
│   ├── types.ts                       # Domain models and econometric interfaces
│   ├── irc-parser.ts                  # High-performance parser for CPRG pdb format
│   ├── session-tracker.ts             # Session reconstruction and running bankroll
│   ├── stream-pipeline.ts             # In-stream dataset generator
│   └── index.ts                       # CLI pipeline entry point
├── analysis/                          # Econometric & Statistical Suite
│   ├── run_robust_regressions.py      # Player FE panel regressions with stack controls
│   ├── 01_house_money_panel.py        # Baseline panel regressions
│   ├── 02_bunching_hazard_stopping.py # McCrary bunching and discrete-time hazard models
│   ├── 03_summary_statistics.py       # Table 1 descriptive statistics generator
│   ├── audit_referee_concerns.py      # Micro-level audit of clawbacks and bust-outs
│   ├── generate_figures.py            # Publication vector & PNG figure generator
│   ├── build_paper_docx.py            # Formatted Word manuscript compiler
│   └── build_paper_pdf.py             # Headless Chromium PDF compiler
├── figures/                           # High-Resolution Publication Figures
│   ├── fig1_house_money_curve.png     # House money curve & absolute bet sizing
│   ├── fig2_breakeven_bunching.png    # Terminal wealth density bunching at W=0
│   ├── fig3_stopping_hazard.png       # Discrete-time termination hazard rate
│   └── fig4_duration_escalation.png   # Duration CDF and length distributions
├── paper/                             # Manuscript Artifacts
│   ├── manuscript.md                  # Complete academic text
│   ├── Dynamic_Risk_Preferences_Poker_Economics.docx
│   └── Dynamic_Risk_Preferences_Poker_Economics.pdf
├── package.json                       # Node.js / TypeScript configuration
├── tsconfig.json                      # Strict TypeScript compiler options
├── LICENSE                            # MIT License
└── README.md                          # Documentation and replication guide
```

---

## Replication Guide

### 1. Requirements
- Node.js (v18+)
- Python (v3.10+)
- Python libraries: `pandas`, `numpy`, `statsmodels`, `scipy`, `matplotlib`, `python-docx`

### 2. TypeScript Pipeline Compilation
```bash
npm install
npm run build
npm run typecheck
```

### 3. Econometric Estimation & Figure Generation
To replicate the regression tables and figures:
```bash
# Run Player Fixed Effects regressions with stack controls (Table 2)
python analysis/run_robust_regressions.py

# Run Bunching and Hazard Survival models (Table 3)
python analysis/02_bunching_hazard_stopping.py

# Generate publication figures (Figures 1-4)
python analysis/generate_figures.py

# Recompile Word and PDF manuscripts
python analysis/build_paper_docx.py
python analysis/build_paper_pdf.py
```

---

## Data Source

Data is sourced from the Computer Poker Research Group at the University of Alberta:
- Billings, D., Davidson, A., Schaeffer, J., & Szafron, D. (2002). The challenge of poker. *Artificial Intelligence*, 134(1-2), 201-240.
- Database access: [https://poker.cs.ualberta.ca/irc_poker_database.html](https://poker.cs.ualberta.ca/irc_poker_database.html)

---

## License

MIT License. Copyright (c) 2026 Atanas Bobev.
