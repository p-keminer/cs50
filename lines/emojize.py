import emoji

emojize = str(input())
 #
if "earth" in emojize:
    print(emoji.emojize(emojize,language = "alias"))
elif "_" in emojize:
    print(emoji.emojize(emojize))
else:
    print(emoji.emojize(emojize,language = "alias"))
