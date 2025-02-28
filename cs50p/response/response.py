import validators

def main():
    inp = input("What's your email address? ").strip()
    if (validators.email(inp)):
        print("valid")
    else:
        print("invalid")

if __name__ == "__main__":
    main()
