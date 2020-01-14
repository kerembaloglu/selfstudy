import random

user_num = float(input("What is your number between 1-9 ?: "))
rand_num = random.choice([1,9])

def core(user_num,rand_num):
    user_num = float(input("What is your number between 1-9 ?: "))
    rand_num = random.choice([1,9])
    if user_num == rand_num:
        print("Correct")
    elif user_num > rand_num:
        print("Too high")
    else:
        print("Too low")
        
def play():
    core(user_num,rand_num)
    r = input("Play again Y/N ?: ")
    if r == "Y":
        play()
    else:
        print("End")
play()        
