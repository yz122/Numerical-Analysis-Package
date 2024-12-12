def f7 ( x ):
    """value ==(x-4)^20.
    Input :
    x : the argument Output :
    value: the value of function """
    import numpy as np
    value = np.power(x-4, 20)
    return value


def fp7 ( x ):
    """compute derivative of (x-4)^20
    """
    import numpy as np
    yp = 20 * np.power(x - 4, 19)
    return yp