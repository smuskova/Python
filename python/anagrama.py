def anagrama(text1,text2):
    set1=set(text1)
    set2=set(text2)
    if set1==set2:
        return 1
    else:
        return 0
print(anagrama(text1=input('Text1:'), text2=input('Text2:')))
    
    
