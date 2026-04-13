sales = float(input("enter the sales amount "))
counter = 0
highSales = 0
tot = 0

while sales != -1 :
    sales= float(input("enter the sales amount "))
    tot = tot + sales 
    counter += 1

    if highSales < sales :
        highSales = sales
    
print("\n Summary")

print(f"number of transactions : {counter} \n total sales is  : R{tot} \n highest sale was : R{highSales} \n the avarage was : R{(tot/counter):.2f}")
