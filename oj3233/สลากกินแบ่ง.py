"""doc"""
a, b = input().split()
c, d = input().split()

if (a == c) and (b == d):
    print(1000000)
elif (a != c) and (b == d):
    print(100000)
elif (a == c) and (b[-3:] == d[-3:]):
    print(2000)
elif (a == c) and (b[-2:] == d[-2:]):
    print(1000)
elif (a != c) and (b[-3:] == d[-3:]):
    print(200)
elif (a != c) and (b[-2:] == d[-2:]):
    print(100)
elif (a == c) and (b != d):
    print(20)
else:
    print(0)
