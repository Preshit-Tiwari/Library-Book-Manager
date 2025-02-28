import sys
import tabulate

def main():
    if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
        table()
    elif len(sys.argv) == 2 and not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

def table():
    try:
        with open(sys.argv[1]) as file:
            l=[]
            for line in file:
                line = line.rstrip().split(",")
                l.append(line)
            print(tabulate.tabulate(l[1:],l[0], tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File do not exist!")

if __name__ == "__main__":
    main()
