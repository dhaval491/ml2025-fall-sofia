import numpy as np


class KNNRegressor:
    def __init__(self, k):
        """Initialize k-NN regressor with given k."""
        self.k = k
        self.points = None  # will be a NumPy array of shape (N, 2)

    def add_points(self, xs, ys):
        """
        Store training points as a NumPy array.
        xs and ys are sequences of equal length.
        """
        xs_array = np.array(xs, dtype=float)
        ys_array = np.array(ys, dtype=float)
        self.points = np.column_stack((xs_array, ys_array))

    def predict(self, x_query):
        """
        Predict Y for the given X using k-NN regression.
        Uses Euclidean distance on the x-coordinate (1D).
        Returns the mean of Y values of the k nearest neighbors.
        """
        if self.points is None or self.points.shape[0] == 0:
            raise ValueError("No data points available for prediction.")

        x_vals = self.points[:, 0]
        y_vals = self.points[:, 1]

        # Compute distances between query and all x values
        distances = np.abs(x_vals - x_query)

        # Indices of k smallest distances
        knn_indices = np.argsort(distances)[:self.k]

        # Mean of the corresponding y values
        y_pred = np.mean(y_vals[knn_indices])
        return float(y_pred)


def main():
    # Read N
    try:
        N = int(input("Enter N (number of points): "))
        k = int(input("Enter k (number of neighbors): "))
    except ValueError:
        print("Error: N and k must be integers.")
        return

    if N <= 0 or k <= 0:
        print("Error: N and k must be positive integers.")
        return

    if k > N:
        print("Error: k cannot be greater than N.")
        return

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

    # Read query X
    try:
        X_query = float(input("Enter X to predict Y for: "))
    except ValueError:
        print("Error: X must be a real number.")
        return

    # Create k-NN regressor and perform prediction
    knn = KNNRegressor(k)
    knn.add_points(xs, ys)

    y_result = knn.predict(X_query)

    # Output the regression result
    print(y_result)


if __name__ == "__main__":
    main()

