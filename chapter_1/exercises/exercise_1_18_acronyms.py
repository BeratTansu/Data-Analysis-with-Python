# Exercise 1.18 (acronyms)

from typing import List

# Characters considered punctuation for simple .strip() cleanup
_PUNCT = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

def acronyms(text: str) -> List[str]:
    """
    Return a list of acronyms found in `text`.

    Rules implemented:
    - Split the text on whitespace.
    - For each token, remove leading/trailing punctuation using strip(_PUNCT).
      (This follows the exercise hint to use strip.)
    - A token is an acronym if:
        * its length is at least 2, and
        * every character is either an uppercase letter (ch.isupper()) or a digit (ch.isdigit()).
    - The function returns acronyms in the order they appear (duplicates preserved).
    """
    out: List[str] = []
    for tok in text.split():
        clean = tok.strip(_PUNCT)
        if len(clean) >= 2 and all((ch.isupper() or ch.isdigit()) for ch in clean):
            out.append(clean)
    return out


def main():
    example = (
        "For the purposes of the EU General Data Protection Regulation (GDPR), "
        "the controller of your personal information is International Business Machines Corporation (IBM Corp.), "
        "1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a "
        "subsidiary or its controls (not established in the European Economic Area (EEA)) is required to appoint a "
        "legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, "
        "North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."
    )

    print(acronyms(example))
    # Example asserts (basic, based on the exercise description)
    res = acronyms(example)
    # Check some expected acronyms are present (order and duplicates preserved)
    assert "EU" in res
    assert "GDPR" in res
    assert "IBM" in res
    assert "EEA" in res
    assert "PO" in res or "PO6" in res  # depends on punctuation splitting; both acceptable
    print("Basic checks passed.")


if __name__ == "__main__":
    main()