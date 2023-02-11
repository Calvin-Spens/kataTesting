def main():
    #this calls the fuinctions of all problems
    #camel()
    #coke()
    #twttr()
    plates()

def camel():
    name = input("Camel Case: ")
    snake = ""
    for i in name:
        if i.isupper():
            snake = snake + "_" + i.lower()
        else:
            snake = snake + i
    print(snake)

def coke():
    print("One coin at a time please:")
    cost = 50 
    while cost > 0:
        coin = int(input("Insert coin: "))
        match coin:
            case 25 | 10 | 5:
                cost = cost - coin
                if cost <= 0: break
                print("Amount due: " + str(cost))
            case _:
                print("Not a valid coin")
    print("Change due: " + str(cost * -1))

def twttr():
    input_long = input("Input: ")
    short_hand = ""
    for i in input_long:
        match i.lower():
            case "a" | "e" | "i" | "o" | "u":
                short_hand = short_hand
            case _ :  
                short_hand = short_hand + i 
    print("Output: " + short_hand)

def plates():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if len(plate) > 6 | len(plate) < 2:
        return False
    elif plate[0].isdigit() | plate[1].isdigit():
        return False
    else:
        return True


main()