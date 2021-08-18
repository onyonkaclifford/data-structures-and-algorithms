import copy
from typing import List


def insertion_sort(x: List) -> List:
    """ Insertion sort compares elements and moves them to their correct position by repeatedly comparing an element
    with previous elements in the list until its correct position is located, then moving the element to its correct
    position. It has an average time complexity of Θ(n^2) due to the nesting of its two loops. Time complexity for the
    worst case, when the list is sorted in reverse order, is O(n^2). Time complexity for the best case, when the list
    is already sorted in the correct order, is Ω(n).

    >>> insertion_sort([4, 2, 3, 1, 0, 5])
    [0, 1, 2, 3, 4, 5]

    :param x: list to be sorted
    :return: new sorted list
    """
    a_list = copy.deepcopy(x)  # To avoid modifying the original list
    length = len(a_list)

    for i in range(length):
        idx_to_insert_at = None

        for current_idx in range(i - 1, -1, -1):
            if a_list[current_idx] > a_list[i]:
                idx_to_insert_at = current_idx
            else:
                # The list upto the current_idx is fully sorted with elements less than the element at index i
                # The inner loop can thus be safely terminated, and the sorting process moved onto the next index
                break

        if idx_to_insert_at is not None:
            a_list.insert(idx_to_insert_at, a_list.pop(i))

    return a_list
