t=int(input())
a=[]
n=[]
for i in range(t):
    n.append(input())
    a.append(input())

for test in a:
    test=test.split()
    s=test[0]
    for i in test:
        if i==s:
            continue
        else:
            s=None
            break
    if s==test[0]:
        print("YES")
    else:
        u=0
        for r in range(len(test)-1):
            if abs(int(test[0])-int(test[-1]))<=1:
                b=min(test[0],test[-1])
                test.remove(b)
            else:
                print("No")
                u=2
                break
        if u!=2:
            print("YES")


