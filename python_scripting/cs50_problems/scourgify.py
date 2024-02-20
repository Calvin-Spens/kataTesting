import sys
import csv
import tabulate

def check_csv_file(test_file):
    try:
        open(test_file).close
    except FileNotFoundError:
        sys.exit("File does not exist")

    if not test_file.lower().endswith('.csv'):
        sys.exit("Not a CSV file")   

def main():
    try:
        check_csv_file(sys.argv[1])
        check_csv_file(sys.argv[2])
    except IndexError:
        sys.exit("Too few comand-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many comand-line arguments")

    name_house = sys.argv[1]
    first_last_house = sys.argv[2]

    with open(name_house) as file:
        reader = csv.DictReader(file)
        data = list(reader)

    for row in data:
        row['Last'], row['First'] = row.pop('name').split(', ', 1)

    fieldnames = ['First', 'Last', 'house']

    with open(first_last_house, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames= fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Modified data from {name_house} into {first_last_house}")



if __name__ == "__main__":
    main()
