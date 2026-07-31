import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return last_are_decimal(s) and is_lenght_ok(s) and is_number_or_alpha(s) and two_chars_at_begin(s)

def is_lenght_ok(plate):
    return ((len(plate)) <= 6 and (len(plate)) >= 2)

def two_chars_at_begin(plate):
    for _ in range(2):
        if plate[_].isalpha():
            is_char = 1
        else:
            is_char = 0
            return 0
    return is_char

def is_number_or_alpha(plate):
    for _ in range(len(plate)):
        if plate[_] in string.punctuation:
            is_no_number_alpha = 0
            return 0
        else:
            is_no_number_alpha = 1
    return is_no_number_alpha

def last_are_decimal(plate):
    if any(char.isdecimal() for char in plate):
        for _ in range(len(plate)):
            if plate[_].isdecimal():
             return plate[_:].isdecimal() and plate[_] != "0"
    else:
        return 1

if __name__ == "__main__":
    main()

