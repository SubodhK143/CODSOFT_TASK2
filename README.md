# 🎮 Tic-Tac-Toe AI – Python Minimax

A **command-line Tic-Tac-Toe game built with Python**, where you play against an AI opponent powered by the **Minimax algorithm**.

The AI evaluates possible moves and selects the optimal move, making it a challenging opponent for the human player.

---

## 🚀 Project Overview

This project demonstrates how **game logic, recursion, and artificial intelligence concepts** can be implemented using Python.

### ✨ Key Features

* 🎮 Interactive command-line gameplay
* 🤖 AI opponent using the **Minimax algorithm**
* 🧠 Optimal AI decision-making
* ✅ Input validation
* 🏆 Automatic win detection
* 🤝 Draw/tie detection
* 📋 Dynamic 3×3 game board
* 🔄 Turn-based gameplay
* 🐍 Built completely with Python

---

## 🛠️ Technologies Used

| Technology   | Purpose                 |
| ------------ | ----------------------- |
| 🐍 Python    | Application development |
| 🧠 Minimax   | AI decision-making      |
| 🔁 Recursion | Game-state evaluation   |
| 💻 CLI       | User interaction        |

---

## 📂 Project Structure

```text
tic-tac-toe-ai/
│
├── tic_tac_toe.py
└── README.md
```

---

## 🧩 How the Game Works

The game uses two players:

* 🤖 **AI → X**
* 👤 **Human → O**

The AI uses the **Minimax algorithm** to evaluate all possible moves.

### Game Flow

```text
                🎮 Start Game
                     │
                     ▼
              Initialize Board
                     │
                     ▼
              🤖 AI's Turn (X)
                     │
                     ▼
             Minimax Evaluation
                     │
                     ▼
               Best Move
                     │
                     ▼
              👤 Human's Turn
                     │
                     ▼
              Validate Input
                     │
                     ▼
             Check Game Status
              /       |       \
           Win      Draw    Continue
            │         │         │
            ▼         ▼         ▼
          🏆 End     🤝 End   Next Turn
```

---

## 🧠 Minimax Algorithm

The AI decision-making is based on the **Minimax algorithm**, a classic algorithm used in two-player games.

The algorithm evaluates possible future game states:

```text
AI wins    → +1
Draw       →  0
AI loses   → -1
```

The AI attempts to **maximize its score**, while considering that the human player will attempt to minimize the score.

### Simplified Logic

```text
If AI wins:
    return +1

If Human wins:
    return -1

If board is full:
    return 0

For every possible move:
    Evaluate future game state

Choose the move with the highest score
```

---

## 🎯 Game Board

The game uses a standard **3×3 Tic-Tac-Toe board**.

Example:

```text
X | O | X
---------
  | X | O
---------
O |   | X
```

When entering a move, provide the row and column numbers:

```text
Enter row (0, 1, 2): 1
Enter column (0, 1, 2): 2
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/tic-tac-toe-ai.git
```

### 2️⃣ Navigate to the Project

```bash
cd tic-tac-toe-ai
```

### 3️⃣ Run the Game

```bash
python tic_tac_toe.py
```

Or, depending on your Python installation:

```bash
python3 tic_tac_toe.py
```

---

## 📋 Example Gameplay

```text
  |   |
---------
  |   |
---------
  |   |

AI's turn (X):

X |   |
---------
  |   |
---------
  |   |

Your turn (O):
Enter row (0, 1, 2): 1
Enter column (0, 1, 2): 1
```

The AI then evaluates the available moves and makes its optimal move.

---

## 🔍 Important Functions

### `initialize_board()`

Creates an empty 3×3 Tic-Tac-Toe board.

### `print_board(board)`

Displays the current board in the terminal.

### `is_winner(board, player)`

Checks whether a player has completed a row, column, or diagonal.

### `is_board_full(board)`

Determines whether all board positions are occupied.

### `is_valid_move(board, row, col)`

Validates whether the selected position is available.

### `minimax(board, depth, maximizing_player)`

Evaluates possible game states and determines the optimal AI strategy.

### `get_ai_move(board)`

Uses Minimax to determine the AI's best available move.

### `play_game()`

Controls the main game loop and manages player turns.

---

## 📚 Concepts Demonstrated

This project provides hands-on practice with:

* 🐍 Python functions
* 🔄 Loops
* 🔀 Conditional statements
* 📋 Lists and nested lists
* 🧠 Recursion
* 🤖 Artificial Intelligence
* 🎯 Algorithmic decision-making
* 🛡️ Input validation
* 🧩 Game-state management
* 📦 Python modules

---

## 🔮 Future Improvements

The project can be extended with:

* 🎨 GUI using **Tkinter**
* 🌐 Web version using **Flask**
* 📊 Score tracking
* 👥 Two-player mode
* 🎚️ Easy / Medium / Hard AI levels
* 🔊 Sound effects
* 🏆 Leaderboard
* 🌐 Multiplayer functionality
* 📱 Web-based responsive interface

---

## 💡 Learning Outcome

Through this project, I practiced implementing a complete Python application while understanding how **recursion and the Minimax algorithm can be used to build an AI game opponent**.

It is a simple project, but it demonstrates important foundations of **Python programming and Artificial Intelligence**.

---

## 👨‍💻 Author

**Subodh Kumar**

🐍 Python | ☁️ AWS | 🚀 DevOps | 🔧 Cloud Engineering

### 🔗 Connect With Me

* 💼 LinkedIn: https://www.linkedin.com/in/subodh-kumar-aws-certified/
* 🐙 GitHub: https://github.com/SubodhK143

---

## ⭐ Support

If you found this project useful for learning Python or AI concepts, consider giving the repository a ⭐.

**Happy Coding! 🚀**
