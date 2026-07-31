import sys
import csv

pizzas=[]

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
#print(sys.argv[1])
elif sys.argv[1][-3:] != "csv" or sys.argv[2][-3:] != "csv":
    sys.exit("not both a csv file")
else:
    try:
        with open(sys.argv[1],"r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                pizzas.append({"name": row["name"], "house": row["house"]})

        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames = ["first","last","house"])
            writer.writeheader()

            for row in pizzas:
                last, first = row["name"].split(", ")
                writer.writerow({"first": first,"last": last, "house": row["house"]})
                #print(f"{first}, {last}, {row['house']}")

    except FileNotFoundError:
        sys.exit("file not found")
    except PermissionError:
        sys.exit("cant read file")
