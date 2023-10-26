import emoji
from pyfiglet import Figlet
import sys
import random
import inflect

def main():
    print("Which Program do you want to run?")
    print("1: emojize")
    print("2: FIGlet")
    print("3: adieu")
    print("4: guess_game")
    print("q: exit")
    which_func = input(">> ")
    match which_func:
        case '1':
            emojize()
        case '2': 
            FIGlet()
        case '3':
            adieu()
        case '4':
            guess_game()
        case 'q' | 'Q':
            return
        case _:
            print("Not a valid option\n")    
    main()            

def emojize():
    e = input('What emoji do you want to see? ')
    print(emoji.emojize(e))

def FIGlet():
    figlet = Figlet()
    arg_list = input("Arguments: ")
    args = arg_list.split()
    print(len(args))
    if len(args) == 0:
        figlet = Figlet(font=random.choice(Figlet().getFonts()))
    else:
        match args[0]:
            case "-f" | "--font":
                if args[1] in Figlet().getFonts():
                    figlet = Figlet(font=args[1]) 
                else:
                    print("Invalid usage\n")
                    return
            case _:
                print("Invalid usage\n")
                return


    phrase = input("Input: ")
    print(figlet.renderText(phrase))
### This is how the actual problem is solved ###
# def FIGlet():
#     figlet = Figlet()
    
#     if len(sys.argv) == 1:
#         figlet = Figlet(font=random.choice(Figlet().getFonts()))
#     else:
#         match sys.argv[1]:
#             case "-f" | "--font":
#                 if sys.argv[2] in Figlet().getFonts():
#                     figlet = Figlet(font=sys.argv[2]) 
#                 else:
#                     sys.exit("Invalid usage")
#             case _:
#                 sys.exit("Invalid usage")


#     phrase = input("Input: ")
#     print(figlet.renderText(phrase))

def get_names():
    names = []
    print("Who do you want to bid Adieu to?")
    try:
        while True:
            name = input("")
            names.append(name)
    except EOFError:
        pass 

    return names

def adieu():
    p = inflect.engine()
    leavers = get_names()
    bye = p.join(leavers)
    print("Adieu, adieu, to", bye, "\n")

def guess_game():
    while True:
        try:
            high_num = int(input("Level: "))
            if high_num > 0:
                break
            else:
                pass
        except ValueError:
            pass

    ans = random.randint(1, high_num)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                pass
            elif guess > ans:
                print('Too large!')
            elif guess < ans:
                print('Too small!')
            else:
                print('Just right!\n')
                break
        except ValueError:
            pass

if __name__ == "__main__":
    main()