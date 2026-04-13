no_employees = int(input("input number of employees "))
bonus = 0
for i in range (1, no_employees+1):
    employees = float(input(f"enter employee {i} salary "))
    print(f"employee {i} sales {employees} and his bonus is {(employees * 0.05):.2f}")
    bonus = bonus + (employees * 0.05)
    
totBonus = bonus
print(f"the total bonus is {bonus:.2f}")