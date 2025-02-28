import re
import sys

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
     matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)
     if matches:
        for i in matches.groups():
            i = int(i)
            if not(0 <= i <= 255):
                return False
        return True
     return False

if __name__ == "__main__":
    main()
