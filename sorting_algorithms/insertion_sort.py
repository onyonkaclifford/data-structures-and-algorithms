import copy
from typing import List


def insertion_sort(x: List) -> List:
    """ Insertion sort compares elements and moves them to their correct position by repeatedly swapping an element
    with adjecent elements till it arrives at its correct position. It has an average time complexity of Θ(n^2) due to
    the nesting of its two loops. Time complexity for the worst case, when the list is sorted in reverse order, is
    O(n^2). Time complexity for the best case, when the list is already sorted in the correct order, is Ω(n).

    >>> insertion_sort([4, 2, 3, 1, 0, 5])
    [0, 1, 2, 3, 4, 5]

    :param x: list to be sorted
    :return: list
    """
    a_list = copy.deepcopy(x)  # To avoid modifying the original list
    length = len(a_list)

    for i in range(length):
        for current_idx in range(i, 0, -1):
            swapped = False
            previous_index = current_idx - 1

            if a_list[current_idx] < a_list[previous_index]:
                swapped = True
                a_list[current_idx], a_list[previous_index] = a_list[previous_index], a_list[current_idx]

            # If no swap takes place, it means that the list upto the current index is fully sorted
            # The inner loop can therefore be safely terminated, and the sorting process moved onto the next index
            if not swapped:
                break

    return a_list
