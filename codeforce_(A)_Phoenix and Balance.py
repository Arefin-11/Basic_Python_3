t=int(input())
coins=[]
for i in range(t):
    coins.append(int(input()))
for coin in coins:
    wei=[]
    for i in range(coin):
        wei.append(2**(i+1))
    l=(len(wei)//2)
    first=wei[-1]
    for i in range(l-1):
        first+=wei[i]
    second=0
    for i in range(l,len(wei)):
        second+=wei[i-1]
    min=first-second
    print(min)
