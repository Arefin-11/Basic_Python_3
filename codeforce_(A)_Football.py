inp=input()
count=0
if len(inp)<7:
    print("NO")
else:
    for i in range(len(inp)-1):
        if inp[i+1]==inp[i]:
            count+=1
        else:
            count=0
        if count>=6:
            print("YES")
            quit()
    print("NO")
