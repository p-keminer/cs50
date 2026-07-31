import sys
from PIL import Image, ImageOps


if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].lower().endswith(("png","jpg","jpeg")) or not sys.argv[2].lower().endswith(("png","jpg","jpeg")):
    sys.exit("not both a jpg or png file")
    #print(f"{sys.argv[1][-3:]}, {sys.argv[2][-3:]}")
elif sys.argv[1][-3:] != sys.argv[2][-3:]:
    sys.exit("not both same fileending")
else:
    try:
        shirt = Image.open("shirt.png")
        foto = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("file not found")
    else:
        groesse = shirt.size
        foto = ImageOps.fit(foto, groesse)

        foto.paste(shirt,(0,0),shirt)
        foto.save(sys.argv[2])

