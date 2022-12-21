def RK4(x0, u0, h, n, f):
    x = [x0 + _n*h for _n in range(0, n+2)]
    v = [0 for i in range(0, n+2)]
    v[0] = u0
    
    for _n in range(1, n+2):
        K1 = f((x[_n-1]), (v[_n-1]))
        K2 = f((x[_n-1]+h/2), (v[_n-1]+K1*h/2))
        K3 = f((x[_n-1]+h/2), (v[_n-1]+K2*h/2))
        K4 = f((x[_n-1]+h), (v[_n-1]+h*K3))
        
        v[_n] = v[_n-1] + (h/6)*(K1+2*K2+2*K3+K4)
        
    return v