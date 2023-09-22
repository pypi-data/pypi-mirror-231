import numpy as np


class KMedoids:

    def __init__(self, n_clusters, max_iters):
        self.clusters = n_clusters
        self.max_iter = max_iters
        self.medoids = None
        self.labels = None
        self.iter = 0

    def fit(self, X):
        # Initialize medoids with random data points
        self.medoids = X[np.random.choice(
            X.shape[0], self.clusters, replace=False)]

        for i in range(self.max_iter):
            self.iter = i
            # Assign each data point to the nearest medoid
            self.labels = np.argmin(np.linalg.norm(
                X[:, np.newaxis] - self.medoids, axis=2), axis=1)

            # Update medoids
            new_medoids = np.empty_like(self.medoids)
            for i in range(self.clusters):
                cluster_points = X[self.labels == i]
                cost = np.sum(np.linalg.norm(cluster_points -
                              cluster_points[:, np.newaxis], axis=2), axis=1)
                new_medoids[i] = cluster_points[np.argmin(cost)]

            # Check for convergence
            if np.all(self.medoids == new_medoids):
                break

            medoids = new_medoids

    def predict(self, X):

        self.labels = np.argmin(np.linalg.norm(
            X[:, np.newaxis] - self.medoids, axis=2), axis=1)
        return self.medoids, self.labels, self.iter