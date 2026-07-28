"""doc"""
import math

def main():
    """doc"""
    N = int(input())

    if N == 1:
        print(0)
        return
    r = math.ceil(math.sqrt(N))
    ans = 2 * (r - 1)

    if (r * r - N) % 2 == 1:
        ans -= 1
    print(ans)
main()
