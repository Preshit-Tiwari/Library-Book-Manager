import re
import sys

def main():
    print(parse(input("HTML: ").strip()))

def parse(s):
    matches = re.search(r'^<iframe.* src="http(?:s)?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)".*></iframe>$', s)
    if matches:
        return "https://youtu.be/" + matches.group(1)
    return None

if __name__ == "__main__":
    main()
