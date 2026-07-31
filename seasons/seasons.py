from datetime import date
import sys
import inflect
p = inflect.engine()

def main():
    try:
        geburtstag = date.fromisoformat(str(input("geburtstag: ")))
    except ValueError:
        sys.exit("false format")
    else:
        print(sing_minutes(geburtstag))

def sing_minutes(geburtstag):

        #print(geburtstag)
        diff = date.today() - geburtstag
        #print(diff)
        #print(p.number_to_words(diff.days *24*60, andword=""))
        return f"{p.number_to_words(diff.days *24*60, andword="").capitalize()} minutes"

if __name__ == "__main__":
    main()
