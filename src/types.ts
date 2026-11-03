/**
 * Core domain types and interfaces for econometric modeling of poker decision-making.
 * Captures within-session wealth dynamics, risk-taking propensity, and session termination.
 */

export interface RawPlayerHand {
  playerName: string;
  timestamp: number;
  numPlayers: number;
  position: number;
  preflopAction: string;
  flopAction: string;
  turnAction: string;
  riverAction: string;
  bankrollBefore: number;
  betAmount: number;
  wonAmount: number;
  holeCards?: [string, string];
}

export interface ProcessedPlayerHand extends RawPlayerHand {
  pnl: number;
  bankrollAfter: number;
  vpip: boolean;        // Voluntarily Put Money in Pot (called, bet, or raised preflop)
  pfr: boolean;         // Preflop Raise
  aggressive: boolean;  // Bet or raised on any street (preflop, flop, turn, river)
  sawFlop: boolean;
  reachedShowdown: boolean;
}

export type WealthDomain = 'gain' | 'loss' | 'breakeven';

export interface IntraSessionHandRecord {
  sessionId: string;
  playerName: string;
  handIndex: number;
  timestamp: number;
  sessionElapsedMinutes: number;
  numPlayers: number;
  position: number;
  
  // Wealth and Reference Point State (measured BEFORE hand decisions)
  sessionStartingStack: number;
  currentStack: number;
  cumSessionPnl: number;
  domain: WealthDomain;
  isInGain: number;       // Indicator: 1 if cumSessionPnl > 0
  isInLoss: number;       // Indicator: 1 if cumSessionPnl < 0
  isBreakEven: number;    // Indicator: 1 if cumSessionPnl == 0
  gainMagnitude: number;  // max(0, cumSessionPnl)
  lossMagnitude: number;  // max(0, -cumSessionPnl)

  // Risk Decisions in Current Hand
  vpip: number;           // 1 if voluntarily entered pot, 0 otherwise
  pfr: number;            // 1 if raised preflop, 0 otherwise
  aggressive: number;     // 1 if bet or raised postflop, 0 otherwise
  betAmount: number;
  betFractionOfStack: number;
  reachedShowdown: number;

  // Outcome
  handPnl: number;
  
  // Stopping Outcome (1 if this was the final hand of the session, 0 otherwise)
  quitAfterHand: number;
}

export interface CompletedSession {
  sessionId: string;
  playerName: string;
  startTime: number;
  endTime: number;
  durationMinutes: number;
  handCount: number;
  
  initialStack: number;
  finalStack: number;
  finalPnl: number;
  peakPnl: number;
  troughPnl: number;
  
  isWinningSession: number;
  isLosingSession: number;
  isExactBreakEven: number;
  isNearBreakEven: number; // Within 1 small bet / big blind
  
  overallVpip: number;
  overallPfr: number;
  overallAggression: number;
}
