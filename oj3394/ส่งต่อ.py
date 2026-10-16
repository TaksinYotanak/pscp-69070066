"""doc"""
n, s = map(int, input().split())

next_student = [0]
for _ in range(n):
    next_student.append(int(input()))

received = [False] * (n + 1)
total = 0

while s and not received[s]:
    received[s] = True
    total += 1
    s = next_student[s]

print(total)
