test=int(input())
length=[]
string=[]
for t in range(test):
    length.append(int(input()))
    string.append(input())
for l in string:
    nums=l.split()
    fin=[]
    for alpha in nums:
        if int(alpha) not in fin:
            fin.append(int(alpha))
            print(alpha+" ",end="")
    print("")

