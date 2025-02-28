import emoji

def main():
    inp = input("Input: ")
    print(emoji.emojize(f'Output: {inp}', language='alias'))

main()
