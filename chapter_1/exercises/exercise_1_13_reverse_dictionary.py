#%% exercise_1_13_reverse_dictionary.py
# Exercise 1.13 (reverse dictionary) - solved

from typing import Dict, List, Any


def reverse_dictionary(d: Dict[str, Any]) -> Dict[str, List[str]]:
    """
    Given a dictionary `d` that maps English words (keys) to Finnish words
    (values — each value may be a single string or a sequence/list of strings),
    return a new dictionary that maps each Finnish word to a list of English
    words that map to it.

    - Input is not modified.
    - If a value in `d` is a string it's treated as a single-item list.
    - The order of English words in each output list follows their first
      appearance when iterating the input dict.
    """
    rev: Dict[str, List[str]] = {}

    for eng, fins in d.items():
        # Normalize fins into an iterable of strings
        if isinstance(fins, str):
            fins_list = [fins]
        else:
            # Accept any iterable (list/tuple/etc.); convert to list to iterate safely
            fins_list = list(fins)

        for fin in fins_list:
            # append eng to the list for fin, creating the list if necessary
            if fin in rev:
                rev[fin].append(eng)
            else:
                rev[fin] = [eng]

    return rev


#%% Demo / quick checks
def _demo():
    print("=== Demo: reverse_dictionary ===")
    d = {
        "move": ["liikuttaa"],
        "hide": ["piilottaa", "salata"],
        "six": ["kuusi"],
        "fir": ["kuusi"],  # homonym: 'kuusi' corresponds to 'six' and 'fir'
        "single_str_value": "yksi",  # demonstrate single-string handling
    }
    print("input:", d)
    rev = reverse_dictionary(d)
    print("reversed:", rev)
    # Expected:
    # {
    #   'liikuttaa': ['move'],
    #   'piilottaa': ['hide'],
    #   'salata': ['hide'],
    #   'kuusi': ['six', 'fir'],
    #   'yksi': ['single_str_value']
    # }

    assert rev["liikuttaa"] == ["move"]
    assert set(rev["piilottaa"]) == {"hide"}
    assert rev["salata"] == ["hide"]
    assert rev["kuusi"] == ["six", "fir"]
    assert rev["yksi"] == ["single_str_value"]

    # Additional checks: empty input, non-list values, duplicate Finnish entries
    assert reverse_dictionary({}) == {}
    d2 = {"a": ["x", "y"], "b": "y", "c": ["x"]}
    assert reverse_dictionary(d2) == {"x": ["a", "c"], "y": ["a", "b"]}

    print("All demo asserts passed.")


if __name__ == "__main__":
    _demo()