"""doc"""
def main():
    """doc"""
    a,b = map(str, input().split())
    w = float(input())
    if a == "BKK" and b == "CNX":
        print(f"{(30*w)+10:.2f}")
    elif a == "CNX" and b == "UBP":
        print(f"{(40*w)+15:.2f}")
    elif a == "UBP" and b == "BKK":
        print(f"{(40*w)+20:.2f}")
    elif a == "BKK" and b == "PKT":
        print(f"{(50*w)+25:.2f}")
    elif a == "PKT" and b == "CNX":
        print(f"{(60*w)+30:.2f}")
    elif a == "UBP" and b == "PKT":
        print(f"{(70*w)+40:.2f}")
    else:
        print("Error")
main()
