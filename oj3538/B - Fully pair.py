"""ddd"""

letters = input().strip()
counts = {}

for letter in letters:
    if letter not in counts:
        counts[letter] = 0
    counts[letter] += 1

unpaired = []
for letter, amount in counts.items():
    if amount % 2:
        unpaired.append(letter)

if unpaired:
    print("".join(unpaired))
else:
    print("fully paired")
