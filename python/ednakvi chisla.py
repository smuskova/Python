list1=[1,2,4,6,2,4]
list2=[]
for i in list1:
    if list1[i]==list1[i+1]:
        list2.append(i)
print(list2)
        
