import cs50

text = cs50.get_string("Text: ")
s = 0
l = 0
w = 1

for i in text:
    if (i == "!" or i == "?" or i == "."):
        s += 1
    elif (i == " "):
        w += 1
    elif ((i >= "a" and i <= "z") or (i >= "A" and i <= "Z")):
        l += 1

L = (l * 100)/ w
S = (s * 100)/ w

C_index = round(0.0588 * L - 0.296 * S - 15.8)

if (C_index >= 16):
    print("Grade 16+")
elif (C_index < 1):
    print("Before Grade 1")
else:
    print(f"Grade {C_index}")

