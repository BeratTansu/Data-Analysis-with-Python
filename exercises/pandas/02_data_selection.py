"""
Pandas Data Selection and Filtering
Exercise 2: Selecting and filtering data in DataFrames
Following MOOC.fi Data Analysis with Python course
"""

import pandas as pd


def select_column():
    """
    Create a DataFrame with columns 'Name', 'Age', 'Salary'.
    Return only the 'Age' column as a Series.
    
    Returns:
        pandas.Series: The Age column
    """
    # TODO: Implement this function
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 28],
        'Salary': [50000, 60000, 70000, 80000, 55000]
    }
    pass


def filter_rows():
    """
    Using the same DataFrame as above, return rows where Age > 30.
    
    Returns:
        pandas.DataFrame: Filtered dataframe
    """
    # TODO: Implement this function
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 28],
        'Salary': [50000, 60000, 70000, 80000, 55000]
    }
    pass


def select_multiple_columns():
    """
    Using the same DataFrame, return only 'Name' and 'Salary' columns.
    
    Returns:
        pandas.DataFrame: DataFrame with selected columns
    """
    # TODO: Implement this function
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 28],
        'Salary': [50000, 60000, 70000, 80000, 55000]
    }
    pass


def main():
    """Main function to test the implementations."""
    print("Exercise 2: Data Selection and Filtering")
    print("-" * 50)
    
    # Test select_column
    age_series = select_column()
    if age_series is not None:
        print("Age column:")
        print(age_series)
        print()
    
    # Test filter_rows
    filtered = filter_rows()
    if filtered is not None:
        print("Rows where Age > 30:")
        print(filtered)
        print()
    
    # Test select_multiple_columns
    selected = select_multiple_columns()
    if selected is not None:
        print("Name and Salary columns:")
        print(selected)


if __name__ == "__main__":
    main()
