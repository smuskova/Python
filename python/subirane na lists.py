import random
list1=[random.randint(1,50) for i in range(7)]
list2=[random.randint(1,50) for i in range(7)]
list3=[]
print(list1)
print(list2)
for i in range(0,len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])
print(list3)
