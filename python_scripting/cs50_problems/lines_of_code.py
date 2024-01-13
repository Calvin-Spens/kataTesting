import sys 

def main():
    try:
        test_file = sys.argv[1]
    except IndexError:
        sys.exit("Too few comand-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many comand-line arguments")
        
    try:
        open(test_file, "r")
    except FileNotFoundError:
        print("File does not exist")
    
    lines = 

    print(test_file)

def get_line_num():
    ...

if __name__ == "__main__":
    main() 