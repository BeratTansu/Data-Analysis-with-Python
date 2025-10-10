"""
NumPy Mathematical Operations
Exercise 3: Statistical and mathematical operations on arrays
Following MOOC.fi Data Analysis with Python course
"""

import numpy as np


def array_statistics():
    """
    Create an array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and calculate:
    - Mean
    - Median
    - Standard deviation
    
    Returns:
        tuple: (mean, median, std)
    """
    # TODO: Implement this function
    pass


def matrix_operations():
    """
    Create two 2x2 matrices and perform matrix multiplication.
    Matrix 1: [[1, 2], [3, 4]]
    Matrix 2: [[5, 6], [7, 8]]
    
    Returns:
        numpy.ndarray: Result of matrix multiplication
    """
    # TODO: Implement this function
    pass


def random_array_operations():
    """
    Create a random array of 100 elements and find:
    - Minimum value
    - Maximum value
    - Sum of all elements
    
    Returns:
        tuple: (min, max, sum)
    """
    # TODO: Implement this function
    np.random.seed(42)  # For reproducibility
    pass


def main():
    """Main function to test the implementations."""
    print("Exercise 3: Mathematical Operations")
    print("-" * 50)
    
    # Test array_statistics
    stats = array_statistics()
    if stats is not None:
        mean, median, std = stats
        print(f"Mean: {mean}, Median: {median}, Std: {std}")
    
    # Test matrix_operations
    result = matrix_operations()
    if result is not None:
        print(f"Matrix multiplication result:\n{result}")
    
    # Test random_array_operations
    random_stats = random_array_operations()
    if random_stats is not None:
        min_val, max_val, sum_val = random_stats
        print(f"Min: {min_val}, Max: {max_val}, Sum: {sum_val}")


if __name__ == "__main__":
    main()
