def main():
    f = open("../../inputfiles/intcode.txt")
    line = f.readline() 
    line = line.replace('\n', '')
    line = line.split(',')
    # line = [1,1,1,4,99,5,6,0,99]
    line[1] = 12
    line[2] = 2
    answer = runner(line)
    print('Answer is: {}'.format(answer))
    

def runner(input):
    outInput = input
    for i in range(len(outInput)):
        if(i % 4 == 0):
            current = int(outInput[i])
            if(current == 99):
                return outInput[0]
            indexOne = int(outInput[i + 1])
            indexTwo = int(outInput[i + 2])
            indexOut = int(outInput[i + 3])
            print('indexOne: {} indexTwo: {} indexOut: {}'.format(outInput[indexOne], outInput[indexTwo], current))
            if(indexOut < 0 or indexOut > len(outInput)):
                return 'error'
            if(current == 1):
                outInput[indexOut] = processAdd(outInput[indexOne], outInput[indexTwo])
            if(current == 2):
                outInput[indexOut] = processMultiply(outInput[indexOne], outInput[indexTwo])
            if(current != 1 and current != 2):
                return 0

def processMultiply(firstIn, secIn):
    return int(firstIn) * int(secIn)

def processAdd(firstIn, secIn):
    return int(firstIn) + int(secIn)

if __name__ == "__main__":
    main()