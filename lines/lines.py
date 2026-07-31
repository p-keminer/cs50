import sys
count=0

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
#print(sys.argv[1])
elif sys.argv[1][-2:] != "py":
    sys.exit("not a python file")
else:
    try:
        with open(sys.argv[1],"r") as file:
            for line in file:
                if line.strip().startswith("#") or line.strip() == "":
                    count+=0
                else:
                    count +=1
    except FileNotFoundError:
        sys.exit("file not found")
print(count)
