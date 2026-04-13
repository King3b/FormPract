import time

my_Time = int(input("Enter the time in seconds: "))

for x in range(my_Time, 0, -1):
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = x // 3600

    print(f"H {hours} : M {minutes} : S {seconds}")
    time.sleep(1)

print("Time's up!")