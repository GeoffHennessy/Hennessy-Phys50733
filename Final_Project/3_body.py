import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as animation


class Body(object):
    def __init__(self,args1,args2):
        self.x = args1[0]
        self.y = args1[1]
        self.vx = args2[0]
        self.vy = args2[1]

def Forces(r,t): # r is as follows [x,y,vx,vy,body2x,body2y,body3x,body3y]
    dx = r[2]
    dy = r[3]

    force1 = np.array([r[4]-r[0] ,r[5]-r[1]]) / (np.sqrt((r[0] - r[4])**2 + (r[1] - r[5])**2)**(3)) # x,y / r ** 3 (body2)
    force2 = np.array([r[6]-r[0], r[7]-r[1]]) / (np.sqrt((r[0] - r[6])**2 + (r[1] - r[7])**2)**(3)) # x,y / r ** 3 (body3)

    dvx =  force1[0] + force2[0] # sum of x components of force
    dvy =  force1[1] + force2[1] # sum of y components of force

    return np.array([dx,dy,dvx,dvy,0,0,0,0]) ### I think I need to put zeros here, but I might need to put the values

def KE(object):
    energy = 1/2 * (object.vx**2 + object.vy**2)
    return energy

def PE(object):
    distance = (object.x**2 + object.y**2)**(1/2)
    potential = -1 / distance
    return potential

def Runga_Kutta(r,function,h,t):
        k1 = h * function(r,t)
        k2 = h * function(r + 0.5*k1, t + 0.5*h)
        k3 =  h * function(r + 0.5*k2, t + 0.5*h)
        k4 = h * function(r + k3, t + h)
        r = r + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
        return r 


b1xVals, b1yVals, b1vxVals, b1vyVals = [], [], [], []
b2xVals, b2yVals, b2vxVals, b2vyVals = [], [], [], []
b3xVals, b3yVals, b3vxVals, b3vyVals = [], [], [], []



b1 = Body([-0.9892620043,0],[0,1.9169244185])
b2 = Body([2.2096177241,0],[0,0.1910268738])
b3 = Body([-1.2203557197,0],[0,-2.1079512924])

dt = 0.0001
Final_T = 34
timeVals = np.arange(0,Final_T,dt)

for i in timeVals:
    # Adjust r vector based on current values
    rb1 = np.array([b1.x, b1.y, b1.vx, b1.vy, b2.x, b2.y, b3.x, b3.y])
    rb2 = np.array([b2.x, b2.y, b2.vx, b2.vy, b1.x, b1.y, b3.x, b3.y])
    rb3 = np.array([b3.x, b3.y, b3.vx, b3.vy, b1.x, b1.y, b2.x, b2.y])

    #Track boyd's values
    b1xVals.append(rb1[0])
    b1yVals.append(rb1[1])
    b1vxVals.append(rb1[2])
    b1vyVals.append(rb1[3])

    b2xVals.append(rb2[0])
    b2yVals.append(rb2[1])
    b2vxVals.append(rb2[2])
    b2vyVals.append(rb2[3])

    b3xVals.append(rb3[0])
    b3yVals.append(rb3[1])
    b3vxVals.append(rb3[2])
    b3vyVals.append(rb3[3])

    # Runga Kutta to adjust values

    rb1 = Runga_Kutta(rb1,Forces,dt,i)
    rb2 = Runga_Kutta(rb2,Forces,dt,i)
    rb3 = Runga_Kutta(rb3,Forces,dt,i)

    b1.x = rb1[0]
    b1.y = rb1[1]
    b1.vx = rb1[2]
    b1.vy = rb1[3]

    b2.x = rb2[0]
    b2.y = rb2[1]
    b2.vx = rb2[2]
    b2.vy = rb2[3]

    b3.x = rb3[0]
    b3.y = rb3[1]
    b3.vx = rb3[2]
    b3.vy = rb3[3]

fig = plt.figure(figsize = (16,10))
ax = plt.subplot(111)
ax.plot(b1xVals,b1yVals, c = 'black')
ax.plot(b2xVals,b2yVals, c = 'r')
ax.plot(b3xVals,b3yVals, c = 'blue')
ax.set_title("Three Body Orbits")
ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")
plt.axis('equal')
plt.show()

# fig2, ax2 = plt.subplots()
# b1Scat = ax2.scatter([],[])
# b2Scat = ax2.scatter([],[])
# b3Scat = ax2.scatter([],[])
# ax2.set_xlim(-5, 5)
# ax2.set_ylim(-5, 5)
# ax2.set_title("Three Body Orbits")
# ax2.set_xlabel("X Position")
# ax2.set_ylabel("Y Position")

# def init():
#      b1Scat.set_offsets(np.empty((0,2)))
#      b2Scat.set_offsets(np.empty((0,2)))
#      b3Scat.set_offsets(np.empty((0,2)))

#      return(b1Scat,b2Scat, b3Scat)

# def update(frame):
     
#      b1Scat.set_offsets([[b1xVals[frame], b1yVals[frame]]])
#      b2Scat.set_offsets([[b2xVals[frame], b2yVals[frame]]])
#      b3Scat.set_offsets([[b3xVals[frame], b3yVals[frame]]])
#      return (b1Scat,b2Scat,b3Scat)

# ani = animation.FuncAnimation(
#     fig=fig2, 
#     func=update,
#     frames=range(0,len(timeVals),500),
#     init_func = init,
#     interval = 10,
#     blit= True)

# ani.save("3_Body_ani.gif", fps = 60)
plt.show()