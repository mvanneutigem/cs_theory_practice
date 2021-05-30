

def binary_search(arr, value, start=None, end=None):
    """Search a sorted list of integers for a value using binary search.

    This function recursively checks whether the mid value of given array
    between start and end is larger or smaller than the value we're looking
    for. This way it can continue to half the search area until the correct 
    value is found.
    
    Args:
        arr (list): sorted list to search for value in.
        value (int): value to search for.
        start (int): start index to search list from.
        end (int): end index to search to list to.
    Returns:
        int: index of value if found.
    """
    if start is None:
        start = 0
    if end is None:
        end = len(arr) -1
        
    index = int((end - start)/2 + start)
    mid_value = arr[index]
    if mid_value == value:
        return index
    elif mid_value > value:
        return binary_search(arr, value, start, index)
    elif mid_value < value:
        return binary_search(arr, value, index, end)
