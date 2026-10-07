number = int(input())
count = 0
biggest_jump = 0
current_jump = 0 

while number != 0 : 
    count += 1 

    if count > 1 : 
        jump = number - current_jump 

        if jump > biggest_jump: 
            biggest_jump = jump 
    current_jump = number
    number = int(input())




print(count)
print(biggest_jump)
