#%% exercise_1_11_interleave.py
# Exercise 1.11 (interleave)

from typing import Any, List, Sequence

def interleave(*lists: Sequence[Any]) -> List[Any]:
    """
    Interleave elements from the given lists and return a new list.

    Usage:
      interleave([1,2,3], [20,30,40], ['a','b','c'])
      -> [1, 20, 'a', 2, 30, 'b', 3, 40, 'c']

    The function accepts an arbitrary number of lists as parameters.
    For convenience, if the caller passes a single argument that is itself
    a sequence of sequences (e.g. interleave([[1,2],[3,4],...])) the inner
    sequences will be used as the input lists.

    All input lists must have equal length; otherwise ValueError is raised.

    Implementation note: uses zip(...) to get tuples of ith elements and
    a list comprehension to flatten them (zip + extend semantics).
    """
    # Allow calling interleave with a single argument that is a sequence of sequences:
    if len(lists) == 1 and isinstance(lists[0], Sequence) and \
       lists[0] and all(isinstance(x, Sequence) for x in lists[0]):
        lists = tuple(lists[0])  # type: ignore

    # If no lists provided, return empty list
    if not lists:
        return []

    # Ensure all inputs behave like sequences and have the same length
    try:
        lengths = [len(lst) for lst in lists]
    except TypeError:
        raise TypeError("All arguments must be sequence types (e.g. list or tuple)")

    if not all(length == lengths[0] for length in lengths):
        raise ValueError("All input lists must have the same length")

    # Use zip to iterate column-wise and flatten with a comprehension
    return [elem for group in zip(*lists) for elem in group]


#%% Demo / quick checks
def _demo():
    print("Demo interleave examples and internal checks:")

    a = [1, 2, 3]
    b = [20, 30, 40]
    c = ['a', 'b', 'c']
    print("interleave(a, b, c) ->", interleave(a, b, c))
    assert interleave(a, b, c) == [1, 20, 'a', 2, 30, 'b', 3, 40, 'c']

    # also accept single sequence-of-sequences
    nested = [[1,2,3], [20,30,40], ['a','b','c']]
    print("interleave(nested) ->", interleave(nested))
    assert interleave(nested) == interleave(a, b, c)

    # edge cases
    print("interleave() ->", interleave())              # []
    assert interleave() == []

    print("interleave([], [], []) ->", interleave([], [], []))  # []
    assert interleave([], [], []) == []

    # unequal lengths -> ValueError
    try:
        interleave([1,2], [3])
    except ValueError as e:
        print("Caught expected ValueError for unequal lengths:", e)

    print("All demo checks done.")


if __name__ == "__main__":
    _demo()