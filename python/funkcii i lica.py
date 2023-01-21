def menu():
    print("Figuri:")
    print("1. Kvadrat")
    print("2. Pravougulnik")
    print("3. Pravougulrn triugulnik")
def kvadrat(n):
    a=int(input('Vuvedetet stoinost za stranata na kvadrata:'))
    s=a*a
    p=4*a
    print("Liceto:{0}". format(s))
    print("Obikolkata:{0}". format(p))
    
        
       
def pravouguknik(n):
    a=int(input('a='))
    b=int(input('b='))
    s=a*b
    p=2*(a+b)
    print("Liceto:{0}". format(s))
    print("Obikolkata:{0}". format(p))
       
        
       
def pravougulenTR(n):
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    s=a*b
    p=a+b+c
    print("Liceto:{0}". format(s))
    print("Obikolkata:{0}". format(p))
menu()   
n=int(input('Izberete figura:'))
if(n==1):
    kvadrat(n)
if(n==2):
    pravougulnik(n)
if(n==3):
    pravougulenTR(n)
