
def main():
    count = 0
    with open("input.txt") as file:
        line = file.readline().strip()
        for char in line:
            count += 1 if char == "(" else -1
    print(count)

if __name__ == "__main__":
    main()
