#%% exercise_1_19_sum_equation.py
from typing import List


def sum_equation(nums: List[int]) -> str:
    """
    Return a string showing an equation of the sum of the elements in `nums`.

    Format examples:
      sum_equation([1, 5, 7]) -> "1 + 5 + 7 = 13"
      sum_equation([3]) -> "3 = 3"
      sum_equation([]) -> "0 = 0"

    The spacing around '+' and '=' matches exactly: " <num> + <num> + ... = <sum> ".
    """
    if not nums:
        return "0 = 0"

    parts = " + ".join(map(str, nums))
    total = sum(nums)
    return f"{parts} = {total}"


def _demo_checks():
    assert sum_equation([1, 5, 7]) == "1 + 5 + 7 = 13"
    assert sum_equation([3]) == "3 = 3"
    assert sum_equation([]) == "0 = 0"
    assert sum_equation([0, 0, 0]) == "0 + 0 + 0 = 0"
    assert sum_equation([10, 20, 30]) == "10 + 20 + 30 = 60"
    print("All basic checks passed.")


if __name__ == "__main__":
    _demo_checks()