# 👾 Proto-Game: A Python Text Adventure 🎮

![Python](https://img.shields.io/badge/Python-3.x-blue.svg?style=flat&logo=python&logoColor=white)

---

### Overview

Welcome to **GameTest**! This is a simple, turn-based text adventure game built in Python. It's a fundamental project designed to explore basic game mechanics, user input handling, and state management within a console environment.

The game pits you against various enemies in a continuous loop, allowing you to level up, improve your stats, and test your strategic decisions against ever-increasing challenges.

---

### Features

* **Turn-Based Combat:** Engage in battles against different enemy types.
* **Player Stats & Leveling:**
    * Manage your **Health Points (HP)** and **Energy**.
    * **Level up** by gaining experience (EXP) to increase your core stats (Max HP, ATK, HEAL, Max Energy, Energy Regen).
* **Dynamic Enemy Encounters:** Encounter Goblins, Orcs, and Ogres, with their stats scaling as you level up.
* **Player Actions:**
    * **Attack (`a`):** Deal damage to the enemy (consumes energy).
    * **Heal (`h`):** Restore your HP (consumes energy).
    * **Defend (`e`):** Reduce incoming enemy damage for one turn (consumes energy).
    * **Parry (`q`):** Counter an enemy attack, dealing damage and negating their current attack (consumes energy).
* **Game Over Condition:** The game ends when your HP drops to zero.

---

### How to Play

1.  **Run `main.py`** with Python 3
2.  **Follow Instructions:** The game will present instructions upon launch.
3.  **Enter Commands:** During your turn, type the corresponding letter for your desired action (`a`, `h`, `e`, `q`) and press Enter.
4.  **Exit:** You can type `quit` at any time to exit the game.

---

### Game Mechanics & Design Notes

This project leverages basic Python constructs such as `while` loops for the game loop, `if/elif/else` statements for decision-making, and variable manipulation to manage game state.

* **Randomness:** Enemy encounters and some action costs/effects incorporate a pseudo-random number generator, adding an element of unpredictability.
* **Scaling:** Both player and enemy stats scale with the player's level, aiming to provide a continuous challenge.
* **Energy Management:** A core mechanic is managing your energy, as most actions consume it, and it regenerates each turn.

---

### Contribution

This project is primarily a learning exercise. Feel free to explore the code, suggest improvements, or fork it to build upon!

---

### License

This project is open-source and available under the MIT License.

---
