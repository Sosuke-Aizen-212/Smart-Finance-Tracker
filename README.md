# Smart Finance Tracker

This is a simple, command-line interface (CLI) application developed in Python to help users track their personal income and expenses. It provides a quick way to record financial transactions, view a comprehensive summary, and analyze spending patterns by category.

# Features

The application provides the following core functionalities through an interactive menu:

- **Add Income**: Record a new income transaction with the amount, source, and description.

- **Add Expense**: Record a new expense transaction with the amount, category, and description.

- **View Summary & Breakdown**:
  - Displays Total Income, Total Expense, and Net Balance.
  - Provides a Categorical Breakdown of expenses, including the percentage each category contributes to the total spending, offering a basic form of financial analysis.

- **View All Transactions**: Lists all recorded transactions with clear, color-coded formatting for easy readability.

- **Save & Exit**: Automatically saves all transaction data to a local `summary_report.csv` file before exiting, ensuring data persistence.

## Files

- `SmartFinanceTracker.py` - Code
- `requirements.txt` - Dependencies

## Installation

```bash
pip install -r requirements.txt
```

## 🚀 How to Run

1. **Prerequisite**  
   Make sure Python 3.6+ is installed on your machine.

2. **Save the File**  
   Drop the code into a file named `finance_tracker.py`.

3. **Execute**  
   Open your terminal, navigate to the folder containing the file, and run:  
   ```bash
   python finance_tracker.py

4. **Interact**
5. Follow the on-screen menu prompts—type 1 to add income, 3 for a summary, etc.


