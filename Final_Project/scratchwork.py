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
    dvx = -G * Sun.mass * (r[0]) / (np.sqrt(r[0]**2 + r[1]**2)**(3))
    dvy = -G * Sun.mass * (r[1]) / (np.sqrt(r[0]**2 + r[1]**2)**(3))

    return np.array([dx,dy,dvx,dvy])

def KE(object):
    energy = 1/2 * object.mass * (object.vx**2 + object.vy**2)
    return energy

def PE(object):
    distance = (object.x**2 + object.y**2)**(1/2)
    potential = -(G * Sun.mass * object.mass)  / distance
    return potential

def Runga_Kutta(r,function,h):
        k1 = h * function(r,i)
        k2 = h * function(r + 0.5*k1, i + 0.5*h)
        k3 =  h * function(r + 0.5*k2, i + 0.5*h)
        k4 = h * function(r + k3, i + h)
        r = r + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
        return r 


JxVals, JyVals, JvxVals, JvyVals = [], [], [], []
SxVals, SyVals, SvxVals, SvyVals = [], [], [], []
CxVals, CyVals, CvxVals, CvyVals = [], [], [], []
KE_total, PE_total, E_Total = [], [], []

Jupiter = Stellar_Body(18.98e26,[1.667e10,7.757e11],[-1.321e4,9.-06e2])
Saturn = Stellar_Body(5.6834e26,[1.424e12,-1.626e-11],[5.592e2,9.576e3])
Ceres = Stellar_Body(1.9e20,[4.138e11,-1.45e11],[5.19e3,1.57e4])
Sun = Stellar_Body(1.989e30,[0,0],[0,0])

timeVals = np.arange(0,33*365*24*60*60,60*60*6)

for i in timeVals:
    # Adjust r vector based on current values
    rJ = np.array([Jupiter.x, Jupiter.y, Jupiter.vx, Jupiter.vy])
    rC = np.array([Ceres.x, Ceres.y, Ceres.vx, Ceres.vy])
    rS = np.array([Saturn.x, Saturn.y, Saturn.vx, Saturn.vy])

    #Track Planet's values
    JxVals.append(rJ[0])
    JyVals.append(rJ[1])
    JvxVals.append(rJ[2])
    JvyVals.append(rJ[3])

    SxVals.append(rS[0])
    SyVals.append(rS[1])
    SvxVals.append(rS[2])
    SvyVals.append(rS[3])

    CxVals.append(rC[0])
    CyVals.append(rC[1])
    CvxVals.append(rC[2])
    CvyVals.append(rC[3])

    #Use Runga_Kutta to get new values for object each timestep
    rJ = Runga_Kutta(rJ,Forces,60*60*6)
    rS = Runga_Kutta(rS,Forces,60*60*6)
    rC = Runga_Kutta(rC,Forces,60*60*6)

    Jupiter.x = rJ[0]
    Jupiter.y = rJ[1]
    Jupiter.vx = rJ[2]
    Jupiter.vy = rJ[3]

    Saturn.x = rS[0]
    Saturn.y = rS[1]
    Saturn.vx = rS[2]
    Saturn.vy = rS[3]

    Ceres.x = rC[0]
    Ceres.y = rC[1]
    Ceres.vx = rC[2]
    Ceres.vy = rC[3]

    KE_total.append(KE(Jupiter) + KE(Saturn) + KE(Ceres))
    PE_total.append(PE(Jupiter) + PE(Saturn) + PE(Ceres))
    E_Total.append(KE(Jupiter) + KE(Saturn) + KE(Ceres) + PE(Jupiter) + PE(Saturn) + PE(Ceres))

fig = plt.figure(figsize = (16,10))
ax = plt.subplot(111)
ax.scatter(JxVals,JyVals)
ax.scatter(SxVals,SyVals)
ax.scatter(CxVals,CyVals)
ax.plot(0,0)
plt.axis('equal')

fig2 = plt.figure(figsize = (16,10))
ax2 = plt.subplot(111)
ax2.plot(timeVals,KE_total)
ax2.plot(timeVals,PE_total)
ax2.plot(timeVals, E_Total)
plt.show()
