"""
NumPy Indexing and Slicing
Exercise 2: Working with array indices and slices
Following MOOC.fi Data Analysis with Python course
"""

import numpy as np


def slice_array():
    """
    Create an array from 0 to 19 and return elements from index 5 to 15.
    
    Returns:
        numpy.ndarray: Sliced array
    """
    # TODO: Implement this function
    pass


def boolean_indexing():
    """
    Create an array from 0 to 9 and return only even numbers using boolean indexing.
    
    Returns:
        numpy.ndarray: Array of even numbers
    """
    # TODO: Implement this function
    pass


def reshape_array():
    """
    Create an array from 1 to 12 and reshape it to 3x4.
    
    Returns:
        numpy.ndarray: Reshaped array
    """
    # TODO: Implement this function
    pass


def main():
    """Main function to test the implementations."""
    print("Exercise 2: Indexing and Slicing")
    print("-" * 50)
    
    # Test slice_array
    sliced = slice_array()
    if sliced is not None:
        print(f"Sliced array: {sliced}")
    
    # Test boolean_indexing
    evens = boolean_indexing()
    if evens is not None:
        print(f"Even numbers: {evens}")
    
    # Test reshape_array
    reshaped = reshape_array()
    if reshaped is not None:
        print(f"Reshaped array:\n{reshaped}")


if __name__ == "__main__":
    main()
