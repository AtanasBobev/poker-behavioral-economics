import pandas as pd
import numpy as np

sess_path = r'C:\Users\Z09057\poker-behavioral-economics\data\q4_session_stopping.csv'
hands_path = r'C:\Users\Z09057\poker-behavioral-economics\data\q2_house_money_risk.csv'

df_sess = pd.read_csv(sess_path)
print(f"Total sessions: {len(df_sess):,}")

# Breakdown of exact W=0 sessions
zero_sess = df_sess[df_sess['final_pnl'] == 0]
active_clawback = df_sess[(df_sess['trough_pnl'] < 0) & (df_sess['final_pnl'] == 0)]
active_giveback = df_sess[(df_sess['peak_pnl'] > 0) & (df_sess['final_pnl'] == 0) & (df_sess['trough_pnl'] == 0)]
passive_flatline = df_sess[(df_sess['peak_pnl'] == 0) & (df_sess['trough_pnl'] == 0)]

print(f"Total exact W=0: {len(zero_sess):,}")
print(f"  - Active clawback (was in deficit, returned to exactly 0): {len(active_clawback):,}")
print(f"  - Active giveback (was in profit, returned to exactly 0): {len(active_giveback):,}")
print(f"  - Passive zero (never won or lost any chip): {len(passive_flatline):,}")

# Non-zero sessions: near break-even [-10, +10]
near_zero = df_sess[(df_sess['final_pnl'].abs() <= 10) & (df_sess['final_pnl'] != 0)]
print(f"Near break-even within 10 chips (excluding exact 0): {len(near_zero):,}")

# Voluntary vs Forced Exits
busted = df_sess[df_sess['final_stack'] <= 0]
voluntary = df_sess[df_sess['final_stack'] > 0]
print(f"\nBust-outs (stack <= 0): {len(busted):,} ({len(busted)/len(df_sess):.2%})")
print(f"Voluntary exits (stack > 0): {len(voluntary):,} ({len(voluntary)/len(df_sess):.2%})")

print("\nVoluntary Exits Duration by Outcome:")
print("Winning:   Mean hands =", voluntary[voluntary['is_winning'] == 1]['hand_count'].mean(),
      "| Mean dur (min) =", voluntary[voluntary['is_winning'] == 1]['duration_minutes'].mean())
print("Losing:    Mean hands =", voluntary[voluntary['is_losing'] == 1]['hand_count'].mean(),
      "| Mean dur (min) =", voluntary[voluntary['is_losing'] == 1]['duration_minutes'].mean())
print("Break-even: Mean hands =", voluntary[voluntary['final_pnl'] == 0]['hand_count'].mean(),
      "| Mean dur (min) =", voluntary[voluntary['final_pnl'] == 0]['duration_minutes'].mean())

# Hands data: check absolute bet amounts
df_hands = pd.read_csv(hands_path)
print("\nHand-level absolute bet amount:")
print("In gain:      Mean bet =", df_hands[df_hands['in_gain'] == 1]['bet_amount'].mean())
print("In loss:      Mean bet =", df_hands[df_hands['in_loss'] == 1]['bet_amount'].mean())
print("At zero (W=0): Mean bet =", df_hands[df_hands['is_breakeven'] == 1]['bet_amount'].mean())

print("\nHand-level VPIP:")
print("In gain:      Mean VPIP =", df_hands[df_hands['in_gain'] == 1]['vpip'].mean())
print("In loss:      Mean VPIP =", df_hands[df_hands['in_loss'] == 1]['vpip'].mean())
print("At zero (W=0): Mean VPIP =", df_hands[df_hands['is_breakeven'] == 1]['vpip'].mean())

print("\nHand-level PFR (Preflop Raise):")
print("In gain:      Mean PFR =", df_hands[df_hands['in_gain'] == 1]['pfr'].mean())
print("In loss:      Mean PFR =", df_hands[df_hands['in_loss'] == 1]['pfr'].mean())
print("At zero (W=0): Mean PFR =", df_hands[df_hands['is_breakeven'] == 1]['pfr'].mean())
