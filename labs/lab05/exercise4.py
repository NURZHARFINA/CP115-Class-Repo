item_name = str(input("what is the item ? "))
price = float(input(" how much the price ? "))
quantity = 3
tax_rate = 0.06

subtotal = price * quantity
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount
print(subtotal)
print(tax_amount)
print(total_cost)