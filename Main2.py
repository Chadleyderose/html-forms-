AnualSalary = int(input("Enter your anual salary:" ))
gross_monthly_salary = (AnualSalary / 12)
print(gross_monthly_salary)



Income_tax = float(input("Enter the amount of Income tax you pay without the percentage sigh: " ))
net_salary = (gross_monthly_salary - Income_tax)
print(net_salary)
