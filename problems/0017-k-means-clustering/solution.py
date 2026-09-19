def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
    centroids = [tuple(map(float, c)) for c in initial_centroids]
    for _ in range(max_iterations):
        clusters = [[] for _ in range(k)]

        for point in points:
            closest = min(
                range(k),
                key=lambda i: sum(
                    (point[d] - centroids[i][d]) ** 2
                    for d in range(len(point))
                )
            )
            clusters[closest].append(point)

        new_centroids = []

        for i, cluster in enumerate(clusters):
            if not cluster:
                new_centroids.append(centroids[i])
                continue

            new_centroid = tuple(
                sum(point[d] for point in cluster) / len(cluster)
                for d in range(len(cluster[0]))
            )
            new_centroids.append(new_centroid)

        if new_centroids == centroids:
            break

        centroids = new_centroids

    return [
        tuple(round(value, 4) for value in centroid)
        for centroid in centroids
    ]