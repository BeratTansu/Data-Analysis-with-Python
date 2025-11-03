"""
NumPy Array Basics
Exercise 1: Creating and manipulating NumPy arrays
Following MOOC.fi Data Analysis with Python course
"""

import numpy as np


def create_array():
    """
    Create a 1D NumPy array with integers from 0 to 9.
    
    Returns:
        numpy.ndarray: Array of integers
    """
    # TODO: Implement this function
    pass


def array_shape():
    """
    Create a 3x3 array filled with zeros.
    
    Returns:
        numpy.ndarray: 3x3 array of zeros
    """
    # TODO: Implement this function
    pass


def array_operations():
    """
    Perform basic operations on arrays.
    Create an array [1, 2, 3, 4, 5] and multiply each element by 2.
    
    Returns:
        numpy.ndarray: Result of the operation
    """
    # TODO: Implement this function
    pass


def main():
    """Main function to test the implementations."""
    print("Exercise 1: Creating and manipulating NumPy arrays")
    print("-" * 50)
    
    # Test create_array
    arr = create_array()
    if arr is not None:
        print(f"Array created: {arr}")
    
    # Test array_shape
    zeros = array_shape()
    if zeros is not None:
        print(f"Shape: {zeros.shape}")
        print(f"Zeros array:\n{zeros}")
    
    # Test array_operations
    result = array_operations()
    if result is not None:
        print(f"Operation result: {result}")


if __name__ == "__main__":
    main()
