import * as fs from 'fs';
import * as path from 'path';
import { IrcPokerParser } from './irc-parser.js';
import { SessionTracker } from './session-tracker.js';
import { ProcessedPlayerHand, IntraSessionHandRecord, CompletedSession } from './types.js';

export interface PipelineOptions {
  dataDir: string;
  outputDir: string;
  maxMonths?: number;
}

export class StreamPipeline {
  private readonly options: PipelineOptions;
  private readonly tracker: SessionTracker;

  constructor(options: PipelineOptions) {
    this.options = options;
    this.tracker = new SessionTracker();
  }

  /**
   * Processes all player data across available months and writes structured econometric datasets.
   */
  public async run(): Promise<{ totalHands: number; totalSessions: number }> {
    console.log(`[StreamPipeline] Initializing pipeline from ${this.options.dataDir}`);
    fs.mkdirSync(this.options.outputDir, { recursive: true });

    const riskCsvPath = path.join(this.options.outputDir, 'q2_house_money_risk.csv');
    const sessionsCsvPath = path.join(this.options.outputDir, 'q4_session_stopping.csv');

    const riskWriteStream = fs.createWriteStream(riskCsvPath, { flags: 'w' });
    const sessionWriteStream = fs.createWriteStream(sessionsCsvPath, { flags: 'w' });

    // Write CSV Headers
    riskWriteStream.write(
      'session_id,player_name,hand_index,timestamp,elapsed_minutes,num_players,position,' +
      'initial_stack,current_stack,cum_session_pnl,domain,is_in_gain,is_in_loss,is_break_even,' +
      'gain_magnitude,loss_magnitude,vpip,pfr,aggressive,bet_amount,bet_fraction,reached_showdown,hand_pnl,quit_after_hand\n'
    );

    sessionWriteStream.write(
      'session_id,player_name,start_time,end_time,duration_minutes,hand_count,' +
      'initial_stack,final_stack,final_pnl,peak_pnl,trough_pnl,' +
      'is_winning,is_losing,is_exact_breakeven,is_near_breakeven,overall_vpip,overall_pfr,overall_aggression\n'
    );

    let totalHandsWritten = 0;
    let totalSessionsWritten = 0;

    // Scan for monthly directories in dataDir
    // Expected structure: dataDir/holdem/YYYYMM/pdb/pdb.<player>
    const holdemDir = path.join(this.options.dataDir, 'holdem');
    if (!fs.existsSync(holdemDir)) {
      console.warn(`[StreamPipeline] Holdem directory not found at ${holdemDir}`);
      return { totalHands: 0, totalSessions: 0 };
    }

    const monthDirs = fs.readdirSync(holdemDir)
      .filter(f => /^\d{6}$/.test(f))
      .sort();

    const selectedMonths = this.options.maxMonths 
      ? monthDirs.slice(0, this.options.maxMonths)
      : monthDirs;

    console.log(`[StreamPipeline] Processing ${selectedMonths.length} months: ${selectedMonths.join(', ')}`);

    for (const month of selectedMonths) {
      const pdbDir = path.join(holdemDir, month, 'pdb');
      if (!fs.existsSync(pdbDir)) continue;

      const playerFiles = fs.readdirSync(pdbDir).filter(f => f.startsWith('pdb.'));
      console.log(`[StreamPipeline] Month ${month}: Found ${playerFiles.length} players`);

      for (const pFile of playerFiles) {
        const fullPath = path.join(pdbDir, pFile);
        try {
          const content = fs.readFileSync(fullPath, 'utf-8');
          const lines = content.split('\n');

          const hands: ProcessedPlayerHand[] = [];
          for (const line of lines) {
            const parsed = IrcPokerParser.parsePdbLine(line);
            if (parsed) {
              hands.push(parsed);
            }
          }

          if (hands.length < 5) continue;

          const playerName = hands[0].playerName;
          const { handRecords, sessions } = this.tracker.processPlayerHands(playerName, hands);

          for (const rec of handRecords) {
            riskWriteStream.write(
              `${rec.sessionId},${rec.playerName},${rec.handIndex},${rec.timestamp},${rec.sessionElapsedMinutes},` +
              `${rec.numPlayers},${rec.position},${rec.sessionStartingStack},${rec.currentStack},${rec.cumSessionPnl},` +
              `${rec.domain},${rec.isInGain},${rec.isInLoss},${rec.isBreakEven},${rec.gainMagnitude},${rec.lossMagnitude},` +
              `${rec.vpip},${rec.pfr},${rec.aggressive},${rec.betAmount},${rec.betFractionOfStack.toFixed(4)},` +
              `${rec.reachedShowdown},${rec.handPnl},${rec.quitAfterHand}\n`
            );
            totalHandsWritten++;
          }

          for (const sess of sessions) {
            sessionWriteStream.write(
              `${sess.sessionId},${sess.playerName},${sess.startTime},${sess.endTime},${sess.durationMinutes},` +
              `${sess.handCount},${sess.initialStack},${sess.finalStack},${sess.finalPnl},${sess.peakPnl},${sess.troughPnl},` +
              `${sess.isWinningSession},${sess.isLosingSession},${sess.isExactBreakEven},${sess.isNearBreakEven},` +
              `${sess.overallVpip.toFixed(4)},${sess.overallPfr.toFixed(4)},${sess.overallAggression.toFixed(4)}\n`
            );
            totalSessionsWritten++;
          }
        } catch (err) {
          // Skip corrupted or unreadable files
        }
      }
    }

    riskWriteStream.end();
    sessionWriteStream.end();

    console.log(`[StreamPipeline] Successfully extracted ${totalHandsWritten.toLocaleString()} hand observations across ${totalSessionsWritten.toLocaleString()} completed sessions.`);
    return { totalHands: totalHandsWritten, totalSessions: totalSessionsWritten };
  }
}
