def bisection(f, a, b, tolerance, max_iterations):
    if f(a) * f(b) >= 0:
        print("The bisection method cannot be applied: f(a) and f(b) must have opposite signs.")
        return None
    
    iteration = 0
    while(b-a)/2 > tolerance and iteration <max_iterations:
        c = (a+b)/2
        if f(c) == 0 or (b-a)/2 < tolerance:
            return c

        if f(a) * f(c) < 0:
            b=c
        else:
            a=c    
        iteration += 1
    return (a+b)/2   

if __name__ == "__main__" :
    def func(x):
        return x**3 - x - 2
    
    a = 1
    b = 2

    # Set tolerance and maximum number of iterations
    tolerance = 1e-6
    max_iterations = 1000

    root = bisection(func, a, b, tolerance, max_iterations)

    if root is not None:
        print(f"Approximate root: {root}")