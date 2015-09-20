a = int(input())
b = int(input())
c = int(input())

if a >= b:
    if b >= c:
        print(a)
        print(c)
        print(b)
    elif a>= c:
        print(a)
        print(b)
        print(c)
    else:
        print(c)
        print(b)
        print(a)
else:
    if b <= c:
        print(c)
        print(a)
        print(b)
    elif a <= c:
        print(b)
        print(a)
        print(c)
    else:
        print(b)
        print(c)
        print(a)