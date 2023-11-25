def main():
    tank_amount = fuel()
    #taqueria()
    print(tank_amount)

def fuel_main():
    fraction = input("Fraction [x/x]:")
    gague = tank_status(fraction)

def fuel():
    tank = float(tank_status()) * 100
    if tank <= 1:
        return 'E'
    elif tank >= 99:
        return 'F'
    else:
        return (str(int(tank)) + "%")

def tank_status(fraction):
    nums = fraction.split("/")
    try:
        gas = int(nums[0]) / int(nums[1])
    except: 
        print("That's not a proper fraction")
        fuel_main()
    
    if gas <= 1:
        return f'{gas:.2f}'
    else:
        print("Can't overfill your gas tank")

    fuel_main()
    
def taqueria():
    while True :
        item = input("Item: ")
    # I guess I never finished problem set 3 


if __name__ == "__main__":
    main() 