import emoji

def main():
    print("Which Program do you want to run?")
    print("1: emojize")
    program = input(">> ")
    match program:
        case '1':
            emojize()
        case _:
            print("Not a valid option")    
    return            

def emojize():
    e = input('What emoji do you want to see? ')
    print(emoji.emojize(e))

if __name__ == "__main__":
    main()