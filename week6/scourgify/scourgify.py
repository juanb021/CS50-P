import sys
import csv

def main():
    csv_editor()

def check_argv():

    # Check the ammount of elements in the argv.
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Check if the file is a CSV.
    if not ".csv" in sys.argv[1]:
        sys.exit("Not a CSV file")

def csv_editor():
    # Check the argv.
    check_argv()
    output = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                split_name = row["name"].split(',')
                output.append({'first': split_name[1].lstrip(), 'last': split_name[0], 'house': row["house"]})


    except FileNotFoundError:
        sys.exit("File does not exist")

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        writer.writerow({'first': 'first', 'last': 'last', 'house': 'house'})
        for row in output:
            writer.writerow({'first': row['first'], 'last': row['last'], 'house': row['house']})


if __name__ == "__main__":
    main()