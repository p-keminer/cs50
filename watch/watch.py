import re
import sys

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if html := re.search(r"^<iframe .*?src=\"([^\"]+)\".*?></iframe>$",s):
      print(html.groups(1))
      link = html.group(1)
      #print(link)
      if "youtube.com" in link:
          id = re.sub(r"https?://(:?www.)?youtube\.com/embed/","https://youtu.be/", link)
          return id

if __name__ == "__main__":
    main()
