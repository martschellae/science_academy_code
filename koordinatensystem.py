import matplotlib.pyplot as plt
class koordinatensystem:
    def __init__(self, x_groesse, y_groesse, z_groesse):
        plt.style.use('seaborn-v0_8-notebook')
        
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.set_xlim([-x_groesse, x_groesse])
        ax.set_ylim([-y_groesse, y_groesse])
        ax.set_zlim([-z_groesse, z_groesse])
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        plt.title ("Magnetfeldkamera") #Hier habe ich den Titel der Visualisierung hinzugefügt.

    def punkt (self, x, y,z, farbe):
        plt.plot(x, y,z, marker='o', color=farbe, alpha = 0.1)

    def show (self):
        plt.show()