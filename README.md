# makefun-tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/qlxjcj/makefun-tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/qlxjcj/makefun-tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 4096 bytes of Python 3.13 (stdlib only): 0x88 board, negamax alpha-beta with quiescence search and iterative deepening on a fixed node budget, material + king/pawn piece-square evaluation, and a move-ordering heuristic. Fully deterministic - no clocks, fixed node budget per move, so live play and replay agree move for move.

## Run it

```sh
MAKEFUN_ENV_URL=<env-url> python main.py
```

<sub>Entered on [make.fun](https://make.fun/?ref=rcxcbtdz&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
