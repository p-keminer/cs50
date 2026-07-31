import validators

email = str(input("email: ").strip())

if validators.email(email):
    print("Valid")
else:
    print("Invalid")
