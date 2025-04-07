## 🛡️ Feature: 5v5 Team Battle Mode (by [Your Name])

### 🔥 Feature Overview
This feature introduces a new 5v5 battle system between a team of 5 Heroes and 5 Monsters. It adds more depth, strategy, and replayability to the game.

### 🎮 Gameplay Highlights
- Prepare 5 Heroes: each gets a weapon roll, 2 loot items, optional dream level
- Fight 5 Monsters: each receives a random magical buff
- Combat is turn-based, round-by-round
- Final scoreboard shows HP and Combat Strength for all characters
- Stars are awarded based on surviving heroes and saved to `save.txt`

### 💡 Implementation Notes
- Each hero is individually prepared using existing game systems (`functions.py`)
- Monsters are randomly powered using `monster_powers`
- Final result uses `functions.save_game()` for consistency
- No changes made to shared game files (`main.py`, etc.)

### 🧪 How to Run
Clone the repo and in this branch, run:

```bash
python Shayan_feature.py
