import sys

def main():
    if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
        print(lines())
    elif len(sys.argv) == 2 and not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

def lines():
    try:
        n = 0
        with open(sys.argv[1]) as file:
            for line in file:
                if not(line.lstrip().startswith("#") or line.lstrip() == ""):
                    n+=1
        return n
    except FileNotFoundError:
        sys.exit("File do not exist!")

if __name__ == "__main__":
    main()
