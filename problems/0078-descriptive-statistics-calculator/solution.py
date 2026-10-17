import numpy as np

def descriptive_statistics(data):
    values, counts = np.unique(data, return_counts=True)

    q1, q2, q3 = np.percentile(data, [25, 50, 75])

    return {
        "mean": round(float(np.mean(data)), 4),
        "median": round(float(np.median(data)), 4),
        "mode": values[np.argmax(counts)].item(),
        "variance": round(float(np.var(data)), 4),
        "standard_deviation": round(float(np.std(data)), 4),
        "25th_percentile": float(q1),
        "50th_percentile": float(q2),
        "75th_percentile": float(q3),
        "interquartile_range": float(q3 - q1)
    }