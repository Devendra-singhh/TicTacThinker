# 🧠 Tic-Tac-Toe AI with Monte Carlo Tree Search (MCTS)

This project implements a terminal-based **Tic-Tac-Toe** game featuring an intelligent AI opponent powered by **Monte Carlo Tree Search (MCTS)**. The AI simulates thousands of possible outcomes to make optimal decisions.

---

## 🚀 Features

- Human vs AI gameplay
- AI uses MCTS with UCT (Upper Confidence Bound)
- Win/draw detection and illegal move handling
- No external libraries required
- Written in clean, modular Python

---

## 📦 Files

- `board.py` — Game board, user interaction, rules
- `mcts.py` — MCTS algorithm: selection, expansion, simulation, backpropagation

---

## ▶️ How to Run

Make sure you have Python 3.7+ installed.

🎮 How to Play

Format: col,row (e.g. 2,1 for column 2, row 1)
Player 'x' always moves first
Type exit to quit
-------------------
 "x" to move:
-------------------
 . . .
 . . .
 . . .

> 2,1

🤖 How the AI Works

MCTS evaluates possible moves via random simulations
Each move is scored by how often it leads to a win
The AI chooses moves with the highest average success, balancing exploration and exploitation

✅ Example Flow

You enter a move
AI simulates ~10,000 games per turn
AI plays its best move
Game continues until win or draw

🧪 Future Ideas

Add GUI using tkinter or pygame
Implement difficulty levels (iterations/time limit)
Add support for multiplayer or remote play

