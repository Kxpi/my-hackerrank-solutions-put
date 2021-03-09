t=int(input())
s=0
mn=[]
x=[]
while s!=t:
    mn = list(map(int, input().split()))
    for i in mn:
        x.append(i)
    mn.clear()
    s+=1
for i in range(0, len(x), 2):
    if x[i] > x[i + 1]:
        print(x[i], " is greater than ", x[i + 1])
    if x[i] < x[i + 1]:
        print(x[i], " is smaller than ", x[i + 1])
    if x[i] == x[i + 1]:
        print('n is equal m: ',x[i])
