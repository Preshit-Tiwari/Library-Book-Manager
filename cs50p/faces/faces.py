def main():
    a = input()
    print(convert(a))

def convert(inp):
    inp = inp.replace(":)", "🙂")
    inp = inp.replace(":(", "🙁")
    return inp

main()
