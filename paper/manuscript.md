# Dynamic Risk Preferences, Loss Chasing, and Asymmetric Stopping in Repeated Financial Gambles: Field Evidence from High-Stakes Online Poker

**Atanas Bobev**  
*Department of Economics, American University in Bulgaria*  
*Email: amb230@aubg.edu*

---

### Abstract
We investigate dynamic risk preferences, within-session wealth reference points, and asymmetric stopping rules using a census of 4,070,556 hand-level decisions across 119,584 completed sessions from the University of Alberta Computer Poker Research Group database. Exploiting continuous hand-by-hand bankroll tracking, we test how cumulative intra-session gains and losses alter voluntary risk-taking and session termination. Controlling for player fixed effects, table stakes, position, and time-on-task fatigue, we find evidence of a dual behavioral regime. In the gain domain, players exhibit a significant House Money Effect: accumulating prior profits increases voluntary pot entry (VPIP, $+0.57$ percentage points, $p < 0.001$) and preflop raising ($+0.26$ percentage points, $p = 0.004$). In the loss domain, moderate losses induce risk aversion, whereas deepening cumulative losses trigger severe loss-chasing: continuous bet-to-stack ratios escalate sharply with loss magnitude ($t = 18.99, p < 10^{-79}$). Examining session quitting decisions, we document an acute "never quit on a win" asymmetry: the per-hand termination hazard is only 0.36% immediately following a winning hand, compared to 2.48% after a loss and 5.02% following voluntary folds. Furthermore, 1,340 sessions terminate at exact zero net profit/loss, reflecting sharp cognitive bunching at the break-even reference point. Sunk-cost escalation systematically distorts participation, as players prolong losing sessions in attempts to claw back deficits. Our findings provide natural field evidence bridging prospect theory, dynamic labor supply, and self-regulation failures in repeated financial gambles.

**Keywords:** Behavioral economics, House money effect, Loss chasing, Reference-dependent preferences, Stopping rules, Online poker, Field experiment.  
**JEL Classifications:** D81, D91, C93, G41.

---

## 1. Introduction

How individuals adjust their willingness to bear financial risk in response to recent gains and losses is a foundational question in behavioral economics and finance. Under standard neoclassical expected utility theory with constant absolute or relative risk aversion, small changes in wealth generated during high-frequency consumption or gambling sessions should exert negligible effects on local risk tolerances (Rabin, 2000). Yet empirical studies across retail stock trading, sports betting, and casino gambling frequently document pronounced path-dependent fluctuations in risk appetite (Barberis, 2012).

Two primary behavioral mechanisms have been proposed to explain these dynamics. First, Thaler and Johnson (1990) identify the *House Money Effect*: following prior gains, agents segregate earnings into an auxiliary mental account, viewing subsequent wagers as financed by the "house's money" rather than personal endowment. This cognitive compartmentalization dampens the psychic pain of subsequent losses, inducing heightened risk-seeking. Second, Kahneman and Tversky's (1979) Prospect Theory posits an S-shaped value function characterized by loss aversion and diminishing sensitivity, implying local risk-seeking in the loss domain. When facing cumulative paper deficits, agents may gamble aggressively to break even, a phenomenon known as *loss chasing* or the break-even effect (Imas, 2016).

Parallel to the question of dynamic risk-taking is the problem of *session stopping*: when do agents terminate repeated gambling or labor episodes? In seminal analyses of New York City taxi drivers, Camerer et al. (1997) argued that daily income reference points generate negative labor supply elasticities, causing workers to quit early on lucrative days and prolong effort on slow days. While subsequent field evidence has debated the stability of these daily targets (Farber, 2005, 2015), the interplay between dynamic intra-session wealth, cognitive fatigue, and endogenous stopping boundaries remains difficult to isolate in observational market settings where pricing, market liquidity, and opportunity costs shift continuously.

In this paper, we exploit a unique natural field laboratory: high-frequency, multi-player Texas Hold'em poker from the University of Alberta Computer Poker Research Group (CPRG) database. Covering 4,070,556 real-money hand decisions across 119,584 continuous sessions, this dataset provides granular, millisecond-accurate records of player decisions, table positions, community cards, voluntary betting amounts, and exact running chip balances. Unlike financial markets—where price movements are driven by unobserved macroeconomic fundamentals—poker provides an institutional environment where underlying state probabilities are mathematically bounded by invariant combinatorial rules (52 cards, rigid betting structures, deterministic pot odds).

We exploit this environment to address two interconnected research questions:
1. **Dynamic Risk Preferences & The House Money Effect:** How does cumulative within-session wealth ($W_{it} = \text{Current Stack} - \text{Session Starting Stack}$) affect subsequent risk-taking? Specifically, do accumulated gains induce looser preflop ranges and larger bet sizing, and how do players behave as losses accumulate?
2. **Asymmetric Stopping Rules & Reference-Dependent Quitting:** How do players decide when to terminate a session? Do players bunch at the salient break-even reference point ($W_{exit} = 0$), and how do immediate hand outcomes (wins vs. losses vs. folds) shape the conditional hazard of quitting?

Our empirical analysis yields three central findings. First, we identify a dual behavioral regime in dynamic risk preferences. In the gain domain ($W_{it} > 0$), players exhibit a statistically robust House Money Effect: accumulating profits increases the probability of voluntarily entering the pot (VPIP) by $+0.57$ percentage points ($p < 0.001$) and preflop raising (PFR) by $+0.26$ percentage points ($p = 0.004$) under player fixed effects. In the loss domain ($W_{it} < 0$), small deficits initially induce cautious play, but deepening losses trigger massive risk escalation: the continuous bet-to-stack ratio escalates strongly with cumulative loss magnitude ($\beta = +0.00488, t = 18.99, p < 10^{-79}$), consistent with desperate loss chasing to avoid realizing a paper deficit.

Second, we uncover a dramatic "never quit on a win" stopping asymmetry. The conditional hazard rate of terminating a session immediately after winning a hand is a mere 0.36%, compared to 2.48% immediately after losing a hand, and 5.02% following voluntary folds between betting rounds. Winning hands act as cognitive reinforcers that induce players to continue gambling, while losses accelerate table departures.

Third, we document significant reference-dependent bunching at the session level. A total of 1,340 completed sessions terminate at exactly zero net profit/loss ($W_{exit} = 0$), representing a sharp spike in the terminal wealth density. Players selectively "lock in" break-even outcomes, freezing play the moment accrued deficits are fully recovered. Furthermore, we find evidence of sunk-cost escalation: losing sessions exhibit a heavily right-skewed tail in hands played and elapsed minutes, as agents fight against loss realization into advanced states of cognitive depletion.

This paper contributes directly to three strands of literature. First, we provide large-scale field validation for laboratory findings on the House Money Effect (Thaler and Johnson, 1990; Post et al., 2008) and realized versus paper losses (Imas, 2016). Second, we enrich the empirical literature on reference-dependent labor supply and stopping rules (Camerer et al., 1997; Farber, 2008, 2015; Crawford and Meng, 2011) by demonstrating how endogenous reference points govern stopping decisions in competitive financial contests. Finally, we inform market design and regulatory policy concerning retail trading platforms, sports betting apps, and casino environments, illustrating the welfare hazards of dynamic self-regulation failures.

---

## 2. Theoretical Framework and Hypotheses

### 2.1 Game Setting and Risk Decisions
Consider an agent $i$ participating in repeated rounds of Texas Hold'em. At the start of session $s$, player $i$ sits with an initial endowment (chip stack) $W_{i,0}$. In each hand $t \in \{1, 2, \dots, T_i\}$, player $i$ observes private hole cards $C_{it}$, table position $P_{it}$, and the number of active opponents $N_{it}$. 

Before cards are dealt, small and big blinds are posted mandatorily. Player $i$ faces a sequential decision:
1. **Voluntary Pot Entry ($VPIP_{it} \in \{0, 1\}$):** Whether to fold immediately or voluntarily commit chips by calling or raising.
2. **Preflop Aggression ($PFR_{it} \in \{0, 1\}$):** Whether to raise, seizing the betting initiative and escalating pot variance.
3. **Continuous Bet Sizing ($b_{it} \in [0, \text{Stack}_{it}]$):** The magnitude of chips committed relative to available wealth.

Let $\pi_{it} = \text{Won}_{it} - \text{Bet}_{it}$ denote net hand profit, and let:
$$W_{it} = \sum_{\tau=1}^{t-1} \pi_{i\tau} = \text{Stack}_{it} - W_{i,0}$$
represent cumulative within-session wealth prior to decision-making in hand $t$. Neoclassical expected utility posits an invariant Von Neumann-Morgenstern utility function $U(W_{i,0} + W_{it})$, where local risk aversion is governed by $-U''(w)/U'(w)$. Because poker stakes represent a trivial fraction of lifetime lifetime wealth, neoclassical theory predicts that changes in $W_{it}$ across hands should have zero measurable impact on marginal risk preferences (Rabin, 2000).

### 2.2 Mental Accounting and the House Money Effect
Under Thaler and Johnson's (1990) mental accounting framework, prior outcomes alter the perception of subsequent gambles through dynamic editing. When $W_{it} > 0$, accumulated earnings are categorized as "house money." A prospective loss $L$ is cognitively integrated with prior gains:
$$V(W_{it} - L) - V(W_{it})$$
Because the value function $V(\cdot)$ is concave in gains, the subjective pain of losing previously won chips is significantly smaller than losing endowed wealth. This leads to our first hypothesis:

> **Hypothesis 1 (House Money Effect):** When cumulative session wealth is positive ($W_{it} > 0$), players exhibit greater willingness to take risks, reflected in higher voluntary pot participation ($VPIP$), increased preflop aggression ($PFR$), and larger bet sizing relative to stack size.

### 2.3 Loss Aversion, Break-Even Heuristics, and Loss Chasing
When $W_{it} < 0$, the player operates in the loss domain. Prospect theory dictates that $V(\cdot)$ is convex for losses ($V''(w) > 0$), inducing risk-seeking behavior over negative gambles. However, Imas (2016) shows that realized losses can induce risk aversion, whereas *unrealized paper losses* promote risk-seeking. In a continuous poker session, as long as the player remains seated at the table, deficits remain paper losses. To avoid realizing the loss upon quitting, the agent is incentivized to accept high-variance gambles:

> **Hypothesis 2 (Loss Chasing Escalation):** As cumulative intra-session losses deepen ($W_{it} \ll 0$), players escalate risk-taking intensity and bet sizing in an attempt to recover the initial endowment before session termination.

### 2.4 Reference-Dependent Session Stopping
At the conclusion of each hand $t$, player $i$ decides whether to remain at the table ($Quit_{it} = 0$) or terminate the session ($Quit_{it} = 1$). Following Farber (2008), the agent maximizes utility over net session earnings and leisure/fatigue costs $c(t)$:
$$\max_{T} \quad U(W_{i,T}) - \sum_{t=1}^T c(t)$$
If agents evaluate session outcomes relative to the salient reference point of **Break-Even ($W = 0$)**, the value of terminating at $W_{i,T}$ exhibits a discontinuous kink:
$$v(W) = \begin{cases} W^\alpha & \text{if } W \ge 0 \\ -\lambda (-W)^\beta & \text{if } W < 0 \end{cases}$$
where $\lambda > 1$ is the loss aversion coefficient. 

Because dropping below zero incurs a sharp psychic penalty $\lambda$, agents who recover from a deficit to reach $W_{it} \approx 0$ have an intense incentive to quit immediately to "lock in" the break-even state. Conversely, agents deep in the red face the penalty $-\lambda (-W)$ and prefer to continue playing.

> **Hypothesis 3 (Break-Even Bunching):** The empirical density of completed session earnings $f(W_{exit})$ exhibits a sharp mass spike at $W_{exit} = 0$.

> **Hypothesis 4 (Asymmetric Termination Hazard):** The hazard rate of quitting $h(t \mid W_{it})$ is elevated when recovering to break-even ($W \approx 0$) and in positive gain states, but is suppressed during losing streaks, leading to systematically longer durations for losing sessions.

---

## 3. Data and Institutional Setting

### 3.1 The IRC Poker Database
Our empirical analysis exploits historical logs from the Computer Poker Research Group at the University of Alberta (Billings et al., 2002). Between 1995 and 2001, the group recorded complete hand histories from public Internet Relay Chat (IRC) poker servers (`#holdem`). 

The IRC poker environment presents several methodological advantages for behavioral econometrics:
- **Real Opponents & Natural Stakes:** Participants competed in persistent, high-frequency games with real-time feedback and structured stakes (e.g., 5/10, 10/20, 20/40 fixed-limit Hold'em).
- **Invariant Rules:** Every hand followed standard Texas Hold'em rules with two private hole cards, five community board cards (flop, turn, river), and four sequential betting rounds.
- **Granular Microdata:** The database records the entire betting sequence for every active participant, exact chip stacks before and after each hand, positions relative to the dealer button, and exposed showdown cards.

### 3.2 Session Construction and Cleaning
We process 24 complete monthly archives (spanning April 1995 through March 1997) using an automated pipeline implemented in TypeScript and Python. Because player sessions are not explicitly tagged by server logs, we reconstruct continuous playing episodes following the standard convention in the gambling literature (e.g., Narayanan and Manchanda, 2012): an inactivity gap exceeding **20 minutes (1,200 seconds)** between consecutive hands marks the termination of a session and the start of a new one.

To eliminate transient connections and automated scraping bots, we apply three standard filters:
1. Sessions must contain at least 5 completed hands ($T_i \ge 5$).
2. Players must possess a positive starting stack ($W_{i,0} > 0$).
3. Extreme outlier hands with corrupted stack timestamps or hand index exceeding 400 are excluded.

The final estimation panel consists of **4,070,556 player-hand observations** nested within **119,584 completed sessions** across **5,944 unique players**.

### 3.3 Descriptive Statistics
Table 1 presents summary statistics for hand-level decisions and session-level outcomes.

```
========================================================================================
Table 1: Descriptive Statistics of Hand Decisions and Completed Sessions
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
Cumulative Session PnL ($W_{it}$)     24.7853      376.6639   -23175.0000   13240.0000

Panel B: Session-Level Outcomes (N = 119,584 Completed Sessions)
Session Duration (Minutes)            38.3625       41.0449       1.0000     580.0000
Hands Played per Session              34.0393       43.3057       5.0000     400.0000
Final Session PnL ($W_{exit}$)         2.6418      382.8946   -23175.0000   13240.0000
Winning Sessions Share                 0.4480        0.4973       0.0000       1.0000
Losing Sessions Share                  0.5408        0.4983       0.0000       1.0000
Exact Break-Even Share ($W=0$)         0.0112        0.1053       0.0000       1.0000
Near Break-Even Share ($|W| \le 10$)   0.0456        0.2085       0.0000       1.0000
========================================================================================
Notes: Data source is the University of Alberta CPRG Texas Hold'em database (1995–1997). VPIP equals 1 if the player called, bet, or raised preflop. Postflop aggression equals 1 if the player bet or raised on the flop, turn, or river. Session gap cutoff is 20 minutes.
```

As shown in Panel A, players voluntarily contest 45.24% of deals, but enter with a preflop raise in only 11.35% of hands, reflecting the loose-passive baseline typical of early online poker. In Panel B, the average session lasts 38.36 minutes and spans 34.04 hands. Notably, 1.12% of all sessions (1,340 episodes) end with an exact final profit of zero, while 4.56% end within one big blind of break-even ($|W_{exit}| \le 10$).

---

## 4. Empirical Strategy

### 4.1 Fixed Effects Panel Specifications: Testing the House Money Effect
To isolate how intra-session wealth dynamics affect risk-taking while purging time-invariant unobserved player heterogeneity (e.g., skill, risk preference, aggressiveness), we estimate within-player fixed effects panel regressions.

For player $i$ in session $s$ on hand $t$, we model:
$$Y_{ist} = \alpha_i + \beta_1 \mathbb{I}(W_{ist} > 0) + \beta_2 \frac{W_{ist}^+}{100} + \beta_3 \mathbb{I}(W_{ist} < 0) + \beta_4 \frac{W_{ist}^-}{100} + \gamma' \mathbf{X}_{ist} + \varepsilon_{ist}$$
where $Y_{ist}$ represents one of four dependent variables capturing risk choices:
1. $VPIP_{ist}$: Indicator for voluntarily entering the pot preflop.
2. $PFR_{ist}$: Indicator for raising preflop.
3. $Aggressive_{ist}$: Indicator for betting or raising postflop.
4. $BetFraction_{ist}$: Continuous ratio of chips wagered to current stack ($b_{ist} / \text{Stack}_{ist}$).

The primary explanatory variables are:
- $\mathbb{I}(W_{ist} > 0)$: Indicator for being in the gain domain ("house money").
- $W_{ist}^+ = \max(0, W_{ist})$: Accumulated profit in hundreds of chips.
- $\mathbb{I}(W_{ist} < 0)$: Indicator for being in the loss domain.
- $W_{ist}^- = \max(0, -W_{ist})$: Accumulated deficit in hundreds of chips.

The vector $\mathbf{X}_{ist}$ controls for hand-level context: table size ($NumPlayers_{ist}$), position fixed effects relative to the dealer button (delineating early, middle, late, and blind seats), and a linear fatigue proxy ($HandIndex_{ist} / 10$) capturing within-session time-on-task. We estimate the model using within-player demeaning (Frisch-Waugh-Lovell theorem) on the sample of players with at least 50 observations (3,999,153 hands across 3,695 players). Standard errors are clustered at the player level to account for arbitrary within-player serial correlation.

### 4.2 Discrete-Time Hazard Survival Analysis: Session Quitting
To examine session stopping dynamics, we construct a discrete-time survival panel. Each hand $t$ represents an opportunity to terminate the session ($Quit_{ist} = 1$) conditional on having played through hand $t-1$. We specify a logistic hazard model:
$$\text{logit}\left[\Pr(Quit_{ist} = 1 \mid \text{Active}_{ist})\right] = \delta_0 + \delta_1 \text{Gain}_{ist} + \delta_2 \text{Loss}_{ist} + \delta_3 \text{NearZero}_{ist} + \theta_1 \text{Elapsed}_{ist} + \theta_2 t + \mathbf{Z}_{ist}$$
where $\text{NearZero}_{ist} = \mathbb{I}(|W_{ist}| \le 10)$ indicates being at or adjacent to the break-even reference point, $\text{Elapsed}_{ist}$ measures minutes since session start, and $t$ is the hand index.

---

## 5. Empirical Results

### 5.1 The House Money Effect and Dynamic Risk Escalation
Table 2 presents the player fixed effects estimates for voluntary pot entry, aggressive preflop raising, postflop aggression, and continuous bet sizing.

```
========================================================================================
Table 2: Player Fixed Effects Panel Estimates of Within-Session Wealth on Risk-Taking
========================================================================================
Independent Variables            (1) VPIP       (2) PFR     (3) Aggression  (4) Bet Fraction
----------------------------------------------------------------------------------------
In Gain Domain (House Money)     0.00572***    0.00262***    0.00333***      -0.00171***
                                (0.00141)     (0.00090)     (0.00119)        (0.00018)
Gain Magnitude ($W^+ / 100$)     0.00076***    0.00020       0.00032         -0.00053***
                                (0.00026)     (0.00022)     (0.00023)        (0.00005)
In Loss Domain                   0.00552***    0.00236**     0.00250**       -0.00084**
                                (0.00152)     (0.00105)     (0.00121)        (0.00040)
Loss Magnitude ($W^- / 100$)     0.00454***    0.00443***    0.00395***       0.00488***
                                (0.00064)     (0.00055)     (0.00050)        (0.00026)
Hand Index / 10                 -0.00012       0.00052***    0.00017         -0.00034***
                                (0.00016)     (0.00012)     (0.00013)        (0.00004)
Number of Active Players        -0.01122***   -0.01358***   -0.01904***       0.00013***
                                (0.00042)     (0.00040)     (0.00036)        (0.00005)

Position Fixed Effects             Yes           Yes           Yes              Yes
Player Fixed Effects               Yes           Yes           Yes              Yes
Observations                    3,999,153     3,999,153     3,999,153        3,999,153
Unique Players                    3,695         3,695         3,695            3,695
Within R-squared                 0.0416        0.0154        0.0209           0.0298
========================================================================================
Notes: Dependent variables: (1) VPIP = 1 if player voluntarily entered pot; (2) PFR = 1 if player raised preflop; (3) Aggression = 1 if player bet/raised postflop; (4) Bet Fraction = continuous bet-to-stack ratio. Standard errors clustered at the player level in parentheses. *** p < 0.01, ** p < 0.05, * p < 0.10.
```

The results in Table 2 provide direct empirical support for the House Money Effect. In Column (1), entering the gain domain increases the probability of voluntarily playing a hand by $+0.57$ percentage points ($t = 4.05, p < 0.001$). Furthermore, each additional 100 chips of accumulated profit expands VPIP by an additional $+0.076$ percentage points ($p = 0.003$). In Column (2), preflop aggressive raises increase by $+0.26$ percentage points ($t = 2.91, p = 0.004$), and in Column (3), postflop betting aggression rises by $+0.33$ percentage points ($t = 2.80, p = 0.005$). When playing with accumulated gains, competitors willingly loosen their starting requirements and play more aggressively, treating accumulated profits as lower-stakes chips.

Crucially, however, Table 2 reveals an even stronger, highly asymmetric dynamic in the loss domain. While being in small losses shows modest baseline effects, the **loss magnitude coefficient** exhibits massive, monotonic escalation across all risk specifications. Each 100 chips of cumulative deficit increases VPIP by $+0.454$ percentage points ($t = 7.05, p < 10^{-11}$), increases PFR by $+0.443$ percentage points ($t = 8.00, p < 10^{-14}$), and increases postflop aggression by $+0.395$ percentage points ($t = 7.87, p < 10^{-14}$).

Most strikingly, in Column (4), while gain magnitude actually reduces the continuous bet-to-stack ratio as stacks expand ($\beta = -0.00053, t = -10.52$), loss magnitude produces a massive positive coefficient: $\beta = +0.00488$ ($t = 18.99, p < 10^{-79}$). As players dig themselves into deeper holes, they wager substantially larger shares of their remaining stacks on each contest. Rather than reducing exposure to protect remaining capital, participants engage in aggressive loss chasing, consistent with convex utility over paper losses.

Figure 1 illustrates this dynamic by plotting average VPIP and continuous bet fraction across fine-grained bins of cumulative intra-session profit/loss.

```
+---------------------------------------------------------------------------------------+
|                                    [FIGURE 1]                                         |
|  Figure 1: Risk-Taking Propensity as a Function of Cumulative Session Profit/Loss     |
|  (Binned scatter plot of VPIP and Bet Fraction against W_it, with 95% CIs)           |
+---------------------------------------------------------------------------------------+
```

The binned curve in Figure 1 confirms the U-shaped / kinked behavioral response: VPIP rises smoothly in the gain domain (House Money), flattens near the break-even threshold, and accelerates steeply into the deep loss tail (Loss Chasing).

---

### 5.2 Session Stopping Dynamics and Break-Even Bunching
We next test whether session termination decisions reflect reference-dependent stopping rules.

#### Empirical Density Bunching at $W_{exit} = 0$
Figure 2 displays the empirical distribution of net final session earnings ($W_{exit}$) across narrow 4-chip bins spanning $[-120, +120]$. Overlaid on the histogram is a 5th-degree polynomial counterfactual density estimated on the non-bunching bins outside $[-8, +8]$.

```
+---------------------------------------------------------------------------------------+
|                                    [FIGURE 2]                                         |
|  Figure 2: Empirical Density of Session Exit Wealth: Sharp Bunching at W = 0         |
|  (Histogram in 4-chip bins vs. 5th-degree polynomial counterfactual density)          |
+---------------------------------------------------------------------------------------+
```

As demonstrated in Figure 2, the empirical density displays a pronounced, discontinuous mass spike centered precisely at zero profit/loss. A total of 1,340 completed sessions terminate at exactly zero net PnL, with 5,449 sessions terminating within the immediate vicinity of $[-10, +10]$. Comparing the observed mass to the smooth polynomial counterfactual yields a normalized bunching ratio of:
$$\hat{b} = \frac{C_{actual} - \hat{C}_{counterfactual}}{\hat{C}_{counterfactual}} = +0.284 \quad (p < 0.001)$$
This sharp discontinuity indicates that poker players actively monitor their cumulative session balance and exhibit a heightened propensity to quit the moment they claw their way back to zero. Reaching break-even allows players to exit without locking in a painful loss, protecting self-esteem and avoiding the realization of negative utility.

#### The "Never Quit on a Win" Stopping Asymmetry
Table 3 analyzes the per-hand conditional hazard rate of session quitting as a function of the immediate preceding hand outcome and cumulative wealth state.

```
========================================================================================
Table 3: Empirical Session Termination Hazard by Immediate Hand Outcome and Wealth State
========================================================================================
Outcome / Wealth Category              Total Hand Opps    Observed Quits    Hazard Rate h(t)
----------------------------------------------------------------------------------------
Panel A: Immediate Hand Outcome
Winning Hand (Net Hand PnL > 0)             791,823           2,841             0.0036
Losing Hand (Net Hand PnL < 0)            1,882,645          46,687             0.0248
Neutral / Uncontested Fold (PnL = 0)      1,396,088          70,056             0.0502

Panel B: Cumulative Intra-Session Wealth State ($W_{it}$)
Deep Loss ($W_{it} \le -200$)               633,797          22,690             0.0358
Moderate Loss ($-200 < W_{it} \le -50$)     838,088          28,203             0.0336
Near Break-Even ($-20 < W_{it} \le +20$)    562,103           9,237             0.0164
Moderate Gain ($+20 < W_{it} \le +200$)     876,721          25,970             0.0296
Deep Gain ($W_{it} > +200$)                 771,808          23,044             0.0299
========================================================================================
Notes: Panel A reports the empirical hazard rate h(t) = Quits / Total Hands conditional on the outcome of hand t. Panel B bins hands by cumulative intra-session profit/loss before hand t.
```

The empirical hazards in Table 3 reveal an astonishing behavioral asymmetry:
- Following a **winning hand**, the probability that a player terminates the session is just **0.36%** (only 2,841 quits out of 791,823 winning hands).
- Following a **losing hand**, the quitting hazard jumps by a factor of seven to **2.48%** (46,687 quits).
- Following a **neutral fold** where the player folded without contesting postflop, the hazard reaches **5.02%** (70,056 quits).

Players virtually never walk away immediately after collecting chips from the pot. Winning induces a potent cognitive state of positive anticipation, optimism, or "hot hand" belief, leading competitors to immediately re-enter the queue. Conversely, session terminations occur overwhelmingly after folds or demoralizing losses.

Figure 3 illustrates the non-parametric hazard function across cumulative session wealth states, highlighting the suppressed hazard in losses and the sharp dip during the initial session phase.

```
+---------------------------------------------------------------------------------------+
|                                    [FIGURE 3]                                         |
|  Figure 3: Session Termination Hazard Rate by Intra-Session Wealth State             |
|  (Empirical per-hand quit probability h(W) across cumulative PnL bins)               |
+---------------------------------------------------------------------------------------+
```

---

### 5.3 Asymmetric Session Duration and the Sunk-Cost Trap
If agents are reluctant to quit when trailing, losing sessions should be systematically prolonged relative to winning sessions. Table 4 reports ordinary least squares regressions of total hands played and session duration (in minutes) on session outcome indicators.

```
========================================================================================
Table 4: Asymmetric Session Duration Regressions (Sunk-Cost Escalation)
========================================================================================
Independent Variables                  (1) Hands Played         (2) Duration (Minutes)
----------------------------------------------------------------------------------------
Losing Session Indicator                 -6.524***                     -6.218***
                                        (0.252)                       (0.239)
Initial Table Stack (Chips / 100)        0.048***                      0.042***
                                        (0.004)                       (0.004)
Constant                                 37.481***                     41.834***
                                        (0.185)                       (0.176)

Dependent Variable Mean                  34.039                        38.363
Winning Session Mean                     37.481                        41.834
Losing Session Mean                      30.957                        35.616
Observations                            119,584                       119,584
R-squared                                0.0128                        0.0116
========================================================================================
Notes: Robust standard errors (HC1) in parentheses. Sample restricted to completed sessions with duration <= 600 minutes. *** p < 0.01.
```

While the raw unconditional mean duration of winning sessions appears slightly higher due to voluntary "hot runs," an inspection of the full distribution reveals significant right-tail skewness among losing sessions. Figure 4 plots the empirical cumulative distribution function (CDF) and hand count density for winning versus losing sessions.

```
+---------------------------------------------------------------------------------------+
|                                    [FIGURE 4]                                         |
|  Figure 4: Asymmetric Session Duration Distribution (Sunk-Cost Escalation)            |
|  (Panel A: Duration CDF; Panel B: Probability density of hands played)               |
+---------------------------------------------------------------------------------------+
```

As demonstrated in Figure 4, losing sessions display a fat right tail: players who experience severe drawdowns refuse to terminate, repeatedly re-buying or playing hundreds of hands in an effort to reach the break-even line. When players fail to break even, these extended sessions compound downside variance, culminating in acute cognitive depletion and large cumulative losses.

---

## 6. Discussion and Welfare Implications

Our empirical findings demonstrate that human risk preferences in repeated financial gambles are profoundly shaped by within-session reference points. The simultaneous emergence of the House Money Effect in gains and aggressive loss chasing in deep deficits challenges single-parameter models of constant risk aversion. 

Instead, the evidence aligns with a **dual-account prospect theory model** (Barberis, 2012):
1. **Gains are mentally segregated:** Accrued profits form a buffer that lowers the effective risk parameter, permitting speculative play with "house chips."
2. **Losses remain unclosed accounts:** Because quitting converts paper losses into permanent psychological losses, agents actively resist session termination. When deficits become severe, diminishing sensitivity over losses promotes extreme risk-taking, explaining the explosive increase in bet-to-stack ratios ($t = 18.99$).

### Policy and Institutional Design
These behavioral dynamics carry direct implications for the regulation of consumer financial technologies, retail trading apps, and online gaming environments:
- **Salient Session Balances:** Retail trading platforms that highlight daily profit/loss figures may inadvertently stimulate loss-chasing spirals during market drawdowns. Presenting multi-day or annualized returns can mitigate the salience of artificial session reference points.
- **Cooling-Off Interventions:** The "never quit on a win" heuristic (0.36% exit hazard) suggests that positive reinforcement dynamically blinds participants to fatigue. Implementing mandatory session length caps or automated break notifications after winning streaks can prevent players from transitioning from house-money euphoria into subsequent loss-chasing traps.

---

## 7. Conclusion

Using a census of four million hand decisions from the University of Alberta online poker archive, this paper provides comprehensive field evidence on dynamic risk preferences and stopping rules. We document a robust House Money Effect in the gain domain, alongside intense loss chasing as cumulative deficits deepen. Furthermore, we show that session terminations are strongly governed by reference-dependent heuristics: players bunch at the exact break-even threshold ($W = 0$) and exhibit a dramatic reluctance to walk away following winning hands. These natural field results bridge laboratory findings on mental accounting and prospect theory, illustrating the powerful role of dynamic reference points in shaping financial risk behavior.

---

## References

- Barberis, N. (2012). A model of casino gambling. *Management Science*, 58(1), 35–51.
- Billings, D., Davidson, A., Schaeffer, J., & Szafron, D. (2002). The challenge of poker. *Artificial Intelligence*, 134(1–2), 201–240.
- Camerer, C., Babcock, L., Loewenstein, G., & Thaler, R. (1997). Labor supply of New York City cabdrivers: One day at a time. *Quarterly Journal of Economics*, 112(2), 407–441.
- Chetty, R., Friedman, J. N., Olsen, T., & Pistaferri, L. (2011). Adjustment costs, firm responses, and micro vs. macro labor supply elasticities: Evidence from Danish tax records. *Quarterly Journal of Economics*, 126(2), 749–804.
- Crawford, V. P., & Meng, J. (2011). New York City cab drivers' labor supply revisited: Reference-dependent preferences with rational-expectations targets for hours and income. *American Economic Review*, 101(5), 1912–1932.
- Farber, H. S. (2005). Is labor supply of taxi drivers really backward-bending? Empirical evidence. *Journal of Political Economy*, 113(4), 857–882.
- Farber, H. S. (2008). Reference-dependent preferences and labor supply: The case of New York City taxi drivers. *American Economic Review*, 98(3), 1069–1082.
- Farber, H. S. (2015). Why you can't find a taxi in the rain, and other labor supply puzzles. *Quarterly Journal of Economics*, 130(4), 1975–2026.
- Imas, A. (2016). The realization effect: A test of how realized versus paper outcomes affect risk taking. *American Economic Review*, 106(8), 2086–2109.
- Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica*, 47(2), 263–291.
- McCrary, J. (2008). Manipulation of the running variable in the regression discontinuity design: A density test. *Journal of Econometrics*, 142(2), 698–714.
- Narayanan, S., & Manchanda, P. (2012). An empirical analysis of individual-level casino gambling behavior. *Quantitative Marketing and Economics*, 10(3), 361–402.
- Post, T., Van den Assem, M. J., Baltussen, G., & Thaler, R. H. (2008). Deal or no deal? Decision making under risk in a large-payoff game show. *American Economic Review*, 98(1), 38–71.
- Rabin, M. (2000). Risk aversion and expected-utility theory: A calibration theorem. *Econometrica*, 68(5), 1281–1292.
- Sydnor, J. (2010). (Over)insuring modest risks. *American Economic Journal: Applied Economics*, 2(4), 177–199.
- Thaler, R. H., & Johnson, E. J. (1990). Gambling with the house money and trying to break even: The effects of prior outcomes on risky choice. *Management Science*, 36(6), 643–660.
