coffee_name="coffee"
coffee_price= 3.50
coffee_qty = 2
total_coffee = coffee_price * coffee_qty

muffin_name = "muffin"
muffin_price = 2.10 
muffin_qty = 3
total_muffin = muffin_price * muffin_qty

water_name = "water"
water_price = 1.05 
water_qty = 4
total_water = water_price * water_qty

subtotal = total_coffee + total_muffin + total_water
tax = subtotal * 0.06
Total = subtotal + tax






store ="==========RECEIPT==========\nItem\tprice\tqty\ttotal"
print(store)
print(f"{coffee_name}\t${coffee_price: .2f}\t{coffee_qty}\t${total_coffee:.2f}\n"  #I LOVE COFFEE
      f"{muffin_name}\t${muffin_price: .2f}\t{muffin_qty}\t${total_muffin:.2f}\n"
      f"{water_name}\t${water_price: .2f}\t{water_qty}\t${total_water:.2f}\n")
print("------------------------------")
print(f"Subtotal\t\t${subtotal:.2f}\n"
      f"Tax(6%)\t\t\t${tax:.2f}\n"
      f"Total\t\t\t${Total:.2f}\n"
      f"=============================")
      
      