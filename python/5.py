text = input("Text: ");
dict1 = {};

i = 0;
while i < len(text):
    dict1[text[i]] = text.replace(text[i], "", 1);
    i += 1;

print(dict1);



