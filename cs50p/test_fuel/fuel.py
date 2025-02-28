def main():
    frac = input("Fraction: ")
    percentage = convert(frac)
    print(gauge(percentage))

def convert(fraction):
    x,y = fraction.split("/")
    x= int(x)
    y= int(y)
    if y == 0:
        raise ZeroDivisionError
    if x/y > 1:
        raise ValueError
    return round(x/y * 100)

def gauge(p):
    if p <= 1:
        return("E")
    elif p >= 99:
        return("F")
    else:
        return(f'{p}%')

if __name__ == "__main__":
    main()

