main_course = input()
drink = input()
dessert = input()

if main_course == "Chicken": 
    food = 10
elif main_course == "Beef":
    food = 12
else : 
    food = 11

if drink == "Soft Drink":
    drink_price = 2
else:
    drink_price = 3

if dessert == "Ice Cream" :
    dessert_price = 4
else:
    dessert_price = 5

final_bill =( food + drink_price + dessert_price ) * 1.10

print(f"{final_bill:.2f}")
