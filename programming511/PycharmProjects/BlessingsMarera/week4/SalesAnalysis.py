sales = float(input("enter sales "))
counter = 0
record = 0
highSale = 0

while sales != -1:
    sales = float(input("enter sales "))
    counter += sales
    record += 1
    if sales > highSale:
        highSale = sales
    
print("\n sales summary")

Avarge = counter / record
print(f"s")

    
