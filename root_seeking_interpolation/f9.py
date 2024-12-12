
def f9 ( x ):
    """value: f9 =x^3+1
    Input :
    x : the argument Output :
    value: the value of function """
    import numpy as np
    value = np.power(x, 3) 
    return value


def fp9 ( x ):
    """compute derivative of x^3 + 1
    """
    import numpy as np
    yp = 3 * np.power(x, 2)
    return yp