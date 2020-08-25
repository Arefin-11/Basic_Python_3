no=int(input())
string=[]
for i in range(no):
    string.append(input())
for alpha in string:
    test=alpha.split()
    mini=min(int(test[0]),int(test[1]),int(test[2]))
    maxi = max(int(test[0]), int(test[1]), int(test[2]))
    count_mini=0
    count_maxi=0
    for i in test:
        if int(i)==mini:
            count_mini+=1
    for i in test:
        if int(i)==maxi:
            count_maxi+=1
    if count_mini==2 or count_maxi==1:
        print("NO")
    else:
        print("YES")
        if count_mini==3:
            a=int(test[0])
            b=int(test[1])
            c=int(test[2])
            print(a,b,c)
        else:
            a=int(maxi)
            b=int(mini)
            c=1
            print(a, b, c)



