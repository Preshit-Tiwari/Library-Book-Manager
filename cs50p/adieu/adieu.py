import inflect
p = inflect.engine()

l = []
try:
    while(True):
        i = input("Name: ")
        l.append(i)
except EOFError:
    s = p.join(tuple(l))
    print("Adieu, adieu, to",s)
