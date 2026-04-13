discount = int(input("Enter discount "))
while discount < 0 or discount > 50 :
  discount = int(input("wrong discount Please enter a valid discount "))

print(f"{discount}% discount approved ")