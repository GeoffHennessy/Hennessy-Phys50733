import numpy as np

G = 6.6743E-11
class Stellar_Body(Stellar_Body):
    def __init__(self,mass,args1,args2):
        assert len(args1 == 2), "position args takes 2 inputs"
        assert len(args2 == 2), "velocity args takes 2 inputs"
        self.mass = mass
        self.x = args1[0]
        self.y = args1[1]
        self.vx = args2[0]
        self.vy = args2[1]

def Distance(body1, body2):
    delx = body1.x - body2.x
    dely = body1.y - body2.y
    return (np.sqrt(delx**2 + dely**2))

def Forces(body1,body2):
    
    dV = body1.m * np.array[body1.x - body2.x, body1.y - body2.y] \
    / Distance(body1,body2)**3
    # body1.x += body1.vx
    # body1.y += body1.vy
    return dV

def Runga_Kutta(xVals,yVals,r,function,h):
        xVals.append(r[0])
        yVals.append(r[1])
        k1 = h * function(r,i)
        k2 = h * function(r + 0.5*k1, i + 0.5*h)
        k3 =  h * function(r + 0.5*k2, i + 0.5*h)
        k4 = h * function(r + k3, i + h)
        r = r + 1/6 * (k1 + 2*k2 + 2*k3 + k4)

Jupiter = Stellar_Body(18.98E26,[0,69911000],[13.07,0])
timeVals = np.arange(10000)
for i in timeVals:
    r = [Jupiter.x,Jupiter.y,Jupiter.vx,Jupiter.vy]