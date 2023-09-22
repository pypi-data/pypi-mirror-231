"""K-Means clustering algorithm."""
import numpy as np


class KMeans:
    """K-Means class for clustering algorithm."""

    def __init__(self, n_clusters, max_iters=1000, tol=1e-5):
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.tol = tol
        self.centroids = None
        self.labels = None
        self.iter = 0

    def fit(self, X):
        """Fit the model to the data X."""
        n_samples, n_features = X.shape

        # Initialize centroids randomly
        idx = np.random.default_rng().choice(n_samples, self.n_clusters, replace=False)
        self.centroids = X[idx]

        for i in range(self.max_iters):
            self.iter = i
            # Assign each data point to the nearest centroid
            distances = self._calc_distances(X)
            self.labels = np.argmin(distances, axis=1)

            # Update centroids
            new_centroids = np.zeros((self.n_clusters, n_features))
            for j in range(self.n_clusters):
                new_centroids[j] = np.mean(X[self.labels == j], axis=0)

            # Check for convergence
            if np.sum(np.abs(new_centroids - self.centroids)) < self.tol:
                break

            self.centroids = new_centroids

    def predict(self, X):
        """Predict the closest cluster each sample in X belongs to."""
        distances = self._calc_distances(X)
        return np.argmin(distances, axis=1), distances, self.iter

    def _calc_distances(self, X):
        """Calculate the distances from each point to each centroid."""
        distances = np.zeros((X.shape[0], self.n_clusters))
        for i, centroid in enumerate(self.centroids):
            distances[:, i] = np.linalg.norm(X - centroid, axis=1)
        return distances
