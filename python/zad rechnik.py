text= input("Text: ")
d={}
for i in text:
    occ=text.count(i);
    d[i]=occ
print(d)
