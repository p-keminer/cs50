def main():
    text = str(input("Input: "))
    shorten(text)

def shorten(text):
    vocals = ["a","e","i","o","u","A","E","I","O","U"]

    for vocal in vocals:
        text = text.replace(vocal,"")
    print("output: " + text)
    return text

if __name__ == "__main__":
    main()
