"""doc"""
def main():
    """doc"""
    a = int(input())
    count = 0
    for _ in range(a):
        b = input()
        if b == "+":
            count += 10
        elif b == "-":
            count -= 5
    print(count)
main()
