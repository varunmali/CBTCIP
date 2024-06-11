# CBTCIP Repository 🚀

Welcome to the CBTCIP repository! This repository contains various Python projects developed as part of my internship at CipherByte Technologies. Each project showcases different aspects of Python programming, ranging from simple games to creating payment receipts.

## Projects

### 1. Rock-Paper-Scissors Game ✊📄✂️

This is a simple Rock-Paper-Scissors game implemented in Python. You can play against the computer and test your luck!

#### Features 🌟

- Classic Rock-Paper-Scissors gameplay
- User input validation
- Single-letter input options (r, p, s) for rock, paper, scissors
- Play again functionality
- Score tracking for multiple rounds

#### How to Play 🎮

1. **Clone or download the repository**:
    ```bash
    git clone https://github.com/varunmali/CBTCIP.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd CBTCIP/Rock_Paper_Scissor_Game
    ```

3. **Install any required dependencies**:
    This game doesn't require additional installations.

4. **Run the game using Python**:
    ```bash
    python Rock_Paper_Scissor_Game.py
    ```

5. **Follow the on-screen instructions**:
    - Choose your hand gesture: rock (r), paper (p), or scissors (s).
    - The computer will also choose a hand gesture.
    - The program will determine the winner and display the result.
    - You can choose to play again or exit the game.

6. **Play again or exit**:
    - After each round, you will be prompted to play again.
    - To exit, enter `n` when asked if you want to play again.

### 2. Creating Payment Receipt 🧾

This project is a simple transaction receipt generator using Python and the ReportLab library. It allows users to input transaction details and generates a PDF receipt.

#### Features 🌟

- Collects transaction details from the user.
- Generates a PDF receipt with itemized transaction details, subtotal, tax, and total amount.
- Uses the ReportLab library to create PDF documents.

#### Installation 🛠️

1. **Clone the repository**:
    ```bash
    git clone https://github.com/varunmali/CBTCIP.git
    cd CBTCIP/Creating_Payment_Receipt
    ```

2. **(Optional) Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required package**:
    ```bash
    pip install reportlab
    ```

#### Usage 📄

Run the script and follow the prompts to enter transaction details. The script will generate a PDF receipt.

```bash
python generate_receipt.py
```

## Repository Structure 📁

```
CBTCIP/
│
├── Rock_Paper_Scissor_Game/
│   ├── Rock_Paper_Scissor_Game.py
│   └── README.md
│
├── Creating_Payment_Receipt/
│   ├── generate_receipt.py
│   └── README.md
│
└── README.md
```

## About ℹ️

This repository is a collection of Python projects developed during my internship at CipherByte Technologies. It serves as a portfolio of my work and a demonstration of my skills in Python programming.
