def main():
    frac = input("Fraction: ")
    try:
        x,y = frac.split("/")
        x= int(x)
        y= int(y)
        if x/y <= 1:
            print(frac_to_perc(x,y))
        else:
            main()
    except Exception as e:
        main()

def frac_to_perc(a,b):
    p = round(a/b * 100)
    if p <= 1:
        return("E")
    elif p >= 99:
        return("F")
    else:
        return(f'{p}%')
        
if __name__ == "__main__":
    main()

