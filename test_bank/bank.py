def main():
    greeting = str(input("dont say hello: "))
    value(greeting)

def value(greeting):
    if greeting.lower().strip().split(",")[0] == "hello": #strip takes space [0] for first word in string
        print("$0")
        return 0
    elif greeting.lower().strip()[0] == "h": #[0] for first char in string
        print("$20")
        return 20
    else:
        print("$100")
        return 100

if __name__ == "__main__":
    main()
