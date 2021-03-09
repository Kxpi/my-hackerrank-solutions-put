h=int(input())
n=int(input())

for i in range(n):
    if i==0:
        for j in range(1,h+1):
            print(j * '* ')

    else:
        h+=1
        for k in range(1,h+1):
            print(k * '* ')
