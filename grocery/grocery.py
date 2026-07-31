
items_dict = {}
while True:
    try:
        item = str(input())
        if item in items_dict:
            items_dict[item] += 1
        else:
            items_dict[item] = 1
    except EOFError:
        break
    else:
        continue

for keys in sorted(items_dict):
    print(f"{items_dict[keys]} {keys.upper()}")

