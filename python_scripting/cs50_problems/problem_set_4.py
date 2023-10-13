import emoji
from pyfiglet import Figlet
import sys

# def main():
#     print("Which Program do you want to run?")
#     print("1: emojize")
#     print("q: exit")
#     which_func = input(">> ")
#     match which_func:
#         case '1':
#             emojize()
#         case '2': 
#             FIGlet()
#         case 'q' | 'Q':
#             return
#         case _:
#             print("Not a valid option")    
#     main()            

# def emojize():
#     e = input('What emoji do you want to see? ')
#     print(emoji.emojize(e))

def FIGlet():
    figlet = Figlet()

    if len(sys.argv) == 3:
        if sys.argv != ''
    else:    
        sys.exit("Invalid usage")
    phrase = input("Input: ")
    print(figlet.renderText(phrase))

FIGlet()
# if __name__ == "__main__":
#     main()