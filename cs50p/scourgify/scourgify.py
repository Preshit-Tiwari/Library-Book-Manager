import csv
import sys

def main():
    if len(sys.argv) == 3 and sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        rewrite()
    elif len(sys.argv) == 3 and (not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv")):
        sys.exit("Not a CSV file")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

def rewrite():
    try:
        newlist = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                l = row["name"].rstrip().split(", ")
                newlist.append({"first": l[1].lstrip(), "last": l[0], "house": row["house"]})
        #newlist =  sorted(newlist, key=lambda newlist: newlist["first"])
        with open(sys.argv[2], "w") as file:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(newlist)
    except FileNotFoundError:
        sys.exit("File do not exist!")

if __name__ == "__main__":
    main()
