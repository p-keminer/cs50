import random

while True:
    try:
        zahl = int(input("Level: "))
        number = random.randint(1,zahl)
    except:
        print("", end="")
    else:
        break

while True:
    try:
        geraten = int(input("Guess: "))
    except EOFError:
        print("")
        break
    except ValueError:
        print("", end="")
    except:
        continue
    else:
        if geraten <= 0:
            print("", end="")
        elif geraten < number:
            print("Too small!")
        elif geraten > number:
            print("Too large!")
        else:
            print("Just right!")
            break

