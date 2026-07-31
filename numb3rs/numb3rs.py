import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if numbers := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$",ip):
       for number in numbers.groups():
            #print(int(number))
            if int(number) > 255:
              return False
            elif (len(number) > 1 and number.startswith("0")):
              return False
            else:
              continue
       return True
    else:
       return False

if __name__ == "__main__":
    main()
