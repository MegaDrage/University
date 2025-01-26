import numpy as np
from scipy.integrate import solve_ivp

def F(x, y):
    z = y[0]  # Assuming z is the same as y[0]
    F = [0.0, 0.0]
    F[0] = np.sin(z) + np.sin(np.exp(x)) + np.sin(y[0]) + y[0]
    F[1] = np.exp(x) + 3 * np.sin(np.exp(x))
    return F

def shooting_method(y0, y1_prime, t_span, tol=1e-8, max_iter=100):
    t0, tf = t_span
    
    def residual(y_prime_0):
        sol = solve_ivp(lambda t, y: [y[1], F(t, y)[1]], t_span, [y0, y_prime_0], t_eval=[tf])
        return sol.y[1, -1] - y1_prime
    
    y_prime_0_low = -100  # Initial guess for lower bound of y'(0)
    y_prime_0_high = 100  # Initial guess for upper bound of y'(0)
    
    for _ in range(max_iter):
        y_prime_0_mid = (y_prime_0_low + y_prime_0_high) / 2
        res_mid = residual(y_prime_0_mid)
        
        if abs(res_mid) < tol:
            sol = solve_ivp(lambda t, y: [y[1], F(t, y)[1]], t_span, [y0, y_prime_0_mid])
            return sol
        
        if residual(y_prime_0_low) * res_mid < 0:
            y_prime_0_high = y_prime_0_mid
        else:
            y_prime_0_low = y_prime_0_mid
    
    raise ValueError("Shooting method did not converge within the maximum number of iterations.")

# Example usage:
y0 = 1  # Initial condition y(0) = 1
y1_prime = np.exp(1)  # Boundary condition y'(1) = exp(1)
t_span = (0, 1)  # Interval of integration

sol = shooting_method(y0, y1_prime, t_span)

# Print the solution table
print("x\t y(x)\t y'(x)")
for t, y in zip(sol.t, sol.y.T):
    print(f"{t:.2f}\t {y[0]:.6f}\t {y[1]:.6f}")