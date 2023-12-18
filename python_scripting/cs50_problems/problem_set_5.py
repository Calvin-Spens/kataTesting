

def main():
    print("This program was created to practicve Unit testing")
    print("it therefore doesn't realy do anything")
    print("Run 'pytest test_set_5.py' to test this program")
    bank_main()
    
def shorten_main():    
    word = input("Phrase to be shortened: ")
    short_word = shorten(word)
    print(short_word)

def shorten(word):
    short_hand = ""
    for i in word:
        match i.lower():
            case "a" | "e" | "i" | "o" | "u":
                short_hand = short_hand
            case _ :  
                short_hand = short_hand + i 
    return short_hand

def bank_main():
    greeting = input("Please enter a greeting: ")
    print(bank(greeting))

def bank(greeting):
    greet = greeting.split()
    first_word = greet[0].lower()
    if first_word[:5] == "hello":
        amount = "$0"
    elif first_word[0][0] == "h":
        amount = "$20"
    else:
        amount = "$100"
    return amount

if __name__ == "__main__":
    main() 