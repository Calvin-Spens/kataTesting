def deep():
    life = input("What is the meaning of life? ").lower()
    match life:
        case '42' | 'forty two' | 'fourty-two':
            print("You are correct")
        case _:
            print("Nope")
    return 

def bank():
    greet = input("Please enter a greeting: ").split()
    if greet[0].lower() == "hello":
        print("$0")
    elif greet[0][0].lower() == "h":
        print("$20")
    else:
        print('$100')
    return

def extensions():
    file = input("Enter the file name: ").split(".")
    if len(file) == 1:
        print("application/octet-stream")
        return
    match file[-1]:
        case 'gif' | 'png':
            print("image/"+file[-1])
        case 'jpg' | 'jpeg':
            print("image/jpeg")
        case 'pdf' | 'zip':
            print("application/"+file[-1])
        case 'txt':
            print("text/plain")
        case _:
            print("application/octet-stream")    
    return                

def interpreter():
    math = eval(input("Expression: "))
    print(f'{math:.2f}')
    return

def meal():
    time = input("What time is it? ")
    int_time = convert(time)
    match int_time:
        case int_time if 7 <= int_time <= 8:
            print("breakfast time")
        case int_time if 12 <= int_time <= 13:
            print("lunch time")
        case int_time if 18 <= int_time <= 19:
            print("dinner time")
        case _:
            return
    return


def convert(time):
    return(int(time.split(":")[0])+(int(time.split(":")[1]) / 60))


meal()
interpreter()    
extensions()
deep()
bank()