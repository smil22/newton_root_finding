import library

f = lambda x: x**3 + 2*x**2 + 10*x -20 #Define your function or polynomial here.
df = lambda x: 3*x**2 + 4*x + 10       #Define its derivative.
a,b,tol,itermax = 1,2,1e-5,14

root = library.newton_root(f, df, a, b, tol, itermax)

print('Root: {0:3.4f}\tEvaluation: {1:3.4e}'.format(root,f(root)))