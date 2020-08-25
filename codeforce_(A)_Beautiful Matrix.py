matrix=[]
m=0
for i in range(5):
    n=0
    m += 1
    a=input().split()
    for entity in a:
        n+=1
        if int(a[n-1])==1:
            c=m
            b=n
    matrix.append(a)
count=abs(3-c)
count+=abs(3-b)
print(count)
