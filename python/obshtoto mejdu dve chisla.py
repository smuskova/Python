a= int(input('chislo1:'))
b= int(input('chislo2:'))
digits_a=[int(x) for x in str(a)]
digits_b=[int(z) for z in str(b)]
print(digits_a)
print(digits_b)
c=0
d=[]
for i in digits_a:
    for j in digits_b:
        if i==j:
            d.append(i)
            c+=1
print(d)

            
