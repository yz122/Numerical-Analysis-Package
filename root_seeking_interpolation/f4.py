def f4 ( x ):
    """value =  2 * cos(3x) - exp(x)
    Input :
    x : the argument Output :
    value: the value of function """
    import numpy as np
    value = 2 * np.cos(3 * x) - np.exp(x)
    return value


def fp4 ( x ):
    """ compute derivative of 2 * cos(3x) - exp(x) """
    import numpy as np
    yp = -6 * np.sin(3 * x) - np.exp(x)
    return yp