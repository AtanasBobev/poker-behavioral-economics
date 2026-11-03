import os
import json
import pandas as pd
import numpy as np

def main():
    data_dir = r'C:\Users\Z09057\poker-behavioral-economics\data'
    hands_file = os.path.join(data_dir, 'q2_house_money_risk.csv')
    sess_file = os.path.join(data_dir, 'q4_session_stopping.csv')

    print("Computing Table 1 summary statistics...")
    df_hands = pd.read_csv(hands_file)
    df_sess = pd.read_csv(sess_file)

    n_hands = len(df_hands)
    n_sess = len(df_sess)
    n_players = df_hands['player'].nunique()

    # Hand-level stats
    vpip_mean = df_hands['vpip'].mean()
    vpip_sd = df_hands['vpip'].std()
    pfr_mean = df_hands['pfr'].mean()
    pfr_sd = df_hands['pfr'].std()
    agg_mean = df_hands['aggressive'].mean()
    agg_sd = df_hands['aggressive'].std()
    bet_mean = df_hands['bet_amount'].mean()
    bet_sd = df_hands['bet_amount'].std()
    bet_frac_mean = df_hands['bet_fraction'].mean()
    bet_frac_sd = df_hands['bet_fraction'].std()
    stack_mean = df_hands['current_stack'].mean()
    stack_sd = df_hands['current_stack'].std()
    cum_pnl_mean = df_hands['cum_session_pnl'].mean()
    cum_pnl_sd = df_hands['cum_session_pnl'].std()
    showdown_mean = df_hands['showdown'].mean()

    # Session-level stats
    dur_mean = df_sess['duration_minutes'].mean()
    dur_sd = df_sess['duration_minutes'].std()
    hands_per_sess_mean = df_sess['hand_count'].mean()
    hands_per_sess_sd = df_sess['hand_count'].std()
    final_pnl_mean = df_sess['final_pnl'].mean()
    final_pnl_sd = df_sess['final_pnl'].std()
    win_sess_pct = (df_sess['final_pnl'] > 0).mean()
    loss_sess_pct = (df_sess['final_pnl'] < 0).mean()
    exact_be_pct = (df_sess['final_pnl'] == 0).mean()
    near_be_pct = (df_sess['final_pnl'].abs() <= 10).mean()

    summary_stats = {
        'n_hands': int(n_hands),
        'n_sess': int(n_sess),
        'n_players': int(n_players),
        'hand_level': {
            'vpip': {'mean': float(vpip_mean), 'sd': float(vpip_sd)},
            'pfr': {'mean': float(pfr_mean), 'sd': float(pfr_sd)},
            'aggression': {'mean': float(agg_mean), 'sd': float(agg_sd)},
            'bet_amount': {'mean': float(bet_mean), 'sd': float(bet_sd)},
            'bet_fraction': {'mean': float(bet_frac_mean), 'sd': float(bet_frac_sd)},
            'current_stack': {'mean': float(stack_mean), 'sd': float(stack_sd)},
            'cum_pnl': {'mean': float(cum_pnl_mean), 'sd': float(cum_pnl_sd)},
            'showdown': {'mean': float(showdown_mean)}
        },
        'session_level': {
            'duration_minutes': {'mean': float(dur_mean), 'sd': float(dur_sd)},
            'hands_per_session': {'mean': float(hands_per_sess_mean), 'sd': float(hands_per_sess_sd)},
            'final_pnl': {'mean': float(final_pnl_mean), 'sd': float(final_pnl_sd)},
            'win_fraction': float(win_sess_pct),
            'loss_fraction': float(loss_sess_pct),
            'exact_breakeven_fraction': float(exact_be_pct),
            'near_breakeven_fraction': float(near_be_pct)
        }
    }

    out_file = os.path.join(data_dir, 'summary_statistics.json')
    with open(out_file, 'w') as f:
        json.dump(summary_stats, f, indent=2)

    print(f"Summary statistics calculated and saved to {out_file}")
    print(json.dumps(summary_stats, indent=2))

if __name__ == '__main__':
    main()
