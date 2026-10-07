score = int(input())
player_a = 0
player_b = 0
turn = 1
total_a = 0
total_b = 0

while score != -1 :
    if turn % 2 == 1 :
        player_a += score
        total_a = player_a
    else: 
        player_b += score
        total_b = player_b
    turn += 1
    score = int(input())
if player_a > player_b :
    winner = "A" 
elif player_b > player_a:
    winner = "B"
else : 
    winner = "Tie"


print(total_a)
print(total_b)
print(winner)
