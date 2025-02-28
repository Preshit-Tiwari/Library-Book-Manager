import random
import sys


def main():
    l = get_level()
    user_score = 0
    for i in range(10):
        r1 = generate_integer(l)
        r2 = generate_integer(l)
        result = r1 + r2
        chance = 3
        while(chance):
            try:
                user_ans = int(input(f"{r1} + {r2} = "))
            except ValueError:
                print("EEE")
                chance -= 1
            except EOFError:
                print()
                sys.exit()
            else:
                if user_ans != result:
                    print("EEE")
                    chance -= 1
                else:
                    break
        if chance == 0:
            print(f"{r1} + {r2} = {result}")
        else:
            user_score += 1
    print("Score:", user_score)

def get_level():
    while True:
        try:
            inp = int(input("Level: "))
            if inp in [1, 2, 3]:
                return inp
        except ValueError:
            pass
        except EOFError:
            print()
            sys.exit()

def generate_integer(level):
    if level not in [1, 2, 3]:
        raise(ValueError)
    if level == 1:
        return random.randint(0,9)
    return random.randint(10**(level-1), 10**level -1)

if __name__ == "__main__":
    main()
