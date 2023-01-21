m=int(input('chislo 1:'))
n=int(input('chislo 2:'))
pr=1
for x in range(m, n+1):
    if(x%3==0 or x%4==0):
        print(x)
        pr*=x
print(pr)
        
