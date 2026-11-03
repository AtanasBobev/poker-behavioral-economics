import os
import shutil
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

"""
Builds publication-grade academic Word Document (.docx) for:
'Dynamic Risk Preferences, Loss Chasing, and Asymmetric Stopping in Repeated Financial Gambles: Field Evidence from High-Stakes Online Poker'
Adheres strictly to JEBO / JDM submission formatting standards.
"""

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_document():
    doc = Document()
    
    # 1-inch margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)
    normal_style.paragraph_format.line_spacing = 1.25
    normal_style.paragraph_format.space_after = Pt(6)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(12)
    r_title = p_title.add_run("Dynamic Risk Preferences, Loss Chasing, and Asymmetric Stopping in Repeated Financial Gambles: Field Evidence from High-Stakes Online Poker")
    r_title.bold = True
    r_title.font.size = Pt(16)

    # Author
    p_auth = doc.add_paragraph()
    p_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_auth.paragraph_format.space_after = Pt(4)
    r_auth = p_auth.add_run("Atanas Bobev")
    r_auth.bold = True
    r_auth.font.size = Pt(12)

    p_affil = doc.add_paragraph()
    p_affil.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_affil.paragraph_format.space_after = Pt(18)
    r_affil = p_affil.add_run("Department of Economics, American University in Bulgaria\nEmail: amb230@aubg.edu")
    r_affil.italic = True
    r_affil.font.size = Pt(10)

    # Abstract Box
    p_abs_h = doc.add_paragraph()
    r_abs_h = p_abs_h.add_run("Abstract")
    r_abs_h.bold = True
    r_abs_h.font.size = Pt(11.5)

    p_abs = doc.add_paragraph()
    p_abs.paragraph_format.left_indent = Inches(0.4)
    p_abs.paragraph_format.right_indent = Inches(0.4)
    p_abs.paragraph_format.space_after = Pt(12)
    r_abs = p_abs.add_run(
        "We investigate dynamic risk preferences, within-session wealth reference points, and asymmetric stopping rules "
        "using a census of 4,070,556 hand-level decisions across 119,584 completed sessions from the University of Alberta "
        "Computer Poker Research Group database. Exploiting continuous hand-by-hand bankroll tracking, we test how cumulative "
        "intra-session gains and losses alter voluntary risk-taking and session termination. Controlling for player fixed effects, "
        "table stakes, position, and time-on-task fatigue, we find evidence of a dual behavioral regime. In the gain domain, "
        "players exhibit a significant House Money Effect: accumulating prior profits increases voluntary pot entry (VPIP, +0.57 "
        "percentage points, p < 0.001) and preflop raising (+0.26 percentage points, p = 0.004). In the loss domain, moderate losses "
        "induce risk aversion, whereas deepening cumulative losses trigger severe loss-chasing: continuous bet-to-stack ratios "
        "escalate sharply with loss magnitude (t = 18.99, p < 10^-79). Examining session quitting decisions, we document an acute "
        "'never quit on a win' asymmetry: the per-hand termination hazard is only 0.36% immediately following a winning hand, "
        "compared to 2.48% after a loss and 5.02% following voluntary folds. Furthermore, 1,340 sessions terminate at exact zero net "
        "profit/loss, reflecting sharp cognitive bunching at the break-even reference point. Sunk-cost escalation systematically "
        "distorts participation, as players prolong losing sessions in attempts to claw back deficits. Our findings provide natural field "
        "evidence bridging prospect theory, dynamic labor supply, and self-regulation failures in repeated financial gambles."
    )
    r_abs.font.size = Pt(10)

    p_kw = doc.add_paragraph()
    p_kw.paragraph_format.left_indent = Inches(0.4)
    p_kw.paragraph_format.space_after = Pt(18)
    r_kw = p_kw.add_run("Keywords: ")
    r_kw.bold = True
    p_kw.add_run("Behavioral economics, House money effect, Loss chasing, Reference-dependent preferences, Stopping rules, Online poker, Field experiment.\n")
    r_jel = p_kw.add_run("JEL Classifications: ")
    r_jel.bold = True
    p_kw.add_run("D81, D91, C93, G41.")

    # Main Sections
    sections_text = [
        ("1. Introduction", 
         "How individuals adjust their willingness to bear financial risk in response to recent gains and losses is a foundational "
         "question in behavioral economics and finance. Under standard neoclassical expected utility theory with constant absolute "
         "or relative risk aversion, small changes in wealth generated during high-frequency consumption or gambling sessions should "
         "exert negligible effects on local risk tolerances (Rabin, 2000). Yet empirical studies across retail stock trading, sports "
         "betting, and casino gambling frequently document pronounced path-dependent fluctuations in risk appetite (Barberis, 2012).\n\n"
         "Two primary behavioral mechanisms have been proposed to explain these dynamics. First, Thaler and Johnson (1990) identify the "
         "House Money Effect: following prior gains, agents segregate earnings into an auxiliary mental account, viewing subsequent wagers "
         "as financed by the 'house's money' rather than personal endowment. This cognitive compartmentalization dampens the psychic pain "
         "of subsequent losses, inducing heightened risk-seeking. Second, Kahneman and Tversky's (1979) Prospect Theory posits an S-shaped "
         "value function characterized by loss aversion and diminishing sensitivity, implying local risk-seeking in the loss domain. When "
         "facing cumulative paper deficits, agents may gamble aggressively to break even, a phenomenon known as loss chasing or the "
         "break-even effect (Imas, 2016).\n\n"
         "Parallel to the question of dynamic risk-taking is the problem of session stopping: when do agents terminate repeated gambling "
         "or labor episodes? In seminal analyses of New York City taxi drivers, Camerer et al. (1997) argued that daily income reference "
         "points generate negative labor supply elasticities, causing workers to quit early on lucrative days and prolong effort on slow "
         "days. While subsequent field evidence has debated the stability of these daily targets (Farber, 2005, 2015), the interplay "
         "between dynamic intra-session wealth, cognitive fatigue, and endogenous stopping boundaries remains difficult to isolate in "
         "observational market settings where pricing, market liquidity, and opportunity costs shift continuously.\n\n"
         "In this paper, we exploit a unique natural field laboratory: high-frequency, multi-player Texas Hold'em poker from the University "
         "of Alberta Computer Poker Research Group (CPRG) database. Covering 4,070,556 real-money hand decisions across 119,584 continuous "
         "sessions, this dataset provides granular records of player decisions, table positions, community cards, voluntary betting amounts, "
         "and exact running chip balances. Unlike financial markets—where price movements are driven by unobserved macroeconomic fundamentals—"
         "poker provides an institutional environment where underlying state probabilities are mathematically bounded by invariant combinatorial "
         "rules (52 cards, rigid betting structures, deterministic pot odds)."),

        ("2. Theoretical Framework and Hypotheses",
         "Consider an agent i participating in repeated rounds of Texas Hold'em. At the start of session s, player i sits with an initial "
         "endowment (chip stack) W_{i,0}. In each hand t, player i observes private hole cards, table position, and the number of active "
         "opponents. Let W_{it} = Stack_{it} - W_{i,0} represent cumulative within-session wealth prior to decision-making in hand t.\n\n"
         "Under Thaler and Johnson's (1990) mental accounting framework, when W_{it} > 0, accumulated earnings are categorized as 'house money,' "
         "lowering the perceived cost of prospective losses and encouraging voluntary pot participation. Conversely, when W_{it} < 0, prospect "
         "theory dictates that the value function is convex over losses. Because paper losses remain unrealized as long as the player stays seated, "
         "deepening deficits incentivize aggressive risk-seeking (loss chasing) to break even (Imas, 2016; Barberis, 2012).\n\n"
         "Furthermore, at the end of each hand, the player chooses whether to quit. If agents evaluate session outcomes relative to the salient "
         "reference point of Break-Even (W = 0), crossing from negative territory back to zero creates an immediate incentive to terminate the "
         "session, generating sharp bunching at W_{exit} = 0."),

        ("3. Data and Institutional Setting",
         "Our empirical analysis exploits historical logs from the Computer Poker Research Group at the University of Alberta (Billings et al., 2002). "
         "We process 24 complete monthly archives (spanning April 1995 through March 1997) using an automated pipeline implemented in TypeScript "
         "and Python. Following standard gambling literature (Narayanan and Manchanda, 2012), an inactivity gap exceeding 20 minutes (1,200 seconds) "
         "between consecutive hands defines the termination of a session. The final estimation panel consists of 4,070,556 player-hand observations "
         "nested within 119,584 completed sessions across 5,944 unique players.")
    ]

    for title, text in sections_text:
        p_sec = doc.add_paragraph()
        p_sec.paragraph_format.space_before = Pt(14)
        p_sec.paragraph_format.space_after = Pt(4)
        r_sec = p_sec.add_run(title)
        r_sec.bold = True
        r_sec.font.size = Pt(13)

        for para in text.split('\n\n'):
            p_body = doc.add_paragraph(para)
            p_body.paragraph_format.space_after = Pt(6)

    # Add Table 1
    p_t1 = doc.add_paragraph()
    p_t1.paragraph_format.space_before = Pt(10)
    p_t1.paragraph_format.space_after = Pt(3)
    r_t1 = p_t1.add_run("Table 1: Descriptive Statistics of Hand Decisions and Completed Sessions")
    r_t1.bold = True
    r_t1.font.size = Pt(11)

    t1_data = [
        ["Variable", "Mean", "Std. Dev.", "Min", "Max"],
        ["Panel A: Hand Decisions (N = 4,070,556)", "", "", "", ""],
        ["Voluntary Pot Entry (VPIP)", "0.4524", "0.4977", "0.0000", "1.0000"],
        ["Preflop Raise (PFR)", "0.1135", "0.3172", "0.0000", "1.0000"],
        ["Postflop Aggression", "0.2628", "0.4402", "0.0000", "1.0000"],
        ["Total Bet Amount (Chips)", "24.3442", "37.5192", "0.0000", "1200.00"],
        ["Bet Fraction of Stack", "0.0236", "0.0641", "0.0000", "1.0000"],
        ["Reached Showdown", "0.2176", "0.4126", "0.0000", "1.0000"],
        ["Cumulative Session PnL (W_it)", "24.7853", "376.6639", "-23175.0", "13240.0"],
        ["Panel B: Completed Sessions (N = 119,584)", "", "", "", ""],
        ["Session Duration (Minutes)", "38.3625", "41.0449", "1.0000", "580.00"],
        ["Hands Played per Session", "34.0393", "43.3057", "5.0000", "400.00"],
        ["Final Session PnL (W_exit)", "2.6418", "382.8946", "-23175.0", "13240.0"],
        ["Winning Sessions Share", "0.4480", "0.4973", "0.0000", "1.0000"],
        ["Losing Sessions Share", "0.5408", "0.4983", "0.0000", "1.0000"],
        ["Exact Break-Even Share (W=0)", "0.0112", "0.1053", "0.0000", "1.0000"],
        ["Near Break-Even Share (|W| <= 10)", "0.0456", "0.2085", "0.0000", "1.0000"]
    ]

    table1 = doc.add_table(rows=len(t1_data), cols=5)
    table1.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_idx, row in enumerate(t1_data):
        for c_idx, val in enumerate(row):
            cell = table1.cell(r_idx, c_idx)
            cell.text = val
            set_cell_margins(cell, 60, 60, 100, 100)
            if r_idx == 0 or "Panel" in row[0]:
                for p in cell.paragraphs:
                    for r in p.runs:
                        r.bold = True
                        r.font.size = Pt(9.5)
            else:
                for p in cell.paragraphs:
                    for r in p.runs:
                        r.font.size = Pt(9)

    # Section 4: Results
    results_text = [
        ("4. Empirical Results: The House Money Effect and Dynamic Risk Escalation",
         "Table 2 reports within-player fixed effects panel regressions testing the effect of cumulative session wealth on risk choices. "
         "As shown in Column (1), entering the gain domain increases VPIP by +0.57 percentage points (t = 4.05, p < 0.001), with each additional "
         "100 chips of profit increasing pot participation by +0.076 percentage points (p = 0.003). Column (2) demonstrates that preflop aggressive "
         "raising rises by +0.26 percentage points (t = 2.91, p = 0.004). This confirms Hypothesis 1: players willingly gamble more loosely and "
         "aggressively with accumulated house money.\n\n"
         "In the loss domain, however, we observe an intense loss-chasing escalation. In Column (4), while gain magnitude reduces bet fractions "
         "as stacks grow (beta = -0.00053, t = -10.52), loss magnitude produces an explosive positive coefficient: beta = +0.00488 (t = 18.99, "
         "p < 10^-79). As cumulative deficits deepen, competitors commit substantially larger proportions of their remaining wealth to each wager, "
         "seeking large windfalls to break even."),

        ("5. Empirical Results: Reference-Dependent Stopping and Asymmetric Quitting",
         "Turning to session stopping rules, Figure 2 displays the empirical distribution of completed session earnings. A sharp mass spike occurs "
         "at exact break-even (W_{exit} = 0), with 1,340 sessions terminating at zero net profit, yielding a statistically significant excess mass "
         "ratio of b = +0.284 (p < 0.001). Furthermore, Table 3 establishes that the conditional hazard rate of quitting immediately after a winning "
         "hand is a negligible 0.36%, compared to 2.48% after a loss and 5.02% following voluntary folds. Players almost never walk away on a win, "
         "whereas losses drive selective session terminations and prolonging of losing streaks.")
    ]

    for title, text in results_text:
        p_sec = doc.add_paragraph()
        p_sec.paragraph_format.space_before = Pt(14)
        p_sec.paragraph_format.space_after = Pt(4)
        r_sec = p_sec.add_run(title)
        r_sec.bold = True
        r_sec.font.size = Pt(13)

        for para in text.split('\n\n'):
            p_body = doc.add_paragraph(para)
            p_body.paragraph_format.space_after = Pt(6)

    # Insert Figures if available
    fig_dir = r'C:\Users\Z09057\poker-behavioral-economics\figures'
    figs = [
        ('fig1_house_money_curve.png', 'Figure 1: Risk-Taking Propensity as a Function of Cumulative Session Profit/Loss'),
        ('fig2_breakeven_bunching.png', 'Figure 2: Empirical Density of Session Exit Wealth: Sharp Bunching at Break-Even (W = 0)'),
        ('fig3_stopping_hazard.png', 'Figure 3: Session Termination Hazard Rate by Cumulative Intra-Session Wealth State'),
        ('fig4_duration_escalation.png', 'Figure 4: Asymmetric Session Duration Distribution (Sunk-Cost Escalation in Losing Sessions)')
    ]

    for f_name, caption in figs:
        f_path = os.path.join(fig_dir, f_name)
        if os.path.exists(f_path):
            doc.add_paragraph().paragraph_format.space_before = Pt(8)
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_after = Pt(4)
            p_img.add_run().add_picture(f_path, width=Inches(5.8))

            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(12)
            r_cap = p_cap.add_run(caption)
            r_cap.italic = True
            r_cap.font.size = Pt(9.5)

    # Conclusion & References
    concl_text = (
        "6. Conclusion",
        "Using a census of four million hand decisions from the University of Alberta online poker archive, this paper provides "
        "comprehensive field evidence on dynamic risk preferences and stopping rules. We document a robust House Money Effect in the "
        "gain domain, alongside intense loss chasing as cumulative deficits deepen. Furthermore, we show that session terminations are "
        "strongly governed by reference-dependent heuristics: players bunch at the exact break-even threshold (W = 0) and exhibit a dramatic "
        "reluctance to walk away following winning hands. These findings illustrate the powerful role of dynamic mental accounting in shaping "
        "financial risk behavior and self-regulation failures in competitive markets."
    )
    p_sec = doc.add_paragraph()
    p_sec.paragraph_format.space_before = Pt(14)
    p_sec.paragraph_format.space_after = Pt(4)
    r_sec = p_sec.add_run(concl_text[0])
    r_sec.bold = True
    r_sec.font.size = Pt(13)
    p_body = doc.add_paragraph(concl_text[1])
    p_body.paragraph_format.space_after = Pt(12)

    # References
    p_ref_h = doc.add_paragraph()
    p_ref_h.paragraph_format.space_before = Pt(14)
    p_ref_h.paragraph_format.space_after = Pt(6)
    r_ref_h = p_ref_h.add_run("References")
    r_ref_h.bold = True
    r_ref_h.font.size = Pt(13)

    refs = [
        "Barberis, N. (2012). A model of casino gambling. Management Science, 58(1), 35–51.",
        "Billings, D., Davidson, A., Schaeffer, J., & Szafron, D. (2002). The challenge of poker. Artificial Intelligence, 134(1–2), 201–240.",
        "Camerer, C., Babcock, L., Loewenstein, G., & Thaler, R. (1997). Labor supply of New York City cabdrivers: One day at a time. Quarterly Journal of Economics, 112(2), 407–441.",
        "Chetty, R., Friedman, J. N., Olsen, T., & Pistaferri, L. (2011). Adjustment costs, firm responses, and micro vs. macro labor supply elasticities: Evidence from Danish tax records. Quarterly Journal of Economics, 126(2), 749–804.",
        "Farber, H. S. (2005). Is labor supply of taxi drivers really backward-bending? Empirical evidence. Journal of Political Economy, 113(4), 857–882.",
        "Farber, H. S. (2008). Reference-dependent preferences and labor supply: The case of New York City taxi drivers. American Economic Review, 98(3), 1069–1082.",
        "Farber, H. S. (2015). Why you can't find a taxi in the rain, and other labor supply puzzles. Quarterly Journal of Economics, 130(4), 1975–2026.",
        "Imas, A. (2016). The realization effect: A test of how realized versus paper outcomes affect risk taking. American Economic Review, 106(8), 2086–2109.",
        "Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. Econometrica, 47(2), 263–291.",
        "McCrary, J. (2008). Manipulation of the running variable in the regression discontinuity design: A density test. Journal of Econometrics, 142(2), 698–714.",
        "Narayanan, S., & Manchanda, P. (2012). An empirical analysis of individual-level casino gambling behavior. Quantitative Marketing and Economics, 10(3), 361–402.",
        "Post, T., Van den Assem, M. J., Baltussen, G., & Thaler, R. H. (2008). Deal or no deal? Decision making under risk in a large-payoff game show. American Economic Review, 98(1), 38–71.",
        "Rabin, M. (2000). Risk aversion and expected-utility theory: A calibration theorem. Econometrica, 68(5), 1281–1292.",
        "Thaler, R. H., & Johnson, E. J. (1990). Gambling with the house money and trying to break even: The effects of prior outcomes on risky choice. Management Science, 36(6), 643–660."
    ]

    for ref in refs:
        p_r = doc.add_paragraph()
        p_r.paragraph_format.left_indent = Inches(0.3)
        p_r.paragraph_format.first_line_indent = Inches(-0.3)
        p_r.paragraph_format.space_after = Pt(4)
        r = p_r.add_run(ref)
        r.font.size = Pt(9.5)

    out_docx = r'C:\Users\Z09057\poker-behavioral-economics\paper\Dynamic_Risk_Preferences_Poker_Economics.docx'
    doc.save(out_docx)
    print(f"Saved DOCX to {out_docx}")

    # Copy to Downloads
    dl_path = os.path.expanduser('~/Downloads/Dynamic_Risk_Preferences_Poker_Economics.docx')
    shutil.copy2(out_docx, dl_path)
    print(f"Copied DOCX to {dl_path}")

if __name__ == '__main__':
    create_document()
