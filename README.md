# [cite_start]Smart Finance Tracker (Python CLI Application) 

## [cite_start]🎯 Project Overview [cite: 2]

[cite_start]This is a simple, command-line interface (CLI) application developed in Python to help users track their personal income and expenses[cite: 3]. [cite_start]It provides a quick way to record financial transactions, view a comprehensive summary, and analyze spending patterns by category[cite: 4].

[cite_start]The project is designed to demonstrate proficiency in fundamental Python programming concepts, particularly those covered in an introductory course like **CSE1021: Introduction to Problem Solving and Programming**[cite: 5].

---

## [cite_start]✨ Features [cite: 6]

[cite_start]The application provides the following core functionalities through an interactive menu[cite: 7]:

* [cite_start]**Add Income**: Record a new income transaction with amount, source, and description[cite: 8].
* [cite_start]**Add Expense**: Record a new expense transaction with amount, category, and description[cite: 9].
* [cite_start]**View Summary & Breakdown**: [cite: 10]
    * [cite_start]Displays **Total Income**, **Total Expense**, and **Net Balance**[cite: 11].
    * [cite_start]Provides a **Categorical Breakdown** of expenses, including the percentage each category contributes to the total spending, offering a basic form of financial analysis[cite: 12].
* [cite_start]**View All Transactions**: Lists all recorded transactions with clear, color-coded formatting for easy readability[cite: 13].
* [cite_start]**Save & Exit**: Automatically saves all transaction data to a local `finance_data.json` file before exiting, ensuring data persistence[cite: 14].

---

## [cite_start]💻 How to Run [cite: 15]

1.  [cite_start]**Prerequisite**: Ensure you have Python installed on your system (**Python 3.6+ is recommended**)[cite: 16].
2.  [cite_start]**Save the File**: Save the provided code as `finance_tracker.py`[cite: 17].
3.  **Execute**: Open your terminal or command prompt, navigate to the directory where you saved the file, and run:
    ```bash
    python finance_tracker.py
    ``` [cite: 18]
4.  **Interact**: Follow the on-screen menu instructions (e.g., enter `1` for Add Income, `3` for Summary, etc.)[cite: 19].

---

## [cite_start]🎓 Educational Concepts Demonstrated [cite: 20]

[cite_start]This project successfully integrates several key programming concepts from the course curriculum[cite: 21]:

| Course Concept (Unit/Experiment) | Implementation in Tracker |
| :--- | :--- |
| **Lists and Dictionaries** (Unit 5) | Used the `TRANSACTIONS` **List** to hold all records, and each record is stored as a **Dictionary**. Dictionaries are also used for `category_totals` in the summary. |
| **Input and Output** (Exp. 2) | Used `input()` to receive transaction details and `print()` with ANSI color codes for enhanced, readable output. |
| **Functions** (Unit 2) | Modularized the code using functions like `add_transaction()`, `view_summary()`, `load_data()`, and `save_data()`. |
| **Control Flow (if/else, while)** (Unit 3, Exp. 4) | The `main_menu()` uses a `while True` loop and `if-elif-else` statements to control the application flow based on user choice. |
| **Summation** (Unit 3) | Implemented summation logic within `view_summary()` to calculate `total_income`, `total_expense`, and `balance`. |
| **Data Persistence** | Used the standard `json` library to save and load data, preventing data loss between sessions. |
