from Hennessy_Integrate import Runga_Kutta as RK
import numpy as np

def partial(r,t, w = 1):
    dx = r[0]*r[1] - r[0] # xy -x 
    dy = r[1] - r[0]*r[1] + np.sin(w*t)**2 # y - xy + sin^2(wt)
    return np.array([dx,dy])

# Initializing conditions. Setting up x0, y0 as (1,1)
r = np.array([1,1])
xVals = []
yVals = []
w = 1
t0 = 0
tf = 10
N = 100
h = (tf-t0)/N
timeVals = np.arange(t0,tf,h)

= RK()