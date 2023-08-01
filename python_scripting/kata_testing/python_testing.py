import math
def cubes(n):
    num = 0
    cube = int(n)
    for i in range(int(cube)):
        num = num + (cube - i)**3
    print(num)

def main():
    while True: 
        test = input("Number to test: ")
        if test == "q": break
        cubes(test)
    return print("Thanks!")

main()
