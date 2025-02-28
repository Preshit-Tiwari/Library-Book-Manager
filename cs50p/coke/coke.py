a_due = 50
a_inp = 0
while(a_inp < a_due):
    print("Amount Due:", a_due - a_inp)
    inp = int(input("Insert Coin: "))
    if inp in [25,10,5]:
        a_inp += inp
print("Change Owed:", a_inp - a_due)
