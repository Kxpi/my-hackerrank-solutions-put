numbers = list(map(int, input().split()))
n = numbers[0]
x = numbers[1]
y = numbers[2]
result=0
for a in range(n + 1):
    for b in range(n + 1):
        for c in range(n + 1):
            for d in range(n + 1):
                if x*a*a + y*b*b== x*c*c + y*d*d:
                    result+=1

print(result)
