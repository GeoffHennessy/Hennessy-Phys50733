import numpy as np

G = 6.6743E-11
class Stellar_Body(Stellar_Body):
    def __init__(self,mass,args1,args2):
        assert len(args1 == 3), "position args takes 3 inputs"
        assert len(args2 == 3), "velocity args takes 3 inputs"
        self.mass = mass
        self.x = args1[0]
        self.y = args1[1]
        self.z = args1[2]
        self.vx = args2[0]
        self.vy = args2[1]
        self.vz = args2[2]

def Distance(body1, body2):
    delx = body1.x - body2.x
    dely = body1.y - body2.y
    delz = body1.z - body2.z
    return (np.sqrt(delx**2 + dely**2 + delz**z))

def Forces(body1,body2):
    f1 = G * body1.m * body2.m * np.array[body1.x - body2.x, body1.y - body2.y, body1.z - body2.z] \
    / Distance(body1,body2)**3
    f2 = -f1

def Runga_Kutta(xVals,yVals,function,h,timeVals):
    for i in timeVals:
        xVals.append(r[0])
        yVals.append(r[1])
        k1 = h * function(r,i)
        k2 = h * function(r + 0.5*k1, i + 0.5*h)
        k3 =  h * function(r + 0.5*k2, i + 0.5*h)
        k4 = h * function(r + k3, i + h)
        r = r + 1/6 * (k1 + 2*k2 + 2*k3 + k4)