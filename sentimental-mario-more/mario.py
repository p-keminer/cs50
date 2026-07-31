def main():
    draw_pyramid(get_int_between_1_and_8())


def get_int_between_1_and_8():
    while True:  # other logic cs do while dont exist
        height = input("Give me height between 1 and 8: ")
        try:   # for non numeric input and no crash
            height = int(height)  # following happening if int() is working
            if height >= 1 and height <= 8:
                break
            else:
                print("height must between 1 and 8: ")
        except:  # folowing happening if int() isnt working
            print("no numeric input, try again!")
    return height


def draw_pyramid(height):
    for i in range(height):  # for wants to get only number
        for line in range(height-1-i):
            print(" ", end="")  # everytime, we dont need an \n end=""
        for line in range(i+1):
            print("#", end="")  # logic is the same
        print("  ", end="")
        for line in range(i+1):
            print("#", end="")
        print("")   # dont forget to print \n


main()
