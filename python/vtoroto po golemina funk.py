import random
def golemina(s):
    s.sort()
    
    return s[3]
list1=[random.randint(1,50) for i in range(5)]
print(list1)
print(golemina(list1))        
