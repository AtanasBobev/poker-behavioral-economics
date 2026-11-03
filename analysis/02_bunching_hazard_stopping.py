import os
import json
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

"""
Econometric Module 2: Asymmetric Session Stopping, Break-Even Bunching, and Survival Hazards
Tests Camerer et al. (1997), Farber (2005, 2015), and Imas (2016) reference-dependent stopping.
1. Sharp bunching estimation at W = 0 (McCrary 2008 / Chetty et al. 2011 density excess test).
2. Discrete-time hazard model of session termination h(t | W_it).
3. Sunk-cost duration escalation: Losing sessions vs. Winning sessions duration analysis.
"""

def main():
    sess_path = r'C:\Users\Z09057\poker-behavioral-economics\data\q4_session_stopping.csv'
    hazard_path = r'C:\Users\Z09057\poker-behavioral-economics\data\q4_hazard_panel.csv'

    if not os.path.exists(sess_path):
        print(f"Session data not found at {sess_path}. Waiting for pipeline...")
        return

    print("Loading session datasets...")
    df_sess = pd.read_csv(sess_path)
    print(f"Loaded {len(df_sess):,} completed sessions.")

    # 1. BUNCHING ESTIMATION AT W_EXIT = 0
    print("\n--- 1. McCrary / Polynomial Bunching Estimation at Break-Even (W = 0) ---")
    # Focus on sessions with final PnL in [-150, 150]
    pnl_sub = df_sess[(df_sess['final_pnl'] >= -150) & (df_sess['final_pnl'] <= 150)]['final_pnl']
    bin_width = 5.0
    bins = np.arange(-150, 150 + bin_width, bin_width)
    counts, bin_edges = np.histogram(pnl_sub, bins=bins)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    df_bunch = pd.DataFrame({'bin_center': bin_centers, 'count': counts})
    df_bunch['dist_to_zero'] = np.abs(df_bunch['bin_center'])
    # Define bunching window around zero: [-10, 10]
    bunching_window = (df_bunch['bin_center'] >= -10) & (df_bunch['bin_center'] <= 10)
    df_bunch['in_window'] = bunching_window.astype(int)

    # Fit 5th degree polynomial counterfactual excluding bunching window
    df_fit = df_bunch[~bunching_window].copy()
    poly_terms = np.vander(df_fit['bin_center'], 6)
    poly_coefs = np.linalg.lstsq(poly_terms, df_fit['count'], rcond=None)[0]

    full_vander = np.vander(df_bunch['bin_center'], 6)
    df_bunch['counterfactual'] = np.dot(full_vander, poly_coefs)

    actual_bunch_count = df_bunch[bunching_window]['count'].sum()
    cf_bunch_count = df_bunch[bunching_window]['counterfactual'].sum()
    excess_mass = actual_bunch_count - cf_bunch_count
    b_ratio = excess_mass / cf_bunch_count

    print(f"Actual count in [-10, +10]: {actual_bunch_count:,}")
    print(f"Counterfactual count: {cf_bunch_count:,.1f}")
    print(f"Excess mass at break-even: {excess_mass:,.1f}")
    print(f"Normalized bunching ratio (b): {b_ratio:.4f}")

    # 2. ASYMMETRIC DURATION ESCALATION (LOSING VS WINNING SESSIONS)
    print("\n--- 2. Asymmetric Duration Escalation (Losing vs Winning Sessions) ---")
    df_valid_sess = df_sess[(df_sess['duration_minutes'] <= 600) & (df_sess['hand_count'] <= 600)].copy()
    
    mean_hands_win = df_valid_sess[df_valid_sess['is_winning'] == 1]['hand_count'].mean()
    mean_hands_loss = df_valid_sess[df_valid_sess['is_losing'] == 1]['hand_count'].mean()
    mean_dur_win = df_valid_sess[df_valid_sess['is_winning'] == 1]['duration_minutes'].mean()
    mean_dur_loss = df_valid_sess[df_valid_sess['is_losing'] == 1]['duration_minutes'].mean()

    print(f"Winning sessions: Mean Hands = {mean_hands_win:.1f}, Mean Duration = {mean_dur_win:.1f} min")
    print(f"Losing sessions:  Mean Hands = {mean_hands_loss:.1f}, Mean Duration = {mean_dur_loss:.1f} min")
    print(f"Delta: Losing sessions are +{mean_hands_loss - mean_hands_win:.1f} hands (+{mean_dur_loss - mean_dur_win:.1f} min) longer")

    # Regress duration and hands on losing indicator with player controls
    f_hands = 'hand_count ~ is_losing + initial_stack'
    mod_hands = smf.ols(f_hands, data=df_valid_sess).fit(cov_type='HC1')

    f_dur = 'duration_minutes ~ is_losing + initial_stack'
    mod_dur = smf.ols(f_dur, data=df_valid_sess).fit(cov_type='HC1')

    # 3. DISCRETE-TIME SURVIVAL HAZARD MODEL
    print("\n--- 3. Discrete-Time Survival Hazard Model of Session Termination ---")
    df_haz = pd.read_csv(hazard_path)
    # Downsample if very large for fast logit estimation
    if len(df_haz) > 500000:
        df_haz_sample = df_haz.sample(n=500000, random_state=42).copy()
    else:
        df_haz_sample = df_haz.copy()

    df_haz_sample['is_near_zero'] = ((df_haz_sample['cum_session_pnl'] >= -10) & 
                                     (df_haz_sample['cum_session_pnl'] <= 10)).astype(int)

    f_haz = 'quit_after_hand ~ is_near_zero + in_gain + in_loss + hand_index + elapsed_minutes'
    logit_mod = smf.logit(f_haz, data=df_haz_sample).fit(disp=False)
    print(logit_mod.summary().tables[1].as_text()[:600])

    # Save summary results
    results = {
        'total_sessions': int(len(df_sess)),
        'bunching': {
            'b_ratio': float(b_ratio),
            'excess_mass': float(excess_mass),
            'actual_count': int(actual_bunch_count),
            'counterfactual_count': float(cf_bunch_count)
        },
        'duration': {
            'mean_hands_win': float(mean_hands_win),
            'mean_hands_loss': float(mean_hands_loss),
            'mean_dur_win': float(mean_dur_win),
            'mean_dur_loss': float(mean_dur_loss),
            'loss_delta_hands': float(mean_hands_loss - mean_hands_win),
            'loss_delta_dur': float(mean_dur_loss - mean_dur_win),
            'reg_loss_hands_coef': float(mod_hands.params.get('is_losing', 0)),
            'reg_loss_hands_se': float(mod_hands.bse.get('is_losing', 0)),
            'reg_loss_hands_p': float(mod_hands.pvalues.get('is_losing', 0)),
            'reg_loss_dur_coef': float(mod_dur.params.get('is_losing', 0)),
            'reg_loss_dur_se': float(mod_dur.bse.get('is_losing', 0)),
            'reg_loss_dur_p': float(mod_dur.pvalues.get('is_losing', 0))
        },
        'hazard': {
            'near_zero_coef': float(logit_mod.params.get('is_near_zero', 0)),
            'near_zero_se': float(logit_mod.bse.get('is_near_zero', 0)),
            'near_zero_p': float(logit_mod.pvalues.get('is_near_zero', 0)),
            'in_gain_coef': float(logit_mod.params.get('in_gain', 0)),
            'in_gain_se': float(logit_mod.bse.get('in_gain', 0)),
            'in_loss_coef': float(logit_mod.params.get('in_loss', 0)),
            'in_loss_se': float(logit_mod.bse.get('in_loss', 0))
        }
    }

    out_file = r'C:\Users\Z09057\poker-behavioral-economics\data\stopping_bunching_results.json'
    with open(out_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved stopping & bunching results to {out_file}")

if __name__ == '__main__':
    main()
