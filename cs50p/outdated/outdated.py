def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    try:
        a = input("Date: ")
        a = a.strip()
        a.index("/")
        l = a.split("/")
        if len(l) == 3:
            if l[0].isdigit() and (1 <= int(l[0]) <= 12):
                m = int(l[0])
                if l[1].isdigit() and (1 <= int(l[1]) <= 31):
                    d = int(l[1])
                    if l[2].isdigit() and (1 <= int(l[2]) <= 9999 ):
                        y = int(l[2])
                        print(f"{y:04}-{m:02}-{d:02}")
                        return
        main()
    except Exception as e:
        l = a.split(" ")
        if len(l) == 3 and l[0] in months:
            m = months.index(l[0]) + 1
            if l[1][-1] == ',' and l[1][:-1].isdigit() and (1 <= int(l[1][:-1]) <= 31):
                d = int(l[1][:-1])
                if l[2].isdigit() and  (1 <= int(l[2]) <= 9999):
                    y = int(l[2])
                    print(f"{y:04}-{m:02}-{d:02}")
                    return
        main()

main()
