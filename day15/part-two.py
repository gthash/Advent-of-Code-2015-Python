
import numpy as np

def main():
    possibilities = np.array([[i, j, k, 100 - i - j - k]
                                                for i in range(0, 101)
                                                for j in range(0, 101 - i)
                                                for k in range(0, 101 - i - j)])

    properties = np.transpose(np.array([    [2, 0, -2, 0, 3],
                                            [0, 5, -3, 0, 3],
                                            [0, 0, 5, -1, 8],
                                            [0, -1, 0, 5, 8]    ]))
    greatest_score = 0

    for elements in possibilities:
        score, result = 1, 0
        if sum(np.multiply(elements, properties[4])) == 500:
            for i in range(0, 4):
                result = np.multiply(elements, properties[i]).sum()
                if result < 0:
                    break               
                score *= result
            if score >= greatest_score:
                greatest_score = score

    print(greatest_score)

if __name__ == "__main__":
    main()
    
    
