import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def logistic_map(x: float, r: float) -> float:
    """Compute one iteration of the logistic map."""
    return r * x * (1 - x)


def logistic_derivative(x: float, r: float) -> float:
    """Derivative of the logistic map with respect to x."""
    return r * (1 - 2 * x)


def simulate_trajectory(r: float, x0: float, n_steps: int) -> np.ndarray:
    """Simulate a trajectory of the logistic map."""
    trajectory = np.empty(n_steps)
    x = x0
    for i in range(n_steps):
        x = logistic_map(x, r)
        trajectory[i] = x
    return trajectory


def plot_time_series(r: float = 3.9, x0: float = 0.2, n_steps: int = 100) -> None:
    """Plot a time series in a chaotic regime."""
    trajectory = simulate_trajectory(r=r, x0=x0, n_steps=n_steps)

    plt.figure(figsize=(10, 5))
    plt.plot(range(n_steps), trajectory)
    plt.title(f"Logistic Map Time Series (r = {r})")
    plt.xlabel("Iteration")
    plt.ylabel("x")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("time_series_logistic_map.png", dpi=300)
    plt.close()


def plot_bifurcation_diagram(
    r_min: float = 2.5,
    r_max: float = 4.0,
    n_r: int = 1200,
    iterations: int = 1000,
    last: int = 100,
    x0: float = 1e-5
) -> None:
    """Plot the bifurcation diagram of the logistic map."""
    r_values = np.linspace(r_min, r_max, n_r)
    x = np.full(n_r, x0)

    plt.figure(figsize=(10, 6))
    for i in range(iterations):
        x = r_values * x * (1 - x)
        if i >= iterations - last:
            plt.plot(r_values, x, ",k", alpha=0.25)

    plt.title("Bifurcation Diagram of the Logistic Map")
    plt.xlabel("Control parameter r")
    plt.ylabel("Asymptotic state x")
    plt.tight_layout()
    plt.savefig("bifurcation_diagram.png", dpi=300)
    plt.close()


def plot_sensitivity_to_initial_conditions(
    r: float = 3.9,
    x0_a: float = 0.500000,
    x0_b: float = 0.500001,
    n_steps: int = 60
) -> None:
    """Compare nearby trajectories to illustrate sensitivity to initial conditions."""
    traj_a = simulate_trajectory(r=r, x0=x0_a, n_steps=n_steps)
    traj_b = simulate_trajectory(r=r, x0=x0_b, n_steps=n_steps)
    diff = np.abs(traj_a - traj_b)

    plt.figure(figsize=(10, 5))
    plt.plot(range(n_steps), traj_a, label=f"x0 = {x0_a}")
    plt.plot(range(n_steps), traj_b, label=f"x0 = {x0_b}", linestyle="--")
    plt.title(f"Sensitivity to Initial Conditions (r = {r})")
    plt.xlabel("Iteration")
    plt.ylabel("x")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("sensitivity_initial_conditions.png", dpi=300)
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.semilogy(range(n_steps), diff + 1e-16)
    plt.title(f"Divergence of Nearby Trajectories (r = {r})")
    plt.xlabel("Iteration")
    plt.ylabel(r"$| \Delta x |$ (log scale)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("trajectory_divergence.png", dpi=300)
    plt.close()


def estimate_lyapunov_exponent(
    r: float,
    x0: float = 0.4,
    n_steps: int = 2000,
    transient: int = 500
) -> float:
    """
    Estimate the Lyapunov exponent for the logistic map.

    The exponent is computed as:
        lambda = average of log(|f'(x_n)|)
    after discarding a transient.
    """
    x = x0

    for _ in range(transient):
        x = logistic_map(x, r)

    lyapunov_sum = 0.0
    valid_steps = 0

    for _ in range(n_steps):
        derivative = abs(logistic_derivative(x, r))

        # Avoid log(0) in pathological cases
        if derivative > 1e-12:
            lyapunov_sum += np.log(derivative)
            valid_steps += 1

        x = logistic_map(x, r)

    if valid_steps == 0:
        return np.nan

    return lyapunov_sum / valid_steps


def plot_lyapunov_exponent(
    r_min: float = 2.5,
    r_max: float = 4.0,
    n_r: int = 1000,
    x0: float = 0.4,
    n_steps: int = 2000,
    transient: int = 500
) -> None:
    """Plot the Lyapunov exponent as a function of r."""
    r_values = np.linspace(r_min, r_max, n_r)
    lyapunov_values = np.array([
        estimate_lyapunov_exponent(
            r=r,
            x0=x0,
            n_steps=n_steps,
            transient=transient
        )
        for r in r_values
    ])

    plt.figure(figsize=(10, 6))
    plt.plot(r_values, lyapunov_values, linewidth=1)
    plt.axhline(0, linestyle="--")
    plt.title("Lyapunov Exponent of the Logistic Map")
    plt.xlabel("Control parameter r")
    plt.ylabel(r"Lyapunov exponent $\lambda$")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("lyapunov_exponent.png", dpi=300)
    plt.close()


def print_reference_values() -> None:
    """Print Lyapunov exponent estimates for selected parameter values."""
    test_values = [2.8, 3.2, 3.5, 3.9]
    print("Estimated Lyapunov exponents:")
    for r in test_values:
        lam = estimate_lyapunov_exponent(r)
        print(f"r = {r:.2f} -> lambda = {lam:.6f}")


if __name__ == "__main__":
    plot_time_series()
    plot_bifurcation_diagram()
    plot_sensitivity_to_initial_conditions()
    plot_lyapunov_exponent()
    print_reference_values()
