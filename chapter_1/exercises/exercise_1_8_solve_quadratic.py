#%% exercise_1_8_solve_quadratic.py
# Solve quadratic (Exercise 1.8)
# Put this file into chapter_1/exercises and run it.
# Implements solve_quadratic(a, b, c) that returns a 2-tuple with both roots.

import math
import cmath
from typing import Tuple, Union

Number = Union[float, complex]

def solve_quadratic(a: float, b: float, c: float) -> Tuple[Number, Number]:
    """
    Return the two solutions of a*x^2 + b*x + c = 0 as a tuple (x1, x2),
    where x1 uses the '+' branch (-b + sqrt(d)) / (2a) and x2 uses the '-' branch.
    - If a == 0: raises ValueError (not a quadratic equation).
    - If discriminant >= 0: returns floats.
    - If discriminant < 0: returns complex numbers.
    """
    if a == 0:
        raise ValueError("Coefficient 'a' must not be zero for a quadratic equation")

    d = b * b - 4 * a * c  # discriminant

    # choose sqrt depending on sign of discriminant to keep floats when possible
    if d >= 0:
        sqrt_d = math.sqrt(d)
    else:
        sqrt_d = cmath.sqrt(d)

    x1 = (-b + sqrt_d) / (2 * a)
    x2 = (-b - sqrt_d) / (2 * a)

    # helper: if result is complex but imaginary part is effectively zero, convert to float
    def clean_value(x: Number) -> Number:
        if isinstance(x, complex):
            if abs(x.imag) < 1e-12:
                return float(x.real)
            return x
        else:
            return float(x)

    return (clean_value(x1), clean_value(x2))


def main():
    # Examples from the exercise
    print("Example 1: solve_quadratic(1, -3, 2) ->", solve_quadratic(1, -3, 2))
    print("Example 2: solve_quadratic(1, 2, 1) ->", solve_quadratic(1, 2, 1))

    # Extra examples (including complex roots)
    print("Extra: solve_quadratic(1, 0, 1) ->", solve_quadratic(1, 0, 1))   # complex: i and -i
    # double root example
    print("Double root: solve_quadratic(1, -2, 1) ->", solve_quadratic(1, -2, 1))  # (1.0, 1.0)

if __name__ == "__main__":
    main()