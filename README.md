# Tic-Tac-Toe

This project provides a simple implementation of the classic TicTacToe game in Python. The core logic and game mechanics are encapsulated within the `tictactoe.py` file.

## Overview

The `tictactoe.py` module defines a `TicTacToe` class that manages the game board, player turns, and win/draw conditions. This implementation is suitable for learning purposes, quick prototyping, or as a foundation for more advanced features.

## Usage

1. **Initialization**  
   Create a new game instance:

   ```python
   from tictactoe import TicTacToe
   game = TicTacToe()
   ```

2. **Making Moves**  
   Use the `play(x,y)` method to place a mark for the current player at the specified position (row and column indices start at 0):

   ```python
   game.play(0, 1)  # Player X moves to the top-middle cell
   ```

3. **Checking Game Status**

   - `isEnded()` returns `True` if the game is ended.
   - `getWinner()` returns `0` if X wins and `1` if O wins. If it's a draw, it returns `-1`.
   - `getFreeCells()` returns the list of free cells in the game.

4. **Displaying the Board**  
   Use the `display()` method to print the current state of the game board to the console.

## Example

This is a simple usage of the `TicTacToe` class :

```python
from tictactoe import TicTacToe
from random import choice

g = TicTacToe()

while not g.isEnded():
    g.display()
    x = int(input())
    y = int(input())
    g.play(x,y)
    if not g.isEnded():
        c = choice(g.getFreeCells())
        g.play(c[0],c[1])

g.display()
if g.getWinner()==-1:
    print("Draw")
else:
    print(f"The winner is {"O" if g.getWinner() else "X"}")
```
