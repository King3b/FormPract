product="Laptop"
price = 1249.9999
quantity = 3
tax_rate = 0.0875

subTotal = price * quantity
tax = tax_rate * subTotal

total = subTotal + tax

print(f"{total: .2f}")