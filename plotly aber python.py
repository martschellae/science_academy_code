
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import time
data = np.random.rand(6, 1000) 
fig = go.FigureWidget()
fig.add_cone(x = [data[0, 0]], y = [data[1, 0]], z = [data[2, 0]],
                          u = [data[3, 0]], v = [data[4, 0]], w = [data[5, 0]],
                          colorscale = 'Portland', sizemode = "absolute", sizeref = 0)
display(fig)
for i in range (data.shape[1]):
    with fig.batch_update():
    
       fig.data = [data[0, i], data[1, i], data[2, i], data[3, i], data[4, i], data[5, i]]
       time.sleep(0.05)
       