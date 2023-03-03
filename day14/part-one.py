
import re

def reindeer_distance(speed, flying, rest):
    frequency, seconds = 0, 0   
    while (seconds <= 2503):
        frequency += 1
        seconds += rest if frequency % 2 == 0 else flying
    if frequency % 2 == 1:
        return (frequency - 1)/2 * flying * speed \
                    + (flying - (seconds - 2503)) * speed
    else:
        return frequency/2 * flying * speed

def main():
    distances = []
    with open("input.txt") as file:
        for line in file:
            distances.append(reindeer_distance(*[int(x) for x \
                                        in re.findall(r'\d+', line)]))

    print(max(distances))

if __name__ == "__main__":
    main()
    
