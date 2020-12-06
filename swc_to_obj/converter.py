import math
import numpy as np
import os





#function that create the vertices of a sphere and export in obj format
def createSphere(x, y, z, radius, f):
    total = 200
    for i in range (total):
        lat = (i/total)*(math.pi)
        for j in range (total):
            lon = (j/total)* (2*math.pi)
            xout = str(round( radius * math.sin(lon) * math.cos(lat) +x , 7))
            yout = str(round( radius * math.sin(lon) * math.sin(lat) +y , 7))
            zout = str(round ( radius * math.cos(lon) +z , 7))
            f.write("v " + xout +" " + yout + " " + zout + "\n")



#code to create and open output file
fout  = open("demofile3.obj", "w")
# createSphere(0,0,0,3,fout)

#getting the line by line of swc file 
fin = open("./swc_to_obj/sample_neuron.swc", "r")
flines = fin.readlines()
for f in flines: 
    chunks = f.split(" ")
    if(chunks[0] == "#"):
        continue
    elif(chunks[1] == "1"):
        createSphere(float(chunks[2]), float(chunks[3]), float(chunks[4]), float(chunks[5]), fout)
        print("X " + chunks[2]+ " y " + chunks[3] +" Z "+chunks[4])
        print(chunks)
    else:
        continue



fout.close()

#Helpful functions 
# print(os.listdir())