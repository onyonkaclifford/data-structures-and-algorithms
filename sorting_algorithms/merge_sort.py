from typing import List


def merge_sort(x: List) -> List:
    """ Merge sort divides a list into two smaller lists, and recursively repeats the process on the two smaller lists
    till lists of single elements are obtained. These smaller lists are then combined to form a single sorted list of
    the original elements. It has an average time complexity of Θ(nlogn). Time complexity for the worst case is
    O(nlogn). Time complexity for the best case is Ω(nlogn).

    >>> merge_sort([4, 2, 3, 1, 0, 5])
    [0, 1, 2, 3, 4, 5]

    :param x: list to be sorted
    :return: list
    """
    length = len(x)

    if length <= 1:
        return x

    mid_idx = length // 2
    left = merge_sort(x[0:mid_idx])
    right = merge_sort(x[mid_idx:length])

    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)

    return result
