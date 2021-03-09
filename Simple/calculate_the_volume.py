tab=input().split()
volume=1
for i in range(len(tab)):
    tab[i]=int(tab[i])
    volume*=tab[i]
print(volume)
