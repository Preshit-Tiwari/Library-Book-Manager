import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    matches = re.search(r"(\d?\d):?(\d\d)? (AM|PM) to (\d?\d):?(\d\d)? (PM|AM)", s)
    if matches:
        l =[ 0 if i in [None, "AM", "PM"] else int(i) for i in matches.groups()]
        if (0 <= l[1] < 60 and 0 <= l[4] < 60 and 1 <= l[0] <= 12 and 1 <= l[3] <= 12):
            if matches.group(3) == "AM" and l[0] == 12:
                l[0] = 0
            if matches.group(3) == "PM" and l[0] < 12:
                l[0] += 12
            if matches.group(6) == "AM" and l[3] == 12:
                l[3] = 0
            if matches.group(6) == "PM" and l[3] < 12:
                l[3] += 12
            return f"{l[0]:02}:{l[1]:02} to {l[3]:02}:{l[4]:02}"
    raise ValueError

if __name__ == "__main__":
    main()
