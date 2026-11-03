import * as path from 'path';
import { StreamPipeline } from './stream-pipeline.js';

async function main() {
  const defaultDataDir = path.resolve('C:/Users/Z09057/poker_extracted');
  const defaultOutputDir = path.resolve('./data');

  console.log('================================================================');
  console.log('  IRC Poker Econometrics Suite: House Money & Stopping Analysis ');
  console.log('================================================================');

  const pipeline = new StreamPipeline({
    dataDir: defaultDataDir,
    outputDir: defaultOutputDir,
    maxMonths: 24
  });

  const result = await pipeline.run();
  console.log(`Pipeline complete. Hands: ${result.totalHands}, Sessions: ${result.totalSessions}`);
}

main().catch(err => {
  console.error('Fatal error in pipeline execution:', err);
  process.exit(1);
});
