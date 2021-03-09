n=int(input())
k=0
h=[]
th=0
l=list()
max_ar=0
while k!=n:
    th=int(input())
    h.append(th)
    th=0
    k+=1
areas=[]
k=0
while k<len(h):
    if(not l) or (h[l[-1]]<=h[k]):
        l.append(k)
        k+=1
    else:
        tl=l.pop()
        ar = (h[tl] *((k - l[-1] - 1) if l else k))
        max_ar = max(max_ar, ar)
while l:
    tl=l.pop()
    ar = (h[tl] * ((k - l[-1] - 1) if l else k))
    max_ar = max(max_ar, ar)
print(max_ar)
