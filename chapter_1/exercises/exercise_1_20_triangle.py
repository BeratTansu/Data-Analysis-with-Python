#%% exercise_1_20_triangle.py
"""
triangle.py — simple geometry utilities for right-angled triangles.

Functions:
 - hypotenuse(a, b): return the length of the hypotenuse for a right-angled triangle
   with legs of length a and b.
 - area(a, b): return the area of a right-angled triangle with perpendicular sides a and b.

Module attributes:
 - __version__
 - __author__

This module is safe to import (no top-level side effects). When executed directly it runs a small demo.
"""

from math import hypot
from typing import Union

Number = Union[int, float]

__version__ = "0.1.0"
__author__ = "BeratTansu"

def hypotenuse(a: Number, b: Number) -> float:
    """
    Return the length of the hypotenuse for a right-angled triangle
    with legs of lengths `a` and `b`.

    Implementation note:
    - Uses math.hypot for numerical stability and clarity (equivalent to sqrt(a*a + b*b)).

    Example:
      hypotenuse(3, 4) -> 5.0
    """
    return float(hypot(a, b))


def area(a: Number, b: Number) -> float:
    """
    Return the area of a right-angled triangle whose two perpendicular sides
    have lengths `a` and `b`.

    Formula: (1/2) * a * b

    Example:
      area(3, 4) -> 6.0
    """
    return 0.5 * float(a) * float(b)


def _demo() -> None:
    """Internal demo used when module is run as a script."""
    examples = [
        (3, 4),
        (5, 12),
        (1.5, 2.0),
    ]
    for a, b in examples:
        print(f"sides: a={a}, b={b}")
        print(f"  hypotenuse(a,b) -> {hypotenuse(a, b)}")
        print(f"  area(a,b)       -> {area(a, b)}")
        print("-" * 40)


if __name__ == "__main__":
    _demo()