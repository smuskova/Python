n=int(input('vuvedete chislo: '))
list=[k for k in range(1,n+1)]
d={}
list1= list[::-1]
for i in list:
    d[i]=list1[i-1]
print(d)
