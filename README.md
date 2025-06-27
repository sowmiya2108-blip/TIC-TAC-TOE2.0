# TIC-TAC-TOE2.0
✅ Overview
This project implements an unbeatable AI agent for the classic game of Tic-Tac-Toe using the Minimax algorithm with Alpha-Beta Pruning. The AI competes against a human player in a terminal-based interface, consistently making optimal moves. It serves as a hands-on example of applying game theory, recursion, and search algorithms in artificial intelligence.

🚀 Features
Human vs AI gameplay

AI uses Minimax algorithm with Alpha-Beta Pruning

Unbeatable game logic (always optimal moves)

Easy-to-understand and maintainable code

Console-based user interface

Input validation and turn-based gameplay

💻 Technologies Used
Python 3.6+ – Core programming language

Standard Python libraries – math and built-in functions

Algorithm – Minimax algorithm with Alpha-Beta pruning

🔁 Workflow
Board Setup: A 3x3 board is initialized with empty cells.

Game Loop:

Human makes a move.

Board is updated and checked for win/draw.

AI makes a move using the Minimax strategy.

Loop continues until a win or draw is detected.

AI Decision Making:

Recursively evaluates all possible moves.

Maximizes its own winning chances, minimizes human's.

Prunes subtrees using alpha-beta bounds to optimize performance.

⚙️ Installation
Ensure Python 3 is installed:


python --version
Clone or download the code:

git clone https://github.com/yourusername/tic-tac-toe-ai.git
cd tic-tac-toe-ai
Run the game:
python tic_tac_toe_ai.py
🕹 Usage
On running, the program displays the game board.

The player is prompted to enter a number (1–9) to mark a position.

The AI responds with an optimal move.

Game ends with a win, lose, or draw message.

🌐 Applications
Game AI Development: Demonstrates core AI techniques used in decision-making engines.

Academic Projects: Ideal for showcasing understanding of search algorithms, recursion, and game theory.

Technical Interviews: Good example of practical application of Minimax algorithm.

Learning Tool: Helps beginners understand algorithmic problem-solving and turn-based logic.

