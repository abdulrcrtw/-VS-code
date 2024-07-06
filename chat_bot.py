def ask_name():
    name = input("What is your name ? ").capitalize()
    return name 

def calculate_expenses(expenses):
    sum_total = sum(expenses) 
    return sum_total

def calculate_savings(income, expenses):
    """Subtracts expenses from income to calculate savings."""
    savings = income - expenses 
    return f"Total savings: ${savings: .2f}"

def simple_interest(principal, rate, time):
    """Calculate simple interest on a principal over time at a given rate."""
    interest = principal * (rate / 100) * time 
    return f"Simple interest: ${interest: .2f}"

def compound_interest(principal, rate, times_compounded, years):
    """Calculate compound interest."""
    amount = principal * (1 + (rate / 100) / times_compounded) ** (times_compounded * years)
    interest = amount - principal 
    return f"Compound interest: ${interest: .2f}"
    
command = input("Which command would you like to run? Options: expenses, ask_name, simple_interest, compound_interest ")

if command == "expenses":
    num_expenses = int(input("How many expenses do u have? "))
    expenses = []
    for i in range (num_expenses):
        expense = float(input(f"Enter expense {i+1}: "))
        expenses.apppend(expenses) 
    print(f"Total expenses: ${calculate_expenses(expenses):.2f}")

elif command == "ask_name":
    name = ask_name()
    print(f"Hello, {name}!")

elif command == "savings":
    income = float(input("What is your income? "))
    num_expenses = int(input("How many expenses do u have? "))
    expenses = []
    for i in range(num_expenses):
        expense = float(input(f"Enter expense {i+1}: "))
        expenses.append(expenses)
    total_expenses = calculate_expenses(expenses)
    print(calculate_savings(income, total_expenses))

elif command == "simple_interest":
    principal = float(input("What is the principal amount? "))
    rate = float(input("What is the rate (in %)? "))
    time = float(input("For how many years? "))
    print(simple_interest(principal, rate, time))

elif command == "compound_interest":
    principal = float(input("What is the principal amount? "))
    rate = float(input("What is the interest rate (in %)? "))
    times_compounded = float(input("How many times is the interest compounded per year? "))
    years = float(input("For how many years? "))
    print(compound_interest(principal, rate, times_compounded, years))

else:
    print("Invalid comment")
    










    

