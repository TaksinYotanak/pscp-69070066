"""doc"""
w, h, m, n = map(int, input().split())
xs = [0] + list(map(int, input().split())) + [w]
ys = [0] + list(map(int, input().split())) + [h]

a = 0
b = 0

for i in range(m + 1):
    dx = xs[i + 1] - xs[i]

    for j in range(n + 1):
        dy = ys[j + 1] - ys[j]
        area = dx * dy

        if area >= a:
            b = a
            a = area
        elif area > b:
            b = area

print(a, b)
