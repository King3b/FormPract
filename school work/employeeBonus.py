employee = int(input("how many employees at the company "))
bonus = 0
for i in range (1,employee + 1):
    employee_sales= float(input(f"enter employee  {i} sales  "))
    bonus = bonus + (employee_sales *0.05)
    print(f"\n employee {i}s bonus is {(employee_sales *0.05):.2f}")
print(f"total bonuses is {bonus}")