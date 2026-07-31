import sys
from tabulate import tabulate
import csv

pizzas=[]

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
#print(sys.argv[1])
elif sys.argv[1][-3:] != "csv":
    sys.exit("not a csv file")
else:
    try:
        with open(sys.argv[1],"r") as file:
            reader = csv.reader(file)
            header = next(reader)
            print(tabulate(reader, header, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("file not found")

