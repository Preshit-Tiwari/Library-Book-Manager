def main():
    a = input("What time is it? ")
    t = convert(a)
    if t >= 7 and t <= 8:
        print("breakfast time")
    elif t >= 12 and t <= 13:
        print("lunch time")
    elif t >= 18 and t <= 19:
        print("dinner time")


def convert(time):
    x, y= time.split(":")
    return int(x) + int(y)/60


if __name__ == "__main__":
    main()
