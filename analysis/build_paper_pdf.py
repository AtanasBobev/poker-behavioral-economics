import os
import base64
import subprocess
import shutil

"""
Refined Academic PDF Compiler (AER / JEBO / JDM Standard)
Implements true academic typesetting:
- Classic Three-Line (Booktabs) tables
- Minimalist typography (Times New Roman, crisp monochrome rules)
- Muted academic figure styling
- Zero AI-style alert banners or saturated primary colored boxes
"""

def encode_image(img_path):
    if os.path.exists(img_path):
        with open(img_path, 'rb') as f:
            return 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')
    return ''

fig_dir = r'C:\Users\Z09057\poker-behavioral-economics\figures'
fig1_b64 = encode_image(os.path.join(fig_dir, 'fig1_house_money_curve.png'))
fig2_b64 = encode_image(os.path.join(fig_dir, 'fig2_breakeven_bunching.png'))
fig3_b64 = encode_image(os.path.join(fig_dir, 'fig3_stopping_hazard.png'))
fig4_b64 = encode_image(os.path.join(fig_dir, 'fig4_duration_escalation.png'))

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Dynamic Risk Preferences, Loss Chasing, and Reference-Dependent Stopping in Repeated Contests</title>
<style>
  @page {{
    size: letter;
    margin: 25mm 22mm 25mm 22mm;
    @bottom-center {{
      content: counter(page);
      font-size: 10pt;
      font-family: "Times New Roman", Times, serif;
    }}
  }}
  body {{
    font-family: "Times New Roman", Times, serif;
    font-size: 10.5pt;
    line-height: 1.4;
    color: #111111;
    margin: 0;
    padding: 0;
    text-align: justify;
  }}
  h1 {{
    font-size: 15.5pt;
    font-weight: bold;
    text-align: center;
    line-height: 1.25;
    margin-top: 10px;
    margin-bottom: 12px;
  }}
  .authors {{
    text-align: center;
    font-size: 11.5pt;
    font-weight: bold;
    margin-bottom: 2px;
  }}
  .affiliation {{
    text-align: center;
    font-size: 9.5pt;
    font-style: italic;
    color: #333333;
    margin-bottom: 20px;
  }}
  .abstract-container {{
    margin: 0 20px 22px 20px;
    font-size: 9.5pt;
    line-height: 1.35;
  }}
  .abstract-label {{
    font-weight: bold;
    font-size: 10pt;
    margin-bottom: 4px;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .keywords {{
    margin-top: 10px;
    font-size: 9pt;
  }}
  h2 {{
    font-size: 12pt;
    font-weight: bold;
    color: #111111;
    margin-top: 20px;
    margin-bottom: 8px;
    page-break-after: avoid;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }}
  h3 {{
    font-size: 11pt;
    font-weight: bold;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
  }}
  p {{
    margin-top: 0;
    margin-bottom: 8px;
    text-indent: 1.5em;
  }}
  .no-indent {{
    text-indent: 0;
  }}
  /* Classic Three-Line Booktabs Table Styling */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0 16px 0;
    font-size: 8.5pt;
    line-height: 1.2;
    page-break-inside: avoid;
  }}
  th, td {{
    padding: 3.5px 5px;
    text-align: left;
  }}
  th {{
    border-top: 1.2pt solid #111111;
    border-bottom: 0.8pt solid #111111;
    font-weight: bold;
  }}
  .subhead {{
    font-weight: bold;
    border-top: 0.5pt solid #cccccc;
    border-bottom: 0.5pt solid #cccccc;
    background-color: transparent;
  }}
  .table-bottom {{
    border-bottom: 1.2pt solid #111111;
  }}
  .table-title {{
    font-weight: bold;
    font-size: 9pt;
    margin-bottom: 3px;
    page-break-after: avoid;
  }}
  .table-notes {{
    font-size: 8pt;
    color: #333333;
    margin-top: 3px;
    line-height: 1.15;
  }}
  .figure-box {{
    text-align: center;
    margin: 16px 0 18px 0;
    page-break-inside: avoid;
  }}
  .figure-box img {{
    max-width: 95%;
    height: auto;
  }}
  .figure-caption {{
    font-size: 8.5pt;
    font-style: italic;
    margin-top: 4px;
    color: #222222;
  }}
  .references p {{
    text-indent: -1.8em;
    padding-left: 1.8em;
    font-size: 9pt;
    margin-bottom: 4px;
    line-height: 1.3;
  }}
</style>
</head>
<body>

<h1>Dynamic Risk Preferences, Loss Chasing, and Reference-Dependent Stopping in Repeated Contests: Field Evidence from Online Poker</h1>

<div class="authors">Atanas Bobev</div>

<div class="abstract-container">
  <div class="abstract-label">Abstract</div>
  We examine how dynamic within-session wealth fluctuations alter risk-taking and session termination decisions in repeated contests. Analyzing 4,070,556 hand-level decisions across 119,584 completed sessions from the University of Alberta Computer Poker Research Group archive (1995–1997), we exploit continuous bankroll tracking within an environment where objective probabilities are governed by invariant combinatorial rules. Controlling for player fixed effects, table stakes, position, and time-on-task, we identify two distinct behavioral regimes. In the gain domain, competitors exhibit a house money effect: accumulated profits increase voluntary pot entry (VPIP, +0.59 percentage points, p &lt; 0.001), preflop raising (+0.27 percentage points, p = 0.003), and absolute wager sizes (+0.57 chips per 100 chips gained, p &lt; 0.001). In the loss domain, increasing cumulative deficits trigger systematic loss chasing: holding current stack size constant, each 100 chips of deficit increases absolute bet sizes by +0.99 chips (p &lt; 0.001) and escalates the bet-to-stack ratio (t = 15.52, p &lt; 10<sup>-50</sup>). At the session level, termination choices exhibit sharp reference dependence. Players display an acute "never quit on a win" asymmetry: the per-hand exit hazard is 0.36% immediately following a winning hand, compared to 2.48% after a loss and 5.02% after uncontested folds. Furthermore, 1,340 sessions terminate at exact net break-even (W = 0), with active round-trip clawbacks accounting for 54.9% of these exits. While capital constraints truncate losing sessions on average, surviving losing sessions display pronounced right-tail persistence, consistent with selective sunk-cost chasing. Our results provide empirical support for dynamic mental accounting and dual-account prospect theory.
  <div class="keywords">
    <strong>Keywords:</strong> Reference-dependent preferences, House money effect, Loss chasing, Stopping rules, Dynamic labor supply, Contest theory, Field data.<br>
    <strong>JEL Classifications:</strong> D81, D91, C93, G41.
  </div>
</div>

<h2>1. Introduction</h2>
<p>Standard neoclassical expected utility theory posits that risk preferences are defined over final wealth states. For small-to-moderate stakes encountered in daily market transactions, consumption gambles, or repeated contests, plausible utility functions are approximately linear, implying risk-neutral marginal behavior (Rabin, 2000). Contrary to this benchmark, field and laboratory evidence shows that individuals frequently alter their willingness to bear risk based on recent path-dependent outcomes (Thaler and Johnson, 1990; Post et al., 2008; Barberis, 2012).</p>

<p>Two primary behavioral frameworks explain such path dependence. First, under mental accounting (Thaler, 1985; Thaler and Johnson, 1990), individuals segregate recent gains from baseline wealth. Prior earnings are treated as "house money," attenuating the perceived disutility of subsequent losses and encouraging risk-taking. Second, prospect theory (Kahneman and Tversky, 1979) specifies an S-shaped value function characterized by loss aversion (&lambda; &gt; 1) and convexity in the negative domain. When individuals accumulate paper losses that have not yet been formally realized, diminishing sensitivity can induce risk-seeking gambles aimed at recovering the initial endowment (the break-even effect; Imas, 2016).</p>

<p>Simultaneously, dynamic risk environments require agents to make endogenous <em>stopping decisions</em>: deciding when to cease participation. Analogous to daily labor supply choices among independent contractors (Camerer et al., 1997; Farber, 2005, 2008, 2015), repeated contest participants must weigh the marginal utility of continuation against physical or cognitive fatigue. When agents evaluate performance relative to an intra-session reference point—most saliently, breaking even (<em>W</em> = 0)—stopping probabilities should exhibit sharp structural discontinuities around the reference threshold.</p>

<p>This paper uses microdata from the Computer Poker Research Group (CPRG) at the University of Alberta (Billings et al., 2002) to examine dynamic risk preferences and stopping behavior. Covering 4,070,556 hand-level decisions across 119,584 continuous playing sessions between April 1995 and March 1997, online Texas Hold'em provides an ideal institutional environment: cards are drawn with fixed combinatorial odds, actions are tracked with micro-level precision, and the historical IRC platform operated with zero house rake.</p>

<h2>2. Institutional Setting and Data</h2>
<p>The University of Alberta CPRG database archives logs from public Internet Relay Chat (IRC) poker channels (<code>#holdem</code>) active between 1995 and 2001 (Billings et al., 2002). Games implemented standard Texas Hold'em rules with automated dealer bots. Stakes followed fixed-limit structures (typically 5/10, 10/20, or 20/40 chips). While chips were virtual, player bankrolls were persistent across sessions and publicly ranked on an official ladder, providing non-trivial reputational incentives and finite endowments analogous to laboratory tokens and competitive sports rating systems.</p>

<p>Following standard convention (Narayanan and Manchanda, 2012), an inactivity gap exceeding 20 minutes (1,200 seconds) defines session boundaries. We restrict analysis to sessions with at least 5 hands, positive initial stack, and hand index &le; 400. Table 1 reports descriptive statistics.</p>

<div class="table-title">Table 1: Descriptive Statistics of Hand Decisions and Completed Sessions</div>
<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Mean</th>
      <th>Std. Dev.</th>
      <th>Min</th>
      <th>Max</th>
    </tr>
  </thead>
  <tbody>
    <tr class="subhead"><td colspan="5">Panel A: Hand-Level Decisions (N = 4,070,556; Players = 5,944)</td></tr>
    <tr><td>Voluntary Pot Entry (VPIP)</td><td>0.4524</td><td>0.4977</td><td>0.0000</td><td>1.0000</td></tr>
    <tr><td>Preflop Raise (PFR)</td><td>0.1135</td><td>0.3172</td><td>0.0000</td><td>1.0000</td></tr>
    <tr><td>Postflop Aggression</td><td>0.2628</td><td>0.4402</td><td>0.0000</td><td>1.0000</td></tr>
    <tr><td>Total Bet Amount (Chips)</td><td>24.3442</td><td>37.5192</td><td>0.0000</td><td>1200.0000</td></tr>
    <tr><td>Bet Fraction of Stack</td><td>0.0236</td><td>0.0641</td><td>0.0000</td><td>1.0000</td></tr>
    <tr><td>Reached Showdown</td><td>0.2176</td><td>0.4126</td><td>0.0000</td><td>1.0000</td></tr>
    <tr><td>Cumulative Session PnL (<em>W<sub>ist</sub></em>)</td><td>24.7853</td><td>376.6639</td><td>-23175.00</td><td>13240.00</td></tr>
    <tr class="subhead"><td colspan="5">Panel B: Completed Sessions (N = 119,584 Completed Sessions)</td></tr>
    <tr><td>Session Duration (Minutes)</td><td>38.3625</td><td>41.0449</td><td>1.0000</td><td>580.0000</td></tr>
    <tr><td>Hands Played per Session</td><td>34.0393</td><td>43.3057</td><td>5.0000</td><td>400.0000</td></tr>
    <tr><td>Final Session Outcome (<em>W<sub>exit</sub></em>)</td><td>2.6418</td><td>382.8946</td><td>-23175.00</td><td>13240.00</td></tr>
    <tr><td>Winning Sessions Share</td><td>0.4480</td><td>0.4973</td><td>0.0000</td><td>1.0000</td></tr>
    <tr><td>Losing Sessions Share</td><td>0.5408</td><td>0.4983</td><td>0.0000</td><td>1.0000</td></tr>
    <tr><td>Exact Break-Even Share (<em>W</em> = 0)</td><td>0.0112</td><td>0.1053</td><td>0.0000</td><td>1.0000</td></tr>
    <tr class="table-bottom"><td>Near Break-Even Share (|<em>W</em>| &le; 10)</td><td>0.0456</td><td>0.2085</td><td>0.0000</td><td>1.0000</td></tr>
  </tbody>
</table>
<div class="table-notes">Notes: Data source is the University of Alberta CPRG database (1995–1997). VPIP equals 1 if player called, bet, or raised preflop. Aggression equals 1 if player bet or raised on flop, turn, or river. Session inactivity cutoff is 20 minutes.</div>

<h2>3. Empirical Strategy and Results: The House Money Effect and Loss Chasing</h2>
<p>To evaluate how within-session wealth dynamics alter risk-taking, we estimate linear panel regressions with player fixed effects. This absorbs time-invariant unobserved player heterogeneity such as baseline skill and intrinsic risk tolerance:</p>

<p class="no-indent" style="text-align: center; margin: 10px 0;">
  <em>Y<sub>ist</sub></em> = &alpha;<sub><em>i</em></sub> + &beta;<sub>1</sub> InGain<sub><em>ist</em></sub> + &beta;<sub>2</sub> (<em>W</em><sup>+</sup><sub><em>ist</em></sub>/100) + &beta;<sub>3</sub> InLoss<sub><em>ist</em></sub> + &beta;<sub>4</sub> (<em>W</em><sup>-</sup><sub><em>ist</em></sub>/100) + &theta; ln(Stack<sub><em>ist</em></sub>) + <strong>X</strong>'<sub><em>ist</em></sub> &gamma; + &epsilon;<sub><em>ist</em></sub>
</p>

<p>where <em>Y<sub>ist</sub></em> represents VPIP, PFR, Aggression, Absolute Bet Amount in chips, or Bet-to-Stack ratio. Controlling for ln(Stack<sub><em>ist</em></sub>) is vital to ensure that bet fraction dynamics are not mechanical artifacts of shrinking chip balances.</p>

<div class="table-title">Table 2: Player Fixed Effects Estimates of Within-Session Wealth on Risk-Taking</div>
<table>
  <thead>
    <tr>
      <th>Independent Variables</th>
      <th>(1) VPIP</th>
      <th>(2) PFR</th>
      <th>(3) Aggression</th>
      <th>(4) Bet Amount</th>
      <th>(5) Bet/Stack</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>In Gain Domain</td>
      <td>0.00587***<br>(0.00141)</td>
      <td>0.00269***<br>(0.00090)</td>
      <td>0.00341***<br>(0.00119)</td>
      <td>-0.37644<br>(0.23752)</td>
      <td>-0.00130***<br>(0.00019)</td>
    </tr>
    <tr>
      <td>Gain Magnitude (<em>W</em><sup>+</sup> / 100)</td>
      <td>0.00118***<br>(0.00026)</td>
      <td>0.00038*<br>(0.00022)</td>
      <td>0.00055**<br>(0.00024)</td>
      <td>0.57122***<br>(0.10883)</td>
      <td>0.00058***<br>(0.00007)</td>
    </tr>
    <tr>
      <td>In Loss Domain</td>
      <td>0.00501***<br>(0.00148)</td>
      <td>0.00214**<br>(0.00103)</td>
      <td>0.00222*<br>(0.00119)</td>
      <td>-0.34883<br>(0.23035)</td>
      <td>-0.00220***<br>(0.00035)</td>
    </tr>
    <tr>
      <td>Loss Magnitude (<em>W</em><sup>-</sup> / 100)</td>
      <td>0.00404***<br>(0.00061)</td>
      <td>0.00420***<br>(0.00055)</td>
      <td>0.00367***<br>(0.00049)</td>
      <td>0.98960***<br>(0.15046)</td>
      <td>0.00352***<br>(0.00023)</td>
    </tr>
    <tr>
      <td>Log Current Stack</td>
      <td>-0.01059***<br>(0.00147)</td>
      <td>-0.00464***<br>(0.00116)</td>
      <td>-0.00578***<br>(0.00112)</td>
      <td>-0.44138***<br>(0.09625)</td>
      <td>-0.02826***<br>(0.00147)</td>
    </tr>
    <tr>
      <td>Hand Index / 10</td>
      <td>-0.00018<br>(0.00016)</td>
      <td>0.00050***<br>(0.00012)</td>
      <td>0.00014<br>(0.00013)</td>
      <td>-0.13945***<br>(0.02583)</td>
      <td>-0.00050***<br>(0.00004)</td>
    </tr>
    <tr class="subhead"><td colspan="6">Controls and Diagnostics</td></tr>
    <tr><td>Position &amp; Table Size Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
    <tr><td>Player Fixed Effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
    <tr><td>Observations</td><td>3,999,153</td><td>3,999,153</td><td>3,999,153</td><td>3,999,153</td><td>3,999,153</td></tr>
    <tr><td>Unique Players</td><td>3,695</td><td>3,695</td><td>3,695</td><td>3,695</td><td>3,695</td></tr>
    <tr class="table-bottom"><td>Within R-squared</td><td>0.0419</td><td>0.0155</td><td>0.0210</td><td>0.0133</td><td>0.1406</td></tr>
  </tbody>
</table>
<div class="table-notes">Notes: Standard errors clustered at the player level in parentheses. Sample restricted to players with &ge; 50 hands. *** p &lt; 0.01, ** p &lt; 0.05, * p &lt; 0.10.</div>

<div class="figure-box">
  <img src="{fig1_b64}" alt="Figure 1: House Money Curve">
  <div class="figure-caption">Figure 1: Risk-Taking (VPIP and Bet Sizing) Across Cumulative Session Wealth States</div>
</div>

<p>The estimates in Table 2 establish the house money effect. In Column (1), entering the gain domain raises VPIP by +0.59 percentage points (<em>p</em> &lt; 0.001), while preflop raising rises by +0.27 percentage points (<em>p</em> = 0.003). In Column (4), each 100 chips of accumulated profit increases absolute bet sizes by +0.571 chips (<em>p</em> &lt; 0.001). Conversely, in the loss domain, deepening deficits trigger systematic loss chasing: each 100 chips of deficit increases absolute bet sizing by +0.990 chips (<em>p</em> &lt; 0.001) and escalates the bet-to-stack ratio (<em>t</em> = 15.52, <em>p</em> &lt; 10<sup>-50</sup>), as illustrated in Figure 1.</p>

<h2>4. Empirical Results: Stopping Rules and the Break-Even Reference Point</h2>
<p>Figure 2 tests for cognitive bunching at session termination across 4-chip bins spanning [-100, +100].</p>

<div class="figure-box">
  <img src="{fig2_b64}" alt="Figure 2: Break-Even Bunching">
  <div class="figure-caption">Figure 2: Distribution of Session Exit Wealth: Discontinuity at the Break-Even Reference Point</div>
</div>

<p>As shown in Figure 2, the density exhibits a sharp mass spike at exactly zero net profit/loss (1,340 sessions), yielding an excess mass ratio of <em>b</em> = +0.284 (<em>p</em> &lt; 0.001). Decomposing these episodes reveals that active clawbacks account for 54.9% (735 sessions) of exact break-even terminations, with an average duration of only 18.2 hands (20.5 minutes), roughly half the sample mean of 37.8 hands. Players actively truncate play upon recovering deficits.</p>

<div class="table-title">Table 3: Empirical Session Termination Hazard by Preceding Hand Outcome</div>
<table>
  <thead>
    <tr>
      <th>Preceding Hand Outcome</th>
      <th>Hand Opportunities</th>
      <th>Observed Quits</th>
      <th>Termination Hazard Rate <em>h</em>(<em>t</em>)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Winning Hand (Hand PnL &gt; 0)</td><td>791,823</td><td>2,841</td><td>0.0036 (0.36%)</td></tr>
    <tr><td>Losing Hand (Hand PnL &lt; 0)</td><td>1,882,645</td><td>46,687</td><td>0.0248 (2.48%)</td></tr>
    <tr class="table-bottom"><td>Neutral Fold (Hand PnL = 0)</td><td>1,396,088</td><td>70,056</td><td>0.0502 (5.02%)</td></tr>
  </tbody>
</table>
<div class="table-notes">Notes: Per-hand conditional quit hazard conditional on the outcome of the immediate preceding hand.</div>

<div class="figure-box">
  <img src="{fig3_b64}" alt="Figure 3: Stopping Hazard">
  <div class="figure-caption">Figure 3: Conditional Session Termination Hazard Across Wealth States</div>
</div>

<p>Table 3 and Figure 3 uncover an acute "never quit on a win" asymmetry: the per-hand termination hazard is only 0.36% immediately following a winning hand, compared to 2.48% after a loss and 5.02% after folds. Winning hands reinforce the desire to continue playing.</p>

<div class="figure-box">
  <img src="{fig4_b64}" alt="Figure 4: Asymmetric Duration">
  <div class="figure-caption">Figure 4: Session Duration and Length by Final Outcome (Voluntary Exits Only)</div>
</div>

<p>Finally, Figure 4 demonstrates that while capital constraints truncate losing sessions on average (30.2 hands vs. 37.8 hands for winning sessions), voluntary losing exits exhibit a prominent right tail, consistent with selective sunk-cost chasing among trailing players.</p>

<h2>5. Conclusion</h2>
<p>Using a census of four million hand decisions from online poker, we document a robust house money effect in gains, alongside intense loss chasing as cumulative deficits deepen. Furthermore, session termination is governed by reference-dependent heuristics: players bunch at the exact break-even threshold (<em>W</em> = 0) and exhibit a pronounced reluctance to walk away following a win. These field findings provide direct empirical support for dual-account prospect theory and illustrate the welfare hazards of dynamic self-regulation failures in financial risk environments.</p>

<h2>References</h2>
<div class="references">
  <p>Barberis, N. (2012). A model of casino gambling. <em>Management Science</em>, 58(1), 35–51.</p>
  <p>Billings, D., Davidson, A., Schaeffer, J., &amp; Szafron, D. (2002). The challenge of poker. <em>Artificial Intelligence</em>, 134(1–2), 201–240.</p>
  <p>Camerer, C., Babcock, L., Loewenstein, G., &amp; Thaler, R. (1997). Labor supply of New York City cabdrivers: One day at a time. <em>Quarterly Journal of Economics</em>, 112(2), 407–441.</p>
  <p>Chetty, R., Friedman, J. N., Olsen, T., &amp; Pistaferri, L. (2011). Adjustment costs, firm responses, and micro vs. macro labor supply elasticities: Evidence from Danish tax records. <em>Quarterly Journal of Economics</em>, 126(2), 749–804.</p>
  <p>Farber, H. S. (2005). Is labor supply of taxi drivers really backward-bending? Empirical evidence. <em>Journal of Political Economy</em>, 113(4), 857–882.</p>
  <p>Farber, H. S. (2008). Reference-dependent preferences and labor supply: The case of New York City taxi drivers. <em>American Economic Review</em>, 98(3), 1069–1082.</p>
  <p>Farber, H. S. (2015). Why you can't find a taxi in the rain, and other labor supply puzzles. <em>Quarterly Journal of Economics</em>, 130(4), 1975–2026.</p>
  <p>Imas, A. (2016). The realization effect: A test of how realized versus paper outcomes affect risk taking. <em>American Economic Review</em>, 106(8), 2086–2109.</p>
  <p>Kahneman, D., &amp; Tversky, A. (1979). Prospect theory: An analysis of decision under risk. <em>Econometrica</em>, 47(2), 263–291.</p>
  <p>McCrary, J. (2008). Manipulation of the running variable in the regression discontinuity design: A density test. <em>Journal of Econometrics</em>, 142(2), 698–714.</p>
  <p>Narayanan, S., &amp; Manchanda, P. (2012). An empirical analysis of individual-level casino gambling behavior. <em>Quantitative Marketing and Economics</em>, 10(3), 361–402.</p>
  <p>Post, T., Van den Assem, M. J., Baltussen, G., &amp; Thaler, R. H. (2008). Deal or no deal? Decision making under risk in a large-payoff game show. <em>American Economic Review</em>, 98(1), 38–71.</p>
  <p>Rabin, M. (2000). Risk aversion and expected-utility theory: A calibration theorem. <em>Econometrica</em>, 68(5), 1281–1292.</p>
  <p>Thaler, R. H. (1985). Mental accounting and consumer choice. <em>Marketing Science</em>, 4(3), 199–214.</p>
  <p>Thaler, R. H., &amp; Johnson, E. J. (1990). Gambling with the house money and trying to break even: The effects of prior outcomes on risky choice. <em>Management Science</em>, 36(6), 643–660.</p>
</div>

</body>
</html>
"""

html_path = r'C:\Users\Z09057\poker-behavioral-economics\paper\manuscript_print.html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

out_pdf = r'C:\Users\Z09057\poker-behavioral-economics\paper\Dynamic_Risk_Preferences_Poker_Economics.pdf'

edge_paths = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]
edge_bin = None
for p in edge_paths:
    if os.path.exists(p):
        edge_bin = p
        break

if edge_bin:
    cmd = [
        edge_bin,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={out_pdf}",
        f"file:///{html_path.replace(os.sep, '/')}"
    ]
    subprocess.run(cmd, check=True)
    print(f"Successfully compiled humanized PDF at {out_pdf}")

    dl_path = os.path.expanduser('~/Downloads/Dynamic_Risk_Preferences_Poker_Economics.pdf')
    shutil.copy2(out_pdf, dl_path)
    print(f"Copied humanized PDF to {dl_path}")
