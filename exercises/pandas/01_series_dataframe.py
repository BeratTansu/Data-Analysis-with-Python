"""
Pandas Series and DataFrame Basics
Exercise 1: Creating and working with Series and DataFrames
Following MOOC.fi Data Analysis with Python course
"""

import pandas as pd
import numpy as np


def create_series():
    """
    Create a Pandas Series with values [10, 20, 30, 40, 50]
    and custom index ['a', 'b', 'c', 'd', 'e'].
    
    Returns:
        pandas.Series: The created series
    """
    # TODO: Implement this function
    pass


def create_dataframe():
    """
    Create a DataFrame with the following data:
    Name: ['Alice', 'Bob', 'Charlie', 'David']
    Age: [25, 30, 35, 40]
    City: ['New York', 'Paris', 'London', 'Tokyo']
    
    Returns:
        pandas.DataFrame: The created dataframe
    """
    # TODO: Implement this function
    pass


def dataframe_info():
    """
    Create a DataFrame with 3 columns and 5 rows of random data.
    Return the shape, column names, and first 3 rows.
    
    Returns:
        tuple: (shape, columns, head)
    """
    # TODO: Implement this function
    np.random.seed(42)  # For reproducibility
    pass


def main():
    """Main function to test the implementations."""
    print("Exercise 1: Series and DataFrame Basics")
    print("-" * 50)
    
    # Test create_series
    series = create_series()
    if series is not None:
        print("Series created:")
        print(series)
        print()
    
    # Test create_dataframe
    df = create_dataframe()
    if df is not None:
        print("DataFrame created:")
        print(df)
        print()
    
    # Test dataframe_info
    info = dataframe_info()
    if info is not None:
        shape, columns, head = info
        print(f"Shape: {shape}")
        print(f"Columns: {columns}")
        print(f"First 3 rows:\n{head}")


if __name__ == "__main__":
    main()
