"""doc"""

number = []
while True:
    n = int(input())

    if n == -1:
        break

    number.append(n)

result = []

if number:
    start = number[0]

    for i in range(1, len(number)):
        if number[i] == number[i - 1] + 1:
            continue

        end = number[i - 1]

        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + "-" + str(end))

        start = number[i]

    end = number[-1]

    if start == end:
        result.append(str(start))
    else:
        result.append(str(start) + "-" + str(end))

print(", ".join(result))
