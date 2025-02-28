
import cs50

change = cs50.get_float("Change: ")
while(change < 0):
    change = cs50.get_float("Change: ")
coins = 0
change = int (100 * change)

coins += change // 25
change %= 25

coins += change // 10
change %= 10

coins += change // 5
change %= 5

coins += change

print(coins)
