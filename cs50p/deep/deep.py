a = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
a = a.strip()
if a == "42" or a.lower() == "forty-two" or a.lower() == "forty two":
    print("Yes")
else:
    print("No")
