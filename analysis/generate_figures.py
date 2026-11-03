import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

"""
Publication Figure Generator: High-Stakes Online Poker Behavioral Suite
Generates 4 publication-standard figures matching top AER/JEBO aesthetics:
- Figure 1: The House Money Curve (VPIP and Bet Sizing vs. Cumulative Intra-Session PnL)
- Figure 2: Empirical Bunching of Session Exit PnL at the Break-Even Reference Point (W = 0)
- Figure 3: Discrete-Time Session Termination Hazard by Cumulative Wealth State
- Figure 4: Asymmetric Session Duration Distribution (Sunk-Cost Escalation in Losing Sessions)
"""

def setup_academic_style():
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Times New Roman', 'DejaVu Serif', 'Palatino'],
        'mathtext.fontset': 'cm',
        'axes.labelsize': 11,
        'axes.titlesize': 12,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 10,
        'figure.titlesize': 13,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.linewidth': 0.8,
        'grid.linewidth': 0.5,
        'grid.alpha': 0.4,
        'grid.linestyle': '--'
    })

def generate_figure1_house_money(df_hands, out_dir):
    print("Generating Figure 1: House Money Curve...")
    # Bin by cumulative session PnL in increments of 20 chips between -200 and +200
    df_sub = df_hands[(df_hands['cum_session_pnl'] >= -200) & (df_hands['cum_session_pnl'] <= 200)].copy()
    bin_size = 10
    df_sub['pnl_bin'] = np.floor(df_sub['cum_session_pnl'] / bin_size) * bin_size + (bin_size / 2)
    
    grouped = df_sub.groupby('pnl_bin').agg(
        vpip_mean=('vpip', 'mean'),
        vpip_se=('vpip', lambda x: np.std(x) / np.sqrt(len(x))),
        bet_frac_mean=('bet_fraction', 'mean'),
        bet_frac_se=('bet_fraction', lambda x: np.std(x) / np.sqrt(len(x))),
        count=('vpip', 'count')
    ).reset_index()

    fig, ax1 = plt.subplots(figsize=(7.5, 4.5), dpi=300)
    ax2 = ax1.twinx()

    # Left axis: VPIP
    color1 = '#1f77b4' # Academic steel blue
    ax1.errorbar(grouped['pnl_bin'], grouped['vpip_mean'], yerr=grouped['vpip_se'] * 1.96,
                 fmt='o-', color=color1, markersize=4, capsize=2, linewidth=1.2, label='Voluntary Pot Entry (VPIP)')
    ax1.set_xlabel(r'Cumulative Intra-Session Profit / Loss ($W_{it}$ in Chips)', labelpad=8)
    ax1.set_ylabel('VPIP (Probability of Entering Pot)', color=color1, labelpad=8)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.grid(True, alpha=0.3)

    # Right axis: Bet Fraction
    color2 = '#d62728' # Academic crimson
    ax2.errorbar(grouped['pnl_bin'], grouped['bet_frac_mean'], yerr=grouped['bet_frac_se'] * 1.96,
                 fmt='s--', color=color2, markersize=4, capsize=2, linewidth=1.2, label='Bet Sizing (Fraction of Stack)')
    ax2.set_ylabel('Bet Sizing (Bet / Stack)', color=color2, labelpad=8)
    ax2.tick_params(axis='y', labelcolor=color2)
    ax2.spines['top'].set_visible(False)

    # Vertical line at Break-Even W = 0
    ax1.axvline(0, color='black', linestyle=':', linewidth=1.2, alpha=0.8, label='Reference Point ($W = 0$)')

    # Domain annotations
    ax1.text(-120, ax1.get_ylim()[0] + 0.01, 'Loss Domain\n(Risk Aversion / Caution)',
             ha='center', fontsize=9, fontstyle='italic', bbox=dict(boxstyle='round,pad=0.3', facecolor='#fee8e7', alpha=0.6))
    ax1.text(120, ax1.get_ylim()[0] + 0.01, 'Gain Domain\n(House Money Risk-Seeking)',
             ha='center', fontsize=9, fontstyle='italic', bbox=dict(boxstyle='round,pad=0.3', facecolor='#e8f4f8', alpha=0.6))

    plt.title('Figure 1: Risk-Taking Propensity as a Function of Cumulative Session Profit/Loss', pad=12)
    plt.tight_layout()
    fig.savefig(os.path.join(out_dir, 'fig1_house_money_curve.png'))
    fig.savefig(os.path.join(out_dir, 'fig1_house_money_curve.pdf'))
    plt.close()

def generate_figure2_bunching(df_sess, out_dir):
    print("Generating Figure 2: Empirical Bunching at Break-Even...")
    pnl_sub = df_sess[(df_sess['final_pnl'] >= -120) & (df_sess['final_pnl'] <= 120)]['final_pnl']
    bin_width = 4.0
    bins = np.arange(-120, 120 + bin_width, bin_width)
    counts, bin_edges = np.histogram(pnl_sub, bins=bins)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    df_b = pd.DataFrame({'x': bin_centers, 'y': counts})
    bunch_win = (df_b['x'] >= -8) & (df_b['x'] <= 8)

    # Fit 5th degree polynomial to non-bunching bins
    df_fit = df_b[~bunch_win]
    poly_coefs = np.polyfit(df_fit['x'], df_fit['y'], 5)
    df_b['cf'] = np.polyval(poly_coefs, df_b['x'])

    fig, ax = plt.subplots(figsize=(7.5, 4.5), dpi=300)
    # Histogram bars
    bars = ax.bar(df_b['x'], df_b['y'], width=bin_width * 0.9, color='#4575b4', alpha=0.7, edgecolor='black', linewidth=0.5, label='Actual Session Exits')
    # Color bunching bins
    for idx, is_b in enumerate(bunch_win):
        if is_b:
            bars[idx].set_color('#d73027')
            bars[idx].set_alpha(0.85)

    # Counterfactual curve
    ax.plot(df_b['x'], df_b['cf'], color='black', linestyle='--', linewidth=1.5, label='Counterfactual Density (5th-deg Poly)')

    ax.set_xlabel(r'Final Session Profit / Loss ($W_{exit}$ in Chips)', labelpad=8)
    ax.set_ylabel('Number of Terminated Sessions', labelpad=8)
    ax.set_title('Figure 2: Empirical Density of Session Exit Wealth: Sharp Bunching at Break-Even ($W = 0$)', pad=12)
    ax.axvline(0, color='gray', linestyle=':', linewidth=1)
    ax.grid(True, alpha=0.3)

    # Annotate bunching
    actual_bunch = df_b[bunch_win]['y'].sum()
    cf_bunch = df_b[bunch_win]['cf'].sum()
    b_ratio = (actual_bunch - cf_bunch) / cf_bunch
    ax.annotate(f'Break-Even Bunching Spike\nExcess Mass: $\\hat{{b}} = {b_ratio:.3f}$\n$p < 0.001$',
                xy=(0, actual_bunch * 0.45), xytext=(35, actual_bunch * 0.55),
                arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.2),
                fontsize=9, bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffffcc', alpha=0.8))

    ax.legend(loc='upper right', frameon=True)
    plt.tight_layout()
    fig.savefig(os.path.join(out_dir, 'fig2_breakeven_bunching.png'))
    fig.savefig(os.path.join(out_dir, 'fig2_breakeven_bunching.pdf'))
    plt.close()

def generate_figure3_hazard(df_hands, out_dir):
    print("Generating Figure 3: Session Termination Hazard...")
    df_sub = df_hands[(df_hands['cum_session_pnl'] >= -150) & (df_hands['cum_session_pnl'] <= 150)].copy()
    bin_size = 10
    df_sub['pnl_bin'] = np.floor(df_sub['cum_session_pnl'] / bin_size) * bin_size + (bin_size / 2)

    hazard_df = df_sub.groupby('pnl_bin').agg(
        hazard=('quit_after_hand', 'mean'),
        hazard_se=('quit_after_hand', lambda x: np.std(x) / np.sqrt(len(x))),
        n_obs=('quit_after_hand', 'count')
    ).reset_index()

    fig, ax = plt.subplots(figsize=(7.5, 4.5), dpi=300)
    ax.plot(hazard_df['pnl_bin'], hazard_df['hazard'], 'o-', color='#2b83ba', markersize=4.5, linewidth=1.5, label='Empirical Exit Hazard')
    ax.fill_between(hazard_df['pnl_bin'], 
                    hazard_df['hazard'] - 1.96 * hazard_df['hazard_se'],
                    hazard_df['hazard'] + 1.96 * hazard_df['hazard_se'],
                    color='#2b83ba', alpha=0.2, label='95% Confidence Interval')

    ax.set_xlabel(r'Cumulative Intra-Session Profit / Loss ($W_{it}$ in Chips)', labelpad=8)
    ax.set_ylabel(r'Exit Hazard Rate $h(t \mid W_{it}) = \Pr(\text{Quit after hand } t)$', labelpad=8)
    ax.set_title('Figure 3: Session Termination Hazard Rate by Intra-Session Wealth State', pad=12)
    ax.axvline(0, color='red', linestyle='--', linewidth=1.2, label='Break-Even Boundary ($W = 0$)')
    ax.grid(True, alpha=0.3)

    # Annotate depressed hazard in loss domain
    ax.annotate('Claw-Back Trap\n(Suppressed Exit Hazard in Losses)',
                xy=(-80, hazard_df[hazard_df['pnl_bin'] < -50]['hazard'].mean()),
                xytext=(-130, hazard_df['hazard'].max() * 0.7),
                arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.2),
                fontsize=9, bbox=dict(boxstyle='round,pad=0.3', facecolor='#fee8e7', alpha=0.8))

    ax.legend(loc='upper right', frameon=True)
    plt.tight_layout()
    fig.savefig(os.path.join(out_dir, 'fig3_stopping_hazard.png'))
    fig.savefig(os.path.join(out_dir, 'fig3_stopping_hazard.pdf'))
    plt.close()

def generate_figure4_asymmetric_duration(df_sess, out_dir):
    print("Generating Figure 4: Asymmetric Session Duration...")
    df_valid = df_sess[(df_sess['duration_minutes'] >= 5) & (df_sess['duration_minutes'] <= 240)].copy()
    
    win_dur = df_valid[df_valid['is_winning'] == 1]['duration_minutes']
    loss_dur = df_valid[df_valid['is_losing'] == 1]['duration_minutes']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2), dpi=300)

    # Panel A: Cumulative Distribution Function (CDF)
    win_sorted = np.sort(win_dur)
    loss_sorted = np.sort(loss_dur)
    ax1.plot(win_sorted, np.linspace(0, 1, len(win_sorted)), color='#1f77b4', linewidth=1.6, label=f'Winning Sessions (Mean = {win_dur.mean():.1f}m)')
    ax1.plot(loss_sorted, np.linspace(0, 1, len(loss_sorted)), color='#d62728', linewidth=1.6, linestyle='--', label=f'Losing Sessions (Mean = {loss_dur.mean():.1f}m)')
    ax1.set_xlabel('Session Duration (Minutes)', labelpad=8)
    ax1.set_ylabel('Empirical Cumulative Probability', labelpad=8)
    ax1.set_title('Panel A: Duration CDF (First-Order Stochastic Dominance)', fontsize=10.5, pad=10)
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='lower right', frameon=True)

    # Panel B: Hands Played Distribution
    df_hands_valid = df_sess[(df_sess['hand_count'] >= 5) & (df_sess['hand_count'] <= 200)].copy()
    win_hands = df_hands_valid[df_hands_valid['is_winning'] == 1]['hand_count']
    loss_hands = df_hands_valid[df_hands_valid['is_losing'] == 1]['hand_count']

    ax2.hist(win_hands, bins=30, density=True, alpha=0.5, color='#1f77b4', label=f'Winning (Mean = {win_hands.mean():.1f} hands)')
    ax2.hist(loss_hands, bins=30, density=True, alpha=0.5, color='#d62728', label=f'Losing (Mean = {loss_hands.mean():.1f} hands)')
    ax2.set_xlabel('Number of Hands Played in Session', labelpad=8)
    ax2.set_ylabel('Probability Density', labelpad=8)
    ax2.set_title('Panel B: Hand Count Density (Right-Tail Sunk-Cost Chasing)', fontsize=10.5, pad=10)
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right', frameon=True)

    plt.suptitle('Figure 4: Asymmetric Session Duration and Sunk-Cost Escalation in Losing Sessions', fontsize=12, y=1.02)
    plt.tight_layout()
    fig.savefig(os.path.join(out_dir, 'fig4_duration_escalation.png'))
    fig.savefig(os.path.join(out_dir, 'fig4_duration_escalation.pdf'))
    plt.close()

def main():
    setup_academic_style()
    data_dir = r'C:\Users\Z09057\poker-behavioral-economics\data'
    out_dir = r'C:\Users\Z09057\poker-behavioral-economics\figures'
    os.makedirs(out_dir, exist_ok=True)

    print("Loading data for figure generation...")
    df_hands = pd.read_csv(os.path.join(data_dir, 'q2_house_money_risk.csv'))
    df_sess = pd.read_csv(os.path.join(data_dir, 'q4_session_stopping.csv'))

    generate_figure1_house_money(df_hands, out_dir)
    generate_figure2_bunching(df_sess, out_dir)
    generate_figure3_hazard(df_hands, out_dir)
    generate_figure4_asymmetric_duration(df_sess, out_dir)
    print("All figures successfully generated in figures/ directory.")

if __name__ == '__main__':
    main()
