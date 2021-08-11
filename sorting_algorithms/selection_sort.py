import copy
from typing import List


def selection_sort(x: List) -> List:
    """ Selection sort repeatedly swaps the minimum element of a list with the left-most unsorted element. It has an
    average time complexity of Θ(n^2) due to the nesting of its two loops. Time complexity for the worst case, when the
    list is sorted in reverse order, is O(n^2). Time complexity for the best case, when the list is already sorted in
    the correct order, is Ω(n^2).

    >>> selection_sort([4, 2, 3, 1, 0, 5])
    [0, 1, 2, 3, 4, 5]

    :param x: list to be sorted
    :return: list
    """
    a_list = copy.deepcopy(x)  # To avoid modifying the original list
    length = len(a_list)

    for i in range(length):
        unsorted_min_idx = i

        for idx, element in enumerate(a_list[i:]):
            if element < a_list[unsorted_min_idx]:
                unsorted_min_idx += idx

        a_list[i], a_list[unsorted_min_idx] = a_list[unsorted_min_idx], a_list[i]

    return a_list
