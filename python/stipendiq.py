n= float(input('vuvedete uspeha si:'))
st=float(input('Vuvedete maximalnata stipendiq:'))
if(n>=5.50):
    print("Vie shte poluchavate maximalna sripendiq:". format(st))
elif(n<5.50 and n>=5.00):
    procent1= st*70/100
    print("Vie shte poluchavate:{0}". format(procent1))
elif(n>=4.50 and n<5.00):
    procent2=st*50/100
    print("Vie shte poluchavate:{0}". format(procent2))
else:
    print("ne poluchavsh stipendiq")
