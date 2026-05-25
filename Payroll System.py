a = float(input("Enter Basic Salary ?"))
b = float(input("Enter Extra Hours ?"))
c = float(input("Enter Working Days ?"))

total = a + (c*(a*0.05)) + b * 250  
tax = total * 0.12

salary = total - tax
print("salary is ", salary)



