"""doc"""
a,y = map(int,input().split())
total = 0
distance = 0
for i in range(a,0,-2):
    total += i
    distance += 1
    if total >= y:
        print(distance)
        break
if total < y:
    print(-1)
