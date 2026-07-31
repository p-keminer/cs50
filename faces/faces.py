def convert(userinput):
    userinput = userinput.replace(":)","🙂")
    userinput = userinput.replace(":(","🙁")
    return userinput

def main():
    userinput = str(input("Enter your input: "))
    print(convert(userinput))

main()
