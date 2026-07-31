input = str(input("whats the Answer to the great question…? "))
match input.lower().strip():
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
