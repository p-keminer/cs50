input = str(input("say arithemtik formula: "))
if input.count("+") == 1:
    x = float(input.strip().split("+")[0])
    y = float(input.strip().split("+")[1])
    print(x + y)
elif input.count("-") == 1:
    x = float(input.strip().split("-")[0])
    y = float(input.strip().split("-")[1])
    print(x - y)
elif input.count("*") == 1:
    x = float(input.strip().split("*")[0])
    y = float(input.strip().split("*")[1])
    print(x * y)
elif input.count("/") == 1:
    x = float(input.strip().split("/")[0])
    y = float(input.strip().split("/")[1])
    print(x / y)
