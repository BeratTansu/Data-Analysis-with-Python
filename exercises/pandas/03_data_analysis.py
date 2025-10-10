"""
Pandas Data Analysis
Exercise 3: Analyzing data with groupby, aggregations, and statistics
Following MOOC.fi Data Analysis with Python course
"""

import pandas as pd


def calculate_statistics():
    """
    Create a DataFrame with 'Product', 'Category', and 'Sales' columns.
    Calculate mean, median, and sum of Sales.
    
    Returns:
        dict: Dictionary with 'mean', 'median', 'sum' keys
    """
    # TODO: Implement this function
    data = {
        'Product': ['A', 'B', 'C', 'D', 'E'],
        'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics'],
        'Sales': [1000, 500, 1500, 800, 1200]
    }
    pass


def groupby_operations():
    """
    Using the same DataFrame as above, group by Category and calculate
    the total sales for each category.
    
    Returns:
        pandas.Series: Total sales by category
    """
    # TODO: Implement this function
    data = {
        'Product': ['A', 'B', 'C', 'D', 'E'],
        'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics'],
        'Sales': [1000, 500, 1500, 800, 1200]
    }
    pass


def sort_and_rank():
    """
    Using the same DataFrame, sort by Sales in descending order
    and add a 'Rank' column.
    
    Returns:
        pandas.DataFrame: Sorted dataframe with rank
    """
    # TODO: Implement this function
    data = {
        'Product': ['A', 'B', 'C', 'D', 'E'],
        'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics'],
        'Sales': [1000, 500, 1500, 800, 1200]
    }
    pass


def main():
    """Main function to test the implementations."""
    print("Exercise 3: Data Analysis")
    print("-" * 50)
    
    # Test calculate_statistics
    stats = calculate_statistics()
    if stats is not None:
        print("Statistics:")
        for key, value in stats.items():
            print(f"  {key}: {value}")
        print()
    
    # Test groupby_operations
    grouped = groupby_operations()
    if grouped is not None:
        print("Total sales by category:")
        print(grouped)
        print()
    
    # Test sort_and_rank
    ranked = sort_and_rank()
    if ranked is not None:
        print("Sorted and ranked data:")
        print(ranked)


if __name__ == "__main__":
    main()
