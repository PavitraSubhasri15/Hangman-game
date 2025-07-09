## Hangman Game 🎮

This is a simple interactive word-guessing game implemented in **Python**.

### 📝 Description

The game uses the **NLTK** (Natural Language Toolkit) library to randomly select a word, which remains hidden from the user.

A custom `hangman()` function handles the core game logic:
- It first displays a series of underscores (`_`) representing the unknown word.
- The user is prompted to guess one letter at a time.
- If the guessed letter appears in the word, all occurrences of that letter are revealed in the correct positions.
- The user is given a total number of chances equal to **(length of the word + 3)** to guess all the letters.

The game continues until:
- The user correctly guesses the entire word (win), or
- The user runs out of attempts before completing the word (loss).
