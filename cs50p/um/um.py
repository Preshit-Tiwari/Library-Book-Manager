import re
import sys


def main():
    print(count(input("Text: ").strip()))


def count(s):
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    if matches:
        return len(matches)
    return 0


if __name__ == "__main__":
    main()
