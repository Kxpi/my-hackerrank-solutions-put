n = int(input())
tab = []
for i in range(n):
    tab.append(int(input()))
    
if len(set(tab))==1:
    print(True)
else:
    print(False)
