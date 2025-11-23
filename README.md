# 💰 Smart Finance Tracker (CLI)

A simple, command-line interface (CLI) personal finance application written in Python. This tracker allows users to log income and expenses, view a financial summary, and save data persistence using JSON files.

## ✨ Features

* **Transaction Logging:** Easily record new income and expense entries.
* **Input Validation:** Ensures only positive numerical amounts are accepted for transactions.
* **Data Persistence:** Saves all transactions to a `finance_data.json` file, so data is retained between sessions.
* **Financial Summary:** Calculates and displays:
    * Total Income
    * Total Expense
    * Net Balance (color-coded based on positive/negative)
* **Expense Breakdown:** Provides a detailed, categorized breakdown of all expenses, including the percentage of total expenditure.
* **Color-Coded Output:** Uses ANSI escape codes for enhanced readability and clear distinction between income (Green) and expenses (Red).

## 🚀 How to Run

### Prerequisites

You need **Python 3.x** installed on your system. No external libraries are strictly required, as it only uses the standard `json` module.

### Execution

1.  **Save the Code:** Save the provided code as a file named `tracker.py` (or similar).
2.  **Run from Terminal:** Open your terminal or command prompt and navigate to the directory where you saved the file.
3.  Execute the script:

    ```bash
    python tracker.py
    ```

## 🛠️ Menu Options

| Option | Action | Description |
| :---: | :--- | :--- |
| **1** | Add Income | Prompts for amount, source, and description. |
| **2** | Add Expense | Prompts for amount, category, and description. |
| **3** | View Summary | Shows Total Income, Total Expense, Net Balance, and a categorized Expense Breakdown. |
| **4** | View All | Lists every recorded transaction with color-coding. |
| **5** | Save & Exit | Writes all current transactions to `finance_data.json` and closes the application. |

## 📁 File Structure

The project primarily consists of two files that will be managed:

| File Name | Purpose | Notes |
| :--- | :--- | :--- |
| `tracker.py` | The main application code containing all functions and the execution loop. | **Source Code** (Should be committed) |
| `finance_data.json` | Stores the user's transaction data (initially empty). | **Data File** (Can be ignored in Git) |

***

## 🚫 Suggested .gitignore

Since the `finance_data.json` file contains user-specific data that may change frequently and isn't part of the core source code, it's best to exclude it from Git tracking.

Create a file named **`.gitignore`** in your project's root directory with the following content:

```gitignore
# Data file (since it changes per user/session)
finance_data.json

# Environment/Build files
__pycache__/
*.pyc
venv/
.venv/
