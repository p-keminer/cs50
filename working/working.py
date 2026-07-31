import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time := re.search(r"^([0-9]?[0-9]):?([0-9]{2})? (AM|PM) to ([0-9]?[0-9]):?([0-9]{2})? (AM|PM)$",s):
        hr1, min1, t1, hr2, min2, t2 = time.groups()
        if min1 is None: min1 = "00"
        if min2 is None: min2 = "00"
    else:
         raise ValueError


    if int(hr1) > 12 or int(hr2) > 12:
            raise ValueError
    elif int(min1) > 59 or int(min2) > 59:
            raise ValueError
    else:
          std1 = int(hr1); std2= int(hr2)
          if t1 == "PM" and std1 != 12:
                std1 +=12
          elif t1 == "AM" and std1 == 12:
                std1 = 0
          if t2 == "PM" and std2 != 12:
                std2 +=12
          elif t2 == "AM" and std2 == 12:
                std2 = 0
    time1 = f"{std1:02}:{min1}"; time2= f"{std2:02}:{min2}"

    return(f"{time1} to {time2}")




# h1 min1 t1 hr2 min2 t2
# -- 9:00 AM to 5:00 PM
# 9, 00, AM, 5, 00, PM

# -- 9 AM to 5 PM
# 9, None, AM, 5, None, PM

# -- 9:00 AM to 5 PM
# 9, 00, AM, 5, None, PM

# -- 9 AM to 5:00 PM
# 9, None, AM, 5, 00, PM


if __name__ == "__main__":
    main()
