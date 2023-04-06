"""
Numerische Grundlagen der Data Science

Sammlung der Methoden aus der Vorlesung
"""

import numpy as np


######### Interpolation #######################################################


def interpolate_linear(
    x_data: np.ndarray, y_data: np.ndarray, x: np.ndarray
) -> np.ndarray:
    n = len(x_data)
    i_upper = np.searchsorted(x_data, x)
    i_upper = np.where(i_upper < n, i_upper, n - 1)
    i_upper = np.where(i_upper > 1, i_upper, 1)
    i_lower = i_upper - 1
    x_upper = x_data[i_upper]
    y_upper = y_data[i_upper]
    x_lower = x_data[i_lower]
    y_lower = y_data[i_lower]
    return (y_upper - y_lower) / (x_upper - x_lower) * (x - x_lower) + y_lower


######### Nullstellen #########################################################


def root_bisection_steps(f, a0, b0, n):
    assert a0 < b0 and n >= 0
    a, b = a0, b0
    for _ in range(n):
        ya, yb = f(a), f(b)
        assert ya * yb <= 0
        x = (a + b) / 2
        y = f(x)
        if y == 0:
            return x
        elif ya * y < 0:
            b = x
        else:
            a = x
    return x


def root_newton_steps(f, fprime, x0, n):
    assert n >= 0
    x = x0
    for _ in range(n):
        x = x - f(x) / fprime(x)
    return x


def root_bisection_tolerance(f, a0, b0, tol):
    assert a0 < b0 and tol > 0
    a, b = a0, b0
    x = (a + b) / 2
    y = f(x)
    xs = [x]
    ys = [y]
    while abs(y) >= tol:
        if f(a) * y < 0:
            b = x
        else:
            a = x
        x = (a + b) / 2
        y = f(x)
        xs.append(x)
        ys.append(y)
    return (xs, ys)


def root_newton_tolerance(f, fprime, x0, tol):
    assert tol > 0
    x = x0
    y = f(x)
    xs = [x]
    ys = [y]
    while abs(y) >= tol:
        x = x - y / fprime(x)
        y = f(x)
        xs.append(x)
        ys.append(y)
    return (xs, ys)


def root_newton_error_estimate(f, fprime, x0, xtol, ytol, n):
    assert xtol > 0 and ytol > 0 and n >= 0
    x = x0
    y = f(x)
    y_by_yprime = y / fprime(x)
    Dy = abs(y)
    Dx = abs(y_by_yprime)
    steps = 0
    res = [(steps, x, Dx, Dy)]
    while (Dx > xtol or Dy > ytol) and steps < n:
        x = x - y_by_yprime
        y = f(x)
        y_by_yprime = y / fprime(x)
        Dy = abs(y)
        Dx = abs(y_by_yprime)
        steps += 1
        res.append((steps, x, Dx, Dy))
    return res


def root_bisection_error_estimate(f, a0, b0, xtol, ytol, n):
    assert a0 < b0 and xtol > 0 and ytol > 0 and n >= 0
    a, b = a0, b0

    x = (a + b) / 2
    y = f(x)
    ya = f(a)
    Dx = abs(b - a) / 2
    Dy = abs(y)
    steps = 0
    res = [(steps, x, Dx, Dy)]

    while (Dx > xtol or Dy > ytol) and steps < n:
        if ya * y < 0:
            b = x
        else:
            a = x
            ya = y
        x = (a + b) / 2
        y = f(x)
        Dx = abs(b - a) / 2
        Dy = abs(y)
        steps += 1
        res.append((steps, x, Dx, Dy))
    return res


######### Ableitung ###########################################################


def derivative_function(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


def derivative_data(x, y):
    dy = np.diff(y)
    dx = np.diff(x)
    dydx = dy / dx
    yprime = np.empty_like(y)
    yprime[1:-1] = (dydx[:-1] + dydx[1:]) / 2
    yprime[0] = dydx[0]
    yprime[-1] = dydx[-1]
    return yprime


def derivative_function_partial_dfdx1(f, x1, x2, h=1e-6):
    return (f(x1 + h, x2) - f(x1 - h, x2)) / (2 * h)


def derivative_function_partial_dfdx2(f, x1, x2, h=1e-6):
    return (f(x1, x2 + h) - f(x1, x2 - h)) / (2 * h)


def gradient_function(f, x1, x2, h=1e-6):
    return np.array(
        [
            derivative_function_partial_dfdx1(f, x1, x2, h),
            derivative_function_partial_dfdx2(f, x1, x2, h),
        ]
    )


def gradient_descent_1d(grad_f, x0, alpha, tol, max_steps):
    x = x0
    grad = grad_f(x)
    err = np.inf
    res = [(x, err)]
    while len(res) < max_steps and err > tol:
        grad = grad_f(x)
        x = x - alpha * grad
        err = abs(grad)
        res.append((x, err))
    return res


def gradient_descent_2d(grad_f, x0, y0, alpha, tol, max_steps):
    x, y = x0, y0
    grad = grad_f(x, y)
    err = np.sqrt(np.sum(grad**2))
    res = [(x, y, err)]
    while len(res) < max_steps and err > tol:
        grad = grad_f(x, y)
        x = x - alpha * grad[0]
        y = y - alpha * grad[1]
        err = np.sqrt(np.sum(grad**2))
        res.append((x, y, err))
    return res


if __name__ == "__main__":
    ######### Tests ###############################################################

    pass
