from Hennessy_Integrate import Runga_Kutta as RK
import numpy as np
from matplotlib import pyplot as plt

def my_partial(r,t, w = 1):
    dx = r[0]*r[1] - r[0] # xy -x 
    dy = r[1] - r[0]*r[1] + np.sin(w*t)**2 # y - xy + sin^2(wt)
    return np.array([dx,dy])

def sin(x,t):
    return x**2 + np.sin(t)

def linear(x,t):
    return x + t

## Graph 1: PDE
# Initializing conditions. Setting up x0, y0 as (1,1)
r = np.array([1,1])
xVals = []
yVals = []
w = 1
t0 = 0
tf = 10
N = 1000
timeVals = np.linspace(t0,tf,N)


data = RK.Runga_Kutta2(r,my_partial,0.001,timeVals)
xVals = data[0][:]
yVals = data[1][:]

fig = plt.figure(figsize = (10,6))
ax = plt.subplot(211)
ax2 = plt.subplot(212)
ax.scatter(timeVals,xVals)
ax2.scatter(timeVals,yVals)
ax.set_ylabel("x")
ax2.set_ylabel("y")
ax2.set_xlabel("time")
ax.set_title("PDE System")
## Section 2: Integrating sin:
x0 = 0
xVals2 = RK.Runga_Kutta1(x0,sin,0.001,timeVals)
fig2 = plt.figure(figsize = (10,6))
ax = plt.subplot(111)
ax.scatter(timeVals,xVals2)

ax.set_xlabel("time")
ax.set_ylabel("x")
ax.set_title("Runga Kutta for x^2 + sin(t)")

## Section 3: Exponential:
x0 = 1
xVals2 = RK.Runga_Kutta1(x0,linear,0.001,timeVals)
fig3 = plt.figure(figsize = (10,6))
ax = plt.subplot(111)
ax.scatter(timeVals,xVals2)
ax.set_xlabel("time")
ax.set_ylabel("x")
ax.set_title("Runga Kutta for linear function")

plt.show()