
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python while practicing string manipulation, loops, conditionals, and user input handling. By the end of this assignment, you will create a playable command-line game with clear win and lose outcomes.

## 📝 Tasks

### 🛠️ Set Up the Game State

#### Description
Create the core game setup, including a word list, random word selection, and variables needed to track guesses and remaining attempts.

#### Requirements
Completed program should:

- Store at least 5 possible words in a predefined list.
- Randomly choose one word for the current game.
- Initialize a collection for guessed letters.
- Initialize a counter for incorrect guesses remaining (for example, 6).

### 🛠️ Implement the Guessing Loop

#### Description
Write the main game loop that asks the player for one letter at a time, updates progress, and checks for game completion.

#### Requirements
Completed program should:

- Prompt the player to enter a single letter each turn.
- Show the current word progress using underscores for unknown letters (example: `_ a _ _ m a _`).
- Decrease remaining attempts only when the guessed letter is not in the word.
- End the game with a win message when all letters are guessed.
- End the game with a lose message when no attempts remain.

Example interaction:

```text
Word: _ _ _ _
Guess a letter: a
Good guess!
Word: _ a _ _
Attempts left: 6
```
