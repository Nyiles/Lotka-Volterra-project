# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:32:25 2024

@author: nicny
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint

data = np.zeros((16, 16))
def comp(y, t, alpha, beta, delta, gamma, tenma, f, g):
    x, y1, y2 = y
    dxdt =  alpha * x - beta * x * (y1) - tenma * x * (y2)
    dy1dt = delta * beta * x * y1 - gamma * y1
    dy2dt = delta * beta * x * y2 - gamma * y2
    return [dxdt, dy1dt, dy2dt]
alpha = 0.1  # Prey birth rate
beta = 0.05  # Predation rate
delta = 0.1  # Conversion efficiency
gamma = 0.1  # Predator death rate
tenma = 0.02
f = 0.02
g = 0.1
x0 =10  # Initial prey population
y10 = 10  # Initial population of predator species 1
y20 = 2  # Initial population of predator species 2
y0 = [x0, y10, y20]


fig, ax = plt.subplots()
heatmap = ax.imshow(data, cmap='hot', interpolation='nearest')

t = np.linspace(0, 500, 1000)
y = odeint(comp, [10,10,2], t, args=(alpha, beta, delta, gamma, tenma, f, g))
g=(y[:,0])
g1= (y[:,1])
g2 = (y[:,2])



for i in range (len(g)):
    print(1+int(int(g[i])%16))

prev_value = 0
def update(frame):
    if frame% 1 == 0:
        ax.grid(True, color='grey', linewidth=1)
    global prev_value 
    if int(g1[frame]) < int(prev_value):
        data.fill(0)
        
    if frame % 2 == 0:
        for i in range(0, 1+int(g1[frame]/16)):
            for j in range(0, 1+int(int(g1[frame])%16)):
                data[i, j] = 0.3
          
                
    prev_value = g1[frame]  
        
    
    heatmap.set_array(data)
    
    return heatmap,


ani = FuncAnimation(fig, update, frames=len(t), interval=100, blit=True)

plt.colorbar(heatmap)  
plt.title('Wolves heatmap')
plt.show()
