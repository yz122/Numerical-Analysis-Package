def f3 ( x ):
    """ value =  x*exp(-x)
    Input :
    x : the argument Output :
    value: the value of function """
    import numpy as np
    value = x * np.exp(-x)
    return value


def fp3 ( x ):
    """ compute derivative of x * exp(-x) """
    import numpy as np
    yp = np.exp(-x) - x * np.exp(-x)
    return yp