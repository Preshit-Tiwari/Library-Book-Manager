a = input("Expression: ")
x, y, z = a.split(" ")
x, z = int(x),int(z)
if y == "*":
    print(float(x*z))
elif y == "+":
    print(float(x+z))
elif y == "-":
    print(float(x-z))
elif y == "/":
    print(float(x/z))
