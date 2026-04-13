name = input("Enter your name: ")
tscore1 = int(input("Enter your score 1: "))
tscore2 = int(input("Enter your score 2: "))
tscore3 = int(input("Enter your score 3: "))

totalScore = (tscore1 + tscore2 + tscore3)
avarage = round(totalScore / 3)

print(totalScore)

print("Your average score is " + str(avarage))


