"""DOC"""
L, N = map(int, input().split())

line = 1
total = 0

while total < N:
    total += line
    line += 1

line -= 1

band = (line + L - 1) // L

print(band)
