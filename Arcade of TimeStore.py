"""Arcade of Time: Store Check"""
num, _ = map(int, input().split())
shops = []

for _ in range(num):
    start, stop = map(int, input().split())
    shops.append([start, stop])

times = list(map(int, input().split()))

for time in times:
    count = 0
    for shop in shops:
        start = shop[0]
        stop = shop[1]

        if start <= time < stop:
            count += 1

    print(count, end=" ")
