a = list(map(int,input().split()))
m = int(a[0])
n = int(a[1])
a = int(a[2])
if n <= a and m <= a:
    count = 1
elif n > a and m <= a:
    count = n // a
    p = n % a
    if p > 0:
        count += 1
elif n <= a and m > a:
    count = m // a
    p = m % a
    if p > 0:
        count += 1
elif n > a and m > a:
    e = n // a
    f = m // a
    p = n % a
    q = m % a
    if p > 0:
        e += 1
    if q > 0:
        f += 1
    count = e*f
print(count)

