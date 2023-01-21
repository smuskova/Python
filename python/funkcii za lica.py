def lica():
    print("Figuri:")
    print("1. Kvadrat")
    print("2. Pravougulnik")
    print("3. Pravougulrn triugulnik")
    n=int(input('Izberete figura:'))
    if(n==1):
        a=int(input('Vuvedetet stoinost za stranata na kvadrata:'))
        s=a*a
        p=4*a
        print("Liceto:{0}". format(s))
        print("Obikolkata:{0}". format(p))
    
    elif(n==2):
        a=int(input('a='))
        b=int(input('b='))
        s=a*b
        p=2*(a+b)
        print("Liceto:{0}". format(s))
        print("Obikolkata:{0}". format(p))
    
    elif(n==3):
         a=int(input('a='))
         b=int(input('b='))
         c=int(input('c='))
         s=a*b
         p=a+b+c
         print("Liceto:{0}". format(s))
         print("Obikolkata:{0}". format(p))
lica()
   
