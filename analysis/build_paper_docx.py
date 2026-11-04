import os
import shutil
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

"""
Humanized Academic Word Document Compiler (.docx)
Formats paper to traditional AER / JEBO / JDM submission standards.
Includes all 5-column regression estimates and high-res vector figures.
"""

def set_cell_margins(cell, top=80, bottom=80, left=120, right=120):
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

    for s in doc.sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)

    # Styles
    normal = doc.styles['Normal']
    normal.font.name = 'Times New Roman'
    normal.font.size = Pt(11)
    normal.font.color.rgb = RGBColor(0x11, 0x11, 0x11)
    normal.paragraph_format.line_spacing = 1.25
    normal.paragraph_format.space_after = Pt(6)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(10)
    r_title = p_title.add_run("Dynamic Risk Preferences, Loss Chasing, and Reference-Dependent Stopping in Repeated Contests: Field Evidence from Online Poker")
    r_title.bold = True
    r_title.font.size = Pt(15)

    # Author
    p_auth = doc.add_paragraph()
    p_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_auth.paragraph_format.space_before = Pt(4)
    p_auth.paragraph_format.space_after = Pt(28)
    r_auth = p_auth.add_run("Atanas Bobev")
    r_auth.bold = True
    r_auth.font.size = Pt(12)

    # Abstract Box
    p_abs_h = doc.add_paragraph()
    r_abs_h = p_abs_h.add_run("Abstract")
    r_abs_h.bold = True
    r_abs_h.font.size = Pt(11)

    p_abs = doc.add_paragraph()
    p_abs.paragraph_format.left_indent = Inches(0.35)
    p_abs.paragraph_format.right_indent = Inches(0.35)
    p_abs.paragraph_format.space_after = Pt(10)
    r_abs = p_abs.add_run(
        "We examine how dynamic within-session wealth fluctuations alter risk-taking and session termination decisions "
        "in repeated contests. Analyzing 4,070,556 hand-level decisions across 119,584 completed sessions from the University "
        "of Alberta Computer Poker Research Group archive (1995–1997), we exploit continuous bankroll tracking within an environment "
        "where objective probabilities are governed by invariant combinatorial rules. Controlling for player fixed effects, table stakes, "
        "position, and time-on-task, we identify two distinct behavioral regimes. In the gain domain, competitors exhibit a house money effect: "
        "accumulated profits increase voluntary pot entry (VPIP, +0.59 percentage points, p < 0.001), preflop raising (+0.27 percentage points, "
        "p = 0.003), and absolute wager sizes (+0.57 chips per 100 chips gained, p < 0.001). In the loss domain, increasing cumulative deficits "
        "trigger systematic loss chasing: holding current stack size constant, each 100 chips of deficit increases absolute bet sizes by +0.99 chips "
        "(p < 0.001) and escalates the bet-to-stack ratio (t = 15.52, p < 10^-50). At the session level, termination choices exhibit sharp "
        "reference dependence. Players display an acute 'never quit on a win' asymmetry: the per-hand exit hazard is 0.36% immediately following "
        "a winning hand, compared to 2.48% after a loss and 5.02% after uncontested folds. Furthermore, 1,340 sessions terminate at exact net break-even "
        "(W = 0), with active round-trip clawbacks accounting for 54.9% of these exits. While capital constraints truncate losing sessions on average, "
        "surviving losing sessions display pronounced right-tail persistence, consistent with selective sunk-cost chasing. Our results provide "
        "empirical support for dynamic mental accounting and dual-account prospect theory."
    )
    r_abs.font.size = Pt(10)

    p_kw = doc.add_paragraph()
    p_kw.paragraph_format.left_indent = Inches(0.35)
    p_kw.paragraph_format.space_after = Pt(16)
    r_kw = p_kw.add_run("Keywords: ")
    r_kw.bold = True
    p_kw.add_run("Reference-dependent preferences, House money effect, Loss chasing, Stopping rules, Dynamic labor supply, Contest theory, Field data.\n")
    r_jel = p_kw.add_run("JEL Classifications: ")
    r_jel.bold = True
    p_kw.add_run("D81, D91, C93, G41.")

    # Sections
    sections_text = [
        ("1. Introduction",
         "Standard neoclassical expected utility theory posits that risk preferences are defined over final wealth states. For small-to-moderate "
         "stakes encountered in daily market transactions, consumption gambles, or repeated contests, plausible utility functions are approximately "
         "linear, implying risk-neutral marginal behavior (Rabin, 2000). Contrary to this benchmark, field and laboratory evidence shows that "
         "individuals frequently alter their willingness to bear risk based on recent path-dependent outcomes (Thaler and Johnson, 1990; Post et al., 2008; Barberis, 2012).\n\n"
         "Two primary behavioral frameworks explain such path dependence. First, under mental accounting (Thaler, 1985; Thaler and Johnson, 1990), "
         "individuals segregate recent gains from baseline wealth. Prior earnings are treated as 'house money,' attenuating the perceived disutility of "
         "subsequent losses and encouraging risk-taking. Second, prospect theory (Kahneman and Tversky, 1979) specifies an S-shaped value function characterized "
         "by loss aversion (lambda > 1) and convexity in the negative domain. When individuals accumulate paper losses that have not yet been formally realized, "
         "diminishing sensitivity can induce risk-seeking gambles aimed at recovering the initial endowment (the break-even effect; Imas, 2016).\n\n"
         "Simultaneously, dynamic risk environments require agents to make endogenous stopping decisions: deciding when to cease participation. Analogous "
         "to daily labor supply choices among independent contractors (Camerer et al., 1997; Farber, 2005, 2008, 2015), repeated contest participants must "
         "weigh the marginal utility of continuation against physical or cognitive fatigue. When agents evaluate performance relative to an intra-session "
         "reference point—most saliently, breaking even (W = 0)—stopping probabilities should exhibit sharp structural discontinuities around the reference threshold.\n\n"
         "This paper uses microdata from the Computer Poker Research Group (CPRG) at the University of Alberta (Billings et al., 2002) to examine dynamic risk "
         "preferences and stopping behavior. Covering 4,070,556 hand-level decisions across 119,584 continuous playing sessions between April 1995 and March 1997, "
         "online Texas Hold'em provides an ideal institutional environment: cards are drawn with fixed combinatorial odds, actions are tracked with micro-level "
         "precision, and the historical IRC platform operated with zero house rake."),

        ("2. Institutional Setting and Data",
         "The University of Alberta CPRG database archives logs from public Internet Relay Chat (IRC) poker channels (#holdem) active between 1995 and 2001 "
         "(Billings et al., 2002). Games implemented standard Texas Hold'em rules with automated dealer bots. Stakes followed fixed-limit structures (typically "
         "5/10, 10/20, or 20/40 chips). While chips were virtual ('etherbucks'), player bankrolls were persistent across sessions and publicly ranked on an official "
         "ladder, providing non-trivial reputational incentives and finite endowments analogous to laboratory tokens and competitive sports rating systems.\n\n"
         "Following standard convention (Narayanan and Manchanda, 2012), an inactivity gap exceeding 20 minutes (1,200 seconds) defines session boundaries. We restrict "
         "analysis to sessions with at least 5 hands, positive initial stack, and hand index <= 400. The final estimation panel comprises 4,070,556 player-hand "
         "observations across 119,584 completed sessions and 5,944 unique players.")
    ]

    for title, text in sections_text:
        p_sec = doc.add_paragraph()
        p_sec.paragraph_format.space_before = Pt(12)
        p_sec.paragraph_format.space_after = Pt(3)
        r_sec = p_sec.add_run(title)
        r_sec.bold = True
        r_sec.font.size = Pt(12)

        for para in text.split('\n\n'):
            p_body = doc.add_paragraph(para)
            p_body.paragraph_format.space_after = Pt(5)

    # Table 1
    p_t1 = doc.add_paragraph()
    p_t1.paragraph_format.space_before = Pt(8)
    p_t1.paragraph_format.space_after = Pt(2)
    r_t1 = p_t1.add_run("Table 1: Descriptive Statistics of Hand Decisions and Completed Sessions")
    r_t1.bold = True
    r_t1.font.size = Pt(10.5)

    t1_data = [
        ["Variable", "Mean", "Std. Dev.", "Min", "Max"],
        ["Panel A: Hand Decisions (N = 4,070,556)", "", "", "", ""],
        ["Voluntary Pot Entry (VPIP)", "0.4524", "0.4977", "0.0000", "1.0000"],
        ["Preflop Raise (PFR)", "0.1135", "0.3172", "0.0000", "1.0000"],
        ["Postflop Aggression", "0.2628", "0.4402", "0.0000", "1.0000"],
        ["Total Bet Amount (Chips)", "24.3442", "37.5192", "0.0000", "1200.00"],
        ["Bet Fraction of Stack", "0.0236", "0.0641", "0.0000", "1.0000"],
        ["Reached Showdown", "0.2176", "0.4126", "0.0000", "1.0000"],
        ["Cumulative Session PnL (W_ist)", "24.7853", "376.6639", "-23175.0", "13240.0"],
        ["Panel B: Completed Sessions (N = 119,584)", "", "", "", ""],
        ["Session Duration (Minutes)", "38.3625", "41.0449", "1.0000", "580.00"],
        ["Hands Played per Session", "34.0393", "43.3057", "5.0000", "400.00"],
        ["Final Session Outcome (W_exit)", "2.6418", "382.8946", "-23175.0", "13240.0"],
        ["Winning Sessions Share", "0.4480", "0.4973", "0.0000", "1.0000"],
        ["Losing Sessions Share", "0.5408", "0.4983", "0.0000", "1.0000"],
        ["Exact Break-Even Share (W=0)", "0.0112", "0.1053", "0.0000", "1.0000"],
        ["Near Break-Even Share (|W| <= 10)", "0.0456", "0.2085", "0.0000", "1.0000"]
    ]

    t1 = doc.add_table(rows=len(t1_data), cols=5)
    t1.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_idx, row in enumerate(t1_data):
        for c_idx, val in enumerate(row):
            c = t1.cell(r_idx, c_idx)
            c.text = val
            set_cell_margins(c, 50, 50, 80, 80)
            if r_idx == 0 or "Panel" in row[0]:
                for p in c.paragraphs:
                    for r in p.runs:
                        r.bold = True
                        r.font.size = Pt(9)
            else:
                for p in c.paragraphs:
                    for r in p.runs:
                        r.font.size = Pt(8.5)

    # Section 3 & 4
    results_text = [
        ("3. Empirical Strategy and Fixed Effects Model",
         "To evaluate how within-session wealth dynamics alter risk-taking, we estimate linear panel regressions with player fixed effects. "
         "This absorbs time-invariant unobserved player heterogeneity such as baseline skill and intrinsic risk tolerance:\n\n"
         "Y_{ist} = alpha_i + beta_1 InGain_{ist} + beta_2 (W^+_{ist}/100) + beta_3 InLoss_{ist} + beta_4 (W^-_{ist}/100) "
         "+ theta ln(Stack_{ist}) + X'_{ist} gamma + e_{ist}\n\n"
         "where Y_{ist} represents VPIP, PFR, Aggression, Absolute Bet Amount in chips, or Bet-to-Stack ratio. Controlling for ln(Stack_{ist}) "
         "is vital to ensure that bet fraction dynamics are not mechanical artifacts of shrinking chip balances."),

        ("4. Empirical Results: The House Money Effect and Loss Chasing",
         "Table 2 reports the within-player fixed effects panel regression estimates across 3,999,153 observations from 3,695 players with at least 50 hands.")
    ]

    for title, text in results_text:
        p_sec = doc.add_paragraph()
        p_sec.paragraph_format.space_before = Pt(12)
        p_sec.paragraph_format.space_after = Pt(3)
        r_sec = p_sec.add_run(title)
        r_sec.bold = True
        r_sec.font.size = Pt(12)

        for para in text.split('\n\n'):
            p_body = doc.add_paragraph(para)
            p_body.paragraph_format.space_after = Pt(5)

    # Table 2
    p_t2 = doc.add_paragraph()
    p_t2.paragraph_format.space_before = Pt(8)
    p_t2.paragraph_format.space_after = Pt(2)
    r_t2 = p_t2.add_run("Table 2: Player Fixed Effects Estimates of Within-Session Wealth on Risk-Taking")
    r_t2.bold = True
    r_t2.font.size = Pt(10.5)

    t2_data = [
        ["Independent Variables", "(1) VPIP", "(2) PFR", "(3) Aggression", "(4) Bet Amount", "(5) Bet/Stack"],
        ["In Gain Domain", "0.00587***", "0.00269***", "0.00341***", "-0.37644", "-0.00130***"],
        ["", "(0.00141)", "(0.00090)", "(0.00119)", "(0.23752)", "(0.00019)"],
        ["Gain Magnitude (W+ / 100)", "0.00118***", "0.00038*", "0.00055**", "0.57122***", "0.00058***"],
        ["", "(0.00026)", "(0.00022)", "(0.00024)", "(0.10883)", "(0.00007)"],
        ["In Loss Domain", "0.00501***", "0.00214**", "0.00222*", "-0.34883", "-0.00220***"],
        ["", "(0.00148)", "(0.00103)", "(0.00119)", "(0.23035)", "(0.00035)"],
        ["Loss Magnitude (W- / 100)", "0.00404***", "0.00420***", "0.00367***", "0.98960***", "0.00352***"],
        ["", "(0.00061)", "(0.00055)", "(0.00049)", "(0.15046)", "(0.00023)"],
        ["Log Current Stack", "-0.01059***", "-0.00464***", "-0.00578***", "-0.44138***", "-0.02826***"],
        ["", "(0.00147)", "(0.00116)", "(0.00112)", "(0.09625)", "(0.00147)"],
        ["Hand Index / 10", "-0.00018", "0.00050***", "0.00014", "-0.13945***", "-0.00050***"],
        ["", "(0.00016)", "(0.00012)", "(0.00013)", "(0.02583)", "(0.00004)"],
        ["Position & Player FE", "Yes", "Yes", "Yes", "Yes", "Yes"],
        ["Observations", "3,999,153", "3,999,153", "3,999,153", "3,999,153", "3,999,153"],
        ["Within R-squared", "0.0419", "0.0155", "0.0210", "0.0133", "0.1406"]
    ]

    t2 = doc.add_table(rows=len(t2_data), cols=6)
    t2.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_idx, row in enumerate(t2_data):
        for c_idx, val in enumerate(row):
            c = t2.cell(r_idx, c_idx)
            c.text = val
            set_cell_margins(c, 40, 40, 60, 60)
            if r_idx == 0 or r_idx >= len(t2_data) - 3:
                for p in c.paragraphs:
                    for r in p.runs:
                        r.bold = True
                        r.font.size = Pt(8.5)
            else:
                for p in c.paragraphs:
                    for r in p.runs:
                        r.font.size = Pt(8)

    # Insert Figures
    fig_dir = r'C:\Users\Z09057\poker-behavioral-economics\figures'
    figs = [
        ('fig1_house_money_curve.png', 'Figure 1: Risk-Taking (VPIP and Bet Sizing) Across Cumulative Session Wealth States'),
        ('fig2_breakeven_bunching.png', 'Figure 2: Distribution of Session Exit Wealth: Discontinuity at the Break-Even Reference Point'),
        ('fig3_stopping_hazard.png', 'Figure 3: Conditional Session Termination Hazard Across Wealth States'),
        ('fig4_duration_escalation.png', 'Figure 4: Session Duration and Length by Final Outcome (Voluntary Exits Only)')
    ]

    for f_name, caption in figs:
        f_path = os.path.join(fig_dir, f_name)
        if os.path.exists(f_path):
            doc.add_paragraph().paragraph_format.space_before = Pt(6)
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_after = Pt(2)
            p_img.add_run().add_picture(f_path, width=Inches(5.6))

            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(10)
            r_cap = p_cap.add_run(caption)
            r_cap.italic = True
            r_cap.font.size = Pt(9)

    # Section 5 & 6
    stopping_text = [
        ("5. Empirical Results: Stopping Rules and the Break-Even Reference Point",
         "Figure 2 establishes significant cognitive bunching at W_{exit} = 0 (excess mass b = +0.284, p < 0.001). Active clawbacks "
         "(recovering from negative territory to zero and immediately quitting) represent 54.9% of exact break-even exits, with an average "
         "duration of only 18.2 hands (20.5 minutes), roughly half the sample mean. Players actively truncate play to lock in break-even status.\n\n"
         "Furthermore, Table 3 establishes an acute 'never quit on a win' asymmetry: the per-hand exit hazard is only 0.36% following a winning hand, "
         "compared to 2.48% after a loss and 5.02% following uncontested folds. Finally, while capital constraints truncate losing sessions on average "
         "(30.2 hands vs. 37.8 hands for winning sessions), voluntary losing exits exhibit a prominent right tail (Figure 4), consistent with selective "
         "sunk-cost chasing."),

        ("6. Conclusion and Implications",
         "Using a census of four million hand decisions from online poker, this paper provides clean field evidence on dynamic risk preferences and "
         "stopping rules. We document a robust house money effect in gains, alongside intense loss chasing as cumulative deficits deepen. Furthermore, "
         "session termination is governed by reference-dependent heuristics: players bunch at the exact break-even threshold (W = 0) and exhibit a "
         "pronounced reluctance to walk away following a win. These findings bridge laboratory prospect theory and field labor supply models, highlighting "
         "the central role of mental accounting in dynamic financial environments.")
    ]

    for title, text in stopping_text:
        p_sec = doc.add_paragraph()
        p_sec.paragraph_format.space_before = Pt(12)
        p_sec.paragraph_format.space_after = Pt(3)
        r_sec = p_sec.add_run(title)
        r_sec.bold = True
        r_sec.font.size = Pt(12)

        for para in text.split('\n\n'):
            p_body = doc.add_paragraph(para)
            p_body.paragraph_format.space_after = Pt(5)

    # References
    p_ref_h = doc.add_paragraph()
    p_ref_h.paragraph_format.space_before = Pt(12)
    p_ref_h.paragraph_format.space_after = Pt(4)
    r_ref_h = p_ref_h.add_run("References")
    r_ref_h.bold = True
    r_ref_h.font.size = Pt(12)

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
        "Thaler, R. H. (1985). Mental accounting and consumer choice. Marketing Science, 4(3), 199–214.",
        "Thaler, R. H., & Johnson, E. J. (1990). Gambling with the house money and trying to break even: The effects of prior outcomes on risky choice. Management Science, 36(6), 643–660."
    ]

    for ref in refs:
        p_r = doc.add_paragraph()
        p_r.paragraph_format.left_indent = Inches(0.25)
        p_r.paragraph_format.first_line_indent = Inches(-0.25)
        p_r.paragraph_format.space_after = Pt(3)
        r = p_r.add_run(ref)
        r.font.size = Pt(9)

    out_docx = r'C:\Users\Z09057\poker-behavioral-economics\paper\Dynamic_Risk_Preferences_Poker_Economics.docx'
    doc.save(out_docx)
    print(f"Saved refined DOCX to {out_docx}")

    dl_path = os.path.expanduser('~/Downloads/Dynamic_Risk_Preferences_Poker_Economics.docx')
    shutil.copy2(out_docx, dl_path)
    print(f"Copied DOCX to {dl_path}")

if __name__ == '__main__':
    create_document()
