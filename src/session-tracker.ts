import { ProcessedPlayerHand, IntraSessionHandRecord, CompletedSession, WealthDomain } from './types.js';

export const DEFAULT_MAX_SESSION_GAP_SECONDS = 1200; // 20 minutes inactivity triggers new session
export const MIN_HANDS_PER_SESSION = 5; // Minimum session length for statistical validity

export class SessionTracker {
  private readonly maxGapSeconds: number;

  constructor(maxGapSeconds: number = DEFAULT_MAX_SESSION_GAP_SECONDS) {
    this.maxGapSeconds = maxGapSeconds;
  }

  /**
   * Processes a chronologically sorted sequence of hands for a single player
   * into discrete behavioral sessions and hand-level econometric panels.
   */
  public processPlayerHands(
    playerName: string,
    hands: ProcessedPlayerHand[]
  ): {
    handRecords: IntraSessionHandRecord[];
    sessions: CompletedSession[];
  } {
    if (hands.length === 0) {
      return { handRecords: [], sessions: [] };
    }

    // Sort hands chronologically by timestamp
    const sorted = [...hands].sort((a, b) => a.timestamp - b.timestamp);

    const allHandRecords: IntraSessionHandRecord[] = [];
    const allSessions: CompletedSession[] = [];

    let currentSessionHands: ProcessedPlayerHand[] = [];
    let sessionCounter = 1;

    for (let i = 0; i < sorted.length; i++) {
      const currentHand = sorted[i];

      if (currentSessionHands.length === 0) {
        currentSessionHands.push(currentHand);
      } else {
        const prevHand = currentSessionHands[currentSessionHands.length - 1];
        const gap = currentHand.timestamp - prevHand.timestamp;

        // If time gap exceeds threshold, close current session and start new
        if (gap > this.maxGapSeconds) {
          if (currentSessionHands.length >= MIN_HANDS_PER_SESSION) {
            const { records, session } = this.finalizeSession(playerName, sessionCounter++, currentSessionHands);
            allHandRecords.push(...records);
            allSessions.push(session);
          }
          currentSessionHands = [currentHand];
        } else {
          currentSessionHands.push(currentHand);
        }
      }
    }

    // Finalize trailing session if valid
    if (currentSessionHands.length >= MIN_HANDS_PER_SESSION) {
      const { records, session } = this.finalizeSession(playerName, sessionCounter++, currentSessionHands);
      allHandRecords.push(...records);
      allSessions.push(session);
    }

    return { handRecords: allHandRecords, sessions: allSessions };
  }

  private finalizeSession(
    playerName: string,
    sessionSeq: number,
    hands: ProcessedPlayerHand[]
  ): {
    records: IntraSessionHandRecord[];
    session: CompletedSession;
  } {
    const sessionId = `${playerName}_s${sessionSeq}_${hands[0].timestamp}`;
    const startTime = hands[0].timestamp;
    const endTime = hands[hands.length - 1].timestamp;
    const durationMinutes = Math.max(1, Math.round((endTime - startTime) / 60));
    const handCount = hands.length;

    const initialStack = hands[0].bankrollBefore;
    let runningCumPnl = 0;
    let peakPnl = 0;
    let troughPnl = 0;

    let vpipCount = 0;
    let pfrCount = 0;
    let aggCount = 0;

    const records: IntraSessionHandRecord[] = [];

    for (let hIdx = 0; hIdx < hands.length; hIdx++) {
      const h = hands[hIdx];
      const cumPnlBefore = runningCumPnl;
      const sessionElapsedMinutes = Math.round((h.timestamp - startTime) / 60);

      let domain: WealthDomain = 'breakeven';
      if (cumPnlBefore > 0) domain = 'gain';
      else if (cumPnlBefore < 0) domain = 'loss';

      const isInGain = cumPnlBefore > 0 ? 1 : 0;
      const isInLoss = cumPnlBefore < 0 ? 1 : 0;
      const isBreakEven = cumPnlBefore === 0 ? 1 : 0;
      const gainMagnitude = Math.max(0, cumPnlBefore);
      const lossMagnitude = Math.max(0, -cumPnlBefore);

      const isFinalHand = hIdx === hands.length - 1 ? 1 : 0;

      const betFrac = h.bankrollBefore > 0 ? Math.min(1.0, h.betAmount / h.bankrollBefore) : 0;

      if (h.vpip) vpipCount++;
      if (h.pfr) pfrCount++;
      if (h.aggressive) aggCount++;

      records.push({
        sessionId,
        playerName,
        handIndex: hIdx + 1,
        timestamp: h.timestamp,
        sessionElapsedMinutes,
        numPlayers: h.numPlayers,
        position: h.position,
        sessionStartingStack: initialStack,
        currentStack: h.bankrollBefore,
        cumSessionPnl: cumPnlBefore,
        domain,
        isInGain,
        isInLoss,
        isBreakEven,
        gainMagnitude,
        lossMagnitude,
        vpip: h.vpip ? 1 : 0,
        pfr: h.pfr ? 1 : 0,
        aggressive: h.aggressive ? 1 : 0,
        betAmount: h.betAmount,
        betFractionOfStack: betFrac,
        reachedShowdown: h.reachedShowdown ? 1 : 0,
        handPnl: h.pnl,
        quitAfterHand: isFinalHand
      });

      // Update running cumulative profit
      runningCumPnl += h.pnl;
      if (runningCumPnl > peakPnl) peakPnl = runningCumPnl;
      if (runningCumPnl < troughPnl) troughPnl = runningCumPnl;
    }

    const finalPnl = runningCumPnl;
    const finalStack = initialStack + finalPnl;

    const session: CompletedSession = {
      sessionId,
      playerName,
      startTime,
      endTime,
      durationMinutes,
      handCount,
      initialStack,
      finalStack,
      finalPnl,
      peakPnl,
      troughPnl,
      isWinningSession: finalPnl > 0 ? 1 : 0,
      isLosingSession: finalPnl < 0 ? 1 : 0,
      isExactBreakEven: finalPnl === 0 ? 1 : 0,
      isNearBreakEven: Math.abs(finalPnl) <= 10 ? 1 : 0,
      overallVpip: handCount > 0 ? vpipCount / handCount : 0,
      overallPfr: handCount > 0 ? pfrCount / handCount : 0,
      overallAggression: handCount > 0 ? aggCount / handCount : 0
    };

    return { records, session };
  }
}
