import json
TRANSACTIONS = []
DATA_FILE = "finance_data.json"
RESET = "\033[0m"
GREEN = "\033[92m"   # For Income
RED = "\033[91m"     # For Expense
YELLOW = "\033[93m"  # For Info/Menu borders
BLUE = "\033[94m"    # For Section Headers
BOLD = "\033[1m"
SEPARATOR = "=" * 50 # Standard separator length

# --- CORE FUNCTIONS (Based on Unit 2: Functions) ---

def load_data():
    """
    Loads transaction data from a JSON file if it exists.
    Uses basic file I/O operations (implied by Experiment 2).
    """
    global TRANSACTIONS
    try:
        with open(DATA_FILE, 'r') as f:
            # Load the data from the file
            TRANSACTIONS = json.load(f)
        print(f"\n{YELLOW}[INFO]{RESET} Loaded {len(TRANSACTIONS)} transactions from {DATA_FILE}.")
    except FileNotFoundError:
        print(f"\n{YELLOW}[INFO]{RESET} Data file '{DATA_FILE}' not found. Starting with an empty tracker.")
    except json.JSONDecodeError:
        print(f"\n{RED}[ERROR]{RESET} Corrupt data file. Starting with an empty tracker.")
        TRANSACTIONS = []

def save_data():
    """
    Saves the current transactions list to a JSON file.
    """
    try:
        with open(DATA_FILE, 'w') as f:
            # Dump the current list to the file
            json.dump(TRANSACTIONS, f, indent=4)
        print(f"{GREEN}[INFO]{RESET} Data successfully saved to {DATA_FILE}.")
    except Exception as e:
        print(f"{RED}[ERROR]{RESET} Could not save data: {e}")


def add_transaction(transaction_type):
    """
    Function to add a new income or expense transaction.
    Demonstrates input/output and conditional logic (Unit 2, 3).
    """
    # Use color based on transaction type
    prompt_color = GREEN if transaction_type == 'income' else RED
    
    print(prompt_color + BOLD + f"\n--- Add {transaction_type.capitalize()} ---" + RESET)
    
    # Use a loop to ensure valid amount input
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

    # Create the new transaction dictionary (Unit 5: Dictionaries)
    new_transaction = {
        'type': transaction_type,
        'amount': amount,
        'category': category.lower(),
        'description': description
    }

    TRANSACTIONS.append(new_transaction)
    print(f"\n{GREEN if transaction_type == 'income' else RED}Successfully added {transaction_type}: {amount:.2f} (Category: {category}){RESET}")


def view_summary():
    """
    Calculates and displays the financial summary (balance, total income/expense).
    Demonstrates iteration and summation (Unit 3, Experiment 4).
    Also includes a percentage breakdown for better readability.
    """
    total_income = 0.0
    total_expense = 0.0
    category_totals = {} # Dictionary to store category-wise expenses

    # Iterate through the list of transactions (Unit 5: Lists & Dictionaries)
    for t in TRANSACTIONS:
        amount = t['amount']
        category = t['category']

        if t['type'] == 'income':
            # Summation logic
            total_income += amount
        elif t['type'] == 'expense':
            # Summation logic
            total_expense += amount
            
            # Grouping by category
            if category not in category_totals:
                category_totals[category] = 0.0
            category_totals[category] += amount
    
    balance = total_income - total_expense
    balance_color = GREEN if balance >= 0 else RED

    # Display Summary
    print(BLUE + BOLD + "\n" + SEPARATOR)
    print("        FINANCIAL SUMMARY")
    print(SEPARATOR + RESET)
    
    print(f"{BOLD}{'Total Income:':<20}{GREEN}{total_income:15.2f}{RESET}")
    print(f"{BOLD}{'Total Expense:':<20}{RED}{total_expense:15.2f}{RESET}")
    print("-" * 50)
    print(f"{BOLD}{'Net Balance:':<20}{balance_color}{balance:15.2f}{RESET}")
    print(BLUE + SEPARATOR + RESET)

    # Display expense breakdown
    if category_totals:
        print(YELLOW + BOLD + "\nExpense Breakdown by Category:" + RESET)
        # Sort categories alphabetically
        for category, total in sorted(category_totals.items()):
            # Calculate percentage for "smart" analysis
            percentage = (total / total_expense * 100) if total_expense else 0
            print(f"- {category.capitalize():<15}: {RED}{total:10.2f}{RESET} ({percentage:.1f}%)")
    else:
        print("\nNo categorized expenses recorded.")

def display_all_transactions():
    """
    Lists all recorded transactions with enhanced, color-coded formatting.
    Demonstrates basic list iteration (Unit 5).
    """
    if not TRANSACTIONS:
        print("\nNo transactions recorded yet.")
        return

    print(BLUE + BOLD + "\n" + SEPARATOR)
    print("               ALL TRANSACTIONS")
    print(SEPARATOR + RESET)
    
    # Display column headers with bold formatting
    print(f"{BOLD}{'ID':<3} | {'Type':<8} | {'Amount':>10} | {'Category/Source':<18} | Description{RESET}")
    print("-" * 50)

    # Use 'for' loop to display each record (Experiment 4)
    for i, t in enumerate(TRANSACTIONS, 1):
        type_str = t['type'].upper()
        amount_str = f"{t['amount']:.2f}"
        category_str = t['category'].capitalize()
        description_str = t['description']
        
        # Color coding for better readability
        color = GREEN if t['type'] == 'income' else RED
        
        print(f"{i:<3} | {color}{type_str:<8}{RESET} | {color}{amount_str:>10}{RESET} | {category_str:<18} | {description_str}")
    
    print(BLUE + SEPARATOR + RESET)


def main_menu():
    """
    The main control flow loop for the application.
    Uses while loop and conditional statements (Unit 3, Experiment 4).
    """
    
    # Load data on startup
    load_data()

    # Main application loop
    while True:
        print(YELLOW + BOLD + "\n" + SEPARATOR[:30])
        print("  SMART FINANCE TRACKER MENU")
        print(SEPARATOR[:30] + RESET)
        print("1. " + GREEN + "Add Income" + RESET)
        print("2. " + RED + "Add Expense" + RESET)
        print("3. " + BLUE + "View Summary & Breakdown" + RESET)
        print("4. View All Transactions")
        print("5. Save & Exit")
        print(YELLOW + SEPARATOR[:30] + RESET)

        # Get user input
        choice = input("Enter your choice (1-5): ")

        # Conditional control flow (if-elif-else)
        if choice == '1':
            add_transaction('income')
        elif choice == '2':
            add_transaction('expense')
        elif choice == '3':
            view_summary()
        elif choice == '4':
            display_all_transactions()
        elif choice == '5':
            # Exit condition (break)
            print(YELLOW + "\nExiting Tracker. Thank you!" + RESET)
            save_data()
            break
        else:
            print(RED + "\nInvalid choice. Please enter a number between 1 and 5." + RESET)

# --- PROGRAM EXECUTION ---

if __name__ == "__main__":
    # This is the entry point of the program.
    main_menu()