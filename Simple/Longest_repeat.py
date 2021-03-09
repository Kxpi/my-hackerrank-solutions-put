s=input().lower()
letters=[]
max=1
counter=1
for i in s:
    if i.isalpha():
        letters.append(i)

winner=letters[0]

for i in range(1, len(letters)):
    if letters[i]==letters[i-1]:
        counter+=1
    if letters[i]!=letters[i-1] or i==len(letters)-1:
        if counter>max:
            max=counter
            winner = letters[i-1]
        counter=1

print(winner)
