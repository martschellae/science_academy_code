import pandas as pd
import numpy as np
import serial
import time
import csv
from koordinatensystem import koordinatensystem
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

"""f=open("data.csv", "w", newline='')
f.truncate()
try:
    arduino = serial.Serial('/dev/ttyACM0',9600)
except:
    arduino =serial.Serial ('/dev/ttyACM1',9600)

arduino.setDTR(False)
arduino.flushInput()
arduino.setDTR(True)

laenge_x=200
anzahlSensoren=5
for x in range(laenge_x):
    try:
        data=[]
        for i in range (anzahlSensoren):
            sensor =arduino.readline()
            sensor=int(sensor.decode("utf-8").strip('\r\n'))
            data.append(sensor)
                
        writer=csv.writer(f,delimiter=",")
        writer.writerow(data)

    except:
        print ("Error",x)
    time.sleep(0.05)

f.close()"""


def einlesen():
    df = pd.read_csv ('messung3.csv')
    data = df.to_numpy().tolist()
    return data #Liest die csv-Datei ein und konvertiert sie in ein NumPy - Array (6D-Vektor).

def laengeberechnen(data):
    werte=[]
    for i in range(len(data)):
        werte.append(data[i][3]+data[i][4]+data[i][5])
    colourslist = [] #Eine leere Liste für das Speichern der Längen bzw. der Farben.
     
    
    norm =Normalize(vmin=min(werte), vmax=max(werte))
    cmap =plt.get_cmap("RdYlGn")

    for i in range (len(werte)):
        
        colour=cmap(norm(werte[i]))
        colourslist.append (colour)#Hier werden den Längen die Farben zugeordnet und diese Farben werden in der Farbenliste gespeichert.
        
    return colourslist

def visualisieren(colourslist, data):#Visualisierung : ich habe den ein wenig angepassten Code von Julius benutzt.
    max_x=0
    max_y=0
    max_z=0
    for i in range(len(data)):
        max_x=max(max_x,abs(data[i][0]))
        max_y=max(max_y,abs(data[i][1]))
        max_z=max(max_z,abs(data[i][2]))
    u=koordinatensystem(max_x,max_y,max_z)
    for i in range(len(data)):
        u.punkt(data[i][0],data[i][1], data[i][2], colourslist[i])
    u.show()
       
data = einlesen()

colourslist = laengeberechnen(data)

visualisieren(colourslist, data)