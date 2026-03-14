import torch

def grpo_objective(rhos, A, pi_theta_old, pi_theta_ref, epsilon=0.2, beta=0.01) -> torch.Tensor:
    """
    Compute the GRPO objective function.

    Args:
        rhos: List of likelihood ratios (pi_theta / pi_theta_old).
        A: List of advantage estimates.
        pi_theta_old: List of old policy probabilities.
        pi_theta_ref: List of reference policy probabilities.
        epsilon: Clipping parameter for the surrogate objective.
        beta: KL divergence penalty coefficient.

    Returns:
        The computed GRPO objective value as a torch.Tensor.
    """
    rhos = torch.tensor(rhos, dtype=torch.float32)
    A = torch.tensor(A, dtype=torch.float32)
    pi_theta_old = torch.tensor(pi_theta_old, dtype=torch.float32)
    pi_theta_ref = torch.tensor(pi_theta_ref, dtype=torch.float32)

    surrogate1 = rhos * A
    surrogate2 = torch.clamp(rhos, 1 - epsilon, 1 + epsilon) * A
    clipped_surrogate = torch.min(surrogate1, surrogate2)

    pi_theta = rhos * pi_theta_old
    r = pi_theta_ref / pi_theta
    kl_penalty = r * (r - torch.log(r) - 1)
    objective = torch.mean(clipped_surrogate) - beta * torch.mean(kl_penalty)

    return objective