# 💰 Smart Finance Tracker (Python CLI Application)

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## 🎯 Project Overview

This is a simple, command-line interface (CLI) application developed in Python to help users track their personal income and expenses. It provides a quick way to record financial transactions, view a comprehensive summary, and analyze spending patterns by category.

The project is designed to demonstrate proficiency in fundamental Python programming concepts, particularly those covered in an introductory course like **CSE1021: Introduction to Problem Solving and Programming**.

---

## ✨ Features

The application provides the following core functionalities through an interactive menu:

### 📥 Add Income
Record a new income transaction with amount, source, and description.

### 📤 Add Expense
Record a new expense transaction with amount, category, and description.

### 📊 View Summary & Breakdown
- Displays **Total Income**, **Total Expense**, and **Net Balance**
- Provides a **Categorical Breakdown** of expenses, including the percentage each category contributes to the total spending, offering a basic form of financial analysis

### 📋 View All Transactions
Lists all recorded transactions with clear, color-coded formatting for easy readability.

### 💾 Save & Exit
Automatically saves all transaction data to a local `finance_data.json` file before exiting, ensuring data persistence.

---

## 💻 How to Run

### Prerequisite
Ensure you have **Python** installed on your system (Python 3.6+ is recommended).

### Steps to Execute

1. **Save the File**: Save the provided code as `finance_tracker.py`

2. **Execute**: Open your terminal or command prompt, navigate to the directory where you saved the file, and run:
   ```bash
   python finance_tracker.py
