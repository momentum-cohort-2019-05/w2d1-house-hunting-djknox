# user input validation: must be positive integer
valid_input = False
while not valid_input:
    user_input = input("Enter your annual salary: ")
    try:
        annual_salary = int(user_input)    
        if isinstance(annual_salary, int) and annual_salary > 0:
            valid_input = True
        else:
            print("Your annual salary must be a positive integer.")
    except ValueError:
        print("Your annual salary must be an integer.")

# user input validation: must be float between 0.00 and 1.00
valid_input = False
while not valid_input:
    user_input = input("Enter the percent of your salary to save, as a decimal: ")
    try:
        portion_saved = float(user_input)
        if isinstance(portion_saved, float) and portion_saved >= 0.0 and portion_saved <= 1.00:
            valid_input = True
        else:
            print("The percent of your salary must be a decimal number between 0.00 and 1.00.")
    except ValueError:
        print("The percent of your salary must be a decimal number.")

# user input validation: must be float between 0.00 and 1.00
valid_input = False
while not valid_input:
    user_input = input("Enter the expected annual rate of return [0.04]: ") or 0.04
    try:
        annual_rate = float(user_input)
        if isinstance(annual_rate, float) and annual_rate >= 0.0 and annual_rate <= 1.00:
            valid_input = True
        else:
            print("The expected annual rate of return must be a decimal number between 0.00 and 1.00.")
    except ValueError:
        print("The expected annual rate of return must be a decimal number.")

# user input validation: must be positive integer
valid_input = False
while not valid_input:
    user_input = input("Enter the cost of your dream home: ")
    try:
        total_cost = int(user_input)    
        if isinstance(total_cost, int) and total_cost > 0:
            valid_input = True
        else:
            print("The cost of your dream home must be a positive integer.")
    except ValueError:
        print("The cost of your dream home must be an integer.")

# user input validation: must be float between 0.00 and 1.00
valid_input = False
while not valid_input:
    user_input = input("Enter the percent of your home's cost to save as a down payment [0.25]: ") or 0.25
    try:
        portion_down_payment = float(user_input)
        if isinstance(portion_down_payment, float) and portion_down_payment >= 0.0 and portion_down_payment <= 1.00:
            valid_input = True
        else:
            print("The percent of your home's cost to save as a down payment must be a decimal number between 0.00 and 1.00.")
    except ValueError:
        print("The percent of your home's cost to save as a down payment must be a decimal number.")

monthly_salary = annual_salary / 12
current_savings = 0
cost_of_down_payment = total_cost * portion_down_payment

# count number of months it takes to get current_savings to the same as cost_of_down_payment
num_months = 0
while current_savings < cost_of_down_payment:
    num_months += 1
    return_on_investment = current_savings * annual_rate / 12
    current_savings += return_on_investment + (monthly_salary * portion_saved)

print("Number of months:", num_months)