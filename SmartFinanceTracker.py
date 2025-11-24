import csv
import os

TRANSACTIONS = []
# Primary data file remains CSV
DATA_FILE = "summary_report.csv" 
FIELDNAMES = ['type', 'amount', 'category', 'description'] 

# --- Color Definitions ---
RESET = "\033[0m"
GREEN = "\033[92m"   # For Income
RED = "\033[91m"     # For Expense
YELLOW = "\033[93m"  # For Info/Menu borders
BLUE = "\033[94m"    # For Section Headers
BOLD = "\033[1m"
SEPARATOR = "=" * 50
# -------------------------

def load_data():
    global TRANSACTIONS
    if not os.path.exists(DATA_FILE):
        print(f"\n{YELLOW}[INFO]{RESET} Data file '{DATA_FILE}' not found. Starting with an empty tracker.")
        return

    try:
        with open(DATA_FILE, mode='r', newline='') as f:
            reader = csv.DictReader(f)
            TRANSACTIONS = []
            for row in reader:
                try:
                    # Convert the amount back to float for calculations
                    row['amount'] = float(row['amount'])
                    TRANSACTIONS.append(row)
                except ValueError:
                    # Skip corrupt rows
                    continue 

        print(f"\n{YELLOW}[INFO]{RESET} Loaded {len(TRANSACTIONS)} transactions from {DATA_FILE}.")
    except Exception as e:
        print(f"\n{RED}[ERROR]{RESET} Could not load data from CSV: {e}. Starting with an empty tracker.")
        TRANSACTIONS = []

def save_data():
    try:
        with open(DATA_FILE, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            
            writer.writeheader()
            writer.writerows(TRANSACTIONS)
            
        print(f"{GREEN}[INFO]{RESET} Data successfully saved to {DATA_FILE}.")
    except Exception as e:
        print(f"{RED}[ERROR]{RESET} Could not save data: {e}")

def add_transaction(transaction_type):
    prompt_color = GREEN if transaction_type == 'income' else RED
    
    print(prompt_color + BOLD + f"\n--- Add {transaction_type.capitalize()} ---" + RESET)
    
    while True:
        try:
            amount = float(input(f"{prompt_color}Enter amount: {RESET}"))
            if amount <= 0:
                print(f"{RED}Amount must be positive.{RESET}")
                continue
            break
        except ValueError:
            print(f"{RED}Invalid input. Please enter a number.{RESET}")

    description = input(f"{prompt_color}Enter description: {RESET}")
    
    if transaction_type == 'expense':
        category = input(f"{prompt_color}Enter category (e.g., Food, Bills, Rent): {RESET}")
    else:
        category = input(f"{prompt_color}Enter source (e.g., Salary, Gift, Investment): {RESET}")

    new_transaction = {
        'type': transaction_type,
        'amount': amount,
        'category': category.lower(),
        'description': description
    }

    TRANSACTIONS.append(new_transaction)
    print(f"\n{GREEN if transaction_type == 'income' else RED}Successfully added {transaction_type}: {amount:.2f} (Category: {category}){RESET}")


def view_summary():
    total_income = 0.0
    total_expense = 0.0
    category_totals = {}

    for t in TRANSACTIONS:
        amount = t['amount']
        category = t['category']

        if t['type'] == 'income':
            total_income += amount
        elif t['type'] == 'expense':
            total_expense += amount
            
            if category not in category_totals:
                category_totals[category] = 0.0
            category_totals[category] += amount
    
    balance = total_income - total_expense
    balance_color = GREEN if balance >= 0 else RED

    print(BLUE + BOLD + "\n" + SEPARATOR)
    print("        FINANCIAL SUMMARY")
    print(SEPARATOR + RESET)
    
    print(f"{BOLD}{'Total Income:':<20}{GREEN}{total_income:15.2f}{RESET}")
    print(f"{BOLD}{'Total Expense:':<20}{RED}{total_expense:15.2f}{RESET}")
    print("-" * 50)
    print(f"{BOLD}{'Net Balance:':<20}{balance_color}{balance:15.2f}{RESET}")
    print(BLUE + SEPARATOR + RESET)
    if category_totals:
        print(YELLOW + BOLD + "\nExpense Breakdown by Category:" + RESET)
        for category, total in sorted(category_totals.items()):
            percentage = (total / total_expense * 100) if total_expense else 0
            print(f"- {category.capitalize():<15}: {RED}{total:10.2f}{RESET} ({percentage:.1f}%)")
    else:
        print("\nNo categorized expenses recorded.")


def display_all_transactions():
    if not TRANSACTIONS:
        print("\nNo transactions recorded yet.")
        return

    print(BLUE + BOLD + "\n" + SEPARATOR)
    print("               ALL TRANSACTIONS")
    print(SEPARATOR + RESET)
    print(f"{BOLD}{'ID':<3} | {'Type':<8} | {'Amount':>10} | {'Category/Source':<18} | Description{RESET}")
    print("-" * 50)
    for i, t in enumerate(TRANSACTIONS, 1):
        type_str = t['type'].upper()
        amount_str = f"{t['amount']:.2f}" 
        category_str = t['category'].capitalize()
        description_str = t['description']
        color = GREEN if t['type'] == 'income' else RED
        
        print(f"{i:<3} | {color}{type_str:<8}{RESET} | {color}{amount_str:>10}{RESET} | {category_str:<18} | {description_str}")
    
    print(BLUE + SEPARATOR + RESET)


def export_summary_to_csv():
    """Calculates the financial summary and exports it to a new CSV file."""
    if not TRANSACTIONS:
        print(f"{RED}Cannot export summary: No transactions recorded.{RESET}")
        return

    total_income = 0.0
    total_expense = 0.0
    category_totals = {}

    for t in TRANSACTIONS:
        amount = t['amount']
        if t['type'] == 'income':
            total_income += amount
        elif t['type'] == 'expense':
            total_expense += amount
            category = t['category']
            if category not in category_totals:
                category_totals[category] = 0.0
            category_totals[category] += amount
    
    balance = total_income - total_expense
    
    # 1. Prepare Data for Summary CSV
    REPORT_FILE = "summary_report.csv"
    REPORT_FIELDNAMES = ['Type', 'Category', 'Amount', 'Percentage']
    report_data = []

    # Add Overall Totals
    report_data.append({'Type': 'Total Income', 'Category': '', 'Amount': total_income, 'Percentage': ''})
    report_data.append({'Type': 'Total Expense', 'Category': '', 'Amount': total_expense, 'Percentage': ''})
    report_data.append({'Type': 'Net Balance', 'Category': '', 'Amount': balance, 'Percentage': ''})
    
    # Add Expense Breakdown
    report_data.append({'Type': '--- EXPENSE BREAKDOWN ---', 'Category': '', 'Amount': '', 'Percentage': ''})
    for category, total in sorted(category_totals.items()):
        percentage = (total / total_expense * 100) if total_expense else 0
        report_data.append({
            'Type': 'Expense',
            'Category': category.capitalize(),
            'Amount': total,
            'Percentage': f"{percentage:.1f}%"
        })

    # 2. Write to CSV file
    try:
        with open(REPORT_FILE, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=REPORT_FIELDNAMES)
            
            writer.writeheader()
            writer.writerows(report_data)
            
        print(f"\n{GREEN}{BOLD}[SUCCESS]{RESET} Financial Summary exported to '{REPORT_FILE}'.")
    except Exception as e:
        print(f"{RED}[ERROR]{RESET} Could not export summary to CSV: {e}")


def main_menu():
    load_data()
    while True:
        print(YELLOW + BOLD + "\n" + SEPARATOR[:30])
        print("  SMART FINANCE TRACKER MENU")
        print(SEPARATOR[:30] + RESET)
        print("1. " + GREEN + "Add Income" + RESET)
        print("2. " + RED + "Add Expense" + RESET)
        print("3. " + BLUE + "View Summary & Breakdown" + RESET)
        print("4. View All Transactions")
        print("5. Save & Exit")
        # New option for exporting the summary
        print("6. Export Summary to New CSV") 
        print(YELLOW + SEPARATOR[:30] + RESET)
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_transaction('income')
        elif choice == '2':
            add_transaction('expense')
        elif choice == '3':
            view_summary()
        elif choice == '4':
            display_all_transactions()
        elif choice == '5':
            print(YELLOW + "\nExiting Tracker. Thank you!" + RESET)
            save_data()
            break
        elif choice == '6':
            export_summary_to_csv()
        else:
            print(RED + "\nInvalid choice. Please enter a number between 1 and 6." + RESET)

if __name__ == "__main__":
    main_menu()

