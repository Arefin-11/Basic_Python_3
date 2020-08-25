t=int(input())
integers=[]
for i in range(t):
    integers.append(input())
for integer in integers:
    a=len(integer)
    fin=[]
    pos=0
    count=0
    for i in range(-1,-(a+1),-1):
        t=int(integer[i])
        if t>0:
            fin.append(t*(10**pos))
            count+=1
        pos+=1
    print(count)
    you=""
    for i in range(len(fin)):
        you = str(fin[i])+" "+you
    print(you)
    #print(" ".join(fin))


