import re
import numpy as np

state_array = np.empty(shape=(2503, 9))
state_array.fill(0)
points = [0 for i in range(0, 9)]

def populate_array(speed, flying, rest, reindeer):
    count, index, distance = 1, 0, 0 
    while index < 2503:
        if count % (flying + 1) == 0:
            state_array[index: index + 1 + rest, reindeer] = distance
            index += rest; count += 1
        else:
            distance += speed; count += 1
            state_array[index, reindeer] = distance; index += 1

def main():
    with open("input.txt") as file:
        for _, line in enumerate(file):
            populate_array(*([int(x) for x in re.findall(r'\d+', line)] + [_]))

    for i in range(0, 2503):
        max_indexes = np.where(state_array[i] == np.max(state_array[i]))
        for j in max_indexes[0]:
            points[j] += 1 

    print(max(points))

if __name__ == "__main__":
    main()
        


