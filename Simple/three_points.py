coords=[]
for i in range(3):
    coords.append(list(map(int, input().split())))

a=coords[0][0]*(coords[1][1]-coords[2][1])+coords[1][0]*(coords[2][1]-coords[0][1])+coords[2][0]*(coords[0][1]-coords[1][1])
if a==0:
    print("True")
else:
    print("False")
