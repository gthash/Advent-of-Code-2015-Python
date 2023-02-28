
import functools

def main():
    with open("input.txt") as file:
        count = 0
        for line in file:
            numArray = [int(num) for num in line.split("x")]
            numArray.sort()
            count += functools.reduce(lambda a, b: a * b, numArray)
            count += 2 * (numArray[0] + numArray[1])
    print(count)         

if __name__ == "__main__":
    main()
    
