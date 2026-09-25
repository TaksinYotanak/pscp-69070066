"""doc"""
string = []
longest = ""
for  _ in range(5):
    word = input()
    string.append(word)

for word in string:
    if len(word) > len(longest):
        longest = word

print((len(longest) + 4) * "*")

for j in string:
    print("*",j + " " * (len(longest) - len(j)),"*")

print((len(longest) + 4) * "*")
