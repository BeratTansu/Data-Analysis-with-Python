"""
Matplotlib Basic Plots
Exercise 1: Creating basic line and scatter plots
Following MOOC.fi Data Analysis with Python course
"""

import matplotlib.pyplot as plt
import numpy as np


def line_plot():
    """
    Create a simple line plot of y = x^2 for x in range [0, 10].
    Add title, x-label, and y-label.
    """
    # TODO: Implement this function
    pass


def scatter_plot():
    """
    Create a scatter plot with random data points.
    X: 20 random numbers between 0 and 10
    Y: 20 random numbers between 0 and 10
    """
    # TODO: Implement this function
    np.random.seed(42)  # For reproducibility
    pass


def multiple_lines():
    """
    Create a plot with multiple lines:
    - y = x
    - y = x^2
    - y = x^3
    Add a legend to distinguish the lines.
    """
    # TODO: Implement this function
    pass


def main():
    """Main function to test the implementations."""
    print("Exercise 1: Basic Plots")
    print("-" * 50)
    print("Run each function to see the plots.")
    print("Note: Plots will be displayed if running interactively.")
    print()
    
    # Uncomment to test individual functions:
    # line_plot()
    # scatter_plot()
    # multiple_lines()


if __name__ == "__main__":
    main()
