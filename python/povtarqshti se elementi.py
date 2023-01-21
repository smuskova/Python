n=int(input('Broy na chislata:'))
a=0
list1=[]
for i in range(n):
    k=int(input())
    list1.append(k)
for i in range(n):
    if list1.count(list1[i])!=1:
        print("ima povtarqshti se elementi")
        break
    a+=1
    if a==n:
        print("nqma povtarqshti se elementi")
