import numpy as np
from sklearn.metrics import precision_score, recall_score


def main():
    # Read N
    try:
        N = int(input("Enter N (number of samples): "))
    except ValueError:
        print("Error: N must be an integer.")
        return

    if N <= 0:
        print("Error: N must be a positive integer.")
        return

    # Read N (x, y) pairs: x = true label, y = predicted label
    true_labels = []
    pred_labels = []

    print(f"Enter {N} pairs (x then y) where each is 0 or 1:")
    for i in range(N):
        try:
            x = int(input())
            y = int(input())
        except ValueError:
            print("Error: x and y must be integers 0 or 1.")
            return

        if x not in (0, 1) or y not in (0, 1):
            print("Error: x and y must each be either 0 or 1.")
            return

        true_labels.append(x)
        pred_labels.append(y)

    # Convert to NumPy arrays
    y_true = np.array(true_labels, dtype=int)
    y_pred = np.array(pred_labels, dtype=int)

    # Compute precision and recall using scikit-learn
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)

    # Output results
    print("Precision:", precision)
    print("Recall:", recall)


if __name__ == "__main__":
    main()

