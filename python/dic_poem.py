d={'Vazov':'Pod igoto', 'Konstantinov':'Bay Ganio', 'Botev':'Na proshtavane','Pelin':'Kosachi'}
br=0
for i in d.keys():
    print(d[i], ":")
    answer=input()
    if answer==i:
        br+=1
print(br)

