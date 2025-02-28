import sys
from pyfiglet import Figlet
figlet = Figlet()

if (len(sys.argv) == 1):
    pass
elif (len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font" ) and (sys.argv[2] in figlet.getFonts())):
    figlet.setFont(font = sys.argv[2])
else:
    print("Invalid usage")
    sys.exit(2)
inp = input("Input: ")
print(figlet.renderText(inp))
