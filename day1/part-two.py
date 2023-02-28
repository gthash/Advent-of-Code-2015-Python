
def main():
    count, index = 0, 0
    with open("input.txt") as file:
        line = file.readline().strip()
        for char in line:
            count += 1 if char == "(" else -1
            index += 1
            if count == -1:
                break
    print(index)

if __name__ == "__main__":
    main()
    
