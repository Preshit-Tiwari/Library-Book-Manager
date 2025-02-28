def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s)<= 6:
        if s[0:2].isalpha():
            l = None
            for i in range(len(s)):
                if s[i].isdigit():
                    l = i
                    break
            if (l == None) or (s[l] != '0' and s[l:].isdigit()):
                return True
    return False

main()
