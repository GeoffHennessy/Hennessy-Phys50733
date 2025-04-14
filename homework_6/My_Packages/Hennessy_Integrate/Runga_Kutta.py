def Runga_Kutta(r,f,h,timeVals):
    xVals = []
    yVals= []

    for i in timeVals:
        xVals.append(r[0])
        yVals.append(r[1])
        k1 = h * f(r,i)
        k2 = h * f(r + 0.5*k1, i + 0.5*h)
        k3 =  h * f(r + 0.5*k2, i + 0.5*h)
        k4 = h * f(r + k3, i + h)
        r = r + 1/6 * (k1 + 2*k2 + 2*k3 + k4)