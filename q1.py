# Given a list, write a Python program to swap first and last element of the list.

def swap_first_last(arr):
    if len(arr) < 2:    # base-case: length of input array less than 2, return the same array
        return arr
    
    arr[0], arr[-1] = arr[-1], arr[0]   # swap first and last element
    return arr

# tests
input_1 = [12, 35, 9, 56, 24]
input_2 = [1, 2, 3]
print('first testcase', swap_first_last(input_1))
print('second testcase', swap_first_last(input_2))