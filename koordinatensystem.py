import matplotlib.pyplot as plt
class koordinatensystem:
    def __init__(self, x_groesse, y_groesse, z_groesse):
        plt.style.use('seaborn-v0_8-notebook')
        
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.set_xlim([-0, 5*x_groesse])
        ax.set_ylim([-0, y_groesse])
        ax.set_zlim([0, z_groesse])
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        plt.title ("Magnetfeldkamera") #Hier habe ich den Titel der Visualisierung hinzugefügt.

    def punkt (self, x, y, farbe):
        plt.plot(x, y, marker='o', color=farbe)

    def show (self):
        plt.show()