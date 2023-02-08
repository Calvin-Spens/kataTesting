def deep():
    life = input("What is the meaning of life? ").lower()
    match life:
        case '42' | 'forty two' | 'fourty-two':
            print("You are correct")
        case _:
            print("Nope")

def bank():
    greet = input("Please enter a greeting: ").split()
    if greet[0].lower() == "hello":
        print("$0")
    elif greet[0][0].lower() == "h":
        print("$20")
    else:
        print('$100')



deep()
bank()