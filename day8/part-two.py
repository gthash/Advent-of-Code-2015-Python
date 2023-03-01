
def main():
    count = 0
    with open ("input.txt", "r") as file:
        for line in file:
            count += len(line.strip().replace("\\", r"\\") \
                        .replace('"', '\\"')) + 2 - len(line.strip()) 
    print(count)
                
if __name__ == "__main__":
    main()
    

