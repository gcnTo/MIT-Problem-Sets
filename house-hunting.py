# 1. Call the cost of your dream home ​ total_cost​ .
total_cost = float(input("Price of your dream house: "))

# 2. Call the portion of the cost needed for a down payment ​ portion_down_payment​ . For
# simplicity, assume that portion_down_payment = 0.25 (25%).
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment

# 3. Call the amount that you have saved thus far ​ current_savings​ . You start with a current
# savings of $0.
current_savings = 0.0

# 4. Assume that you invest your current savings wisely, with an annual return of ​ r ​ (in other words,
# at the end of each month, you receive an additional ​ current_savings*r/12​ funds to put into
# your savings – the 12 is because ​ r ​ is an annual rate). Assume that your investments earn a
# return of r = 0.04 (4%).
r = 0.04
# Additional current savings each month: 
# monthly_return = current_savings * r / 12.0

# 5. Assume your annual salary is ​ annual_salary​ .
annual_salary = float(input("Annual salary: "))

# 6. Assume you are going to dedicate a certain amount of your salary each month to saving for
# the down payment. Call that ​ portion_saved​ . This variable should be in decimal form (i.e. 0.1
# for 10%).
portion_saved = float(input("Portion saved for down-payment: "))

# 7. At the end of each month, your savings will be increased by the return on your investment,
# plus a percentage of your ​ monthly salary ​ (annual salary / 12).
# Increase in savings: monthly_return + salary_return
monthly_salary = annual_salary / 12
salary_return = monthly_salary * portion_saved
month_count = 0
monthly_return = 0.0

# Solution
while(current_savings < down_payment):
    current_savings = current_savings + monthly_return + salary_return
    monthly_return = current_savings * r / 12.0
    # Used for controling if savings go up correctly. To activate remove the # in line 42.
    # print(current_savings)
    month_count = month_count + 1
    
print("Months it took is: " + str(month_count))
