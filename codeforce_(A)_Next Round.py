n=input().split()
k=int(n[1])
points=input().split()
p=int(points[k-1])
count=0
for point in points:
    if int(point) >= p and int(point)!=0:
        count+=1
print(count)
