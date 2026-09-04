"""doc"""
N,K,T = map(int, input().split())
position = 1
count = 1

for i in range(N):
    position = (position + K) % N

    if position == 1:
        break

    count += 1

    if position == T:
        break

print(count)

