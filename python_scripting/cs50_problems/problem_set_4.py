import emoji
from pyfiglet import Figlet
import sys
import random

def main():
    print("Which Program do you want to run?")
    print("1: emojize")
    print("2: FIGlet")
    print("q: exit")
    which_func = input(">> ")
    match which_func:
        case '1':
            emojize()
        case '2': 
            FIGlet()
        case 'q' | 'Q':
            return
        case _:
            print("Not a valid option")    
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

if __name__ == "__main__":
    main()