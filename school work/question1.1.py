score = 0
for i in range (1,6):
    student = int(input("enter score"))
    score = score + student
print(f"the total avarage is {(score/5):.2f}")