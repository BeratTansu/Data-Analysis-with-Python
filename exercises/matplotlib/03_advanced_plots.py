"""
Matplotlib Advanced Plots
Exercise 3: Creating histograms, box plots, and heatmaps
Following MOOC.fi Data Analysis with Python course
"""

import matplotlib.pyplot as plt
import numpy as np


def histogram():
    """
    Create a histogram of 1000 random samples from a normal distribution.
    - Mean: 0
    - Standard deviation: 1
    - Bins: 30
    """
    # TODO: Implement this function
    np.random.seed(42)  # For reproducibility
    pass


def box_plot():
    """
    Create a box plot comparing three datasets:
    - Dataset 1: Normal distribution (mean=0, std=1)
    - Dataset 2: Normal distribution (mean=5, std=2)
    - Dataset 3: Normal distribution (mean=10, std=1.5)
    """
    # TODO: Implement this function
    np.random.seed(42)  # For reproducibility
    pass


def heatmap():
    """
    Create a heatmap of a 10x10 matrix of random values.
    Add a colorbar and labels.
    """
    # TODO: Implement this function
    np.random.seed(42)  # For reproducibility
    pass


def main():
    """Main function to test the implementations."""
    print("Exercise 3: Advanced Plots")
    print("-" * 50)
    print("Run each function to see the advanced plots.")
    print()
    
    # Uncomment to test individual functions:
    # histogram()
    # box_plot()
    # heatmap()


if __name__ == "__main__":
    main()
