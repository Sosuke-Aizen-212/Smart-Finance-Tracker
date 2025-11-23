# 💰 Smart Finance Tracker (Python CLI)

A lightweight, interactive command-line application to help users track personal finances by recording income and expenses, viewing summaries, and analyzing spending patterns — all built with core Python concepts.

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🎯 Project Overview

This project serves as a practical implementation of fundamental programming concepts learned in an introductory course like **CSE1021: Introduction to Problem Solving and Programming**. It allows users to:

- Log income and expense transactions
- View real-time financial summaries
- Analyze spending by category with percentage breakdowns
- Persist data across sessions using JSON storage

The goal is to reinforce understanding of control structures, data types, functions, and file I/O while building a functional tool.

---

## ✨ Features

✅ **Add Income**  
Record sources of income (e.g., salary, freelance, gifts) with amount, source, and description.

✅ **Add Expense**  
Log expenses categorized by purpose (e.g., Food, Rent, Transport) for better organization.

✅ **View Summary & Breakdown**  
- Total Income  
- Total Expenses  
- Net Balance (color-coded: green for positive, red for negative)  
- **Categorical Expense Analysis**: See how much each category contributes to overall spending (in percentages).

✅ **View All Transactions**  
Display a neatly formatted, color-coded table of all recorded transactions with IDs, types, amounts, categories/sources, and descriptions.

✅ **Auto-Save on Exit**  
All data is automatically saved to `finance_data.json` when exiting, and reloaded on next startup.

✅ **User-Friendly CLI Interface**  
Clean menu navigation with input validation and colorful feedback using ANSI escape codes.

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.6 or higher
- No external libraries required (uses only built-in modules: `json`)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart-finance-tracker.git
   cd smart-finance-tracker
Run the application:
Bash

python finance_tracker.py
🔐 Privacy Tip: To avoid committing sensitive financial data, add finance_data.json to your .gitignore file:

gitignore

# .gitignore
finance_data.json
🖥️ How to Use
Upon launching, you'll see the main menu:

text

==============================
  SMART FINANCE TRACKER MENU
==============================
1. Add Income
2. Add Expense
3. View Summary & Breakdown
4. View All Transactions
5. Save & Exit
==============================
Enter your choice (1-5):
Step-by-Step Guide
1. Add Income
Select option 1
Enter amount (must be positive number)
Enter description (e.g., "Freelance project")
Enter source (e.g., "Salary", "Gift")
2. Add Expense
Select option 2
Enter amount (positive number)
Enter description (e.g., "Dinner at restaurant")
Enter category (e.g., "Food", "Transport", "Entertainment")
3. View Summary & Breakdown
Displays:

Total Income
Total Expenses
Net Balance (Income - Expenses)
Expense Breakdown by Category with percentages:
text

Expense Breakdown by Category:
- Food       :    50.00 (50.0%)
- Transport  :    30.00 (30.0%)
- Entertainment: 20.00 (20.0%)
4. View All Transactions
Shows a tabular list of all transactions with color coding:

🟢 Green: Income entries
🔴 Red: Expense entries
Example output:

text

ID  | Type     |     Amount | Category/Source  | Description
--------------------------------------------------
1   | INCOME   |    3000.00 | Salary           | Monthly paycheck
2   | EXPENSE  |      50.00 | Food             | Groceries from Walmart
5. Save & Exit
Saves current transaction data to finance_data.json and exits the program cleanly.
