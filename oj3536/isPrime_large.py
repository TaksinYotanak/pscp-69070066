"""ddd"""

number = int(input())
prime = number >= 2
divisor = 2

while divisor * divisor <= number:
    if not number % divisor:
        prime = False
        break
    divisor += 1

if prime:
    print("YES")
else:
    print("NO")
