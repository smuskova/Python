day=int(print('dneshniq den'))
n=int(input('vuvedete broi dni'))
ostatuk=(day+n)%7
if(ostatuk==1):
    print("ponedelnik")
elif(ostatuk==2):
    print("vtornik")
elif(ostatuk==3):
    print("srqda")
elif(ostatuk==4):
    print("chetvurtak")
elif(ostatuk==5):
    print("petuk")
elif(ostatuk==6):
    print("sybota")
elif(ostatuk==0):
    print("nedelq")
