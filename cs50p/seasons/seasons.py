import inflect
p = inflect.engine()
from datetime import date,datetime
import sys

def main():
    inp = input("Date of Birth: ").strip()
    # op = date_to_minutes(inp)
    # print(p.number_to_words(op, andword="").capitalize(), "minutes")
    print(date_to_minutes(inp))

def date_to_minutes(inp):
    try:
        if date.fromisoformat(inp):
            ans = date.today() - datetime.strptime(inp, "%Y-%m-%d").date()
            # return(ans.days * 24 *60)
            op = ans.days * 24 *60
            return(p.number_to_words(op, andword="").capitalize() + " minutes")
        raise ValueError

    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
