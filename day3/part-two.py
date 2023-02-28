
import numpy as np

def main():
    with open("input.txt") as file:
        line = file.readline().strip()
    gridMotion = {  '>': np.array([1, 0]), '<': np.array([-1, 0]),
                    '^': np.array([0, 1]), 'v': np.array([0, -1])    }
    gridState = {(0,0)}
    state, count = np.array([0, 0]), 1
    
    for i in range(0, len(line), 2):
        state = np.add(state, gridMotion[line[i]])
        if tuple(state) not in gridState:
            count += 1
            gridState.add(tuple(state))

    state = np.array([0, 0])    
    for i in range(1, len(line), 2):
        state = np.add(state, gridMotion[line[i]])
        if tuple(state) not in gridState:
            count += 1
            gridState.add(tuple(state))   

    print(count) 

if __name__ == "__main__":
    main()
    
