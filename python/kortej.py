text= input('Vuvedete text: ')
step=int(input('razstoqnie: '))
tup=tuple(text)
tup2=tup[::step+1]
print(tup2)
