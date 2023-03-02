
#           BASH SCRIPT TO PROCESS INPUT.TXT
# 
#           sed 's/lose /-/g;s/gain //g;s/\.//g' input.txt > temp.txt
#           awk '{printf $1" "$10" "$3"\n" > "proc.txt"}' temp.txt && rm temp.txt

from itertools import permutations

def main():
    names = [
                "Alice", "Bob", "Carol",
                "David", "Eric", "Frank", 
                "George", "Mallory"
            ]
    weights = {}
    with open("proc.txt") as file:
        for line in file:
            data_list = line.strip().split(" ")
            weights[(data_list[0], data_list[1])] = int(data_list[2])

    count, optimal_count = 0, 0

    for arrang in permutations(names):
        arrangement_list = [(arrang[i], arrang[i + 1]) for i in range(0, 7)] + \
                                [(arrang[i + 1], arrang[i]) for i in range(0, 7)] + \
                                [(arrang[7], arrang[0]), (arrang[0], arrang[7])]
        count = sum(map(weights.get, arrangement_list))    
        if count >= optimal_count:
            optimal_count = count

    print(optimal_count)

if __name__ == "__main__":
    main()
    
