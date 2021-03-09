numbers=list(map(int, input().split()))
borders=list(map(int, input().split()))
borders.sort()
i=borders[0]
j=borders[1]
sum=0
new_numbers=numbers[i:j+1]
for i in new_numbers:
    sum+=i
print(sum)
