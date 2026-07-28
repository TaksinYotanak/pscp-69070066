"""doc"""
def main():
    """doc"""
    a = int(input())
    b = int(input())
    c = int(input())

    big = min(b, c // 5)
    small_need = c - 5 * big

    if small_need <= a:
        print(small_need)
    else:
        print(-1)
main()
