import pandas as pd
import numpy as np

df_sess = pd.read_csv(r'C:\Users\Z09057\poker-behavioral-economics\data\q4_session_stopping.csv')
print(f"Total sessions: {len(df_sess):,}")
print("Final PnL distribution percentiles:")
print(df_sess['final_pnl'].describe(percentiles=[0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99]))

print("\nTop 15 most frequent exact final PnL values:")
print(df_sess['final_pnl'].value_counts().head(15))

df_hands = pd.read_csv(r'C:\Users\Z09057\poker-behavioral-economics\data\q2_house_money_risk.csv')
quit_hands = df_hands[df_hands['quit_after_hand'] == 1]
non_quit = df_hands[df_hands['quit_after_hand'] == 0]

print(f"\nQuit hands count: {len(quit_hands):,}")
print(f"Quit on win (pnl > 0): {(quit_hands['hand_pnl'] > 0).mean():.4f}")
print(f"Non-quit on win (pnl > 0): {(non_quit['hand_pnl'] > 0).mean():.4f}")

print(f"Quit on loss (pnl < 0): {(quit_hands['hand_pnl'] < 0).mean():.4f}")
print(f"Non-quit on loss (pnl < 0): {(non_quit['hand_pnl'] < 0).mean():.4f}")

# Look at stack depletion / bust-outs: quitting with stack == 0
busted_quits = (quit_hands['current_stack'] + quit_hands['hand_pnl'] <= 0).sum()
print(f"Busted quits (stack <= 0): {busted_quits:,} ({busted_quits / len(quit_hands):.2%})")

# Voluntary quits (stack > 0)
vol_quits = quit_hands[quit_hands['current_stack'] + quit_hands['hand_pnl'] > 0]
print(f"Voluntary quits: {len(vol_quits):,}")
print(f"Voluntary quit on win: {(vol_quits['hand_pnl'] > 0).mean():.4f}")
print(f"Voluntary quit on loss: {(vol_quits['hand_pnl'] < 0).mean():.4f}")
