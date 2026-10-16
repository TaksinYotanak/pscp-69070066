"""CuteCat CuteFox."""

import ast


def get_number(label):
    """nnn"""
    return int(label[3:])

total = int(input())
animals = {}

for _ in range(total):
    entry = ast.literal_eval(input())

    for name, code in entry.items():
        animals[code.strip()] = name.strip()

if "Garfield" not in animals.values() and "Cat01" not in animals:
    animals["Cat01"] = "Garfield"

if "Fubuki" not in animals.values() and "Fox01" not in animals:
    animals["Fox01"] = "Fubuki"

cats = sorted(
    (code for code in animals if code.startswith("Cat")),
    key=get_number,
)
foxes = sorted(
    (code for code in animals if code.startswith("Fox")),
    key=get_number,
)

print(f"Cat : {len(cats)}")
print(f"Fox : {len(foxes)}")

for code in cats + foxes:
    print(f"{animals[code]} : {code}")
