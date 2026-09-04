import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from math import sqrt 

def einlesen():
    df = pd.read_csv ('magnetfeld_stabmagnet.csv')
    #print(df)
    data = df.to_numpy()
    return data #Liest die csv-Datei ein und konvertiert sie in ein NumPy - Array (6D-Vektor).

def laengeberechnen(data):
    vector = np.delete(data, [0, 1, 2], axis=1) #Hier werden die Daten über die Position gelöscht, wodurch ein Magnetfeldstärke-Vektor entsteht.
    #print("nach loeschen", data)
    cols, rows = vector.shape

    lengthlist = [] 
    colourslist = []#Zwei leere Listen für das Speichern der Längen bzw. der Farben.

    for i in range (cols):
        length = sqrt(vector[i, 0]**2 + vector[i, 1]**2 + vector[i, 2]**2)
        lengthlist.append (length) #Längenberechnung
        
    median = np.median(lengthlist)
    lower_median = np.percentile (lengthlist, 25)
    higher_median = np.percentile(lengthlist, 75)#Hier werden das untere Viertel, das obere Viertel sowie die Mediane der Längenliste ermittelt.

    for i in range (cols):
        if lengthlist [i] <= lower_median:
            colour = 'purple'
        elif lower_median < lengthlist [i] <= median:
            colour = 'blue'
        elif median < lengthlist[i] <= higher_median:
            colour = 'orange'
        else:
            colour = 'red'
        colourslist.append (colour)#Hier werden den Längen die Farben zugeordnet und diese Farben werden in der Farbenliste gespeichert.
        
    return colourslist

def visualisieren(colourslist, data):#Visualisierung : ich habe den ein wenig angepassten Code von Julius benutzt.
    plt.style.use('seaborn-v0_8-notebook')

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.set_xlim([-40, 40])
    ax.set_ylim([-40, 40])
    ax.set_zlim([-40, 40])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.title ("Magnetfeldkamera") #Hier habe ich den Titel der Visualisierung hinzugefügt.

    cmap = plt.get_cmap("YlOrRd")


    ax.quiver(
    data[:, 0], data[:, 1], data[:, 2],
    data[:, 3], data[:, 4], data[:, 5],
    normalize=True, #Hier wird festgelegt, dass die Länge der Pfeile gleich bleibt.
    length = 4,
    color=colourslist[:]
    )

    plt.show()

data = einlesen()

#print(data)

colourslist = laengeberechnen(data)

visualisieren(colourslist, data)
