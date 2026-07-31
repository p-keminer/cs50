allowed_months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    try:
        date = str(input("Date: "))
        if "/" in date:
           #print("erkannt / ")
           month, day, year = date.split("/")
           #month = int(month.strip())
           #day = int(day.strip())
           if int(month.strip()) <= 12 and int(day.strip()) <= 31:
                print(f"{year.strip()}-{month.strip().zfill(2)}-{day.strip().zfill(2)}")
           else:
               continue
        elif date[:3].isalpha() and "," in date:
           # print("erkannt alpha")
            month, day, year = date.split(" ")
            if int(day.strip(",")) <= 31:
                print(f"{year}-{allowed_months[month.title()]:02}-{day.strip(",").zfill(2)}")
            else:
                continue
        else:
            continue
    except EOFError:
        print("")
        break
    except ValueError:
        #print("value error")
        continue
    else:
        #print("passed")
        break

