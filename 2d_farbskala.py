import pandas as pd
import numpy as np
#import serial
import time
import csv
from koordinatensystem import koordinatensystem
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import matplotlib.colors

anzahlSensoren = 5


def einlesen():
    df = pd.read_csv ('data.csv')
    data = df.to_numpy().flatten().tolist()
    return data #Liest die csv-Datei ein und konvertiert sie in ein NumPy - Array (6D-Vektor).

def laengeberechnen(data):
    colourslist = [] #Eine leere Liste für das Speichern der Längen bzw. der Farben.
     
    
    norm =Normalize(vmin=min(data), vmax=max(data))
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("custom", ["#FF0000", "#D6D6D6", "#32CD32"])

    for i in range (len(data)):
        
        colour=cmap(norm(data[i]))
        colourslist.append (colour)#Hier werden den Längen die Farben zugeordnet und diese Farben werden in der Farbenliste gespeichert.
        
    return colourslist

def visualisieren(colourslist, data):#Visualisierung : ich habe den ein wenig angepassten Code von Julius benutzt.

    u=koordinatensystem(1000,500,200)
    for i in range(int(len(data)/anzahlSensoren)):
        for j in range(anzahlSensoren):
            u.punkt(i*10, j*50, colourslist[i*anzahlSensoren+j])
    u.show()
       
data = einlesen()

colourslist = laengeberechnen(data)

print(colourslist)

visualisieren(colourslist, data)
