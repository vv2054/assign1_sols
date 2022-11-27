# Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

def swap_elements(arr, pos1, pos2):
    if pos1 == pos2:    # base-case: same positions
        return arr
    
    arr[pos1-1], arr[pos2-1] = arr[pos2-1], arr[pos1-1]   # swap first and last element
    return arr

# tests
input_1, pos1_1, pos2_1 = [23, 65, 19, 90], 1, 3
input_2, pos1_2, pos2_2 = [1, 2, 3, 4, 5], 2, 5
print('first testcase', swap_elements(input_1, pos1_1, pos2_1))
print('second testcase', swap_elements(input_2, pos1_2, pos2_2))