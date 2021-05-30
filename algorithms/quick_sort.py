

def quick_sort(arr, start=None, end=None):
    """Sort a list of integers in ascending order.

    This algorithm makes use of "partitioning", it recursively divides the
    array in groups based on a value selected from the array. Values
    below the selected value are on one side of it, the ones above it on the 
    other. then the process is repeated for each of these sides and so on.
    
    Args:
        arr (list): list to sort.
        start (int): start index to sort list from
        end (int): end index to sort to list to.
    """
    if start is None:
        start = 0
    if end is None:
        end = len(arr) -1

    pivot = partition(arr, start, end)
    if pivot == start:
        if start + 1 != end:
            quick_sort(arr, start+1, end)
    elif pivot == end:
        if start != end - 1:
            quick_sort(arr, start, end-1)
    else:
        if start != pivot -1:
            quick_sort(arr, start, pivot - 1)
        if pivot + 1 != end:
            quick_sort(arr, pivot + 1, end)


def partition(arr, start, end):
    """"Separate the given array in two chuncks, by selecting a "pivot"value and
    moving all values smaller than the pivot to one side of it, and the values
    bigger than it to the other side of it.
    
    Args:
        arr (list): list to partition.
        start (int): start index to partition.
        end (int): end index to partition.

    Returns:
        int: index of the pivot value after partitioning the list.
    """
    j = start+1
    pivot = arr[start]
    for i in range(start+1, end+1):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    # swap pivot to correct position
    arr[j - 1], arr[start] = arr[start], arr[j - 1]
    return j - 1


def main():
    """Example usage."""
    arr = [8, 4, 76, 23, 5, 78, 9, 5, 2]
    result = [2, 4, 5, 5, 8, 9, 23, 76, 78]
    quick_sort(arr)
    assert(result == arr)
