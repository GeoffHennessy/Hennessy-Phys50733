import numpy as np
from matplotlib import pyplot as plt

G = 6.6743E-11

class Stellar_Body(object):
    def __init__(self,mass,args1,args2):
        self.mass = mass
        self.x = args1[0]
        self.y = args1[1]
        self.vx = args2[0]
        self.vy = args2[1]

# def Distance(body1, body2):
#     delx = body1.x - body2.x
#     dely = body1.y - body2.y
#     return (np.sqrt(delx**2 + dely**2))

def Forces(r,t):
    dx = r[2]
    dy = r[3]
    dvx = G * Sun.mass * (r[0]) / (np.sqrt(r[0]**2 + r[1]**2)**(3))
    dvy = G * Sun.mass * (r[1]) / (np.sqrt(r[0]**2 + r[1]**2)**(3))

    return np.array([dx,dy,dvx,dvy])

def Runga_Kutta(r,function,h):
        k1 = h * function(r,i)
        k2 = h * function(r + 0.5*k1, i + 0.5*h)
        k3 =  h * function(r + 0.5*k2, i + 0.5*h)
        k4 = h * function(r + k3, i + h)
        r = r + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
        return r 


xVals = []
yVals = []
vxVals = []
vyVals = []

Jupiter = Stellar_Body(18.98e26,[0,7.78e11],[13.07e3,0])
Sun = Stellar_Body(1.989e30,[0,0],[0,0])

timeVals = np.arange(0,10,1)

for i in timeVals:
    # Adjust r vector based on current values
    rJ = [Jupiter.x, Jupiter.y, Jupiter.vx, Jupiter.vy]
    rS = [Sun.x, Sun.y, Sun.vx, Sun.vy]

    #Track Jupiter's values
    xVals.append(rJ[0])
    yVals.append(rJ[1])
    vxVals.append(rJ[2])
    vyVals.append(rJ[3])

    #Use Runga_Kutta to get new values for object each timestep
    dr = Runga_Kutta(rJ,Forces,10)
    rJ += dr
    Jupiter.x = rJ[0]
    Jupiter.y = rJ[1]
    Jupiter.vx = rJ[2]
    Jupiter.vy = rJ[3]

fig = plt.figure(figsize = (16,10))
ax = plt.subplot(111)
ax.scatter(xVals,yVals)
plt.show()
