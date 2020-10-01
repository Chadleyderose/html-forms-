#Calculating the increase in salary
print("--The Bright Light Company employees Salary increase--")

Department_code = input("Enter Department code: ")
anSalary = input("Enter Anual salary: ")

a = 0.072
b = 0.068
other = 0.063

if Department_code == a:
    increase_anSalary = anSalary + (anSalary * a)
    monthly_salary = increase_anSalary / 12
    print(monthly_salary)
elif Department_code == b:
    increase_anSalary = anSalary + (anSalary * b)
    monthly_salary = increase_anSalary / 12
    print(monthly_salary)
elif Department_code == other:
    increase_anSalary = anSalary + (anSalary * other)
    monthly_salary = increase_anSalary / 12
    print(monthly_salary)
else:
    print("please check your DepartmentCode and restart")
