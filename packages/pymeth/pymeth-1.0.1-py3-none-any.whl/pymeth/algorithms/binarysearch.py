def binary_search(arr, target):
    """
    Perform binary search on a sorted list to find the target element.

    Args:
        arr (list): A sorted list of comparable elements.
        target: The element to search for in the list.

    Returns:
        int: The index of the target element in the list if found, -1 otherwise.

    Raises:
        ValueError: If the input list is not sorted.

    Example:
        >>> binary_search([1, 2, 3, 4, 5, 6], 4)
        3
        >>> binary_search([10, 20, 30, 40, 50], 25)
        -1
    """
    if not arr or sorted(arr) != arr:
        raise ValueError("Input list must be sorted")

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
