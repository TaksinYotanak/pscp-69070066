"""doc"""
def main():
    """doc"""
    number = int(input())
    for i in range(number,-1,-1):
        if not i % 10:
            print(i,end = " ")
main()
