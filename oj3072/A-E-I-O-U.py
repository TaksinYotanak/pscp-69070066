"""doc"""
def main():
    """doc"""
    text = input().lower()
    alpha = ["a", "e", "i", "o", "u"]

    for i in alpha:
        count = text.count(i)

        if count > 0:
            print(f"{i} : {count}")

main()
