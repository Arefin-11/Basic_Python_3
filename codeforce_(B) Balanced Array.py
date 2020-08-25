t=int(input())
integers=[]
for i in range(t):
    integers.append(int(input()))
for integer in integers:
    if (integer//2)%2!=0:
        print("NO")
    else:
        fin=[]
        a=2
        count=0
        for i in range(integer//2):
            fin.append(a*(i+1))
        for i in range(integer//2):
            if i!=(integer//2)-1:
                fin.append(fin[i]-1)
                count+=1
            else:
                fin.append(fin[i]+count)
        print("YES")
        a = ""
        for i in range(len(fin)):
            a += str(fin[i]) + " "
        print(a)
