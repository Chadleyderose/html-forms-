# Calculating the increase in salary
print("--The Bright Light Company employees Salary increase--")

Deptcode = input("Enter Department code: ")
anSalary = int(input("Enter Anual salary: "))

a = 0.072
b = 0.068
o = 0.063

if Deptcode == a:
    increase_anSalary = anSalary + (anSalary * a)
    monsalary = increase_anSalary / 12
    print(monsalary)
elif Deptcode == b:
    increase_anSalary = anSalary + (anSalary * b)
    monsalary = increase_anSalary / 12
    print(monsalary)
elif Deptcode == o:
    increase_anSalary = anSalary + (anSalary * o)
    monsalary = increase_anSalary / 12
    print(monsalary)
else:
    print("please check your DepartmentCode and restart")
