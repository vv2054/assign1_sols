# Python | Find the length of a string without using len method

def length_of_list(arr):
    if not arr:    # base-case: if list is empty
        return 0
    
    for i, val in enumerate(arr):
        pass
    return i+1

# tests
input_1 = [23, 65, 19, 90]
input_2 = [1, 2, 3]
print('first testcase: ', input_1, length_of_list(input_1))
print('second testcase:', input_2, length_of_list(input_2))