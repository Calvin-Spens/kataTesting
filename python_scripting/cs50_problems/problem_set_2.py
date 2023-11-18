def main():
    #this calls the fuinctions of all problems
    #camel()
    #coke()
    #twttr()
    #plates()
    nutrition()


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
    if len(plate) < 2 or len(plate) > 6:
        print("Too long or too short")
        return False
    if plate[0].isdigit() | plate[1].isdigit():
        print("The first 2 characters must be letters")
        return False
    if not plate.isalnum():
        print("No special characters")
        return False
    for i in range(len(plate)):
        if plate[i].isdigit():
            if int(plate[i]) == 0:
                print("The first number can't be a 0")
                return False
            for j in range(i, len(plate)):
                if plate[j].isalpha():
                    print("Numbers must be at the end")
                    return False
            break 
    return True

def nutrition():
    fruit = input("Item: ")
    fruit_facts(fruit)

def fruit_facts(fruit):
    fruits = [
        {"Fruit": "Apple", "Callories": 130},
        {"Fruit": "Avocado", "Callories": 50},
        {"Fruit": "Banana", "Callories": 110},
        {"Fruit": "Cantaloupe", "Callories": 50},
        {"Fruit": "Grapefruit", "Callories": 60},
        {"Fruit": "Grapes", "Callories": 90},
        {"Fruit": "Honeydew Melon", "Callories": 50},
        {"Fruit": "Kiwifruit", "Callories": 90},
        {"Fruit": "Lemon", "Callories": 15},
        {"Fruit": "Lime", "Callories": 20},
        {"Fruit": "Nectarine", "Callories": 60},
        {"Fruit": "Orange", "Callories": 80},
        {"Fruit": "Peach", "Callories": 60},
        {"Fruit": "Pear", "Callories": 100},
        {"Fruit": "Pineapple", "Callories": 50},
        {"Fruit": "Plums", "Callories": 70},
        {"Fruit": "Straberries", "Callories": 50},
        {"Fruit": "Sweet Cherries", "Callories": 100},
        {"Fruit": "Tangerine", "Callories": 50},
        {"Fruit": "Watermelon", "Callories": 80}
    ]
    for i in fruits:
        if i["Fruit"] == fruit:
            print("Calories: " + str(i["Callories"]))


if __name__ == "__main__":
    main()
