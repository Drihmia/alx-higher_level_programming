#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str and roman_string.isalpha():
        s = roman_string
        count = 0
        r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)):
            if i > 0 and r.get(s[i - 1]) < r.get(s[i]):
                count += r.get(s[i]) - 2 * r.get(s[i - 1])
            else:
                count += r.get(s[i])
        return count
    else:
        return 0
