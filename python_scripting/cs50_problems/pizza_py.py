import sys
import csv
import tabulate

def check_file():
    try:
        test_file = sys.argv[1]
        open(test_file).close
    except IndexError:
        sys.exit("Too few comand-line arguments")
    except FileNotFoundError:
        sys.exit("File does not exist")
    if len(sys.argv) > 2:
        sys.exit("Too many comand-line arguments")
    
    if not test_file.lower().endswith('.csv'):
        sys.exit("Not a CSV file")   

def main():
    check_file()
    menu = []
    file_import = sys.argv[1]

    with open(file_import) as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        for row in reader:
            menu.append([
                row[header[0]], 
                row[header[1]], 
                row[header[2]]
            ])

    print(tabulate.tabulate(menu, headers=header, tablefmt="grid"))


if __name__ == "__main__":
    main()