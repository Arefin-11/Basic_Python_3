n = int(input())
sols=[]
for i in range(n):
    sols.append(input())
fin=0
for sol in sols:
    count=0
    views=sol.split()
    for view in views:
        if int(view)==1:
            count+=1
    if count>1:
        fin+=1
print(fin)
