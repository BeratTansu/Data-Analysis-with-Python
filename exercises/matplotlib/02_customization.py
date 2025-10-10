"""
Matplotlib Plot Customization
Exercise 2: Customizing plots with colors, styles, and markers
Following MOOC.fi Data Analysis with Python course
"""

import matplotlib.pyplot as plt
import numpy as np


def styled_plot():
    """
    Create a line plot with custom styling:
    - Line color: red
    - Line style: dashed
    - Line width: 2
    - Marker: 'o'
    """
    # TODO: Implement this function
    x = np.linspace(0, 10, 20)
    y = np.sin(x)
    pass


def subplots_example():
    """
    Create a figure with 2x2 subplots:
    - Top-left: sin(x)
    - Top-right: cos(x)
    - Bottom-left: tan(x)
    - Bottom-right: x^2
    """
    # TODO: Implement this function
    x = np.linspace(0, 2*np.pi, 100)
    pass


def bar_chart():
    """
    Create a bar chart showing sales data:
    Categories: ['Q1', 'Q2', 'Q3', 'Q4']
    Sales: [15000, 18000, 22000, 25000]
    """
    # TODO: Implement this function
    pass


def main():
    """Main function to test the implementations."""
    print("Exercise 2: Plot Customization")
    print("-" * 50)
    print("Run each function to see the customized plots.")
    print()
    
    # Uncomment to test individual functions:
    # styled_plot()
    # subplots_example()
    # bar_chart()


if __name__ == "__main__":
    main()
