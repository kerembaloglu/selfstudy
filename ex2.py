num = int(input("Give me a number: "))

if num % 2 == 1:
    print("It is an odd number")
elif num % 4 == 0:
    print("It is a multiple of 4")
elif num % 2 == 0:
    print("It is an even number")
else:
    print("What did you type??")
    
#https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html