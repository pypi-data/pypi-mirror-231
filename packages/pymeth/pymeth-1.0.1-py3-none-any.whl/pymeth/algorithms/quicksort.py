def quick_sort(arr):
    """
    Sort a list using the quicksort algorithm.

    Args:
        arr (list): The list of comparable elements to be sorted.

    Returns:
        list: A new sorted list containing the elements from the input list.

    Example:
        >>> quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)