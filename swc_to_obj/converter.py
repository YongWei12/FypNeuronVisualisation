import math
import numpy as np
import os
import rotation  as rt


#Global variable to store the current point index 
ptIndex = 1


#function that create the vertices of a sphere and export in obj format
def createSphere(x, y, z, radius, f):
    total = 30
    global ptIndex
    globe= [[0 for j in range(total + 1)] for i in range(total + 1)]
    for i in range (total + 1):
        lat = (i/total)*(math.pi)
        for j in range (total + 1):
            lon = (j/total)* (2*math.pi)
            xout = str(round( radius * math.sin(lon) * math.cos(lat) +x , 7))
            yout = str(round( radius * math.sin(lon) * math.sin(lat) +y , 7))
            zout = str(round ( radius * math.cos(lon) +z , 7))
            f.write("v " + xout +" " + yout + " " + zout + "\n")
            globe[i][j] = ptIndex
            ptIndex = ptIndex +1

    #Draw the sphere here
    for i in range (total-5):
        for j in range (total -5):
            #if latitude is even 
            if i%2 ==0 :
                #draw the face triangle 
                f.write("f " + str(globe[i][j]) +" " + str(globe[i+1][j]) + " " + str(globe[i][j+1]) + "\n")
            else: 
                f.write("f " + str(globe[i][j+1]) +" " + str(globe[i-1][j+1]) + " " + str(globe[i][j+1]) + "\n")


def createAxon(x, y, z, radius, f):
    total = 8
    for i in range (total):
        lat = (i/total)*(math.pi)
        for j in range (total):
            lon = (j/total)* (2*math.pi)
            xout = str(round( radius * math.sin(lon) * math.cos(lat) +x , 7))
            yout = str(round( radius * math.sin(lon) * math.sin(lat) +y , 7))
            zout = str(round ( radius * math.cos(lon) +z , 7))
            f.write("v " + xout +" " + yout + " " + zout + "\n")

#draw circle for axons and dendrites cells 
def createDendrite(currPos, parentPos, radius, f):
    v2 = (np.array( currPos- parentPos)) / np.linalg.norm(np.array( currPos- parentPos))
    v1 = (np.array([0,0,1]))/np.linalg.norm(np.array([0,0,1]))
    # number of points we want to generate 
    total  = 8
    #for loop over specified number of points for circle 
    for  i in range (total):
        # for each point multiply it by its rotation matrix and add it with the center which is curr pos 
        angle = (i/total) * (2*math.pi)
        point =  np.array([math.cos(angle), math.sin(angle),0 ]) 
        rotationMatrix = rt.UU(rt.FF(v1,v2), rt.GG(v1,v2))
        newPt = currPos + np.matmul(rotationMatrix, point)
        # f.write("v " + str(point[0]) +" " + str(point[1]) + " " + str(point[2]) + "\n")
        f.write("v " + str(newPt[0]) +" " + str(newPt[1]) + " " + str(newPt[2]) + "\n")
        #write this point to a file
    f.write("v " + str(currPos[0]) +" " + str(currPos[1]) + " " + str(currPos[2]) + "\n")






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
        # print("X " + chunks[2]+ " y " + chunks[3] +" Z "+chunks[4])
        # print(chunks)

    elif(chunks[1] == "2" or chunks[1] == "3"):
        # here we need to determine the parent node 
        parent = chunks[-1].rstrip("\n")
        # get the x,y z position for the parent element 
        #for loop though whole data again 
        for f2 in flines:
            #if parent equal to id return its x,y,z 
            innerChunk = f2.split(" ")
            if parent == innerChunk[0]:
                parentAxis =  np.array([float(innerChunk[2]), float(innerChunk[3]), float(innerChunk[4])])
                break
        
        #get the x,y,z for the child element 
        childAxis  = np.array([float(chunks[2]), float(chunks[3]), float(chunks[4])])
        radius = float(chunks[5])
        # call the drawdendrite method and draw the dendrites
        createDendrite(childAxis, parentAxis,radius, fout)


        
    # elif(chunks[1] == "3"):
    #     createAxon(float(chunks[2]), float(chunks[3]), float(chunks[4]), float(chunks[5]), fout)
    else:
        continue



fout.close()

#Helpful functions 
# print(os.listdir())