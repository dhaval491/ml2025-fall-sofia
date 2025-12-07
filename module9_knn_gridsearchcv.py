import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score


def read_positive_int(prompt):
    """Read a positive integer from input."""
    try:
        value = int(input(prompt))
    except ValueError:
        print("Error: value must be an integer.")
        exit(1)

    if value <= 0:
        print("Error: value must be a positive integer.")
        exit(1)

    return value


def read_dataset(num_samples, name):
    """
    Read num_samples pairs (x, y) from input.
    x: real number (feature), y: non-negative integer (class label).
    Returns: X (shape: [num_samples, 1]),_]()

