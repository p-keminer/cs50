from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

allowed = figlet.getFonts()

if len(sys.argv) == 1:
    text = str(input("whats the text? "))
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(text))

elif len(sys.argv) == 3:
    if sys.argv[1] != '-f' and sys.argv[1] != '--font':
        sys.exit("invalid usage")
    elif sys.argv[2] not in figlet.getFonts():
        sys.exit("invalid usage")
    else:
        text = str(input("whats the text? "))
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))
else:
    sys.exit("invalid usage")
