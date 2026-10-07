sales = int(input())
count = 0 
record_days = 0
highest = 0 

while sales != 0 :
    count += 1 

    if sales > highest : 
        record_days += 1 
        highest = sales 

    sales = int(input())

    


print(count)
print(record_days)
