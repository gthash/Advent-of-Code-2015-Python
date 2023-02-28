
def main():
    disallowedStr = {"ab", "cd", "pq", "xy"}
    alloVowels = {"a", "e", "i", "o", "u"}
    count = 0

    with open("input.txt") as file:
        for line in file:
            vowelCount, doubleLetter = 0, False
            for i in range(0, len(line) - 1):
                testStr = line[i : i + 2]
                if testStr not in disallowedStr:
                    if doubleLetter == False and testStr[0] == testStr[1]:
                        doubleLetter = True
                    if i % 2 == 0 and vowelCount < 3:
                        for j in range(0, 2):
                            if vowelCount < 3 and testStr[j] in alloVowels:
                                vowelCount += 1
                else:
                    doubleLetter = False; break
            if doubleLetter == True and vowelCount >= 3:
                count += 1    
    print(count)

if __name__ == "__main__":
    main()
    
