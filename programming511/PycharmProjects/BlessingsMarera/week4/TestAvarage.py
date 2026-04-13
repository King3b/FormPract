
tests = 5
score = 0
for x in range(1,tests+1):
    Student = int(input("enter student score "))
    score = score + Student

avarege = score / tests
print(f"the avarage is  {avarege}")