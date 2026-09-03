import pandas as pd
import numpy as np
import serial
import time
import csv
from koordinatensystem import koordinatensystem
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

f=open("data.csv", "w", newline='')
f.truncate()
try:
    arduino = serial.Serial('/dev/cu.usbmodem1101',250000)
except:
    arduino =serial.Serial ('/dev/cu.usbmodem2101',250000)

arduino.setDTR(False)
arduino.flushInput()
arduino.setDTR(True)

laenge_x=1500
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

f.close()

print("Messung beendet")

print("Öffne Fenster...")

def einlesen():
    df = pd.read_csv ('data.csv', header=None)
    data = df.to_numpy().flatten().tolist()
    return data #Liest die csv-Datei ein und konvertiert sie in ein NumPy - Array (6D-Vektor).

def laengeberechnen(data):
    colourslist = [] #Eine leere Liste für das Speichern der Längen bzw. der Farben.
     
    
    norm =Normalize(vmin=min(data), vmax=max(data))
    cmap =plt.get_cmap("RdYlGn")

    for i in range (len(data)):
        
        colour=cmap(norm(data[i]))
        colourslist.append (colour)#Hier werden den Längen die Farben zugeordnet und diese Farben werden in der Farbenliste gespeichert.
        
    return colourslist

def visualisieren(colourslist, data):#Visualisierung : ich habe den ein wenig angepassten Code von Julius benutzt.

    u=koordinatensystem(500,500,200)
    for i in range(int(len(data)/anzahlSensoren)):
        for j in range(anzahlSensoren):
            u.punkt(i, j*10, 0, colourslist[i*anzahlSensoren+j])
    u.show()
       
data = einlesen()

colourslist = laengeberechnen(data)

visualisieren(colourslist, data)