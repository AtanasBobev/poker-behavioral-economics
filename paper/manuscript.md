# Dynamic Risk Preferences, Loss Chasing, and Reference-Dependent Stopping in Repeated Contests: Field Evidence from Online Poker

**Atanas Bobev**

---

### Abstract
We examine how dynamic within-session wealth fluctuations alter risk-taking and session termination decisions in repeated contests. Analyzing 4,070,556 hand-level decisions across 119,584 completed sessions from the University of Alberta Computer Poker Research Group archive (1995-1997), we exploit continuous bankroll tracking within an environment where objective probabilities are governed by invariant combinatorial rules. Controlling for player fixed effects, table stakes, position, and time-on-task, we identify two distinct behavioral regimes. In the gain domain, competitors exhibit a house money effect: accumulated profits increase voluntary pot entry (VPIP, $+0.59$ percentage points, $p < 0.001$), preflop raising ($+0.27$ percentage points, $p = 0.003$), and absolute wager sizes ($+0.57$ chips per 100 chips gained, $p < 0.001$). In the loss domain, increasing cumulative deficits trigger systematic loss chasing: holding current stack size constant, each 100 chips of deficit increases absolute bet sizes by $+0.99$ chips ($p < 0.001$) and escalates the bet-to-stack ratio ($t = 15.52, p < 10^{-50}$). At the session level, termination choices exhibit sharp reference dependence. Players display an acute "never quit on a win" asymmetry: the per-hand exit hazard is 0.36% immediately following a winning hand, compared to 2.48% after a loss and 5.02% after uncontested folds. Furthermore, 1,340 sessions terminate at exact net break-even ($W = 0$), with active round-trip clawbacks accounting for 54.9% of these exits. While capital constraints truncate losing sessions on average, surviving losing sessions display pronounced right-tail persistence, consistent with selective sunk-cost chasing. Our results provide empirical support for dynamic mental accounting and dual-account prospect theory.

**Keywords:** Reference-dependent preferences, House money effect, Loss chasing, Stopping rules, Dynamic labor supply, Contest theory, Field data.  
**JEL Classifications:** D81, D91, C93, G41.

---

## 1. Introduction

Standard neoclassical expected utility theory posits that risk preferences are defined over final wealth states. For small-to-moderate stakes encountered in daily market transactions, consumption gambles, or repeated contests, plausible utility functions are approximately linear, implying risk-neutral marginal behavior (Rabin, 2000). Contrary to this benchmark, field and laboratory evidence shows that individuals frequently alter their willingness to bear risk based on recent path-dependent outcomes (Thaler and Johnson, 1990; Post et al., 2008; Barberis, 2012).

Two primary behavioral frameworks explain such path dependence. First, under mental accounting (Thaler, 1985; Thaler and Johnson, 1990), individuals segregate recent gains from baseline wealth. Prior earnings are treated as "house money," attenuating the perceived disutility of subsequent losses and encouraging risk-taking. Second, prospect theory (Kahneman and Tversky, 1979) specifies an S-shaped value function characterized by loss aversion ($\lambda > 1$) and convexity in the negative domain. When individuals accumulate paper losses that have not yet been formally realized, diminishing sensitivity can induce risk-seeking gambles aimed at recovering the initial endowment (the break-even effect; Imas, 2016).

Simultaneously, dynamic risk environments require agents to make endogenous *stopping decisions*: deciding when to cease participation. Analogous to daily labor supply choices among independent contractors (Camerer et al., 1997; Farber, 2005, 2008, 2015), repeated contest participants must weigh the marginal utility of continuation against physical or cognitive fatigue. When agents evaluate performance relative to an intra-session reference point-most saliently, breaking even ($W = 0$)-stopping probabilities should exhibit sharp structural discontinuities around the reference threshold.

Testing these theories in field environments involves substantial identification challenges. In financial markets, risk choices are confounded by shifting macroeconomic fundamentals, unobserved beliefs, and endogenous liquidity constraints. In casino or sports betting settings, house edges, opaque bookmaker commissions, and heterogeneous event probabilities complicate the measurement of underlying decision rules.

This paper uses microdata from the Computer Poker Research Group (CPRG) at the University of Alberta (Billings et al., 2002) to examine dynamic risk preferences and stopping behavior. The dataset contains 4,070,556 hand-level decisions across 119,584 continuous playing sessions between April 1995 and March 1997. Online Texas Hold'em provides an ideal institutional environment for behavioral analysis:
1. **Invariant Probability Space:** Cards are drawn from a standard 52-card deck with fixed combinatorial odds. Unlike financial assets, underlying state probabilities do not depend on unobserved macroeconomic parameters.
2. **Granular Micro-Level Tracking:** Every bet, fold, call, and raise is recorded chronologically, along with table position, board cards, and exact chip stacks before and after each hand.
3. **Absence of Rake Distortions:** The historical IRC platform operated with zero transaction fees or house rake, allowing clean observation of strategic and behavioral dynamics without house-edge frictions.

We investigate two primary empirical questions:
1. **Dynamic Risk-Taking Across Wealth States:** Does cumulative intra-session profit ($W_{it}$) induce greater risk-taking via the house money effect, and how do agents respond as cumulative deficits deepen?
2. **Reference-Dependent Stopping Rules:** Do session termination hazards respond asymmetrically to immediate hand outcomes, and do players selectively terminate sessions upon returning to the break-even reference point ($W_{exit} = 0$)?

Our empirical analysis yields four main findings. First, controlling for player fixed effects, table stakes, position, and session fatigue, we observe a robust **house money effect**. Entering the gain domain increases the probability of voluntarily entering the pot (VPIP) by 0.59 percentage points ($p < 0.001$), preflop aggressive raising (PFR) by 0.27 percentage points ($p = 0.003$), and absolute chips wagered by 0.57 chips per 100 chips of profit ($p < 0.001$).

Second, in the loss domain, we document pronounced **loss chasing**. Rather than reducing exposure to preserve capital, players experiencing increasing deficits commit significantly larger wagers. Controlling for the log of current stack size to avoid mechanical denominator artifacts, each 100 chips of cumulative deficit increases absolute bet sizing by $+0.99$ chips ($p < 0.001$) and escalates the bet-to-stack ratio ($\beta = +0.00352, t = 15.52, p < 10^{-50}$).

Third, session quitting decisions exhibit an acute **outcome asymmetry**. The conditional per-hand probability of quitting immediately after a winning hand is 0.36%, compared to 2.48% after a loss and 5.02% following an uncontested fold. Players virtually never leave the contest following a win, indicating that recent success acts as a potent continuation stimulus.

Fourth, we document significant **bunching at the break-even reference point**. Exactly 1,340 sessions terminate at $W_{exit} = 0$. Decomposing these episodes, active clawbacks-sessions where a player was underwater, recovered to zero, and immediately quit-comprise 54.9% (735 sessions) of the total, while active givebacks comprise 14.0% (188 sessions). The average duration of exact break-even sessions is 18.2 hands (20.5 minutes), roughly half the sample average of 37.8 hands, demonstrating that players actively terminate sessions early to lock in break-even outcomes. Finally, while capital constraints truncate losing sessions on average (30.2 hands vs. 37.8 hands for winning sessions), surviving losing sessions exhibit excess right-tail persistence, reflecting selective sunk-cost chasing.

---

## 2. Institutional Setting and Data

### 2.1 The CPRG IRC Poker Environment
The University of Alberta CPRG database archives logs from public Internet Relay Chat (IRC) poker channels (`#holdem`) active between 1995 and 2001 (Billings et al., 2002). The games implemented standard Texas Hold'em rules with automated dealer bots managing the deck, blinds, and pots. 

Stakes followed fixed-limit structures (typically 5/10, 10/20, or 20/40 chips), with predetermined small and big blinds. In each betting round, players could fold, call, or raise up to the table limit. While chips were virtual ("etherbucks"), player bankrolls were persistent across sessions and publicly ranked on an official ladder. Consequently, participants faced non-trivial reputational incentives, finite endowments, and competitive tournament dynamics, closely mirroring laboratory token experiments and online competitive rating systems (e.g., chess or e-sports).

### 2.2 Sample Construction and Session Demarcation
We examine 24 consecutive monthly archives covering April 1995 through March 1997. Player sessions are not explicitly tagged by the IRC server. Following standard empirical practice in the economics of gambling (e.g., Narayanan and Manchanda, 2012), we define a session as an unbroken sequence of hands played by an individual where the elapsed time between consecutive hands does not exceed **20 minutes (1,200 seconds)**. 

We apply three conservative filters:
1. Sessions must contain at least 5 completed hands to eliminate brief network drops.
2. The initial stack must be positive ($W_{i,0} > 0$).
3. To eliminate automated test scripts and outliers, we restrict the panel to hands with index $t \le 400$.

The resulting estimation panel comprises **4,070,556 player-hand observations** across **119,584 completed sessions** and **5,944 unique players**.

### 2.3 Variable Definitions and Descriptive Statistics
For each player $i$ on hand $t$ in session $s$, we record:
- $VPIP_{ist} \in \{0, 1\}$: Voluntary Put Money In Pot, equal to 1 if the player called, bet, or raised preflop, and 0 if they folded (mandatory blinds are excluded unless defended).
- $PFR_{ist} \in \{0, 1\}$: Preflop Raise, equal to 1 if the player initiated or raised preflop.
- $Aggressive_{ist} \in \{0, 1\}$: Equal to 1 if the player bet or raised on any postflop street.
- $BetAmount_{ist}$: Total chips committed by the player during the hand.
- $BetFraction_{ist}$: Ratio of chips wagered to current stack ($BetAmount_{ist} / \text{Stack}_{ist}$).
- $W_{ist} = \text{Stack}_{ist} - W_{i,0}$: Cumulative within-session net profit or loss prior to hand $t$.
- $Quit_{ist} \in \{0, 1\}$: Equal to 1 if hand $t$ was the final hand of session $s$, and 0 otherwise.

Table 1 presents descriptive statistics for the estimation sample.

```
========================================================================================
Table 1: Descriptive Statistics of Hand-Level Decisions and Completed Sessions
========================================================================================
Variable                                Mean        Std. Dev.      Min          Max
----------------------------------------------------------------------------------------
Panel A: Hand-Level Decisions (N = 4,070,556; Players = 5,944)
Voluntary Pot Entry (VPIP)             0.4524        0.4977       0.0000       1.0000
Preflop Raise (PFR)                    0.1135        0.3172       0.0000       1.0000
Postflop Aggression                    0.2628        0.4402       0.0000       1.0000
Total Bet Amount (Chips)              24.3442       37.5192       0.0000    1200.0000
Bet Fraction of Stack                  0.0236        0.0641       0.0000       1.0000
Reached Showdown                       0.2176        0.4126       0.0000       1.0000
Current Stack (Chips)               4434.8160     10966.6900      1.0000  500000.0000
Cumulative Session PnL ($W_{ist}$)    24.7853      376.6639   -23175.0000   13240.0000

Panel B: Completed Sessions (N = 119,584 Completed Sessions)
Session Duration (Minutes)            38.3625       41.0449       1.0000     580.0000
Hands Played per Session              34.0393       43.3057       5.0000     400.0000
Final Session Outcome ($W_{exit}$)     2.6418      382.8946   -23175.0000   13240.0000
Winning Sessions Share                 0.4480        0.4973       0.0000       1.0000
Losing Sessions Share                  0.5408        0.4983       0.0000       1.0000
Exact Break-Even Share ($W=0$)         0.0112        0.1053       0.0000       1.0000
Near Break-Even Share ($|W| \le 10$)   0.0456        0.2085       0.0000       1.0000
========================================================================================
Notes: Data source is the University of Alberta CPRG database (1995-1997). VPIP equals 1 if the player called, bet, or raised preflop. Postflop aggression equals 1 if the player bet or raised on the flop, turn, or river. Session gap cutoff is 20 minutes.
```

---

## 3. Empirical Framework

### 3.1 Econometric Model of Dynamic Risk-Taking
To evaluate how within-session wealth dynamics alter risk-taking, we estimate linear panel models with player fixed effects. This specification controls for time-invariant unobserved player heterogeneity, such as baseline skill, intrinsic risk tolerance, and aggressive disposition.

For player $i$ in session $s$ on hand $t$, we specify:
$$Y_{ist} = \alpha_i + \beta_1 \mathbb{I}(W_{ist} > 0) + \beta_2 \frac{W_{ist}^+}{100} + \beta_3 \mathbb{I}(W_{ist} < 0) + \beta_4 \frac{W_{ist}^-}{100} + \theta \ln(\text{Stack}_{ist}) + \mathbf{X}_{ist}' \boldsymbol{\gamma} + \varepsilon_{ist}$$
where $Y_{ist}$ denotes one of five measures of risk:
1. $VPIP_{ist}$: Voluntary pot entry.
2. $PFR_{ist}$: Preflop aggressive raising.
3. $Aggressive_{ist}$: Postflop betting or raising.
4. $BetAmount_{ist}$: Continuous chips wagered.
5. $BetFraction_{ist}$: Ratio of wager to stack.

The primary variables of interest capture wealth domain and magnitude:
- $\mathbb{I}(W_{ist} > 0)$ indicates that cumulative within-session profit is positive.
- $W_{ist}^+ = \max(0, W_{ist})$ captures the magnitude of accumulated profit (in hundreds of chips).
- $\mathbb{I}(W_{ist} < 0)$ indicates that the player is in deficit.
- $W_{ist}^- = \max(0, -W_{ist})$ captures the magnitude of cumulative losses.

Crucially, we include $\ln(\text{Stack}_{ist})$ in the continuous bet models to directly absorb mechanical changes in stack size. The vector $\mathbf{X}_{ist}$ includes position fixed effects relative to the dealer button (delineating early, middle, late, and blind seats), the number of active competitors ($NumPlayers_{ist}$), and linear within-session fatigue ($HandIndex_{ist} / 10$). Standard errors are clustered at the player level to permit arbitrary within-player correlation across hands and sessions.

### 3.2 Hazard Model of Session Termination
To examine session stopping, we specify a discrete-time logistic hazard model:
$$\text{logit}\left[\Pr(Quit_{ist} = 1 \mid \text{Active}_{ist})\right] = \delta_0 + \sum_{k} \delta_k \text{Outcome}_{k, ist-1} + \mathbf{Z}_{ist}' \boldsymbol{\psi}$$
where $\text{Outcome}_{k, ist-1}$ classifies the outcome of the immediate preceding hand: (a) won chips ($\pi_{ist-1} > 0$), (b) lost chips ($\pi_{ist-1} < 0$), or (c) uncontested fold ($\pi_{ist-1} = 0$). The vector $\mathbf{Z}_{ist}$ controls for cumulative wealth states, session elapsed minutes, and hand index.

---

## 4. Empirical Results

### 4.1 The House Money Effect vs. Loss Chasing
Table 2 reports the within-player fixed effects panel regression estimates.

```
=====================================================================================================
Table 2: Player Fixed Effects Estimates of Within-Session Wealth on Risk-Taking
=====================================================================================================
Independent Variables            (1) VPIP       (2) PFR     (3) Aggression   (4) Bet Amount   (5) Bet/Stack
-----------------------------------------------------------------------------------------------------
In Gain Domain (House Money)     0.00587***    0.00269***    0.00341***      -0.37644         -0.00130***
                                (0.00141)     (0.00090)     (0.00119)        (0.23752)        (0.00019)
Gain Magnitude ($W^+ / 100$)     0.00118***    0.00038*      0.00055**        0.57122***       0.00058***
                                (0.00026)     (0.00022)     (0.00024)        (0.10883)        (0.00007)
In Loss Domain                   0.00501***    0.00214**     0.00222*        -0.34883         -0.00220***
                                (0.00148)     (0.00103)     (0.00119)        (0.23035)        (0.00035)
Loss Magnitude ($W^- / 100$)     0.00404***    0.00420***    0.00367***       0.98960***       0.00352***
                                (0.00061)     (0.00055)     (0.00049)        (0.15046)        (0.00023)
Log Current Stack               -0.01059***   -0.00464***   -0.00578***      -0.44138***      -0.02826***
                                (0.00147)     (0.00116)     (0.00112)        (0.09625)        (0.00147)
Hand Index / 10                 -0.00018       0.00050***    0.00014         -0.13945***      -0.00050***
                                (0.00016)     (0.00012)     (0.00013)        (0.02583)        (0.00004)
Number of Active Players        -0.01122***   -0.01358***   -0.01904***       0.00013***       0.00013***
                                (0.00042)     (0.00040)     (0.00036)        (0.00005)        (0.00005)

Position Fixed Effects             Yes           Yes           Yes              Yes              Yes
Player Fixed Effects               Yes           Yes           Yes              Yes              Yes
Observations                    3,999,153     3,999,153     3,999,153        3,999,153        3,999,153
Unique Players                    3,695         3,695         3,695            3,695            3,695
Within R-squared                 0.0419        0.0155        0.0210           0.0133           0.1406
=====================================================================================================
Notes: Dependent variables: (1) VPIP = 1 if player voluntarily entered pot; (2) PFR = 1 if player raised preflop; (3) Aggression = 1 if player bet/raised postflop; (4) Bet Amount = chips wagered; (5) Bet/Stack = ratio of wager to current stack. Standard errors clustered by player in parentheses. Sample restricted to players with >= 50 hands. *** p < 0.01, ** p < 0.05, * p < 0.10.
```

The estimates in Table 2 provide clear evidence of the house money effect. In Column (1), entering the gain domain increases VPIP by 0.59 percentage points ($t = 4.16, p < 0.001$). For every 100 chips of accumulated profit, VPIP expands by an additional 0.12 percentage points ($p < 0.001$). Similarly, preflop raising (Column 2) and postflop aggression (Column 3) rise by 0.27 and 0.34 percentage points, respectively. 

Crucially, in Column (4), the coefficient on gain magnitude reveals a positive absolute stake response: each 100 chips of accumulated profit increases average bet sizes by $+0.571$ chips ($t = 5.25, p < 0.001$). When playing with accrued earnings, participants contest wider ranges and commit larger quantities of chips, consistent with mental accounting models wherein prior gains cushion future risks.

Conversely, the coefficients in the loss domain reject simple risk aversion. As cumulative deficits deepen, players escalate their risk-taking. In Column (4), each 100 chips of cumulative loss increases absolute bet sizing by $+0.990$ chips ($t = 6.58, p < 0.001$). In Column (5), even after controlling directly for $\ln(\text{Stack})$, each 100 chips of deficit increases the bet-to-stack ratio by $+0.00352$ ($t = 15.52, p < 10^{-50}$). Rather than reducing stakes to protect their remaining bankroll, trailing players systematically escalate bet sizes, exhibiting classic loss-chasing behavior.

Figure 1 displays these dual responses non-parametrically across bins of cumulative profit/loss.

```
+---------------------------------------------------------------------------------------------------+
|                                            [FIGURE 1]                                             |
|  Figure 1: Risk-Taking (VPIP and Bet Sizing) Across Cumulative Session Wealth States             |
|  (Binned scatter plots of voluntary participation and absolute wager amounts with 95% CIs)      |
+---------------------------------------------------------------------------------------------------+
```

Figure 1 confirms the asymmetric kink: VPIP and bet amounts rise steadily in the positive domain (House Money), but escalate steeply in deep negative territory (Loss Chasing).

---

### 4.2 Break-Even Bunching and Reference-Dependent Stopping
We next test whether session stopping decisions respond to cumulative wealth reference points. Figure 2 plots the empirical distribution of final session net profit/loss ($W_{exit}$) in 4-chip bins spanning $[-100, +100]$, alongside a 4th-order polynomial counterfactual density fitted to non-bunching bins.

```
+---------------------------------------------------------------------------------------------------+
|                                            [FIGURE 2]                                             |
|  Figure 2: Distribution of Session Exit Wealth: Discontinuity at the Break-Even Reference Point   |
|  (Empirical density vs. polynomial counterfactual, highlighting the bunching mass spike at W = 0) |
+---------------------------------------------------------------------------------------------------+
```

As shown in Figure 2, the empirical density displays a sharp mass spike centered precisely at zero ($W_{exit} = 0$). Exactly 1,340 sessions terminate at zero profit, yielding a normalized excess mass ratio of $\hat{b} = +0.284$ ($p < 0.001$). 

To ensure this spike is not an artifact of passive players who merely folded several hands without contesting a pot, we decompose the exact break-even sample:
- **Active Clawbacks (54.9%, 735 sessions):** The player experienced an intra-session deficit ($\min W_{ist} < 0$), recovered back to zero, and immediately terminated the session.
- **Active Givebacks (14.0%, 188 sessions):** The player was ahead ($\max W_{ist} > 0$), relinquished their gains back to zero, and quit before entering the negative domain.
- **Passive Flatlines (31.1%, 417 sessions):** The player never won or lost a chip.

Active round-trip sessions comprise over two-thirds (68.9%) of all exact break-even terminations. Furthermore, the mean duration of exact break-even sessions is only **18.2 hands (20.5 minutes)**, compared to **37.8 hands (42.0 minutes)** for winning sessions and **30.2 hands (34.5 minutes)** for losing sessions. This marked brevity proves that players actively truncate their sessions early the moment their net balance returns to the zero baseline.

---

### 4.3 The "Never Quit on a Win" Asymmetry
Table 3 reports the conditional per-hand termination hazard across immediate hand outcomes and cumulative wealth states.

```
========================================================================================
Table 3: Empirical Session Termination Hazard by Immediate Hand Outcome and Wealth State
========================================================================================
Outcome / Wealth Category              Total Hand Opps    Observed Quits    Hazard Rate h(t)
----------------------------------------------------------------------------------------
Panel A: Immediate Preceding Hand Outcome
Winning Hand (Net Hand PnL > 0)             791,823           2,841         0.0036 (0.36%)
Losing Hand (Net Hand PnL < 0)            1,882,645          46,687         0.0248 (2.48%)
Neutral / Uncontested Fold (PnL = 0)      1,396,088          70,056         0.0502 (5.02%)

Panel B: Cumulative Within-Session Wealth ($W_{ist}$)
Deep Loss ($W_{ist} \le -200$)               633,797          22,690         0.0358 (3.58%)
Moderate Loss ($-200 < W_{ist} \le -50$)     838,088          28,203         0.0336 (3.36%)
Near Break-Even ($-20 < W_{ist} \le +20$)    562,103           9,237         0.0164 (1.64%)
Moderate Gain ($+20 < W_{ist} \le +200$)     876,721          25,970         0.0296 (2.96%)
Deep Gain ($W_{ist} > +200$)                 771,808          23,044         0.0299 (2.99%)
========================================================================================
Notes: Panel A reports conditional per-hand exit hazards by the outcome of hand t. Panel B bins hands by cumulative within-session wealth before hand t.
```

Table 3 reveals an acute behavioral asymmetry. Immediately following a winning hand, the conditional probability of quitting is a negligible **0.36%** (2,841 exits out of 791,823 opportunities). By contrast, after a losing hand, the hazard rate increases sevenfold to **2.48%** (46,687 exits), while after an uncontested fold, the hazard reaches **5.02%** (70,056 exits). 

Winning hands act as potent continuation reinforcers: competitors almost never leave immediately after taking down a pot. Quitting occurs overwhelmingly between hands during inactive folds or following a painful loss.

Figure 3 plots the empirical hazard function across cumulative wealth states.

```
+---------------------------------------------------------------------------------------------------+
|                                            [FIGURE 3]                                             |
|  Figure 3: Conditional Session Termination Hazard Across Wealth States                            |
|  (Per-hand quit probability h(W) with 95% confidence intervals)                                   |
+---------------------------------------------------------------------------------------------------+
```

---

### 4.4 Session Duration and the Sunk-Cost Dilemma
A key question is how these stopping rules translate into total session lengths. Unconditionally, winning sessions average 37.8 hands (42.0 minutes), while losing sessions average 30.2 hands (34.5 minutes). 

This gap reflects two countervailing mechanisms:
1. **Mechanical Truncation (Bust-Outs):** When a player loses their table buy-in, they are mechanically prevented from continuing unless they re-buy. In our data, 2,923 sessions (2.44%) end in complete stack depletion ($Stack \le 0$).
2. **The "Riding the Rush" Effect:** Because winning hands carry an exit hazard of only 0.36%, winning players naturally accumulate longer uninterrupted runs.

However, examining the distribution of voluntary exits ($Stack > 0$) reveals significant right-tail persistence among losing sessions. Figure 4 compares the cumulative distribution function (CDF) and length densities of winning versus losing sessions.

```
+---------------------------------------------------------------------------------------------------+
|                                            [FIGURE 4]                                             |
|  Figure 4: Session Duration and Length by Final Outcome (Voluntary Exits Only)                    |
|  (Panel A: Cumulative distribution of duration; Panel B: Session length density)                  |
+---------------------------------------------------------------------------------------------------+
```

As demonstrated in Figure 4, while the median losing session is shorter due to demoralization and rapid buy-in losses, the upper deciles of losing sessions exhibit a prominent right tail. A substantial subset of underwater players refuses to quit, playing well over 100 hands in pursuit of the break-even threshold. When these recovery efforts fail, the resulting extended sessions compound losses and expose participants to cognitive exhaustion.

---

## 5. Discussion and Welfare Implications

Our empirical findings demonstrate that agents in repeated financial contests do not operate with stable, history-independent risk preferences. Instead, decision-making is characterized by a **dual-account mental accounting model** (Barberis, 2012; Imas, 2016):
- **Accumulated gains are segregated:** Profits are mentally filed as house money, lowering effective loss aversion and expanding risk tolerance ($\beta_{VPIP} = +0.00587, p < 0.001$).
- **Accumulated losses are held open:** Because closing a session converts a paper deficit into a realized psychological loss, agents resist quitting when underwater. In deep deficits, diminishing sensitivity induces aggressive risk escalation ($\beta_{bet} = +0.990, p < 0.001$).
- **Break-even acts as an absorbing boundary:** When an agent successfully recovers their starting stake, the sudden absence of loss aversion creates a sharp incentive to stop, producing bunching at $W_{exit} = 0$.

### Regulatory and Platform Design Implications
These mechanisms have direct implications for consumer protection in retail investing, sports betting, and digital gambling:
1. **Salient Session Ledger Displays:** Real-time displays of within-day profit/loss can inadvertently trigger loss-chasing spirals during drawdowns. Allowing users to toggle off short-term PnL counters could reduce impulsive risk escalation.
2. **Cooling-Off Defaults:** Because winning hands suppress termination hazards to near-zero (0.36%), players on winning streaks are cognitively shielded from fatigue. Automated time alerts or mandatory break prompts could prevent players from transitioning from house-money euphoria into subsequent loss-chasing spirals.

---

## 6. Conclusion

Using a census of four million hand decisions from online poker, this paper provides clean field evidence on dynamic risk preferences and stopping rules. We document a robust house money effect in the gain domain, alongside intense loss chasing as cumulative deficits deepen. Furthermore, session termination is governed by reference-dependent heuristics: players bunch at the exact break-even threshold ($W = 0$) and exhibit a pronounced reluctance to walk away following a win. These findings bridge laboratory prospect theory and field labor supply models, highlighting the central role of mental accounting in dynamic financial environments.

---

## References

- Barberis, N. (2012). A model of casino gambling. *Management Science*, 58(1), 35-51.
- Billings, D., Davidson, A., Schaeffer, J., & Szafron, D. (2002). The challenge of poker. *Artificial Intelligence*, 134(1-2), 201-240.
- Camerer, C., Babcock, L., Loewenstein, G., & Thaler, R. (1997). Labor supply of New York City cabdrivers: One day at a time. *Quarterly Journal of Economics*, 112(2), 407-441.
- Chetty, R., Friedman, J. N., Olsen, T., & Pistaferri, L. (2011). Adjustment costs, firm responses, and micro vs. macro labor supply elasticities: Evidence from Danish tax records. *Quarterly Journal of Economics*, 126(2), 749-804.
- Farber, H. S. (2005). Is labor supply of taxi drivers really backward-bending? Empirical evidence. *Journal of Political Economy*, 113(4), 857-882.
- Farber, H. S. (2008). Reference-dependent preferences and labor supply: The case of New York City taxi drivers. *American Economic Review*, 98(3), 1069-1082.
- Farber, H. S. (2015). Why you can't find a taxi in the rain, and other labor supply puzzles. *Quarterly Journal of Economics*, 130(4), 1975-2026.
- Imas, A. (2016). The realization effect: A test of how realized versus paper outcomes affect risk taking. *American Economic Review*, 106(8), 2086-2109.
- Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica*, 47(2), 263-291.
- McCrary, J. (2008). Manipulation of the running variable in the regression discontinuity design: A density test. *Journal of Econometrics*, 142(2), 698-714.
- Narayanan, S., & Manchanda, P. (2012). An empirical analysis of individual-level casino gambling behavior. *Quantitative Marketing and Economics*, 10(3), 361-402.
- Post, T., Van den Assem, M. J., Baltussen, G., & Thaler, R. H. (2008). Deal or no deal? Decision making under risk in a large-payoff game show. *American Economic Review*, 98(1), 38-71.
- Rabin, M. (2000). Risk aversion and expected-utility theory: A calibration theorem. *Econometrica*, 68(5), 1281-1292.
- Thaler, R. H. (1985). Mental accounting and consumer choice. *Marketing Science*, 4(3), 199-214.
- Thaler, R. H., & Johnson, E. J. (1990). Gambling with the house money and trying to break even: The effects of prior outcomes on risky choice. *Management Science*, 36(6), 643-660.
