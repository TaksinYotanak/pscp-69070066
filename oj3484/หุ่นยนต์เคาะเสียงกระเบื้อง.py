"""doc"""
n, p = input().split()
n = int(n)
p = float(p)

col_places = [0] * n
col_tiles = [0] * n
all_places = 0
all_tiles = 0

for _ in range(n):
    row = list(map(int, input().split()))
    row_places = 0
    row_tiles = 0

    for j, x in enumerate(row):
        if x > 0:
            row_places += 1
            col_places[j] += 1

        row_tiles += x
        col_tiles[j] += x

    print(*row, row_places, row_tiles)
    all_places += row_places
    all_tiles += row_tiles

print(*col_places)
print(*col_tiles)
print(all_places, all_tiles, f"{all_tiles * p:.2f}")
