"""
Yizhou Zeng, Oct. 2022
Newtons Method to find a root of given function
"""

def newton1(func, dfunc, x0, maxIts=100):
    """Uses Newtons method to find x so that func(x) = 0.
    Args :
    func : Function to find the root of .
    dfunc : defines the derivative of the function . x0: The initial guess
    maxIts : The maximum number of iterations . Default is 100.
    Returns : 
    x : initial value of Newton method
    numIts :  number of iterations taken, max = maxIts """
    import numpy as np
    EPSILON = 5.0e-5
    
    x = x0
    for numIts in range(1, maxIts+1):
        fx = func(x)
        dfx = dfunc(x)
        
        increment = - fx / dfx
        x += increment
        errorEstimate = np.abs(increment);
        print(f"{numIts}, x= {x}, error estimate = {errorEstimate}")
        if errorEstimate < EPSILON:
            return x , numIts
    
    # if get here , the iteration has failed !
    raise Exception("newton1: maximum number of iterations exceeded.")
