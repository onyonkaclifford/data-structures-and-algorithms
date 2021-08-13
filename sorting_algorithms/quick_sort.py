import copy
from typing import List


def quick_sort(x: List) -> List:
    """ Quick sort repeatedly moves smaller elements left and larger elements right relative to a pivot till all
    elements are sorted. It has an average time complexity of Θ(nlogn). Time complexity for the worst case, when the
    pivot creates the most unbalanced divisions for all recursions, is O(n^2). Time complexity for the best case, when
    the median is always chosen as the pivot, is Ω(nlogn).

    >>> quick_sort([4, 2, 3, 1, 0, 5])
    [0, 1, 2, 3, 4, 5]

    :param x: list to be sorted
    :return: list
    """
    a_list = copy.deepcopy(x)  # To avoid modifying the original list

    def sort_helper(y: List, start_idx: int, stop_idx: int) -> None:
        """ Helper function to recursively sort the list

        :param y: list to be sorted
        :param start_idx: index at which sorting begins from
        :param stop_idx: index at which sorting stops
        """
        if start_idx < stop_idx:
            # ensure pivot is as close to the mid-point as possible while taking care of integer overflow
            pivot_idx = start_idx + int((stop_idx - start_idx)/2)
            pivot = y[pivot_idx]

            i = 0
            values_equal_to_pivot = 0
            while i <= stop_idx:
                if y[i] < pivot and i > pivot_idx:
                    y.insert(pivot_idx, y.pop(i))
                    pivot_idx += 1
                    i += 1
                elif y[i] > pivot and i < pivot_idx:
                    y.insert(pivot_idx, y.pop(i))
                    pivot_idx -= 1
                elif y[i] == pivot:
                    if i == pivot_idx:
                        i += 1
                        continue
                    y.insert(pivot_idx, y.pop(i))
                    values_equal_to_pivot += 1
                    if i < pivot_idx:
                        pivot_idx -= 1
                    else:
                        i += 1
                else:
                    i += 1

            sort_helper(y, start_idx, pivot_idx - 1)
            sort_helper(y, pivot_idx + values_equal_to_pivot + 1, stop_idx)

    sort_helper(a_list, 0, len(a_list) - 1)

    return a_list
