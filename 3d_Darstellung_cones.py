import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from math import sqrt 
import plotly.graph_objects as go

def exp_scale(series, new_min=0, new_max=10, k=5):
    """
    Skaliert eine Spalte exponentiell auf [new_min, new_max].
    k steuert die Stärke der Exponentialkurve (größer = steiler).
    """
    # Erst auf [0, 1] normalisieren
    norm = (series - series.min()) / (series.max() - series.min())
    # Exponentielle Kurve anwenden (Werte bleiben in [0,1], da exp(0)=1, exp(k)=max)
    exp_vals = (np.exp(k * norm) - 1) / (np.exp(k) - 1)
    # Auf Zielbereich skalieren
    return exp_vals * (new_max - new_min) + new_min

def lin_scale(series, factor=5):
    return series * factor


df = pd.read_csv(
    "data2.csv"
)

for col in ["u", "v", "w"]:
    df[col] = exp_scale(df[col], k=5)

for col in ["z"]:
    df[col] = lin_scale(df[col], 0.05)

df.to_csv("skaliert.csv", index=False)

fig = go.Figure(
    data=go.Cone(
        x=df["x"],
        y=df["y"],
        z=df["z"],
        u=df["u"],
        v=df["v"],
        w=df["w"],
        sizemode="raw",
        sizeref=0.1,
        colorscale="Portland",
        opacity=0.1,
        cmin=0,
        cmax=5,
        hoverinfo="u+v+w+text",
        text="-> wind <-",
    ),
    layout=dict(
        width=900, height=600, scene=dict(camera=dict(eye=dict(x=2, y=0, z=1)))
    ),
)


fig.show()




"""def einlesen():
    df = pd.read_csv ('simulierte_werte_magnetfeld_stabmagnet.csv')
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

visualisieren(colourslist, data)"""
