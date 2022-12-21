from sympy import *

def TaylorMethod(x0, u0, h, n, f, order):
    x, u = symbols('x u')
    _x = [x0 + _n*h for _n in range(n+2)]
    _v = [0 for _n in range(n+2)]
    _v[0] = u0
    
    for _n in range(1, n+2):
        taylor = 0
        
        for i in range(1, order+1):
            deriv = f.diff(x, i-1, u, i-1).subs([(x,_x[_n-1]),(u,_v[_n-1])])
            taylor += (deriv * h**i)/factorial(i)
            
        _v[_n] = _v[_n-1] + taylor
    
    return _v