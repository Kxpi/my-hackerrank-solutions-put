sentence=input()
lol=[]
vowels=['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
for x in sentence:
    if x not in vowels:
        lol.append(x)
new_sentence=""
for i in lol:
    new_sentence+=i
print(new_sentence)
