def main():
    a = input("camelCase: ")
    print("snake_case:",snake_case(a))

def snake_case(s):
    ans = ""
    for i in s:
        if i.isalpha() and i.isupper() :
            ans = ans + "_"
            ans = ans + i.lower()
        else:
            ans += i
    return ans

main()
