# Call the cost of your dream home total_cost​.
# Call the portion of the cost needed for a down payment portion_down_payment​. For simplicity, assume that portion_down_payment = 0.25 (25%).
# Call the amount that you have saved thus far current_savings​. You start with a current savings of $0.
# Assume that you invest your current savings wisely, with an annual return of r ​(in other words, at the end of each month, you receive an additional current_savings*r/12​ funds to put into your savings – the 12 is because r​ is an annual rate). Assume that your investments earn a return of r = 0.04 (4%).
# Call your annual salary annual_salary​.
# Assume you are going to dedicate a certain amount of your salary each month to saving for the down payment. Call that portion_saved​. This variable should be in decimal form (i.e. 0.1 for 10%).
# At the end of each month, your savings will be increased by the return on your investment, plus a percentage of your monthly salary ​(annual salary / 12).
# Write a program to calculate how many months it will take you to save up enough money for a down payment.

# Your program should ask the user to enter the following variables:

# The starting annual salary (annual_salary)
# The portion of salary to be saved (portion_saved)
# The cost of your dream home (total_cost)
# Please make your program print results in the format shown in the test cases below.

# Add the ability to set the percentage of the total cost you need for a down payment and the rate of expected return on investment. For each of these, allow the user to enter the value. If they choose not to enter a value, then use the default

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
annual_rate = float(input("Enter the expected annual rate of return [0.04]: ") or 0.04)
total_cost = int(input("Enter the cost of your dream home: "))
portion_down_payment = float(input("Enter the percent of your home's cost to save as a down payment [0.25]: ") or 0.25)

monthly_salary = annual_salary / 12
current_savings = 0
cost_of_down_payment = total_cost * portion_down_payment

# count number of months it takes to get current_savings to the same as cost_of_down_payment
num_months = 0
while current_savings < cost_of_down_payment:
    num_months += 1
    return_on_investment = current_savings * annual_rate / 12
    current_savings += return_on_investment + (monthly_salary * portion_saved)

print("Number of months: " + str(num_months))