kWh = int(input())
if kWh <= 100 :
    totalBill = kWh * 0.3
else:
    if kWh >100 and kWh <= 200 :
        totalBill = (100*0.3) + (kWh - 100) *0.5
    else: 
        totalBill = (100 * 0.3) + (200 * 0.5) + (kWh - 100 - 200)*0.75
print(totalBill)