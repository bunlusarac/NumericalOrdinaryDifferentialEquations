from euler import EulerMethod
from heun import HeunMethod
from picard import PicardMethod
from taylor import TaylorMethod
from rk4 import RK4

f = lambda x, u: x - u

approx_euler = EulerMethod(0, 1, 0.1, 2, f)
approx_heun = HeunMethod(0, 1, 0.1, 2, f)
approx_rk4 = RK4(0, 1, 0.1, 2, f)

x,u = symbols('x, u')
f = x - u

approx_picard = [PicardMethod(0, 1, f, i, n_iterations) for i in [0.1, 0.2, 0.3]]
approx_taylor = TaylorMethod(0, 1, 0.1, 2, f, 3)

print(approx_euler, approx_heun, approx_picard, approx_taylor, approx_rk4, sep='\n')