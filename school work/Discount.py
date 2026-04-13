discount = int(input("enter discount "))
while discount < 0 or discount > 50:
    discount = int(input("error this not a valid discount please enter a valid discount "))
print(f"discount of {discount}% has been granted")