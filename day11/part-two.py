import re
import string
import itertools

def increment_string(string, string_len):
    for i in range(string_len - 1, -1, -1):
        if string[i] != 'z':
            string = string[0:i] + chr(ord(string[i])+1) + string[i+1:]
            break
        else:
            string = string[0:i] + 'a' + string[i+1:]
            if i == 0:
                string = string + 'a'
    return string

def main():
    double_letters = {letter + letter for letter in string.ascii_lowercase}
    increasing_three = {string.ascii_lowercase[i:i+3] for i in range(0, 24)}
    condition = False
    str = "cqjxxyzz"

    while condition == False:
        str_len = len(str); str = increment_string(str, str_len)
        if re.search(r'[iol]', str) == None: 
            set_three = {str[i:i+3] for i in range(0, str_len - 2)}
            if set_three.isdisjoint(increasing_three) == False:
                set_two = {k for k, g in itertools.groupby(\
                                [str[i:i+2] for i in range(0, str_len - 1)])}
                if len(set_two.intersection(double_letters)) >= 2:
                    condition = True

    print(str)

if __name__ == "__main__":
    main()