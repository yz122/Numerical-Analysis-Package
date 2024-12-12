def f2 ( x ):
    """value =  x^5 - x - 1
    Input :
    x : the argument Output :
    value: the value of function """
    import numpy as np
    value = np.power(x, 5) - x - 1
    return value


def fp2 ( x ):
    """compute derivative of x^5 - x - 1 
    """
    import numpy as np
    yp = 5 * np.power(x, 4) - 1
    return yp
