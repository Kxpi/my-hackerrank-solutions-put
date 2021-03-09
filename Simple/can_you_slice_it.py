n=input()
temp_numbers=n.split()
numbers=[]
for i in temp_numbers:
    if i!='':
        i=int(i)
        numbers.append(i)
numbers.sort()
statement=True
if len(numbers)<2:
    statement=True
else:
    diff = numbers[1] - numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i]-numbers[i-1]==diff:
            statement=True
        else:
            statement=False
            break
print(statement)
