from cs50 import get_float # for learning to import smth
from typing import Final # for "constants" better usage are enums


def main():
    print(calculate_change(ask_for_change()))


def ask_for_change():
    while True:
        change = input("Give me my change: $")
        try:
            change = float(change)  # for learning to handle invalid inputs
        except ValueError:
            print("Usage x.xx numerical")
        else:
            if change >= 0.00:
                print("0k, heres your change:", end="")
                break
            else:
                print("no negative change! :)")
    return change


def calculate_change(change):
    # dictionarys are like arrays
    COIN: Final = {"QUARTER":  25, "DIME": 10, "NICKEL": 5, "PENNY": 1}
    coins = {"quarters": 0, "dimes": 0, "nickels": 0, "pennys": 0}

    change = change*100 # for rounding fails

    while change >= COIN["QUARTER"]:
        coins["quarters"] += 1
        change -= COIN["QUARTER"]
    while change >= COIN["DIME"]:
        coins["dimes"] += 1
        change -= COIN["DIME"]  # like c algorh
    while change >= COIN["NICKEL"]:
        coins["nickels"] += 1
        change -= COIN["NICKEL"]
    while change >= COIN["PENNY"]:
        coins["pennys"] += 1
        change -= COIN["PENNY"]

    return sum(coins.values())  # keys = "..."  :X
 #gives back all values ^            values =    ^


main()
