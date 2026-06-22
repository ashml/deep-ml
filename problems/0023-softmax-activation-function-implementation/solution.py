import math

def softmax(scores: list[float]) -> list[float]:
   max_z = max(scores)
   es = [math.e**(z - max_z) for z in scores]
   sum_e = sum(es)
   return [el / sum_e for el in es]