import pandas as pd
import numpy as np
import serial
import time
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import matplotlib.colors
from math import sqrt 
from matplotlib.animation import FuncAnimation
import plotly.express as px

arduino = serial.Serial('/dev/ttyACM0',250000)

arduino.setDTR(False)
arduino.flushInput()
arduino.setDTR(True)

laenge_x=70
laenge_y= 70
laenge_z=70


norm =Normalize(vmin=0, vmax=1023)
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("custom", ["#FF0000", "#D6D6D6","#32CD32"])

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
        
    except:
        print("Error", j)


animation=FuncAnimation(fig,update,frames=None)
plt.show()