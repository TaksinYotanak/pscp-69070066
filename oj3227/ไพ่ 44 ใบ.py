"""pai"""
card = input().upper()

number = card[:-1]
group = card[-1]

number_name = {
    "A": "ace",
    "J": "jack",
    "Q": "queen",
    "K": "king"
}
group_name = {
    "D": "diamonds",
    "H": "hearts",
    "S": "spades",
    "C": "clubs"
}

print(number_name.get(number,number), "of",group_name[group])
