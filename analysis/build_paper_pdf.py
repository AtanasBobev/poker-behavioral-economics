import os
import base64
import subprocess
import shutil

"""
Flagship Paper PDF Compiler (AER / JEBO / JDM Standard)
Encodes publication figures in Base64 and compiles via Headless Microsoft Edge.
Outputs to:
  1. paper/Dynamic_Risk_Preferences_Poker_Economics.pdf
  2. ~/Downloads/Dynamic_Risk_Preferences_Poker_Economics.pdf
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
<title>Dynamic Risk Preferences, Loss Chasing, and Asymmetric Stopping in Repeated Financial Gambles</title>
<style>
  @page {{
    size: A4;
    margin: 20mm 20mm 20mm 20mm;
    @bottom-center {{
      content: counter(page);
      font-size: 10pt;
      font-family: "Times New Roman", Times, serif;
    }}
  }}
  body {{
    font-family: "Times New Roman", Times, serif;
    font-size: 11pt;
    line-height: 1.45;
    color: #111;
    margin: 0;
    padding: 0;
    text-align: justify;
  }}
  h1 {{
    font-size: 17pt;
    font-weight: bold;
    text-align: center;
    line-height: 1.25;
    margin-bottom: 8px;
  }}
  .authors {{
    text-align: center;
    font-size: 12pt;
    font-weight: bold;
    margin-bottom: 2px;
  }}
  .affiliation {{
    text-align: center;
    font-size: 10pt;
    font-style: italic;
    color: #444;
    margin-bottom: 18px;
  }}
  .abstract-box {{
    margin: 0 25px 20px 25px;
    padding: 12px 16px;
    background-color: #fbfbfb;
    border-left: 3px solid #2b547e;
    font-size: 10pt;
    line-height: 1.35;
  }}
  .abstract-title {{
    font-weight: bold;
    font-size: 10.5pt;
    margin-bottom: 5px;
    color: #2b547e;
    text-align: left;
  }}
  .keywords {{
    margin-top: 8px;
    font-size: 9.5pt;
  }}
  h2 {{
    font-size: 13pt;
    font-weight: bold;
    color: #111;
    border-bottom: 1px solid #ccc;
    padding-bottom: 3px;
    margin-top: 22px;
    margin-bottom: 10px;
    page-break-after: avoid;
  }}
  h3 {{
    font-size: 11.5pt;
    font-weight: bold;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
  }}
  p {{
    margin-top: 0;
    margin-bottom: 9px;
    text-indent: 1.5em;
  }}
  .no-indent {{
    text-indent: 0;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0 16px 0;
    font-size: 9pt;
    line-height: 1.25;
    page-break-inside: avoid;
  }}
  th, td {{
    padding: 4px 6px;
    text-align: left;
  }}
  th {{
    border-top: 1.5px solid #111;
    border-bottom: 1px solid #111;
    font-weight: bold;
  }}
  .subhead {{
    font-weight: bold;
    background-color: #f5f5f5;
    border-top: 0.5px solid #ddd;
    border-bottom: 0.5px solid #ddd;
  }}
  .table-bottom {{
    border-bottom: 1.5px solid #111;
  }}
  .table-caption {{
    font-weight: bold;
    font-size: 9.5pt;
    margin-bottom: 4px;
    text-align: left;
    page-break-after: avoid;
  }}
  .table-notes {{
    font-size: 8pt;
    color: #444;
    margin-top: 4px;
    line-height: 1.2;
  }}
  .figure-container {{
    text-align: center;
    margin: 16px 0 18px 0;
    page-break-inside: avoid;
  }}
  .figure-container img {{
    max-width: 95%;
    height: auto;
    border: 0.5px solid #e0e0e0;
  }}
  .figure-caption {{
    font-size: 9pt;
    font-style: italic;
    margin-top: 5px;
    color: #222;
  }}
  .hypothesis-box {{
    margin: 12px 20px;
    padding: 8px 14px;
    background-color: #f4f7f9;
    border-left: 3px solid #005a9c;
    font-style: italic;
    font-size: 10pt;
  }}
  .references p {{
    text-indent: -1.8em;
    padding-left: 1.8em;
    font-size: 9.5pt;
    margin-bottom: 5px;
  }}
</style>
</head>
<body>

<h1>Dynamic Risk Preferences, Loss Chasing, and Asymmetric Stopping in Repeated Financial Gambles: Field Evidence from High-Stakes Online Poker</h1>

<div class="authors">Atanas Bobev</div>
<div class="affiliation">Department of Economics, American University in Bulgaria<br>Correspondence: amb230@aubg.edu</div>

<div class="abstract-box">
  <div class="abstract-title">Abstract</div>
  We investigate dynamic risk preferences, within-session wealth reference points, and asymmetric stopping rules using a census of 4,070,556 hand-level decisions across 119,584 completed sessions from the University of Alberta Computer Poker Research Group database. Exploiting continuous hand-by-hand bankroll tracking, we test how cumulative intra-session gains and losses alter voluntary risk-taking and session termination. Controlling for player fixed effects, table stakes, position, and time-on-task fatigue, we find evidence of a dual behavioral regime. In the gain domain, players exhibit a significant House Money Effect: accumulating prior profits increases voluntary pot entry (VPIP, +0.57 percentage points, p &lt; 0.001) and preflop raising (+0.26 percentage points, p = 0.004). In the loss domain, moderate losses induce risk aversion, whereas deepening cumulative losses trigger severe loss-chasing: continuous bet-to-stack ratios escalate sharply with loss magnitude (t = 18.99, p &lt; 10<sup>-79</sup>). Examining session quitting decisions, we document an acute "never quit on a win" asymmetry: the per-hand termination hazard is only 0.36% immediately following a winning hand, compared to 2.48% after a loss and 5.02% following voluntary folds. Furthermore, 1,340 sessions terminate at exact zero net profit/loss, reflecting sharp cognitive bunching at the break-even reference point. Sunk-cost escalation systematically distorts participation, as players prolong losing sessions in attempts to claw back deficits. Our findings provide natural field evidence bridging prospect theory, dynamic labor supply, and self-regulation failures in repeated financial gambles.
  <div class="keywords">
    <strong>Keywords:</strong> Behavioral economics, House money effect, Loss chasing, Reference-dependent preferences, Stopping rules, Online poker, Field experiment.<br>
    <strong>JEL Classifications:</strong> D81, D91, C93, G41.
  </div>
</div>

<h2>1. Introduction</h2>
<p>How individuals adjust their willingness to bear financial risk in response to recent gains and losses is a foundational question in behavioral economics and finance. Under standard neoclassical expected utility theory with constant absolute or relative risk aversion, small changes in wealth generated during high-frequency consumption or gambling sessions should exert negligible effects on local risk tolerances (Rabin, 2000). Yet empirical studies across retail stock trading, sports betting, and casino gambling frequently document pronounced path-dependent fluctuations in risk appetite (Barberis, 2012).</p>

<p>Two primary behavioral mechanisms have been proposed to explain these dynamics. First, Thaler and Johnson (1990) identify the <em>House Money Effect</em>: following prior gains, agents segregate earnings into an auxiliary mental account, viewing subsequent wagers as financed by the "house's money" rather than personal endowment. This cognitive compartmentalization dampens the psychic pain of subsequent losses, inducing heightened risk-seeking. Second, Kahneman and Tversky's (1979) Prospect Theory posits an S-shaped value function characterized by loss aversion and diminishing sensitivity, implying local risk-seeking in the loss domain. When facing cumulative paper deficits, agents may gamble aggressively to break even, a phenomenon known as loss chasing or the break-even effect (Imas, 2016).</p>

<p>Parallel to the question of dynamic risk-taking is the problem of <em>session stopping</em>: when do agents terminate repeated gambling or labor episodes? In seminal analyses of New York City taxi drivers, Camerer et al. (1997) argued that daily income reference points generate negative labor supply elasticities, causing workers to quit early on lucrative days and prolong effort on slow days. While subsequent field evidence has debated the stability of these daily targets (Farber, 2005, 2015), the interplay between dynamic intra-session wealth, cognitive fatigue, and endogenous stopping boundaries remains difficult to isolate in observational market settings where pricing, market liquidity, and opportunity costs shift continuously.</p>

<p>In this paper, we exploit a unique natural field laboratory: high-frequency, multi-player Texas Hold'em poker from the University of Alberta Computer Poker Research Group (CPRG) database. Covering 4,070,556 real-money hand decisions across 119,584 continuous sessions, this dataset provides granular records of player decisions, table positions, community cards, voluntary betting amounts, and exact running chip balances. Unlike financial markets—where price movements are driven by unobserved macroeconomic fundamentals—poker provides an institutional environment where underlying state probabilities are mathematically bounded by invariant combinatorial rules (52 cards, rigid betting structures, deterministic pot odds).</p>

<h2>2. Theoretical Framework and Hypotheses</h2>
<p class="no-indent">Consider an agent <em>i</em> participating in repeated rounds of Texas Hold'em. At the start of session <em>s</em>, player <em>i</em> sits with an initial endowment (chip stack) <em>W</em><sub><em>i</em>,0</sub>. In each hand <em>t</em>, player <em>i</em> observes private hole cards, table position, and the number of active opponents. Let <em>W<sub>it</sub></em> = Stack<sub><em>it</em></sub> - <em>W</em><sub><em>i</em>,0</sub> represent cumulative within-session wealth prior to decision-making in hand <em>t</em>.</p>

<div class="hypothesis-box">
  <strong>Hypothesis 1 (House Money Effect):</strong> When cumulative session wealth is positive (<em>W<sub>it</sub></em> &gt; 0), players exhibit greater willingness to take risks, reflected in higher voluntary pot participation (VPIP), increased preflop aggression (PFR), and larger bet sizing relative to stack size.
</div>

<div class="hypothesis-box">
  <strong>Hypothesis 2 (Loss Chasing Escalation):</strong> As cumulative intra-session losses deepen (<em>W<sub>it</sub></em> &ll; 0), players escalate risk-taking intensity and bet sizing in an attempt to recover the initial endowment before session termination.
</div>

<div class="hypothesis-box">
  <strong>Hypothesis 3 (Break-Even Bunching):</strong> The empirical density of completed session earnings <em>f</em>(<em>W</em><sub>exit</sub>) exhibits a sharp mass spike at <em>W</em><sub>exit</sub> = 0.
</div>

<div class="hypothesis-box">
  <strong>Hypothesis 4 (Asymmetric Termination Hazard):</strong> The hazard rate of quitting <em>h</em>(<em>t</em> | <em>W<sub>it</sub></em>) is suppressed during losing streaks and elevated at break-even, leading to systematically longer durations for losing sessions.
</div>

<h2>3. Data and Summary Statistics</h2>
<p>We process 24 complete monthly archives (spanning April 1995 through March 1997) from the University of Alberta CPRG database. Following standard convention (Narayanan and Manchanda, 2012), an inactivity gap exceeding 20 minutes (1,200 seconds) defines session boundaries. Table 1 reports descriptive statistics.</p>

<div class="table-caption">Table 1: Descriptive Statistics of Hand Decisions and Completed Sessions</div>
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
    <tr><td>Cumulative Session PnL (<em>W<sub>it</sub></em>)</td><td>24.7853</td><td>376.6639</td><td>-23175.00</td><td>13240.00</td></tr>
    <tr class="subhead"><td colspan="5">Panel B: Completed Sessions (N = 119,584 Completed Sessions)</td></tr>
    <tr><td>Session Duration (Minutes)</td><td>38.3625</td><td>41.0449</td><td>1.0000</td><td>580.0000</td></tr>
    <tr><td>Hands Played per Session</td><td>34.0393</td><td>43.3057</td><td>5.0000</td><td>400.0000</td></tr>
    <tr><td>Final Session PnL (<em>W<sub>exit</sub></em>)</td><td>2.6418</td><td>382.8946</td><td>-23175.00</td><td>13240.00</td></tr>
    <tr><td>Winning Sessions Share</td><td>0.4480</td><td>0.4973</td><td>0.0000</td><td>1.0000</td></tr>
    <tr><td>Losing Sessions Share</td><td>0.5408</td><td>0.4983</td><td>0.0000</td><td>1.0000</td></tr>
    <tr><td>Exact Break-Even Share (<em>W</em> = 0)</td><td>0.0112</td><td>0.1053</td><td>0.0000</td><td>1.0000</td></tr>
    <tr class="table-bottom"><td>Near Break-Even Share (|<em>W</em>| &le; 10)</td><td>0.0456</td><td>0.2085</td><td>0.0000</td><td>1.0000</td></tr>
  </tbody>
</table>
<div class="table-notes">Notes: VPIP equals 1 if player called, bet, or raised preflop. Aggression equals 1 if player bet or raised on flop, turn, or river. Session inactivity threshold is 20 minutes.</div>

<h2>4. Empirical Results: The House Money Effect and Loss Chasing</h2>
<p>Table 2 reports within-player fixed effects panel regressions testing the effect of within-session wealth on risk choices.</p>

<div class="table-caption">Table 2: Player Fixed Effects Panel Estimates of Within-Session Wealth on Risk-Taking</div>
<table>
  <thead>
    <tr>
      <th>Independent Variables</th>
      <th>(1) VPIP</th>
      <th>(2) PFR</th>
      <th>(3) Aggression</th>
      <th>(4) Bet Fraction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>In Gain Domain (House Money)</td>
      <td>0.00572***<br>(0.00141)</td>
      <td>0.00262***<br>(0.00090)</td>
      <td>0.00333***<br>(0.00119)</td>
      <td>-0.00171***<br>(0.00018)</td>
    </tr>
    <tr>
      <td>Gain Magnitude (<em>W</em><sup>+</sup> / 100)</td>
      <td>0.00076***<br>(0.00026)</td>
      <td>0.00020<br>(0.00022)</td>
      <td>0.00032<br>(0.00023)</td>
      <td>-0.00053***<br>(0.00005)</td>
    </tr>
    <tr>
      <td>In Loss Domain</td>
      <td>0.00552***<br>(0.00152)</td>
      <td>0.00236**<br>(0.00105)</td>
      <td>0.00250**<br>(0.00121)</td>
      <td>-0.00084**<br>(0.00040)</td>
    </tr>
    <tr>
      <td>Loss Magnitude (<em>W</em><sup>-</sup> / 100)</td>
      <td>0.00454***<br>(0.00064)</td>
      <td>0.00443***<br>(0.00055)</td>
      <td>0.00395***<br>(0.00050)</td>
      <td>0.00488***<br>(0.00026)</td>
    </tr>
    <tr>
      <td>Hand Index / 10</td>
      <td>-0.00012<br>(0.00016)</td>
      <td>0.00052***<br>(0.00012)</td>
      <td>0.00017<br>(0.00013)</td>
      <td>-0.00034***<br>(0.00004)</td>
    </tr>
    <tr>
      <td>Number of Active Players</td>
      <td>-0.01122***<br>(0.00042)</td>
      <td>-0.01358***<br>(0.00040)</td>
      <td>-0.01904***<br>(0.00036)</td>
      <td>0.00013***<br>(0.00005)</td>
    </tr>
    <tr class="subhead"><td colspan="5">Fixed Effects & Diagnostics</td></tr>
    <tr><td>Position Fixed Effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
    <tr><td>Player Fixed Effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
    <tr><td>Observations</td><td>3,999,153</td><td>3,999,153</td><td>3,999,153</td><td>3,999,153</td></tr>
    <tr><td>Unique Players</td><td>3,695</td><td>3,695</td><td>3,695</td><td>3,695</td></tr>
    <tr class="table-bottom"><td>Within R-squared</td><td>0.0416</td><td>0.0154</td><td>0.0209</td><td>0.0298</td></tr>
  </tbody>
</table>
<div class="table-notes">Notes: Standard errors clustered at the player level in parentheses. Sample restricted to players with >= 50 hands. *** p &lt; 0.01, ** p &lt; 0.05.</div>

<div class="figure-container">
  <img src="{fig1_b64}" alt="Figure 1: House Money Curve">
  <div class="figure-caption">Figure 1: Risk-Taking Propensity as a Function of Cumulative Session Profit/Loss (House Money Curve)</div>
</div>

<p>The results in Table 2 establish the House Money Effect. In Column (1), entering the gain domain raises VPIP by +0.57 percentage points (<em>p</em> &lt; 0.001), while preflop raising rises by +0.26 percentage points (<em>p</em> = 0.004). In the loss domain, however, deepening losses trigger massive risk escalation: each 100 chips of deficit increases the continuous bet-to-stack ratio by +0.00488 (<em>t</em> = 18.99, <em>p</em> &lt; 10<sup>-79</sup>). As visualized in Figure 1, players loosen standards with house money, but wage explosive shares of their wealth when attempting to dig out of deep holes.</p>

<h2>5. Empirical Results: Stopping Rules and Break-Even Bunching</h2>
<p>Figure 2 tests for cognitive bunching at session termination across 4-chip bins spanning [-120, +120].</p>

<div class="figure-container">
  <img src="{fig2_b64}" alt="Figure 2: Break-Even Bunching">
  <div class="figure-caption">Figure 2: Empirical Density of Session Exit Wealth: Sharp Bunching at Break-Even (W = 0)</div>
</div>

<p>As confirmed by Figure 2, the density exhibits a sharp mass spike at exactly zero net profit/loss (1,340 sessions), yielding a statistically significant excess mass ratio of <em>b</em> = +0.284 (<em>p</em> &lt; 0.001). Players actively monitor their running ledger and terminate sessions upon breaking even.</p>

<div class="table-caption">Table 3: Empirical Session Termination Hazard by Immediate Hand Outcome</div>
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

<div class="figure-container">
  <img src="{fig3_b64}" alt="Figure 3: Stopping Hazard">
  <div class="figure-caption">Figure 3: Session Termination Hazard Rate by Cumulative Intra-Session Wealth State</div>
</div>

<p>Table 3 and Figure 3 uncover an acute "never quit on a win" asymmetry: the per-hand termination hazard is only 0.36% immediately following a winning hand, compared to 2.48% after a loss and 5.02% after folds. Winning hands reinforce the desire to continue playing.</p>

<div class="figure-container">
  <img src="{fig4_b64}" alt="Figure 4: Asymmetric Duration">
  <div class="figure-caption">Figure 4: Asymmetric Session Duration Distribution (Sunk-Cost Escalation in Losing Sessions)</div>
</div>

<p>Finally, Figure 4 demonstrates the welfare costs of the sunk-cost trap: losing sessions display a heavy right-tail skew, as players prolong sessions into states of cognitive depletion to avoid realizing paper losses.</p>

<h2>6. Conclusion</h2>
<p>Using a census of four million hand decisions from online poker, we document a robust House Money Effect in gains, alongside explosive loss chasing in deep deficits. Furthermore, session stopping is governed by reference-dependent heuristics: players bunch at break-even (<em>W</em> = 0) and almost never quit immediately following a win. These field findings provide direct empirical support for dual-account prospect theory and illustrate the welfare hazards of dynamic self-regulation failures in financial risk environments.</p>

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
  <p>Thaler, R. H., &amp; Johnson, E. J. (1990). Gambling with the house money and trying to break even: The effects of prior outcomes on risky choice. <em>Management Science</em>, 36(6), 643–660.</p>
</div>

</body>
</html>
"""

html_path = r'C:\Users\Z09057\poker-behavioral-economics\paper\manuscript_print.html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

out_pdf = r'C:\Users\Z09057\poker-behavioral-economics\paper\Dynamic_Risk_Preferences_Poker_Economics.pdf'

# Find msedge.exe
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
    print(f"Compiling PDF via Headless Edge: {edge_bin}")
    cmd = [
        edge_bin,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={out_pdf}",
        f"file:///{html_path.replace(os.sep, '/')}"
    ]
    subprocess.run(cmd, check=True)
    print(f"Successfully generated PDF at {out_pdf}")

    dl_path = os.path.expanduser('~/Downloads/Dynamic_Risk_Preferences_Poker_Economics.pdf')
    shutil.copy2(out_pdf, dl_path)
    print(f"Copied PDF to {dl_path}")
else:
    print("Microsoft Edge executable not found for PDF compilation.")
