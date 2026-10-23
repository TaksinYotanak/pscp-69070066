"""ddd"""

import ast

alive = {}
dead = {}

while True:
    line = input().strip()
    if line == "Start":
        break
    alive.update(ast.literal_eval(line))

while True:
    name = input().strip()
    if name == "End":
        break
    dead[name] = alive.pop(name)

impostors = 0
for role in alive.values():
    if role == "Impostor":
        impostors += 1

print(f"{impostors} Impostor Remains")
print("***Alive***")
for name in sorted(alive):
    print(f"{name} : {alive[name]}")

print("***Dead***")
for name in sorted(dead):
    print(f"{name} : {dead[name]}")
