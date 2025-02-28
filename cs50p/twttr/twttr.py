def main():
    inp = input("Input: ")
    print("Output:",shorten(inp))
def shorten(a):
    s = ""
    for i in a:
        if i.lower() not in ["a","e","i","o","u"]:
            s += i
    return s

if __name__ == "__main__":
    main()
