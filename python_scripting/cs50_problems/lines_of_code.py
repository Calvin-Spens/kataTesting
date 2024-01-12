import sys 

def main():
    try:
        test_file = sys.argv[1]
    except IndexError:
        sys.exit("Too few comand-line arguments")

    print(test_file)

def get_line_num():
    ...

if __name__ == "__main__":
    main() 