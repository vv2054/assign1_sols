# Define a function to convert number to words for upto four digit. Note that you can use any package or library.
# Every word should be defined by you

from num2words import num2words

def int2_word(num):
    return num2words(num).replace(',', '').replace('-', ' ').replace('and ', '')

input = 5
print("int to word: testcase 1: ", input, int2_word(input))
input = 999
print("int to word: testcase 2: ", input, int2_word(input))
input = 9992
print("int to word: testcase 3: ", input, int2_word(input))
