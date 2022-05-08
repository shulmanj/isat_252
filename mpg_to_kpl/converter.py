"""
    Convert MPG to KPL.
"""

def convert(mpg):
    step1 = mpg * 1.609344
    step2 = step1 * 0.2641720524
    return round(step2, 3)

def main():
    print("Please enter a valid mpg. Press 'q' to quit.")
    while True:
        try:
            print("MPG: ", end="")
            mpg = float(input())
            print(convert(mpg), "KPL") 
        except:
            break

if __name__ == "__main__":
    main()