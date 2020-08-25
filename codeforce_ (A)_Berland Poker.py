t=int(input())
tests=[]
for i in range(t):
    tests.append(input())
for test in tests:
    lst=test.split()
    n=int(lst[0])
    m=int(lst[1])
    k=int(lst[2])
    if m==0:
        max=0
    else:
        cpp=n//k
        if m<=cpp:
            max=m
        else:
            remjok=m-cpp
            min=remjok//(k-1)
            if remjok%(k-1) !=0:
                min+=1
            max=cpp-min
    print(max)
