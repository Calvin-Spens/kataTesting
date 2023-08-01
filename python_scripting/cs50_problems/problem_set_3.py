def main():
    #fuel()
    taqueria()

def fuel():
    tank = float(tank_status()) * 100
    if tank <= 1:
        print('E')
    elif tank >= 99:
        print('F')
    else:
        print(str(int(tank)) + "%")

def tank_status():
     while True:
        fract = input("Fraction: ").split("/")
        try:
            gas = int(fract[0]) / int(fract[1])
        except: 
            print("That's not a proper fraction")
            continue
        if gas <= 1:
            return f'{gas:.2f}'
        print("Can't overfill your gas tank")

def taqueria():
    while True :
        item = input("Item: ")
        

    pass 

main()