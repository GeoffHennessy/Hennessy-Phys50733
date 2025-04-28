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
    dx = body1.vx
    dy = body1.dy
    dvx = body1.m * (body1.x - body2.x) \
    / Distance(body1,body2)**3
    dvy = body1.m * (body1.y - body2.y) \
    / Distance(body1,body2)**3

    return np.array([dx,dy,dvx,dvy])

xVals = []
yVals = []
vxVals = []
vyVals = []

def Runga_Kutta(r,function,h):
        # xVals.append(r[0])
        # yVals.append(r[1])
        # vxVals.append(r[2])
        # vyVals.append(r[3])
        k1 = h * function(r,i)
        k2 = h * function(r + 0.5*k1, i + 0.5*h)
        k3 =  h * function(r + 0.5*k2, i + 0.5*h)
        k4 = h * function(r + k3, i + h)
        r = r + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
        return r 



Jupiter = Stellar_Body(18.98E26,[0,69911000],[13.07,0])
Sun = Stellar_Body(1.989E30,[0,0],[0,0])

timeVals = np.arange(0,12*365,1)

for i in timeVals:
    # Adjust r vector based on current values
    rJ = [Jupiter.x, Jupiter.y, Jupiter.vx, Jupiter.vy]
    rS = [Sun.x, Sun.y, Sun.vx, Sun.vy]

    #Track Jupiter's values
    xVals.append(rJ[0])
    yVals.append(rJ[1])
    xVals.append(rJ[2])
    vyVals.append(rJ[3])

    #Use Runga_Kutta to get new values for object each timestep
    dr = Runga_Kutta(rJ,)