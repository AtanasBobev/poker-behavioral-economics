import { RawPlayerHand, ProcessedPlayerHand } from './types.js';

/**
 * High-performance parser for the University of Alberta CPRG IRC Poker Database pdb format.
 * Format:
 * [0] player: string
 * [1] timestamp: integer Unix epoch
 * [2] numPlayers: integer (table size)
 * [3] position: integer
 * [4] preflopAction: string (e.g., 'Bc', 'Bf', 'k', 'r', 'c')
 * [5] flopAction: string
 * [6] turnAction: string
 * [7] riverAction: string
 * [8] bankrollBefore: integer/float (chips before hand)
 * [9] betAmount: integer/float (chips risked/invested in hand)
 * [10] wonAmount: integer/float (chips collected from pot)
 * [11..12] holeCards: optional cards at showdown (e.g. 'Tc', 'Kd')
 */

export class IrcPokerParser {
  /**
   * Parse a single space-delimited line from a pdb.<player> file.
   */
  public static parsePdbLine(line: string): ProcessedPlayerHand | null {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) {
      return null;
    }

    const tokens = trimmed.split(/\s+/);
    if (tokens.length < 11) {
      return null;
    }

    const playerName = tokens[0];
    const timestamp = parseInt(tokens[1], 10);
    const numPlayers = parseInt(tokens[2], 10);
    const position = parseInt(tokens[3], 10);
    const preflopAction = tokens[4];
    const flopAction = tokens[5];
    const turnAction = tokens[6];
    const riverAction = tokens[7];
    const bankrollBefore = parseFloat(tokens[8]);
    const betAmount = parseFloat(tokens[9]);
    const wonAmount = parseFloat(tokens[10]);

    if (isNaN(timestamp) || isNaN(bankrollBefore) || isNaN(betAmount) || isNaN(wonAmount)) {
      return null;
    }

    let holeCards: [string, string] | undefined = undefined;
    if (tokens.length >= 13) {
      holeCards = [tokens[11], tokens[12]];
    }

    // Derived Behavioral Flags
    // VPIP: Voluntarily Put Money in Pot
    // Blinds (B, Bf) are mandatory. Any call (c), bet (b), or raise (r) constitutes voluntary investment.
    const hasVoluntaryPreflop = /[crb]/.test(preflopAction);
    const vpip = hasVoluntaryPreflop;

    // PFR: Preflop Raise
    const pfr = /r/.test(preflopAction);

    // Aggression: Any bet (b) or raise (r) across all streets
    const allActions = `${preflopAction}${flopAction}${turnAction}${riverAction}`;
    const aggressive = /[br]/.test(allActions);

    // Flop viewed (not folded preflop)
    const sawFlop = flopAction !== '-' && flopAction !== '';

    // Reached showdown: revealed cards or saw river action to completion
    const reachedShowdown = holeCards !== undefined || (riverAction !== '-' && riverAction !== '' && !/f/.test(riverAction));

    const pnl = wonAmount - betAmount;
    const bankrollAfter = bankrollBefore + pnl;

    return {
      playerName,
      timestamp,
      numPlayers,
      position,
      preflopAction,
      flopAction,
      turnAction,
      riverAction,
      bankrollBefore,
      betAmount,
      wonAmount,
      holeCards,
      pnl,
      bankrollAfter,
      vpip,
      pfr,
      aggressive,
      sawFlop,
      reachedShowdown
    };
  }
}
