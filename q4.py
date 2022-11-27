# Define a function which takes dictionary as an argument and print sorted dictionary by key first
# and then a value

def sort_by_keys(dict):
    if not dict:    # base-case: if dict is empty
        return {}
    
    # NOTE: dictionary cannot be in a sorted order(Python<3.7)
    return {key: dict[key] for key in sorted(dict.keys())}

def sort_by_values(dt):
    if not dt:    # base-case: if dict is empty
        return {}
    

    return dict(sorted(dt.items(), key=lambda x:x[1]))
# tests
input_1 = {"python" : 5, "javascript" : 10, "c#": 9, "golang" : 3, "java" : 1}
print('first testcase sorted by keys: ', sort_by_keys(input_1))
print('first testcase sorted by values: ', sort_by_values(input_1))