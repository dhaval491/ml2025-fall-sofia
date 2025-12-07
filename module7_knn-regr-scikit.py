import numpy as np
from sklearn.neighbors import KNeighborsRegressor


def main():
    # Read N and k
    try:
        N = int(input("Enter N (number of points): "))
        k = int(input("Enter k (number of neighbors): "))
    except ValueError:
        print("Error: N and k must be integers.")
        return

    if N <= 0 or k <= 0:
        print("Error: N and k must be positive integers.")
        return

    # Read N (x, y) points
    xs = []
    ys = []

    print(f"Enter {N} points (x then y, as real numbers):")
    for i in range(N):
        try:
            x = float(input())
            y = float(input())
        except ValueError:
            print("Error: x and y must be real numbers.")
            return
        xs.append(x)
        ys.append(y)

    # Convert to NumPy arrays
    X_train = np.array(xs, dtype=float).reshape(-1, 1)  # shape (N, 1)
    y_train = np.array(ys, dtype=float)                 # shape (N,)

    # Compute variance of labels in the training dataset
    y_variance = np.var(y_train)  # population variance (ddof=0)

    # Read query X
    try:
        X_query = float(input("Enter X to predict Y for: "))
    except ValueError:
        print("Error: X must be a real number.")
        print("Variance of labels in training data:", y_variance)
        return

    if k > N:
        print("Error: k cannot be greater than N.")
        print("Variance of labels in training data:", y_variance)
        return

    # Create and fit k-NN regressor using scikit-learn
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train, y_train)

    # Predict Y for the given X
    y_pred = knn.predict(np.array([[X_query]]))[0]

    # Output the regression result and variance
    print("Predicted Y:", y_pred)
    print("Variance of labels in training data:", y_variance)


if __name__ == "__main__":
    main()

