s = input("Give me a word: ")
i = 0
lists = list()
while i < len(s):
    if s[i] == s[-(i+1)]:
        lists.append(s[i])
        i = i+1
    else:
        break
print(lists)
if len(lists) == len(s):
    print("pal")
else:
    print("non")
    
#https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html