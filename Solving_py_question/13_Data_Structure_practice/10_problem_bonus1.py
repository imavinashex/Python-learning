# Write a program that takes a list of numbers and removes all duplicates using a set.


def remove_dublicate(numbers):
    
    '''
    Remove duplicates from a list using a set.

    Parameters:
        numbers (list): A list of integers or floats.

    Returns:
        list: A new list with duplicates removed.
    '''
    return list(set(numbers))


nums = [1,2,3,4,3,5,4]

print("original list ", (nums))

print("without Dublicate", remove_dublicate(nums))