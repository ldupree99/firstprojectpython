# Creating a list that contains the different categories
categories = [
    "Fixed Expenses",
    "Variable Expenses",
    "Discretionary Expenses",
    # Add more categories/expenses as needed 
]

# Create an empty list that will store the expenses the user types
expenses = []

# Ask Username
user_name = input("Welcome! What's your name?:")

#Introduction to app
print(f"Hi {user_name}! This is your personal Expense Tracker, We're here to help you take control of your finances and reach your goals. Let's get started on this journey together! ")
#ask if there are expenses for Fixed Expenses category

add_fixed_expenses = input(f"Do you have entries for {categories[0]}? (yes/no): ").lower()
# Check users response 

if add_fixed_expenses == 'yes':
    # Initialize a variable to control the loop
    add_another_expense = 'yes'

    # Use a while loop with the user's choice as the condition
    while add_another_expense.lower() == 'yes':
        expense = input("Enter your expense for Fixed Expenses: ")
        # The expense would be added to category

        # Ask if the user wants to add another expense in current category
        add_another_expense = input("Do you want to add another expense in this category? (yes/no): ")

    print("No more expenses added to Fixed Expenses category")
    
    