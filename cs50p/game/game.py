import random
import sys

def main():
    n = get_p_int("Level: ")
    ans = random.randint(1, n)
    while True:
        guess = get_p_int("Guess: ")
        if guess < ans:
            print("Too small!")
        elif guess > ans:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()

def get_p_int(prompt):
    while True:
        try:
            inp = int(input(prompt))
            if inp > 0:
                return inp
        except ValueError:
            pass

main()
