userinput = str(input("camelCase: "))

def find_indices(userinput):
    indices = []
    for idx in range(len(userinput)):
        if userinput[idx].isupper():
            indices.append(idx)
    return indices

def split_input(liste, userinput):
    parts = []
    prev_idx = 0
    for idx in liste:
        parts.append(userinput[prev_idx:idx])
        prev_idx = idx
    parts.append(userinput[prev_idx:])
    return parts

index = find_indices(userinput)
snakecase = "_".join(split_input(index, userinput))
print(snakecase.lower().strip())



