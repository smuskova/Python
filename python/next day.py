year=int(input("Year: "))
month=int(input("Month: "))
day=int(input("Day: "))
last=year%10
add=1
if day !=30 and day!=28 and day!=31:
    day= day+add
    print(year)
    print(month)
    print(day)
if day==31 and month==12:
    year= year+add
    month=1
    day=1
    print(year)
    print(month)
    print(day)
if day==31:
    month=month+add
    print(year)
    print(month)
    print(day)
if day==30 and month==4 or month==6 or month==9 or month==11:
    month= month+add
    day=1
    print(year)
    print(month)
    print(day)
if day==28 and month==2:
    month= month+add
    day=1
    print(year)
    print(month)
    print(day)


        
            
    
          
    
    
    
