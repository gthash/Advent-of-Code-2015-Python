
def main():
    with open("input.txt") as file:
        count = 0
        for line in file:
            numArray = [int(num) for num in line.split("x")]
            surfaceArray = [numArray[i] * numArray[j] for i in range(0, 3)
                                                      for j in range(i + 1, 3)]
            count += 2 * sum(surfaceArray) + min(surfaceArray)
    print(count)           
            
if __name__ == "__main__":
    main()
    
