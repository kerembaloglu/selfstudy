import random
player_move = input("Rock Paper Scissors?: ")
listgame =["Rock","Paper","Scissors"]
enemy_move = listgame[random.choice(range(3))]
#def enemy_move():
#   k = random.choice(range(3))
#   print(listgame[k])
print(player_move)
print(enemy_move)
#enemy_move()
def play(player_move , enemy_move):
    if (player_move == "Rock") and (enemy_move == "Scissors"):
        print("You win")
    elif (player_move == "Paper") and (enemy_move == "Scissors"):
        print("You lose")
    elif (player_move == "Scissors") and (enemy_move == "Paper"):
        print("You win")
    elif (player_move == "Rock") and (enemy_move == "Paper"):
        print("You lose")
    elif (player_move == "Paper") and (enemy_move == "Rock"):
        print("You win")
    elif (player_move == "Scissors") and (enemy_move == "Rock"):
        print("You lose")
    elif (player_move == enemy_move):
        print("Equal")
  
play(player_move,enemy_move)  
  
#https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
    

    