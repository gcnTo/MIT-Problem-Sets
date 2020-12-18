# import time

current_savings = 0.0
r = 0.04
# annual_salary = 150000 #TEST CASE 1
annual_salary = 300000 #TEST CASE 2
# annual_salary = 10000 #TEST CASE 3
monthly_salary = annual_salary / 12
portion_saved = 0
monthly_return = 0.0
month_count = 0
semi_annual_raise = 0.07
salary_return = monthly_salary * portion_saved
high = 10000
low = 0
bisection = 0

while(current_savings + 100 < 250000 or current_savings - 100 > 250000): 
    
    
    if(portion_saved != 0):
        if(current_savings - 100 > 250000):
            high = int(portion_saved*10000)
            # print("high",high)
            bisection += 1
        
        elif(current_savings + 100 < 250000):
            low = int(portion_saved*10000)
            # print("low",low)
            bisection += 1
        
    portion_saved = int((high + low)/2) / 10000
    current_savings = 0
    if(bisection > 100):
        print("It is not possible to pay the down payment in three years.")
        break
    
    
    
    for month_count in range(36):
        
        if(month_count > 0):
            salary_return = monthly_salary * portion_saved
            monthly_return = current_savings * r / 12.0
            current_savings += monthly_return + salary_return
            
        
        if((month_count + 1) % 6 == 0):
            annual_salary *= semi_annual_raise

        # if(month_count == 35):
            # print("current",current_savings)
            # print("portion", portion_saved)
            # time.sleep(5)
    print("bisection", bisection)
    print("portion_saved", portion_saved)
    # print("current", current_savings)
