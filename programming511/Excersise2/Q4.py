points = int(input("how many point do u have" ))

print("Gold" if points < 1 else "Bronze" if points < 20 else "Silver" if points < 50 else "None")