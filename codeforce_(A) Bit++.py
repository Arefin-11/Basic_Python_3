n=int(input().lower())
states=[]
for i in range(n):
    states.append(input())
count=0
for state in states:
    if state=="++X" or state=="X++":
        count+=1
    else:
        count-=1
print(count)
