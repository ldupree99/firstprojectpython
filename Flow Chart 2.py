# Declare variables
categories = [
    "Fixed Expenses",
    "Variable Expenses",
    "Discretionary Expenses",
    # Add more categories/expenses as needed 

]

expenses = []

# Ask Username
user_name = input("Welcome! What's your name?: ")

#Introduction to app
print(f"Hi {user_name}! This is your personal Expense Tracker, We're here to help you take control of your finances and reach your goals. Let's get started on this journey together! ")

# Initialize a loop to continue processing expenses
while True:
    categories = input("Do you have any Fixed Expenses: ")
    if categories == 'yes':
        print(categories('Fixed Expenses'))