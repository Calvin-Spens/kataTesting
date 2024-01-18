import sys 

def main():
    try:
        test_file = sys.argv[1]
    except IndexError:
        sys.exit("Too few comand-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many comand-line arguments")
        
    try:
        file = open(test_file)
    except FileNotFoundError:
        print("File does not exist")
    file.close

    code_lines = get_line_num(test_file)

    print(code_lines)
    
def get_line_num(code_file):
    with open(code_file) as file:
        lines = file.readlines()
        non_blank = [line for line in lines if line.strip() != '']
        non_comment = [line for line in non_blank if not line.lstrip().startswith('#')]
        return len(non_comment)
    

if __name__ == "__main__":
    main() 