def main():
    userinput = str(input("say time: "))
    time = convert(userinput)
    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    elif time >= 12.0 and time <= 13.0:
        print("lunch time")
    elif time >= 18.0 and time <= 19.0:
        print("dinner time")
    else:
        return

def convert(userinput):
    hour = float(userinput.strip().split(":")[0])
    mins = float(userinput.strip().split(":")[1])
    return (hour + mins/60)

if __name__ == "__main__":
    main()
