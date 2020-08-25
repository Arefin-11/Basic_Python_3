string=input().split("+")
string.sort()
fin=""
for i in range(len(string)):
    fin+=string[i]
    if (i+1)!=len(string):
        fin+="+"
print(fin)
