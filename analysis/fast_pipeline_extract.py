import glob
import os
import tarfile
import time
import re
import pandas as pd
import numpy as np

"""
High-throughput census extraction pipeline for CPRG IRC Texas Hold'em database.
Implements the exact logic from TypeScript types.ts and session-tracker.ts.
Processes monthly .tgz archives directly in-stream to bypass Windows filename limitations.
Generates structured econometric panels:
1. data/q2_house_money_risk.csv (hand-level panel with player FE controls)
2. data/q4_session_stopping.csv (completed session records for bunching & duration)
3. data/q4_hazard_panel.csv (discrete-time hazard panel for survival analysis)
"""

MAX_SESSION_GAP_SECONDS = 1200 # 20 minutes
MIN_HANDS_PER_SESSION = 5

def parse_pdb_line(line):
    line = line.strip()
    if not line or line.startswith('#'):
        return None
    tokens = line.split()
    if len(tokens) < 11:
        return None
    try:
        player = tokens[0]
        ts = int(tokens[1])
        num_players = int(tokens[2])
        pos = int(tokens[3])
        prflop = tokens[4]
        flop = tokens[5]
        turn = tokens[6]
        river = tokens[7]
        stack_before = float(tokens[8])
        bet = float(tokens[9])
        won = float(tokens[10])
    except (ValueError, IndexError):
        return None
    
    # Behavioral markers
    # VPIP: Voluntarily Put Money in Pot (c = call, b = bet, r = raise)
    vpip = 1 if re.search(r'[cbr]', prflop) else 0
    # PFR: Preflop raise
    pfr = 1 if 'r' in prflop else 0
    # Aggressive action on any street
    all_act = prflop + flop + turn + river
    aggressive = 1 if re.search(r'[br]', all_act) else 0
    
    cards = (tokens[11], tokens[12]) if len(tokens) >= 13 else None
    saw_flop = 1 if flop not in ('-', '') else 0
    reached_showdown = 1 if (cards is not None or (river not in ('-', '') and 'f' not in river)) else 0
    
    pnl = won - bet
    return {
        'player': player,
        'timestamp': ts,
        'num_players': num_players,
        'position': pos,
        'stack_before': stack_before,
        'bet': bet,
        'won': won,
        'pnl': pnl,
        'vpip': vpip,
        'pfr': pfr,
        'aggressive': aggressive,
        'saw_flop': saw_flop,
        'showdown': reached_showdown
    }

def process_player_hands(player, hands):
    if len(hands) < MIN_HANDS_PER_SESSION:
        return [], []
    
    hands.sort(key=lambda h: h['timestamp'])
    
    sessions = []
    hand_records = []
    
    curr_hands = []
    sess_id_counter = 1
    
    for h in hands:
        if not curr_hands:
            curr_hands.append(h)
        else:
            gap = h['timestamp'] - curr_hands[-1]['timestamp']
            if gap > MAX_SESSION_GAP_SECONDS:
                if len(curr_hands) >= MIN_HANDS_PER_SESSION:
                    recs, sess = finalize_session(player, sess_id_counter, curr_hands)
                    sess_id_counter += 1
                    hand_records.extend(recs)
                    sessions.append(sess)
                curr_hands = [h]
            else:
                curr_hands.append(h)
                
    if len(curr_hands) >= MIN_HANDS_PER_SESSION:
        recs, sess = finalize_session(player, sess_id_counter, curr_hands)
        hand_records.extend(recs)
        sessions.append(sess)
        
    return hand_records, sessions

def finalize_session(player, sess_seq, hands):
    sess_id = f"{player}_s{sess_seq}_{hands[0]['timestamp']}"
    start_time = hands[0]['timestamp']
    end_time = hands[-1]['timestamp']
    duration_min = max(1, round((end_time - start_time) / 60))
    hand_count = len(hands)
    initial_stack = hands[0]['stack_before']
    
    running_cum_pnl = 0.0
    peak_pnl = 0.0
    trough_pnl = 0.0
    
    vpip_cnt = 0
    pfr_cnt = 0
    agg_cnt = 0
    
    records = []
    for idx, h in enumerate(hands):
        cum_before = running_cum_pnl
        in_gain = 1 if cum_before > 0 else 0
        in_loss = 1 if cum_before < 0 else 0
        is_breakeven = 1 if cum_before == 0 else 0
        gain_mag = max(0.0, cum_before)
        loss_mag = max(0.0, -cum_before)
        
        is_quit = 1 if idx == hand_count - 1 else 0
        bet_frac = min(1.0, h['bet'] / h['stack_before']) if h['stack_before'] > 0 else 0.0
        
        vpip_cnt += h['vpip']
        pfr_cnt += h['pfr']
        agg_cnt += h['aggressive']
        
        records.append({
            'session_id': sess_id,
            'player': player,
            'hand_index': idx + 1,
            'timestamp': h['timestamp'],
            'elapsed_minutes': round((h['timestamp'] - start_time) / 60),
            'num_players': h['num_players'],
            'position': h['position'],
            'initial_stack': initial_stack,
            'current_stack': h['stack_before'],
            'cum_session_pnl': cum_before,
            'in_gain': in_gain,
            'in_loss': in_loss,
            'is_breakeven': is_breakeven,
            'gain_magnitude': gain_mag,
            'loss_magnitude': loss_mag,
            'vpip': h['vpip'],
            'pfr': h['pfr'],
            'aggressive': h['aggressive'],
            'bet_amount': h['bet'],
            'bet_fraction': bet_frac,
            'showdown': h['showdown'],
            'hand_pnl': h['pnl'],
            'quit_after_hand': is_quit
        })
        
        running_cum_pnl += h['pnl']
        if running_cum_pnl > peak_pnl:
            peak_pnl = running_cum_pnl
        if running_cum_pnl < trough_pnl:
            trough_pnl = running_cum_pnl
            
    final_pnl = running_cum_pnl
    final_stack = initial_stack + final_pnl
    
    sess_summary = {
        'session_id': sess_id,
        'player': player,
        'start_time': start_time,
        'end_time': end_time,
        'duration_minutes': duration_min,
        'hand_count': hand_count,
        'initial_stack': initial_stack,
        'final_stack': final_stack,
        'final_pnl': final_pnl,
        'peak_pnl': peak_pnl,
        'trough_pnl': trough_pnl,
        'is_winning': 1 if final_pnl > 0 else 0,
        'is_losing': 1 if final_pnl < 0 else 0,
        'is_exact_breakeven': 1 if final_pnl == 0 else 0,
        'is_near_breakeven': 1 if abs(final_pnl) <= 10 else 0,
        'overall_vpip': vpip_cnt / hand_count,
        'overall_pfr': pfr_cnt / hand_count,
        'overall_aggression': agg_cnt / hand_count
    }
    
    return records, sess_summary

def main():
    t0 = time.time()
    raw_dir = r'C:\Users\Z09057\poker_raw\IRCdata'
    out_dir = r'C:\Users\Z09057\poker-behavioral-economics\data'
    os.makedirs(out_dir, exist_ok=True)
    
    tgzs = sorted(glob.glob(os.path.join(raw_dir, 'holdem.*.tgz')))
    # Filter out corrupted file 199910
    tgzs = [t for t in tgzs if '199910' not in t]
    
    # Process 24 months (2 full years: April 1995 to March 1997) for a clean, dense empirical sample
    target_tgzs = tgzs[:24]
    print(f"Executing extraction across {len(target_tgzs)} monthly holdem archives...")
    
    all_hand_records = []
    all_sessions = []
    
    for tgz_idx, tgz in enumerate(target_tgzs):
        m_name = os.path.basename(tgz)
        t_sub = time.time()
        m_hands = 0
        m_sessions = 0
        with tarfile.open(tgz, 'r:gz') as tar:
            for member in tar.getmembers():
                if '/pdb/pdb.' in member.name:
                    f = tar.extractfile(member)
                    if f is not None:
                        lines = [line.decode('utf-8', errors='ignore') for line in f]
                        parsed_hands = []
                        for l in lines:
                            p = parse_pdb_line(l)
                            if p:
                                parsed_hands.append(p)
                        if parsed_hands:
                            player = parsed_hands[0]['player']
                            recs, sess_list = process_player_hands(player, parsed_hands)
                            if recs:
                                all_hand_records.extend(recs)
                                m_hands += len(recs)
                            if sess_list:
                                all_sessions.extend(sess_list)
                                m_sessions += len(sess_list)
        print(f"[{tgz_idx+1:02d}/{len(target_tgzs):02d}] {m_name}: {m_hands:,} hands, {m_sessions:,} sessions ({time.time() - t_sub:.2f}s)")
        
    print(f"\nCompleted extraction in {time.time() - t0:.2f}s.")
    print(f"Total hand observations: {len(all_hand_records):,}")
    print(f"Total completed sessions: {len(all_sessions):,}")
    
    df_hands = pd.DataFrame(all_hand_records)
    df_sessions = pd.DataFrame(all_sessions)
    
    # Save datasets
    print("Writing CSV files to data/...")
    hands_csv = os.path.join(out_dir, 'q2_house_money_risk.csv')
    sessions_csv = os.path.join(out_dir, 'q4_session_stopping.csv')
    
    df_hands.to_csv(hands_csv, index=False)
    df_sessions.to_csv(sessions_csv, index=False)
    
    # Generate discrete-time hazard panel
    print("Generating discrete-time survival hazard panel...")
    # Sample down or export hazard panel
    hazard_csv = os.path.join(out_dir, 'q4_hazard_panel.csv')
    hazard_cols = ['session_id', 'player', 'hand_index', 'elapsed_minutes', 'cum_session_pnl',
                   'in_gain', 'in_loss', 'is_breakeven', 'gain_magnitude', 'loss_magnitude',
                   'quit_after_hand']
    df_hands[hazard_cols].to_csv(hazard_csv, index=False)
    
    print("All datasets successfully written.")
    print(f"Risk Panel: {os.path.getsize(hands_csv) / 1024 / 1024:.2f} MB")
    print(f"Sessions: {os.path.getsize(sessions_csv) / 1024 / 1024:.2f} MB")
    print(f"Hazard Panel: {os.path.getsize(hazard_csv) / 1024 / 1024:.2f} MB")

if __name__ == '__main__':
    main()
