import pandas as pd
import numpy as np

df_hands = pd.read_csv(r'C:\Users\Z09057\poker-behavioral-economics\data\q2_house_money_risk.csv')

# Hazard across cumulative PnL bins
bins = [-1000, -500, -200, -100, -50, -20, -5, 5, 20, 50, 100, 200, 500, 1000]
df_hands['wealth_bucket'] = pd.cut(df_hands['cum_session_pnl'], bins=bins)

hazard_by_bucket = df_hands.groupby('wealth_bucket', observed=True).agg(
    n_hands=('quit_after_hand', 'count'),
    n_quits=('quit_after_hand', 'sum'),
    hazard=('quit_after_hand', 'mean')
).reset_index()

print("Empirical Session Exit Hazard Rate by Cumulative Intra-Session PnL:")
print(hazard_by_bucket)

# What about after a big loss in hand t vs small loss vs win?
df_hands['hand_outcome'] = 'zero'
df_hands.loc[df_hands['hand_pnl'] > 0, 'hand_outcome'] = 'win'
df_hands.loc[df_hands['hand_pnl'] < 0, 'hand_outcome'] = 'loss'

hazard_by_outcome = df_hands.groupby('hand_outcome').agg(
    n_hands=('quit_after_hand', 'count'),
    n_quits=('quit_after_hand', 'sum'),
    hazard=('quit_after_hand', 'mean')
).reset_index()

print("\nExit Hazard by Immediate Hand Outcome:")
print(hazard_by_outcome)
