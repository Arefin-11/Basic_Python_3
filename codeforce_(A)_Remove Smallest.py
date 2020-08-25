t=int(input())
a=[]
n=[]
for i in range(t):
    n.append(input())
    a.append(input())

for test in a:
    Test=[]
    test=test.split()
    for i in range(len(test)):
        Test.append(int(test[i]))
    Test.sort()
    #print(Test)
    s=Test[0]
    for i in Test:
        if i==s:
            continue
        else:
            s=None
            break
    if s==Test[0]:
        print("YES")
    else:
        u=0
        for r in range(len(Test)-1):
            if abs(int(Test[0])-int(Test[1]))<=1:
                b=min(Test[0],Test[1])
                Test.remove(b)
            else:
                print("No")
                u=2
                break
        if u!=2:
            print("YES")
