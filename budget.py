import json
import os
from datetime import datetime

# Constants for file storage
DATA_FILE = 'budget_data.json'

# Load transactions from file
def load_transactions():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Save transactions to file
def save_transactions(transactions):
    with open(DATA_FILE, 'w') as file:
        json.dump(transactions, file, indent=4)

# Add a transaction
def add_transaction(transactions, transaction_type, category, amount):
    transaction = {
        'type': transaction_type,
        'category': category,
        'amount': amount,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    transactions.append(transaction)
    save_transactions(transactions)

# Calculate the remaining budget
def calculate_budget(transactions):
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_expenses = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    return total_income - total_expenses

# Analyze expenses
def analyze_expenses(transactions):
    expense_categories = {}
    for t in transactions:
        if t['type'] == 'expense':
            if t['category'] not in expense_categories:
                expense_categories[t['category']] = 0
            expense_categories[t['category']] += t['amount']
    
    print("\nExpense Analysis:")
    for category, total in expense_categories.items():
        print(f"{category}: ${total:.2f}")

# Main program loop
def main():
    transactions = load_transactions()
    
    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Budget")
        print("4. Analyze Expenses")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            add_transaction(transactions, 'income', category, amount)
        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_transaction(transactions, 'expense', category, amount)
        elif choice == '3':
            budget = calculate_budget(transactions)
            print(f"\nCurrent Budget: ${budget:.2f}")
        elif choice == '4':
            analyze_expenses(transactions)
        elif choice == '5':
            print("Exiting the budget tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
