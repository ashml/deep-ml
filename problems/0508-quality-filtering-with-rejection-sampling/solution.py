import numpy as np

def quality_filter_rejection_sampling(scores: list, threshold: float, n_select: int = None) -> dict:
    accepted = []

    for i, score in enumerate(scores):
        if score >= threshold:
            accepted.append((i, score))

    acceptance_rate = round(len(accepted) / len(scores), 4) if scores else 0.0

    accepted.sort(key=lambda x: x[1], reverse=True)

    if n_select is not None:
        accepted = accepted[:n_select]

    accepted_indices = [i for i, score in accepted]

    if accepted:
        mean_quality = round(sum(score for i, score in accepted) / len(accepted), 4)
    else:
        mean_quality = 0.0

    return {
        "accepted_indices": accepted_indices,
        "acceptance_rate": acceptance_rate,
        "mean_quality": mean_quality
    }