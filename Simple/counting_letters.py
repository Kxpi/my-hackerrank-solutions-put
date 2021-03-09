sentence=input().lower()
letters=[]
for i in sentence:
    if i.isalpha():
        letters.append(i)
max=0
counter=0
winner=" "
for i in letters:
    counter=letters.count(i)
    if counter>max:
        max=counter
        winner=i

print(winner)
