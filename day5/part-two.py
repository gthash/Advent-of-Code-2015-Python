
def main():
    count = 0
    
    with open("input.txt") as file:
        for line in file:
            verifyState, verifyThree = False, False
            for i in range(0, len(line) - 2):
                testStr = line[i : i + 2]
                if verifyThree == False and testStr[0] == (line[i : i + 3])[-1]:
                    verifyThree = True
                if verifyState == False:
                    for j in range(i + 2, len(line) - 1):
                        if testStr == line[j : j + 2]:
                            verifyState = True; break
                if verifyState == True and verifyThree == True:
                    count += 1; break
    print(count)

if __name__ == "__main__":
    main()
    
