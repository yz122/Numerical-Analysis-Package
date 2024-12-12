def f1 ( x ):
    """Computes y=xˆ2−9. """
    import numpy as np
    value = np.power(x, 2) - 9
    return value

def fp1(x):
    """ Computes the derivative of y=xˆ2−9."""
    yprime = 2 * x
    return yprime