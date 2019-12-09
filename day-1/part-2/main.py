#Advent of code day 2

import math

def main():
    totalFuel = 0
    with open("../../inputfiles/fuel_input.txt") as f: 
        for line in f:
            line = line.replace('\n', '')
            line = fuelAmount(line)
            fuel = line
            totalFuel += fuel
            print('totalFuel is: {}'.format(totalFuel))
            while fuel > 0:
                fuel = extraFuel(fuel)
                print('fuel : {}'.format(fuel))
                totalFuel += fuel
    print(totalFuel)


def fuelAmount(input): 
    return math.floor(int(input) / 3) - 2

def extraFuel(input):
    out = fuelAmount(input)
    return out if out > 0 else 0
if __name__ == "__main__":
    main()