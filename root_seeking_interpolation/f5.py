def f5 ( x ):
    """value =  (x - 1)^5
    Input :
    x : the argument Output :
    value: the value of function """
    import numpy as np
    value = np.power(x-1, 5)
    return value


def fp5 ( x ):
    """ compute derivative of (x-1)^5 """
    import numpy as np
    yp = 5 * np.power(x-1, 4)
    return yp