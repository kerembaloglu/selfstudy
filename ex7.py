#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
import random
a = random.sample(range(100),10)
i = 0
listeven = list()
for i in range(len(a)):
    if a[i] % 2 == 0:
        listeven.append(a[i])
print(listeven)

#https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html