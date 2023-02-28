import re

def main():
    tickerTape = {  ('cats', '7'), 
                    ('samoyeds', '2'),
                    ('pomeranians', '3'),
                    ('akitas', '0'),
                    ('vizslas', '0'),
                    ('goldfish', '5'),
                    ('trees', '3'),
                    ('cars', '2'),
                    ('perfumes', '1'),
                    ('children', '3')       }

    with open("input.txt") as file:
        for line in file:
            result = {tuple(str.strip().split(": ")) for str 
                                in re.sub(r'^[^:]*:', '', line).split(",")}
            if result.issubset(tickerTape) == True:
                print(re.search(r'\d+', line[0:10]).group(0))

if __name__ == "__main__":
    main()
