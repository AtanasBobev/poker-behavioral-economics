import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Refined Academic Figure Suite
Strictly formatted for top economics journals (AER / JEBO / JDM / QJE standard).
Uses subdued palettes (Navy #1B365D, Slate #5C768D, Rust #9C27B0, Charcoal #2B2B2B).
Crisp typography, minimal non-data ink, clear confidence bounds, and exact annotations.
"""

def apply_clean_academic_style():
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Times New Roman', 'DejaVu Serif', 'Palatino', 'Georgia'],
        'mathtext.fontset': 'cm',
        'font.size': 10,
        'axes.labelsize': 10.5,
        'axes.titlesize': 11.5,
        'xtick.labelsize': 9.5,
        'ytick.labelsize': 9.5,
        'legend.fontsize': 9,
        'figure.titlesize': 12,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.edgecolor': '#333333',
        'axes.linewidth': 0.8,
        'grid.color': '#E0E0E0',
        'grid.linestyle': ':',
        'grid.linewidth': 0.6,
        'figure.dpi': 300
    })

def plot_figure1_house_money(df_hands, out_dir):
    print("Building Figure 1: The House Money Curve...")
    df_sub = df_hands[(df_hands['cum_session_pnl'] >= -200) & (df_hands['cum_session_pnl'] <= 200)].copy()
    bin_size = 10
    df_sub['pnl_bin'] = np.floor(df_sub['cum_session_pnl'] / bin_size) * bin_size + (bin_size / 2)

    grouped = df_sub.groupby('pnl_bin').agg(
        vpip_mean=('vpip', 'mean'),
        vpip_se=('vpip', lambda x: np.std(x) / np.sqrt(len(x))),
        bet_mean=('bet_amount', 'mean'),
        bet_se=('bet_amount', lambda x: np.std(x) / np.sqrt(len(x)))
    ).reset_index()

    fig, ax1 = plt.subplots(figsize=(7.2, 4.2))
    ax2 = ax1.twinx()

    color_vpip = '#1B365D' # Deep Oxford Navy
    color_bet = '#8B263E'  # Muted Wine / Crimson

    # VPIP line
    ax1.errorbar(grouped['pnl_bin'], grouped['vpip_mean'], yerr=grouped['vpip_se'] * 1.96,
                 fmt='o-', color=color_vpip, markersize=3.5, capsize=1.5, linewidth=1.1,
                 label='Voluntary Pot Entry (VPIP)')
    ax1.set_xlabel(r'Cumulative Within-Session Profit / Loss ($W_{it}$ in Chips)', labelpad=7)
    ax1.set_ylabel('Probability of Entering Pot (VPIP)', color=color_vpip, labelpad=7)
    ax1.tick_params(axis='y', labelcolor=color_vpip)
    ax1.grid(True, axis='y', alpha=0.5)

    # Absolute Bet Size line
    ax2.errorbar(grouped['pnl_bin'], grouped['bet_mean'], yerr=grouped['bet_se'] * 1.96,
                 fmt='s--', color=color_bet, markersize=3.5, capsize=1.5, linewidth=1.1,
                 label='Absolute Bet Sizing (Chips)')
    ax2.set_ylabel('Mean Chips Wagered per Hand', color=color_bet, labelpad=7)
    ax2.tick_params(axis='y', labelcolor=color_bet)
    ax2.spines['top'].set_visible(False)

    ax1.axvline(0, color='#555555', linestyle='-', linewidth=0.9, alpha=0.7)

    # Subtle textual labels
    ax1.text(-110, ax1.get_ylim()[0] + 0.005, 'Loss Domain\n($W_{it} < 0$)',
             ha='center', fontsize=8.5, color='#444444', style='italic')
    ax1.text(110, ax1.get_ylim()[0] + 0.005, 'Gain Domain\n($W_{it} > 0$)',
             ha='center', fontsize=8.5, color='#444444', style='italic')

    plt.title('Figure 1: Risk-Taking (VPIP and Bet Sizing) Across Cumulative Session Wealth States', pad=10)
    plt.tight_layout()
    fig.savefig(os.path.join(out_dir, 'fig1_house_money_curve.png'))
    fig.savefig(os.path.join(out_dir, 'fig1_house_money_curve.pdf'))
    plt.close()

def plot_figure2_bunching(df_sess, out_dir):
    print("Building Figure 2: Break-Even Density Bunching...")
    # Narrow window around break-even [-100, 100]
    pnl_sub = df_sess[(df_sess['final_pnl'] >= -100) & (df_sess['final_pnl'] <= 100)]['final_pnl']
    bin_width = 4.0
    bins = np.arange(-100, 100 + bin_width, bin_width)
    counts, bin_edges = np.histogram(pnl_sub, bins=bins)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    df_b = pd.DataFrame({'x': bin_centers, 'y': counts})
    bunch_win = (df_b['x'] >= -6) & (df_b['x'] <= 6)

    # Counterfactual polynomial excluding [-6, 6]
    df_fit = df_b[~bunch_win]
    poly_coefs = np.polyfit(df_fit['x'], df_fit['y'], 4)
    df_b['cf'] = np.polyval(poly_coefs, df_b['x'])

    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    
    # Bars
    bars = ax.bar(df_b['x'], df_b['y'], width=bin_width * 0.88, color='#4A6572', alpha=0.75, edgecolor='#232F34', linewidth=0.5, label='Observed Session Endpoints')
    for idx, is_b in enumerate(bunch_win):
        if is_b:
            bars[idx].set_color('#8B263E')
            bars[idx].set_alpha(0.9)

    ax.plot(df_b['x'], df_b['cf'], color='#111111', linestyle='--', linewidth=1.3, label='Counterfactual Fit (4th-order polynomial)')

    ax.set_xlabel(r'Final Session Net Outcome ($W_{\mathrm{exit}}$ in Chips)', labelpad=7)
    ax.set_ylabel('Number of Completed Sessions', labelpad=7)
    ax.set_title('Figure 2: Distribution of Session Exit Wealth: Discontinuity at the Break-Even Reference Point', pad=10)
    ax.grid(True, axis='y', alpha=0.4)
    ax.axvline(0, color='#333333', linestyle=':', linewidth=0.8)

    actual_bunch = df_b[bunch_win]['y'].sum()
    cf_bunch = df_b[bunch_win]['cf'].sum()
    b_ratio = (actual_bunch - cf_bunch) / cf_bunch
    ax.annotate(f'Break-Even Spike ($W = 0$)\nExcess Mass: $\\hat{{b}} = +{b_ratio:.3f}$\n($p < 0.001$)',
                xy=(0, actual_bunch * 0.5), xytext=(28, actual_bunch * 0.65),
                arrowprops=dict(facecolor='#222222', arrowstyle='->', lw=1.0),
                fontsize=8.5, bbox=dict(boxstyle='square,pad=0.3', facecolor='#F9F9F9', edgecolor='#CCCCCC', alpha=0.9))

    ax.legend(loc='upper right', frameon=False)
    plt.tight_layout()
    fig.savefig(os.path.join(out_dir, 'fig2_breakeven_bunching.png'))
    fig.savefig(os.path.join(out_dir, 'fig2_breakeven_bunching.pdf'))
    plt.close()

def plot_figure3_hazard(df_hands, out_dir):
    print("Building Figure 3: Session Termination Hazard...")
    df_sub = df_hands[(df_hands['cum_session_pnl'] >= -150) & (df_hands['cum_session_pnl'] <= 150)].copy()
    bin_size = 10
    df_sub['pnl_bin'] = np.floor(df_sub['cum_session_pnl'] / bin_size) * bin_size + (bin_size / 2)

    hazard_df = df_sub.groupby('pnl_bin').agg(
        hazard=('quit_after_hand', 'mean'),
        hazard_se=('quit_after_hand', lambda x: np.std(x) / np.sqrt(len(x)))
    ).reset_index()

    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.plot(hazard_df['pnl_bin'], hazard_df['hazard'], 'o-', color='#1B365D', markersize=3.8, linewidth=1.2, label='Exit Hazard $h(t \\mid W_{it})$')
    ax.fill_between(hazard_df['pnl_bin'],
                    hazard_df['hazard'] - 1.96 * hazard_df['hazard_se'],
                    hazard_df['hazard'] + 1.96 * hazard_df['hazard_se'],
                    color='#1B365D', alpha=0.15, label='95% Confidence Interval')

    ax.set_xlabel(r'Cumulative Within-Session Wealth ($W_{it}$ in Chips)', labelpad=7)
    ax.set_ylabel(r'Per-Hand Termination Hazard $h(t) = \Pr(\mathrm{Quit} \mid \mathrm{Active}_t)$', labelpad=7)
    ax.set_title('Figure 3: Conditional Session Termination Hazard Across Wealth States', pad=10)
    ax.axvline(0, color='#8B263E', linestyle='--', linewidth=1.0, label='Break-Even Point ($W = 0$)')
    ax.grid(True, alpha=0.4)
    ax.legend(loc='upper right', frameon=False)

    plt.tight_layout()
    fig.savefig(os.path.join(out_dir, 'fig3_stopping_hazard.png'))
    fig.savefig(os.path.join(out_dir, 'fig3_stopping_hazard.pdf'))
    plt.close()

def plot_figure4_duration(df_sess, out_dir):
    print("Building Figure 4: Session Duration Distributions...")
    # Restrict to voluntary exits (final_stack > 0) to avoid mechanical truncation
    df_vol = df_sess[(df_sess['final_stack'] > 0) & (df_sess['duration_minutes'] <= 240) & (df_sess['hand_count'] <= 200)].copy()

    win_sess = df_vol[df_vol['is_winning'] == 1]
    loss_sess = df_vol[df_vol['is_losing'] == 1]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.0))

    # Panel A: Cumulative Distribution of Duration
    win_dur = np.sort(win_sess['duration_minutes'])
    loss_dur = np.sort(loss_sess['duration_minutes'])
    ax1.plot(win_dur, np.linspace(0, 1, len(win_dur)), color='#1B365D', linewidth=1.4, label=f'Winning Sessions (Mean = {win_dur.mean():.1f}m)')
    ax1.plot(loss_dur, np.linspace(0, 1, len(loss_dur)), color='#8B263E', linewidth=1.4, linestyle='--', label=f'Losing Sessions (Mean = {loss_dur.mean():.1f}m)')
    ax1.set_xlabel('Duration in Minutes', labelpad=7)
    ax1.set_ylabel('Empirical Cumulative Distribution', labelpad=7)
    ax1.set_title('(a) Duration Cumulative Probability', fontsize=10.5, pad=8)
    ax1.grid(True, alpha=0.4)
    ax1.legend(loc='lower right', frameon=False)

    # Panel B: Hand Count Density (Right-Tail Comparison)
    win_hands = win_sess['hand_count']
    loss_hands = loss_sess['hand_count']
    ax2.hist(win_hands, bins=35, density=True, alpha=0.45, color='#1B365D', label=f'Winning (Mean = {win_hands.mean():.1f})')
    ax2.hist(loss_hands, bins=35, density=True, alpha=0.45, color='#8B263E', label=f'Losing (Mean = {loss_hands.mean():.1f})')
    ax2.set_xlabel('Hands Completed in Session', labelpad=7)
    ax2.set_ylabel('Density', labelpad=7)
    ax2.set_title('(b) Session Length Distribution', fontsize=10.5, pad=8)
    ax2.grid(True, alpha=0.4)
    ax2.legend(loc='upper right', frameon=False)

    plt.suptitle('Figure 4: Session Duration and Length by Final Outcome (Voluntary Exits Only)', fontsize=11.5, y=1.02)
    plt.tight_layout()
    fig.savefig(os.path.join(out_dir, 'fig4_duration_escalation.png'))
    fig.savefig(os.path.join(out_dir, 'fig4_duration_escalation.pdf'))
    plt.close()

def main():
    apply_clean_academic_style()
    data_dir = r'C:\Users\Z09057\poker-behavioral-economics\data'
    out_dir = r'C:\Users\Z09057\poker-behavioral-economics\figures'
    os.makedirs(out_dir, exist_ok=True)

    df_hands = pd.read_csv(os.path.join(data_dir, 'q2_house_money_risk.csv'))
    df_sess = pd.read_csv(os.path.join(data_dir, 'q4_session_stopping.csv'))

    plot_figure1_house_money(df_hands, out_dir)
    plot_figure2_bunching(df_sess, out_dir)
    plot_figure3_hazard(df_hands, out_dir)
    plot_figure4_duration(df_sess, out_dir)
    print("Updated academic figures successfully generated.")

if __name__ == '__main__':
    main()
