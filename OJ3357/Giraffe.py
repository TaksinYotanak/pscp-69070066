"""Doc"""
g = int(input())
count = []
total = 0
for _ in range(g):
    h = int(input())
    count.append(h)

if g == 1:
    total = 1

else:
    if count[0] > count[1]:
        total += 1

    for i in range(1, len(count) - 1):
        if count[i] > count[i - 1] and count[i] > count[i + 1]:
            total += 1

    if count[-1] > count[-2]:
        total += 1

print(total)
