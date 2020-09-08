import math





#function that create the vertices of a sphere and export in obj format
def createSphere(x, y, z, radius, f):
    total = 100
    for i in range (total):
        lon = (i/total)*(2*math.pi)
        for j in range (total):
            lat = (j/total)* (math.pi)
            xout = str(round( radius * math.sin(lon) * math.cos(lat) +x , 7))
            yout = str(round( radius * math.sin(lon) * math.sin(lat) +y , 7))
            zout = str(round ( radius * math.cos(lon) +z , 7))
            f.write("v " + xout +" " + yout + " " + zout + "\n")



f = open("demofile3.obj", "w")
createSphere(0, 0, 0, 10, f)
f.close()