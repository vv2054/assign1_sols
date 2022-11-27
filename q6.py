# Define a function to convert number to words for upto four digit. Note that you can use any package or library.
# Every word should be defined by you

def int2_word(num):
    if not num: # base-case: if empty
        return 'zero'
    
    ground_words = {1:'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
        20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
    res = []
    if 1000 <= num <= 9999:
        res.append(ground_words[num//1000])
        res.append('thousand')
        num = num%1000
    if 100 <= num <= 999:
        res.append(ground_words[num//100])
        res.append('hundred')
        num = num%100
    if 20 <= num <= 99:
        res.append(ground_words[num-num%10])
        num = num%10
    if 0 < num < 20:
        res.append(ground_words[num])

    return ' '.join(res)

input = 5
print("int to word: testcase 1: ", input, int2_word(input))
input = 999
print("int to word: testcase 2: ", input, int2_word(input))
input = 9992
print("int to word: testcase 3: ", input, int2_word(input))
