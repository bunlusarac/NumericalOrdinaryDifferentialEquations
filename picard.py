from sympy import *

def PicardMethod(x0, u0, f, _x, n_iterations):
    x, t = symbols('x t')
    approximation = u0 + 0*x
    
    for i in range(n_iterations):
        integrand = f.subs([(x, t),(u,approximation.subs(x, t))])
        approximation = u0 + integrate(integrand, (t, x0, x))
    
    return approximation.subs(x, _x)