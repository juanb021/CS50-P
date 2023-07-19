import sys
import csv
from tabulate import tabulate

def main():
    # Get the information from the csv file.
    get_table(sys.argv[1])




def check_argv():

    # Check the ammount of elements in the argv.
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Check if the file is a CSV.
    if not ".csv" in sys.argv[1]:
        sys.exit("Not a CSV file")

def get_table(a):
    # Check the vality of the argv.
    check_argv()

    table = []

    try:
        with open(a) as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)

    # If the file doesnt Open, it doesnt exists.
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(table[1:], headers = table[0], tablefmt="grid"))



if __name__ == "__main__":
    main()