"""doc"""
one = []
two = []
same = []

m = int(input())
n = int(input())
for _ in range(m):
    first = input()
    one.append(first)

for _ in range(n):
    second = input()
    two.append(second)

for i in one:
    if i in two:
        same.append(i)

same.sort(reverse=True)

if not same:
    print("Nope")
else:
    for i in same:
        print(i)
