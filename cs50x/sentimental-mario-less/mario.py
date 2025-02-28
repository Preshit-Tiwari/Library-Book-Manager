import cs50

h = cs50.get_int("Height: ")
while( h < 1 or h > 8):
        h = cs50.get_int("Height: ")
for i in range(1,h+1):
    for j in range(h-i):
        print(" ", end = "")
    for j in range(i):
        print("#", end = "")
    print()

