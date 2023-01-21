import pickle
sth=[22,33,65]
with open ('pickle.exe1_1.txt', 'wb') as file1:
    p1=pickle.dump(sth,file1)
with open ('pickle.exe1_1.txt', 'rb') as file1:
    p2=pickle.load(file1)
    print(p2)
