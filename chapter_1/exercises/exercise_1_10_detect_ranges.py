#%% exercise_1_10_detect_ranges.py
# Exercise 1.10 (detect ranges) - solved
# The function detect_ranges returns a new list where consecutive runs
# of integers are represented as tuples (start, end_exclusive).
# Single, non-consecutive numbers remain as integers.
#
# Example:
#   detect_ranges([2,5,4,8,12,6,7,10,13])
# returns:
#   [2, (4, 9), 10, (12, 14)]
#
# Notes:
# - The second element of a tuple is exclusive (consistent with range()).
# - Input is not modified. The function sorts the input internally.
# - Assumes elements do not appear multiple times in the input, but code
#   tolerates duplicates by removing them.

from typing import List, Union, Tuple

RangeOrInt = Union[int, Tuple[int, int]]

def detect_ranges(nums: List[int]) -> List[RangeOrInt]:
    """
    Transform nums into a list where consecutive integer runs of length >= 2
    are represented as (start, end_exclusive), and isolated numbers are kept as ints.

    Args:
        nums: list of integers (may be unsorted).

    Returns:
        A new list sorted ascending where consecutive runs are tuples.
    """
    if not nums:
        return []

    # Sort and remove duplicates (defensive)
    sorted_vals = sorted(set(nums))

    result: List[RangeOrInt] = []

    start = sorted_vals[0]
    prev = start

    for v in sorted_vals[1:]:
        if v == prev + 1:
            # continues current run
            prev = v
            continue
        else:
            # run ended at prev
            if prev > start:
                # run length >= 2 -> tuple with exclusive end
                result.append((start, prev + 1))
            else:
                # single number
                result.append(start)
            # start new run
            start = v
            prev = v

    # finalize last run
    if prev > start:
        result.append((start, prev + 1))
    else:
        result.append(start)

    return result


# Demo / quick tests
def _demo():
    examples = [
        [2,5,4,8,12,6,7,10,13],   # given in exercise
        [3,4,5,6],                # single long run -> (3,7)
        [1,3,5,7],                # no runs -> all singles
        [1,2,3,5,6,9],            # mixed runs and singles
        [],                       # empty input
        [4],                      # single element
        [1,2,2,3,4],              # duplicates present -> treat as 1,2,3,4 -> (1,5)
    ]

    for nums in examples:
        print("input:", nums)
        print("detect_ranges ->", detect_ranges(nums))
        print()

    # sanity checks matching expected behavior from the exercise:
    assert detect_ranges([2,5,4,8,12,6,7,10,13]) == [2, (4,9), 10, (12,14)]
    assert detect_ranges([3,4,5,6]) == [(3,7)]
    assert detect_ranges([1,3,5,7]) == [1,3,5,7]
    assert detect_ranges([]) == []
    print("All internal asserts passed.")


if __name__ == "__main__":
    _demo()