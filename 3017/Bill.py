"""doc"""
def main():
    """doc"""
    total = int(input())
    service_charge = total * 0.1
    if service_charge < 50:
        service_charge = 50
    elif service_charge > 1000:
        service_charge = 1000
    total_food = total + service_charge
    vat = total_food * 0.07
    print(f"{total_food + vat:.2f}")

main()
