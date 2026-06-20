import numpy as np

def thanksgiving_dish_predictor(preference_scores: list[float]) -> list[float]:
    es = [np.e ** el for el in preference_scores]
    sum_e = sum(es)
    return [el / sum_e for el in es]