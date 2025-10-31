#%% exercise_1_17_positive_list.py
# Exercise 1.17 (positive_list)
from typing import List

def positive_list(nums: List[float]) -> List[float]:
    """
    Return a new list containing only the positive numbers (> 0)
    from the input list `nums`. Uses filter() as required by the exercise.
    """
    return list(filter(lambda x: x > 0, nums))


def _demo():
    examples = [
        ([2, -2, 0, 1, -7], [2, 1]),
        ([], []),
        ([-1, -2, -3], []),
        ([0, 0.0, 0.1, 3.5], [0.1, 3.5]),
    ]

    for inp, expected in examples:
        out = positive_list(inp)
        print(f"positive_list({inp}) -> {out}  expected: {expected}")
        assert out == expected

    print("All demo asserts passed.")


def main():
    _demo()


if __name__ == "__main__":
    main()