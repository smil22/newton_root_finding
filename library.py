def newton_root(f,df,a,b,tol,itermax):
    """
    - f: the function or polynomial of which you're looking a root.
    - df: its derivative.
    - a,b : the search interval boundaries.
    - tol : the expected accuracy.
    - itermax: the maximum number of iterations before algorithm stopping.
    """
    x = (a+b)/2
    for i in range(itermax):
        x0 = x
        x = x - (f(x)/df(x))
        if abs(x - x0) < tol:
            return x
