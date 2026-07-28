"""doc"""
import math
def main():
    """doc"""
    S, N = map(float, input().split())
    results = []
    for _ in range(int(N)):
        X, Y = map(float, input().split())
        t = math.ceil(3.1416 * (X**2 + Y**2) // S)
        results.append(t)
    for r in results:
        print(r)

main()
