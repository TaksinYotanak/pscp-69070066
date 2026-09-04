"""doc"""
a, b = map(int, input().split())

count = 0
prime = []

for i in range(a, b + 1):
    if i < 2:
        continue

    for j in range(2, i):
        if not i % j:
            break
    else:
        count += 1
        prime.append(i)

if prime:
    print(" ".join(map(str, prime)))

print("Total primes:", count)
