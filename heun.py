def HeunMethod(x0, u0, h, n, f):
    x = [x0 + _n*h for _n in range(0, n+2)]
    v = [0 for i in range(0, n+2)]
    v[0] = u0

    for _n in range(1, n+2):
        v[_n] = v[_n-1] + (h/2) * (f(x[_n-1], v[_n-1]) + f(x[_n], v[_n-1]+ h * f(x[_n-1], v[_n-1])))
        
    return v