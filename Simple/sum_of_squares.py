ab=list(map(int, input().split()))
ab.sort()
temp=ab[0]
result=0
while temp<=ab[1]:
    result+=(temp**2)
    temp+=1

print(result)
