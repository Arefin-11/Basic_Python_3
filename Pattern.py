n=input("Enter the value of row:")
n=int(n)
if n%2==0:
    n+=1
c=1
for i in range(n,0,-2):
    if i!=n:
        for k in range(c):
            print(" ",end="")
        c+=1
    for j in range(i):
        print('*',end="")
    print("")
c-=1
for i in range(0,n,2):
    if i!=n:
        for k in range(c):
            print(" ",end="")
        c-=1
    for j in range(i+1):
        print('*',end="")
    print("")