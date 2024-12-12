"""
Yizhou Zeng, Oct. 2022
Newtons Method to find a root of given function
Improved version based on newton1()

"""

def newton2(func, dfunc, x0, maxIts=100):
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

    increment = 1 # this is an arbitrary value

    for numIts in range(1, maxIts+1):
        fx = func(x)
        dfx = dfunc(x)
        
        oldIncrement = increment # this is an arbitrary value
        increment = - fx / dfx
        x += increment
        
        r1 = np.abs(increment / oldIncrement )
        r2 = np.abs(increment / np.power(oldIncrement, 2))
        
        errorEstimate = np.abs(increment);
        # print(f"{numIts}, x= {x}, error estimate = {errorEstimate}")
        print(f"{numIts}, x={x}, r1= {r1}, r2 = {r2}")
        if errorEstimate < EPSILON:
            return x , numIts
    
    # if get here , the iteration has failed !
    raise Exception("newton1: maximum number of iterations exceeded.")
