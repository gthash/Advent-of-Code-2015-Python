
def look_and_say(string):
    string += " "
    test_char, count, new_str = string[0], 0, '' 
    for char in string:
        if test_char == char:
            count += 1
        else:
            new_str += str(count) + test_char  
            test_char, count = char, 1
    return new_str

def main():
    las_str = "1113122113"
    for i in range(0, 40):
        las_str = look_and_say(las_str)
    
    print(len(las_str))

if __name__ == "__main__":
    main()
