import sys
import csv
import tabulate

def check_csv_file():
    try:
        test_file = sys.argv[1]
        open(test_file).close
    except IndexError:
        sys.exit("Too few comand-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")
    if len(sys.argv) > 3:
        sys.exit("Too many comand-line arguments")
    
    if not test_file.lower().endswith('.csv'):
        sys.exit("Not a CSV file")   

def main():
    check_csv_file()
    
    ...

if __name__ == "__main__":
    main()
