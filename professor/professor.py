import random
import sys

def main():

    level = get_level()
    right = 0
    for _ in range(10):
        x,y = generate_integer(level),generate_integer(level)
        counter = 0
        while True:
            try:
                antwort = input(f"{x} + {y} = ")
            except EOFError:
                print("")
                sys.exit()
            else:
                if str(antwort) != str(x + y):
                    print("EEE")
                    counter += 1
                    if counter == 3:
                        print(f"{x} + {y} = {x+y}")
                        counter = 0
                        break
                    else:
                        continue
                else:
                    right +=1
                    break
    print("Score: " + str(right))

def get_level():
   while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
            else:
               continue
        except EOFError:
            print("")
            sys.exit()
        except:
            print("", end="")



def generate_integer(level):
    match level:
            case 1:   return random.randint(0,9)
            case 2:   return random.randint(10,99)
            case 3:   return random.randint(100,999)


if __name__ == "__main__":
    main()
