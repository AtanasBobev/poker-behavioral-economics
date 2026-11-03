import os
import json
import pandas as pd
import numpy as np
import statsmodels.api as sm

"""
Referee-Grade Econometric Panel: Absolute & Relative Risk-Taking
Decomposes both discrete participation (VPIP, PFR, Aggression) and continuous stakes:
1. VPIP (Linear Probability Model with Player FE)
2. PFR (Linear Probability Model with Player FE)
3. Postflop Aggression (Linear Probability Model with Player FE)
4. Absolute Bet Sizing (Chips wagered per hand)
5. Relative Bet Sizing (Bet / Stack), directly controlling for Stack level to prevent denominator artifact!
"""

def demean_series(df, group_col, target_cols):
    means = df.groupby(group_col)[target_cols].transform('mean')
    return df[target_cols] - means

def main():
    data_path = r'C:\Users\Z09057\poker-behavioral-economics\data\q2_house_money_risk.csv'
    df = pd.read_csv(data_path)

    # Filter standard session bounds
    df = df[(df['current_stack'] > 0) & (df['hand_index'] <= 400)].copy()

    df['gain_mag_100'] = df['gain_magnitude'] / 100.0
    df['loss_mag_100'] = df['loss_magnitude'] / 100.0
    df['hand_idx_10'] = df['hand_index'] / 10.0
    df['log_stack'] = np.log(df['current_stack'] + 1.0)
    df['stack_100'] = df['current_stack'] / 100.0

    # Minimum 50 hands per player
    pcounts = df['player'].value_counts()
    valid_players = pcounts[pcounts >= 50].index
    df_reg = df[df['player'].isin(valid_players)].copy()
    n_obs = len(df_reg)
    n_players = len(valid_players)

    # Position dummies
    pos_dummies = pd.get_dummies(df_reg['position'], prefix='pos', drop_first=True)
    for col in pos_dummies.columns:
        df_reg[col] = pos_dummies[col].astype(float)

    reg_x_vars = ['in_gain', 'gain_mag_100', 'in_loss', 'loss_mag_100', 
                 'num_players', 'hand_idx_10', 'log_stack'] + list(pos_dummies.columns)

    demean_vars = ['vpip', 'pfr', 'aggressive', 'bet_amount', 'bet_fraction'] + reg_x_vars
    demeaned = demean_series(df_reg, 'player', demean_vars)

    results = {
        'n_obs': int(n_obs),
        'n_players': int(n_players),
        'models': {}
    }

    dep_vars = [
        ('vpip', 'VPIP'),
        ('pfr', 'PFR'),
        ('aggressive', 'Postflop Aggression'),
        ('bet_amount', 'Absolute Bet Size (Chips)'),
        ('bet_fraction', 'Bet-to-Stack Ratio')
    ]

    X = demeaned[reg_x_vars]

    for dep_var, label in dep_vars:
        y = demeaned[dep_var]
        mod = sm.OLS(y, X).fit(cov_type='cluster', cov_kwds={'groups': df_reg['player']})
        
        ss_res = np.sum(mod.resid ** 2)
        ss_tot = np.sum(y ** 2)
        r2_within = 1.0 - (ss_res / ss_tot)
        
        print(f"\nModel: {label} (Within R2 = {r2_within:.4f})")
        for var in ['in_gain', 'gain_mag_100', 'in_loss', 'loss_mag_100', 'log_stack', 'hand_idx_10']:
            c = mod.params[var]
            se = mod.bse[var]
            tval = mod.tvalues[var]
            pval = mod.pvalues[var]
            print(f"  {var:<14}: Coef = {c:>9.5f}, SE = {se:>8.5f}, t = {tval:>7.2f}, p = {pval:.2e}")

        results['models'][dep_var] = {
            'label': label,
            'r2_within': float(r2_within),
            'coefs': {var: float(mod.params[var]) for var in reg_x_vars},
            'se': {var: float(mod.bse[var]) for var in reg_x_vars},
            'pvals': {var: float(mod.pvalues[var]) for var in reg_x_vars}
        }

    out_file = r'C:\Users\Z09057\poker-behavioral-economics\data\referee_robust_regressions.json'
    with open(out_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved refined regression results to {out_file}")

if __name__ == '__main__':
    main()
