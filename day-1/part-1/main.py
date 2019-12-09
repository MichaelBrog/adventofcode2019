#Advent of code day 1
import math

def main():
    totalFuel = 0
    with open("../../inputfiles/fuel_input.txt") as f: 
        for line in f:
            line = line.replace('\n', '')
            line = math.floor(int(line) / 3) - 2
            totalFuel += line
    print(totalFuel)


    
if __name__ == "__main__":
    main()