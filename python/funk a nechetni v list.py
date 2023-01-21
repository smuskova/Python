import random

def nechetni(s):
    list2=[]
    for i in range(0,len(s)):
        if s[i]%2!=0:
            list2.append(s[i])
    return list2
list1=[random.randint(1,50) for i in range(5)]
print(list1)
print(nechetni(list1))
