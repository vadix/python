a = int(input())
b = int(input())
c = int(input())

if (a > b and a > c) or (a == b and a > c):
    if b > c:
        print("a\nb\nc")

if  b >= a and b >= c:
    if a >= c:
        print(b)
        print(a)
        print(c)
    print(b)
    print(c)
    print(a)


if c >= a and c >= b:
    if a >= b:
        print(c)
        print(a)
        print(b)

