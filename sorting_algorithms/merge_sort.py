from typing import List


def merge_sort(x: List) -> List:
    """ Merge sort repeatedly divides a list to smaller lists of single elements, then combines these lists to form a
    single sorted list of the original elements. It has an average time complexity of Θ(nlogn). Time complexity
    for the worst case is O(nlogn). Time complexity for the best case is Ω(nlogn).

    >>> merge_sort([4, 2, 3, 1, 0, 5])
    [0, 1, 2, 3, 4, 5]

    :param x: list to be sorted
    :return: list
    """
    if len(x) <= 1:
        return x

    left = []
    right = []
    for i, element in enumerate(x):
        left.append(element) if i < len(x)/2 else right.append(element)
    left = merge_sort(left)
    right = merge_sort(right)

    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    result.extend(left)
    result.extend(right)

    return result
