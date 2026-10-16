"""doc"""
required = {
    "Pad Thai Sauce",
    "Tofu",
    "Pickle Turnip",
    "Shrimp",
    "Bean Sprouts",
    "Noodle",
    "Chives",
    "Lime",
    "Egg",
    "Oil",
    "Peanuts",
}

required_tastes = {"Sweet", "Sour", "Salty"}

ingredients = set()
while True:
    item = input().strip()
    if item == "Cook":
        break
    ingredients.add(item)

tastes = set()
while True:
    taste = input().strip()
    if taste == "End":
        break
    tastes.add(taste)

if not ingredients.issubset(required):
    print("This is not Pad Thai!!!")
elif not required.issubset(ingredients):
    print("This is bad!")
elif tastes != required_tastes:
    print("Not Bad...")
else:
    print("Delicious!")
