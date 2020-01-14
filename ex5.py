import random
a = random.sample(range(10),3)
b = random.sample(range(10),4)

print(a)
print(b)
listainb = list()
i = 0
for i in range(0,len(a)):
    if (a[i] in b) and (a[i] not in listainb):
        listainb.append(a[i])
            
print(listainb)
