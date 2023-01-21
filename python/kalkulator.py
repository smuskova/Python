def subirane(a,b):
    return a+b
def izvajdane(a,b):
    return a-b
def umnojenie(a,b):
    return a*b
def delenie(a,b):
    if b==0:
        print('ERROR')
    else:
        return a/b

print("vuvedete chisla:")
a=int(input('a='))
b=int(input('b='))
print("Izberete deystvie")
print("1. subirane ")
print("2. izvajdANE ")
print("3. UMNOJENIE")
print("4. delenie ")
izb=int(input('jelanata operaciq:'))
if izb==1:
    print("Rezultata e:")
    print(subirane(a,b))
if izb==2:
    print("Rezultata e:")
    print(izvajdane(a,b))
if izb==3:
    print("Rezultata e:")
    print(umnojenie(a,b))
if izb==4:
    print("Rezultata e:")
    print(delenie(a,b))
