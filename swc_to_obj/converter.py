import math
import numpy as np





#function that create the vertices of a sphere and export in obj format
def createSphere(x, y, z, radius, f):
    total = 30
    for i in range (total):
        lat = (i/total)*(math.pi)
        for j in range (total):
            lon = (j/total)* (2*math.pi)
            xout = str(round( radius * math.sin(lon) * math.cos(lat) +x , 7))
            yout = str(round( radius * math.sin(lon) * math.sin(lat) +y , 7))
            zout = str(round ( radius * math.cos(lon) +z , 7))
            f.write("v " + xout +" " + yout + " " + zout + "\n")
            vector = np.array([xout,yout,zout])
            



f = open("demofile3.obj", "w")
createSphere(10, 10, 7, 3, f)
f.close()