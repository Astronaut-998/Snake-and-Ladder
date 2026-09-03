# 🐍 Snakes and Ladders (CLI Edition) 🪜

A terminal-based Snakes and Ladders game written in Python, playable against a bot or another human on the same machine. Featuring colored player tokens and a live-updating board rendered right in your terminal.

## Features

- 🎮 Two game modes: **Player vs Bot** and **Player vs Player**
- 🎨 Colored player markers (blue, green, magenta, red)
- 🐍 8 snakes and 🪜 7 ladders scattered across the board
- 📊 Live board redraw after every move
- 🎲 Classic "exact roll to finish" rule — you must land exactly on 100 to win

## Requirements

- Python 3.10+ (uses `match` statements)
- [`termcolor`](https://pypi.org/project/termcolor/)

## Installation

```bash
pip install termcolor
```

## How to Run

```bash
python snakes_and_ladders.py
```

## How to Play

1. Choose a game mode: Player vs Bot, Player vs Player, or Exit.
2. Pick your token color from the list.
3. Press **Enter** to roll the dice on your turn.
4. Land on a ladder 🪜 to climb up, or a snake 🐍 to slide down.
5. You must roll the **exact** number needed to land on square 100 — overshooting wastes your turn.
6. First player to reach square 100 wins!

## Board Legend

| Symbol | Meaning |
|--------|---------|
| `[S]`  | Snake   |
| `[L]`  | Ladder  |
| `[N]`  | Player N's current position |
| `[NN]` | Empty square number |

## Known Issues

- Board columns can misalign slightly in rows containing a snake, ladder, or single-digit player marker, since those cells render narrower than numbered squares.
- Entering a non-numeric value at the game-mode prompt will crash the program (no input validation there yet).

## Roadmap / Ideas for Contribution

- [ ] Fix fixed-width cell rendering for consistent board alignment
- [ ] Add input validation on the game-mode prompt
- [ ] Support more than 2 players
- [ ] Add a "play again" loop instead of exiting after a win

## License

MIT — feel free to fork and improve.
