# Write a program that merges two dictionaries into one.

def merge_x(dict1, dict2):
    '''
    mergeing two dictonary in to one
    
    '''
    return {**dict1, **dict2} # using dictonary unpaking mehtod  to merge two dictonary



d1 = {"apple": "5kg",}
d2 = {"mango": "2kg"}

merged = merge_x(d1,d2)

print(merged)