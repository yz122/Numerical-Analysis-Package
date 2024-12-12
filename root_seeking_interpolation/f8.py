

def f8 ( x ):
    """value: f8=x^2+9
    Input :
    x : the argument Output :
    value: the value of function """
    import numpy as np
    value = np.power(x, 2) + 9
    return value


def fp8 ( x ):
    """compute derivative of x^2+9
    """
    import numpy as np
    yp = 2 * x
    return yp