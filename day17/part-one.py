
import numpy as np

def main():
    max_elem = int('11111111111111111111', 2)
    containers = np.array([33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18,
                           13, 50, 44, 48, 6, 24, 41, 30, 42 ])
    count = 0

    for i in range(0, max_elem + 1):
        result = sum(np.multiply(np.array((20 - len(bin(i)[2:])) * [0] + \
                                    [int(x) for x in bin(i)[2:]]), containers))
        if result == 150:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
    
