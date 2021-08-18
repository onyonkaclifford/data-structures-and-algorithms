import copy
from typing import List


def bubble_sort(x: List) -> List:
    """ Bubble sort repeatedly compares adjacent elements and swaps those that are wrongly ordered. This process is
    repeated till the list is fully sorted. It has an average time complexity of Θ(n^2) due to the nesting of its two
    loops. Time complexity for the worst case, when the list is sorted in reverse order, is O(n^2). Time complexity for
    the best case, when the list is already sorted in the correct order, is Ω(n).

    >>> bubble_sort([4, 2, 3, 1, 0, 5])
    [0, 1, 2, 3, 4, 5]

    :param x: list to be sorted
    :return: new sorted list
    """
    a_list = copy.deepcopy(x)  # To avoid modifying the original list
    length = len(a_list)

    for _ in range(length - 1):
        swapped = False

        for current_idx in range(length - 1):
            next_idx = current_idx + 1

            if a_list[current_idx] > a_list[next_idx]:
                swapped = True
                a_list[current_idx], a_list[next_idx] = a_list[next_idx], a_list[current_idx]

        # If no swap takes place, it means that the list is fully sorted
        # The remaining loops can therefore be safely ignored
        if not swapped:
            break

    return a_list
