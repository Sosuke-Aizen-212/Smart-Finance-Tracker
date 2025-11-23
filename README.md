# Smart Finance Tracker

This is a simple, command-line interface (CLI) application developed in Python to help users track their personal income and expenses. It provides a quick way to record financial transactions, view a comprehensive summary, and analyze spending patterns by category.

#Features

The application provides the following core functionalities through an interactive menu:
Add Income: Record a new income transaction with amount, source, and description.
Add Expense: Record a new expense transaction with amount, category, and description.
View Summary & Breakdown:
Displays Total Income, Total Expense, and Net Balance.
Provides a Categorical Breakdown of expenses, including the percentage each category contributes to the total spending, offering a basic form of financial analysis.
View All Transactions: Lists all recorded transactions with clear, color-coded formatting for easy readability.
Save & Exit: Automatically saves all transaction data to a summary_report.csv file before exiting, ensuring data persistence.
## Files

- `diabetes.csv` - Dataset
- `diabetes_prediction.py` - Model training script
- `predict_new.py` - Interactive prediction script
- `requirements.txt` - Dependencies

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Train the Model
```bash
python diabetes_prediction.py
```

### Make Predictions
```bash
python predict_new.py
```

Enter patient details when prompted to get diabetes prediction and probability.

## Model

- Algorithm: Random Forest Classifier
- Features: 8 health metrics
- Preprocessing: Standard Scaling
- Train/Test Split: 80/20

## Output

The model provides:
- Binary prediction (Diabetic/Not Diabetic)
- Probability scores for both classes
