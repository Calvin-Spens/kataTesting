def main():
    fuel_main()
    
def fuel_main():
    percent = 2
    while float(percent) > 1: 
        fraction = input("Fraction [x/x]:")
        percent = tank_status(fraction)
    tank_amount = fuel(float(percent)*100)
    print(tank_amount)

def fuel(pcent):
    if float(pcent) <= 1:
        return 'E'
    elif float(pcent) >= 99:
        return 'F'
    else:
        return (str(int(pcent)) + "%")

def tank_status(fraction):
    nums = fraction.split("/")
    try:
        gas = int(nums[0]) / int(nums[1])
    except (ValueError, ZeroDivisionError):
        gas = 2
        return gas
    
    if gas <= 1:
        return f'{gas:.2f}'
    else:
        return gas
    
def taqueria():
    while True :
        item = input("Item: ")
    # I guess I never finished problem set 3 


if __name__ == "__main__":
    main() 