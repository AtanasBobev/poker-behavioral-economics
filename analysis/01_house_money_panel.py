import os
import json
import pandas as pd
import numpy as np
import statsmodels.api as sm

"""
High-Speed Econometric Module 1: The House Money Effect and Dynamic Risk Escalation
Employs within-player demeaning (Frisch-Waugh-Lovell Fixed Effects) on 4+ million observations.
Estimates:
  Y_ijt - Y_bar_i = b_1 * (InGain_it - InGain_bar_i) + b_2 * (GainMag_it - GainMag_bar_i)
                  + b_3 * (InLoss_it - InLoss_bar_i) + b_4 * (LossMag_it - LossMag_bar_i)
                  + Gamma * (Controls_it - Controls_bar_i) + e_ijt
"""

def demean_series(df, group_col, target_cols):
    means = df.groupby(group_col)[target_cols].transform('mean')
    return df[target_cols] - means

def main():
    data_path = r'C:\Users\Z09057\poker-behavioral-economics\data\q2_house_money_risk.csv'
    print(f"Loading risk panel from {data_path}...")
    df = pd.read_csv(data_path)
    print(f"Loaded {len(df):,} total hand observations.")

    # Data filtering: reasonable stacks and session lengths
    df = df[(df['current_stack'] > 0) & (df['hand_index'] <= 400)].copy()

    # Scale variables
    df['gain_mag_100'] = df['gain_magnitude'] / 100.0
    df['loss_mag_100'] = df['loss_magnitude'] / 100.0
    df['hand_idx_10'] = df['hand_index'] / 10.0

    # Retain players with at least 50 hands for robust within-player identification
    player_counts = df['player'].value_counts()
    valid_players = player_counts[player_counts >= 50].index
    df_reg = df[df['player'].isin(valid_players)].copy()
    n_obs = len(df_reg)
    n_players = len(valid_players)
    print(f"Estimation sample: {n_obs:,} observations across {n_players:,} unique players.")

    # Create dummy indicators for position (1 to 10)
    pos_dummies = pd.get_dummies(df_reg['position'], prefix='pos', drop_first=True)
    for col in pos_dummies.columns:
        df_reg[col] = pos_dummies[col].astype(float)

    reg_x_vars = ['in_gain', 'gain_mag_100', 'in_loss', 'loss_mag_100', 
                 'num_players', 'hand_idx_10'] + list(pos_dummies.columns)

    print("\nExecuting within-player demeaning (Player Fixed Effects)...")
    demean_vars = ['vpip', 'pfr', 'aggressive', 'bet_fraction'] + reg_x_vars
    demeaned = demean_series(df_reg, 'player', demean_vars)

    results = {
        'n_obs': int(n_obs),
        'n_players': int(n_players),
        'models': {}
    }

    dep_vars = [
        ('vpip', 'Voluntary Pot Entry (VPIP)'),
        ('pfr', 'Preflop Aggressive Raise (PFR)'),
        ('aggressive', 'Postflop Bet/Raise Aggression'),
        ('bet_fraction', 'Continuous Bet Sizing (Bet / Stack)')
    ]

    X = demeaned[reg_x_vars]

    for dep_var, label in dep_vars:
        print(f"\n--- Estimating Model: {label} ---")
        y = demeaned[dep_var]
        
        # OLS without intercept (since demeaned)
        mod = sm.OLS(y, X).fit(cov_type='cluster', cov_kwds={'groups': df_reg['player']})
        
        # Calculate within R-squared
        ss_res = np.sum(mod.resid ** 2)
        ss_tot = np.sum(y ** 2)
        r2_within = 1.0 - (ss_res / ss_tot)
        
        print(f"Variable          Coef       Std.Err    t-stat     p-value")
        print("-" * 55)
        for var in ['in_gain', 'gain_mag_100', 'in_loss', 'loss_mag_100', 'hand_idx_10', 'num_players']:
            coef = mod.params[var]
            se = mod.bse[var]
            tval = mod.tvalues[var]
            pval = mod.pvalues[var]
            print(f"{var:<16} {coef:>10.5f} {se:>10.5f} {tval:>10.2f} {pval:>10.4e}")
        print(f"Within R2: {r2_within:.4f}")

        results['models'][dep_var] = {
            'label': label,
            'r2_within': float(r2_within),
            'coefs': {var: float(mod.params[var]) for var in reg_x_vars},
            'se': {var: float(mod.bse[var]) for var in reg_x_vars},
            'pvals': {var: float(mod.pvalues[var]) for var in reg_x_vars}
        }

    out_file = r'C:\Users\Z09057\poker-behavioral-economics\data\regression_house_money_results.json'
    with open(out_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved regression results to {out_file}")

if __name__ == '__main__':
    main()
