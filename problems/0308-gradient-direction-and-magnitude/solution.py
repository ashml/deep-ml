import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	magnitude = np.sqrt(sum(el**2 for el in gradient))
	direction = [0.0 for _ in gradient]
    descent_direction = [0.0 for _ in gradient]
	if magnitude != 0:
		direction = [el / magnitude for el in gradient]
		descent_direction = [-el / magnitude for el in gradient]
	return {'magnitude': magnitude, 'direction': direction, 'descent_direction': descent_direction}