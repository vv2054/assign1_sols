# 5.1: https://leetcode.com/problems/longest-substring-without-repeating-characters/

def length_of_longest_substring(s):
    if not s:   # base-case: if s is empty
        return 0
    
    visited_unrepeated = {}
    max_len = -float("inf")
    curr_len = 1

    for i in range(len(s)):
        ch = s[i]
        if ch in visited_unrepeated:
           max_len = max(max_len, i-visited_unrepeated[ch])
           visited_unrepeated[ch] = i
        else:
            visited_unrepeated[ch] = i
    max_len = max(max_len, curr_len)

    return max_len

input = "abcabcbb"
print("length_of_longest_substring: testcase 1: ", input, length_of_longest_substring(input))
input = "bbbbb"
print("length_of_longest_substring: testcase 2: ", input, length_of_longest_substring(input))
input = "pwwkew"
print("length_of_longest_substring: testcase 3: ", input, length_of_longest_substring(input))

# 5.2: https://leetcode.com/problems/integer-to-roman/

def int_to_roman(num):
    res = ""
    while(num >= 1000):
        num -= 1000
        res += "M"
    while(num >= 900):
        num -= 900
        res += "CM"
    while(num >= 500):
        num -= 500
        res += "D"
    while(num >= 400):
        num -= 400
        res += "CD"
    while(num >= 100):
        num -= 100
        res += "C"
    while(num >= 90):
        num -= 90
        res += "XC"
    while(num >= 50):
        num -= 50
        res += "L"
    while(num >= 40):
        num -= 40
        res += "XL"
    while(num >= 10):
        num -= 10
        res += "X"
    while(num >= 9):
        num -= 9
        res += "IX"
    while(num >= 5):
        num -= 5
        res += "V"
    while(num >= 4):
        num -= 4
        res += "IV"
    while(num >= 1):
        num -= 1
        res += "I"
    return res

input = 3
print("int to roman: testcase 1: ", input, int_to_roman(input))
input = 58
print("int to roman: testcase 2: ", input, int_to_roman(input))
input = 1994
print("int to roman: testcase 3: ", input, int_to_roman(input))

# 5.3: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

def letter_combinations(digits):
    if not digits:
        return []
    res = []
    mappings = {'2':'abc', '3': 'def', '4': 'ghi', '5':'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def combs(curr, s, res):
        if not s:
            res.append(curr)
        else:
            ch = s[0]
            for mapping in mappings[ch]:
                combs(curr+mapping, s[1:], res)
        
    combs('', digits, res)
    return res

input = "23"
print("letter combinations: testcase 1: ", input, letter_combinations(input))
input = ""
print("letter combinations: testcase 2: ", input, letter_combinations(input))
input = "2"
print("letter combinations: testcase 3: ", input, letter_combinations(input))
    

