#%% exercise_1_15_two_dice_comprehension.py
# List-comprehension solution for "two dice" pairs that sum to a target.

from typing import List, Tuple

def two_dice_pairs_sum(target: int = 5) -> List[Tuple[int, int]]:
    """
    Return a list of (d1, d2) pairs for two dice (1..6) whose sum equals target,
    computed using a list comprehension.
    """
    return [(d1, d2) for d1 in range(1, 7) for d2 in range(1, 7) if d1 + d2 == target]


def main():
    pairs = two_dice_pairs_sum(5)
    # Print one pair per line as requested
    for p in pairs:
        print(p)

    # sanity check: for target 5 there are 4 ordered pairs
    assert len(pairs) == 4, f"expected 4 pairs for sum 5, got {len(pairs)}"


if __name__ == "__main__":
    main()