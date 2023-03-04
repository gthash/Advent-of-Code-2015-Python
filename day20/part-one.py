
from sympy import divisors

def main():
    count, presents = 0, 0
    while presents < 33100000:
        count += 1; presents = 0        
        for divisor in divisors(count):
            presents += 10 * divisor

    print(count)

if __name__ == "__main__":
    main()
    
