"""doc"""
from decimal import Decimal, ROUND_HALF_UP

m = input()
n = int(input())
count = Decimal("0")

for _ in range(n):
    price = Decimal(input())
    count += price

if m == "Y":
    count = count * Decimal("0.95")

elif m == "N" and count >= Decimal("500"):
    count = count * Decimal("0.97")

print(count.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
