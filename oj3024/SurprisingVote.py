"""doc"""
def main():
    """doc"""
    total = float(input())
    max_score = float(input())
    min_score = total - (max_score * 2)
    if min_score < 0:
        min_score = 0
    if max_score - min_score > 2:
        print("Surprising")

    else:
        print("Not surprising")

main()
