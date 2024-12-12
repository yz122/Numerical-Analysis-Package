def f6 ( x ):
    """value ==(x-4)^2.
    Input :
    x : the argument Output :
    value: the value of function """
    import numpy as np
    value = np.power(x-4, 2)
    return value


def fp6 ( x ):
    """compute derivative of (x-4)^2
    """
    import numpy as np
    yp = 2 * (x - 4)
    return yp

