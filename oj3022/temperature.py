"""doc"""
def main():
    """doc"""
    temp = float(input())
    fault = str(input())
    define = str(input())

    if fault == "C":
        C = temp
    elif fault == "K":
        C = temp - 273.15
    elif fault == "F":
        C = (temp - 32) * 5 / 9
    elif fault == "R":
        C = temp * 5 / 9 - 273.15

    if define == "C":
        result = C
    elif define == "K":
        result = C + 273.15
    elif define == "F":
        result = C * 9 / 5 + 32
    else:
        result = (C + 273.15) * 9 / 5

    print(f"{result:.2f}")
main()
