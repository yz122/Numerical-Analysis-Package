"""
Yizhou Zeng, Oct. 2022
Newtons Method to find a root of given function
Improved version based on newton3()

"""

def newtonfd(func, x0, dx, maxIts = 100):
    """Uses Newtons method to find x so that func(x) = 0.
    Args :
    func : Function to find the root of.
    x0: satrting point.
    dx: interval size for derivative approximation.
    maxIts : The maximum number of iterations.
    Returns : 
    x : initial value of Newton method
    numIts :  number of iterations taken, max = maxIts. default = 100 """
    import numpy as np
    EPSILON = 5.0e-5
    
    x = x0

    increment = 1 # this is an arbitrary value

    for numIts in range(1, maxIts+1):
        fx = func(x)
        dfx = ( func(x + dx)-func(x) ) / dx # approximate derivative
        
        oldIncrement = increment # this is an arbitrary value
        increment = - fx / dfx
        x += increment
        
        r1 = np.abs(increment / oldIncrement )
        r2 = np.abs(increment / np.power(oldIncrement, 2))
        
        errorEstimate = np.abs(increment);
        print(f"{numIts}, x = {x}, error estimate = {errorEstimate}")
        # print(f"{numIts}, x={x}, r1= {r1}, r2 = {r2}")
        # if errorEstimate < EPSILON:
        if errorEstimate < EPSILON * (1 - r1):
            return x , numIts
    
    # if get here , the iteration has failed !
    raise Exception("newton1: maximum number of iterations exceeded.")
