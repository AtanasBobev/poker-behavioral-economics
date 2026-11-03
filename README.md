# Dynamic Risk Preferences, Loss Chasing, and Asymmetric Stopping in Repeated Financial Gambles: Field Evidence from High-Stakes Online Poker

**Author:** Atanas Bobev  
**Affiliation:** Department of Economics, American University in Bulgaria  
**Contact:** `amb230@aubg.edu`  
**Working Paper / Replication Repository**

---

## Abstract

We investigate dynamic risk preferences, within-session wealth reference points, and asymmetric stopping rules using a census of 4,070,556 hand-level decisions across 119,584 completed sessions from the University of Alberta Computer Poker Research Group database. Exploiting continuous hand-by-hand bankroll tracking, we test how cumulative intra-session gains and losses alter voluntary risk-taking and session termination. Controlling for player fixed effects, table stakes, position, and time-on-task fatigue, we find evidence of a dual behavioral regime. In the gain domain, players exhibit a significant House Money Effect: accumulating prior profits increases voluntary pot entry (VPIP, $+0.57$ percentage points, $p < 0.001$) and preflop raising ($+0.26$ percentage points, $p = 0.004$). In the loss domain, moderate losses induce risk aversion, whereas deepening cumulative losses trigger severe loss-chasing: continuous bet-to-stack ratios escalate sharply with loss magnitude ($t = 18.99, p < 10^{-79}$). Examining session quitting decisions, we document an acute "never quit on a win" asymmetry: the per-hand termination hazard is only 0.36% immediately following a winning hand, compared to 2.48% after a loss and 5.02% following voluntary folds. Furthermore, 1,340 sessions terminate at exact zero net profit/loss, reflecting sharp cognitive bunching at the break-even reference point. Sunk-cost escalation systematically distorts participation, as players prolong losing sessions in attempts to claw back deficits. Our findings provide natural field evidence bridging prospect theory, dynamic labor supply, and self-regulation failures in repeated financial gambles.

---

## Empirical Findings Summary

| Phenomenon | Empirical Metric | Econometric Estimate | Statistical Significance |
| :--- | :--- | :--- | :--- |
| **House Money (VPIP)** | Voluntary Pot Entry in Gain Domain | $+0.572$ pp | $t = 4.05, p = 5.07 \times 10^{-5}$ |
| **House Money (PFR)** | Preflop Raise in Gain Domain | $+0.262$ pp | $t = 2.91, p = 3.63 \times 10^{-3}$ |
| **Loss Chasing** | Bet / Stack Ratio with Loss Magnitude | $+0.00488$ per 100 chips | $t = 18.99, p = 1.98 \times 10^{-80}$ |
| **Break-Even Bunching** | Sessions Ending at Exact $W = 0$ | $1,340$ sessions ($\hat{b} = +0.284$) | $p < 0.001$ |
| **"Never Quit on Win"** | Exit Hazard after Win vs. Loss | $0.36\%$ vs. $2.48\%$ | $\chi^2 = 14,210, p < 10^{-300}$ |

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
│   ├── 01_house_money_panel.py        # Player fixed-effects panel regressions
│   ├── 02_bunching_hazard_stopping.py # McCrary bunching and discrete-time hazard models
│   ├── 03_summary_statistics.py       # Table 1 descriptive statistics generator
│   ├── generate_figures.py            # Publication vector & PNG figure generator
│   ├── build_paper_docx.py            # Formatted Word manuscript compiler
│   └── build_paper_pdf.py             # Headless Chromium PDF compiler
├── figures/                           # High-Resolution Publication Figures
│   ├── fig1_house_money_curve.png     # House money curve & loss-chasing kink
│   ├── fig2_breakeven_bunching.png    # Terminal wealth density bunching at W=0
│   ├── fig3_stopping_hazard.png       # Discrete-time termination hazard rate
│   └── fig4_duration_escalation.png   # Asymmetric duration distribution
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
# Run Player Fixed Effects regressions (Table 2)
python analysis/01_house_money_panel.py

# Run Bunching and Hazard Survival models (Table 3 & Table 4)
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
- Billings, D., Davidson, A., Schaeffer, J., & Szafron, D. (2002). The challenge of poker. *Artificial Intelligence*, 134(1–2), 201–240.
- Database access: [https://poker.cs.ualberta.ca/irc_poker_database.html](https://poker.cs.ualberta.ca/irc_poker_database.html)

---

## License

MIT License. Copyright (c) 2026 Atanas Bobev.
