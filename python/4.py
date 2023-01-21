num = int(input("n: "));
numbers = [];

print();

i = 0;
while i < num:
    numbers.append(int(input("Number " + str(i + 1) + ": ")));
    i += 1;

print();

current_num = -1;
j = 1;
max_j = -1;
max_i = -1;
first_loop = True;

for i in numbers:
    if (first_loop):
        current_num = i;
        first_loop = False;
        continue;

    if (i == current_num):
        j += 1;
    else:
        if (j > max_j):
            max_j = j;
            max_i = current_num;
        
        current_num = i;
        j = 1;

i = 0;
while i < max_j:
    if (i < max_j - 1):
        print(str(max_i) + ", ", end = "");
    else:
        print(max_i);

    i += 1;
