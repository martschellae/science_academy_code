import pandas as pd
import numpy as np
import serial
import time
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import matplotlib.colors
from math import sqrt 
from matplotlib.animation import FuncAnimation

arduino = serial.Serial('/dev/ttyACM0',250000)

arduino.setDTR(False)
arduino.flushInput()
arduino.setDTR(True)

laenge_x=70
laenge_y= 70
laenge_z=70


norm =Normalize(vmin=0, vmax=1023)
#cmap =plt.get_cmap("RdYlGn")
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("custom", ["#FF0000", "#D6D6D6","#32CD32"])
#punkte=koordinatensystem(80,40,40)

plt.style.use('seaborn-v0_8-notebook')
        
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlim([-0, 80])
ax.set_ylim([-0, 40])
ax.set_zlim([0, 40])
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.title ("Magnetfeldkamera") #Hier habe ich den Titel der Visualisierung hinzugefügt.

def punkt ( x, y,z, farbe):
    plt.plot(x, y,z, marker='o', color=farbe)


"""def laengeberechnen(data):
    vector = np.delete(data, [0, 1, 2], axis=1) #Hier werden die Daten über die Position gelöscht, wodurch ein Magnetfeldstärke-Vektor entsteht.
    cols, rows = vector.shape

    lengthlist = [] 
    colourslist = []#Zwei leere Listen für das Speichern der Längen bzw. der Farben.

    for i in range (cols):
        length = sqrt(vector[i, 0]**2 + vector[i, 1]**2 + vector[i, 2]**2)
        lengthlist.append (length) #Längenberechnung

    
    for i in range (len(data)):
            
        colour=cmap(norm(data[i][3]))
        colourslist.append (colour)#Hier werden den Längen die Farben zugeordnet und diese Farben werden in der Farbenliste gespeichert.
    return colourslist"""

"""def visualisieren(colourslist, data):#Visualisierung : ich habe den ein wenig angepassten Code von Julius benutzt.
    
    for i in range(len(data)):
        punkt(data[i][0],data[i][1], data[i][2], colourslist[i])
    #punkte.show()
    plt.show()"""

j=0
data=np.array
data=arduino.readline()
data=data.decode("utf-8").strip('\r\n')
data=data.split(',')
for i in range(6):
    data[i]=int(data[i])
    
def update(frame):
    global j
    global data
    try:
        zeile=[]
        zeile=np.array
        zeile=arduino.readline()
        zeile=zeile.decode("utf-8").strip('\r\n')
        if zeile.count(',')==5:
            zeile=zeile.split(',')
            for i in range(6):
                zeile[i]=int(zeile[i])
            data=np.vstack((data,zeile))
            j+=1
            punkt(data[j][0],data[j][1],data[j][2],cmap(norm(data[j][3])))
        else:
            print("Übersprungen")

    #if len(data)>250:
        #data.remove(data[0])
    #colours=laengeberechnen(data)
    #visualisieren(colours,data)
            
    except:
        print("Error", j)
    time.sleep(0.005)
   
    
     
"""data=np.array
data=arduino.readline()
data=data.decode("utf-8").strip('\r\n')
data=data.split(',')
for i in range(6):
    data[i]=int(data[i])

for j in range (200):
    zeile=np.array
    zeile=arduino.readline()
    zeile=zeile.decode("utf-8").strip('\r\n')
    zeile=zeile.split(',')
    for i in range(6):
        zeile[i]=int(zeile[i])
    data=np.vstack((data,zeile))"""

    #laengeberechnen(data)
    #time.sleep(0.005)


animation=FuncAnimation(fig,update,frames=None)
plt.show()