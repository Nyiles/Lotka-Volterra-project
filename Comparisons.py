# -*- coding: utf-8 -*-
"""
Created on Fri May  3 09:40:10 2024

@author: nicny
"""


import pygame
import random
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

def comp(y, t, alpha, beta, delta, gamma):
    x, y = y
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]
alpha = 0.1  # Prey birth rate
beta = 0.05  # Predation rate
delta = 0.1  # Conversion efficiency
gamma = 0.1  # Predator death rate
x0 =10  # Initial prey population
y10 = 10  # Initial population of predator 1
# Initial population of predator 2
y0 = [x0, y10]

t = np.linspace(0, 400,500)
y = odeint(comp, y0, t, args=(alpha, beta, delta, gamma))



plt.figure()

plt.plot(t, y[:, 0], 'r-', label='Prey (Rabbits)')
plt.plot(t,y[:, 1], 'b-', label='Predator (Wolves)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend(loc = 'best')
plt.show()


alpha = 0.1  # Prey birth rate
beta = 0.05  # Predation rate
delta = 0.02  # Conversion efficiency
gamma = 0.1  # Predator death rate
x0 =10  # Initial prey population
y10 = 2  # Initial population of predator species 1
# Initial population of predator species 2
y0 = [x0, y10]

t = np.linspace(0, 400,500)
y = odeint(comp, y0, t, args=(alpha, beta, delta, gamma))



plt.figure()

plt.plot(t, y[:, 0], 'r-', label='Prey (Rabbits)')
plt.plot(t,y[:, 1], 'b-', label='Predator (Foxes)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend(loc = 'best')
plt.show()



def lotka_volterra(y, t, alpha, beta, delta, gamma, tenma, f, g):
    x, y1, y2 = y
    dxdt =  alpha * x - beta * x * (y1) - tenma * x * (y2)
    dy1dt = delta * beta * x * y1 - gamma * y1
    dy2dt = f * tenma * x * y2 - g * y2
    return [dxdt, dy1dt, dy2dt]

alpha = 0.3# Prey birth rate
beta = 0.2  # Predation rate
delta = 0.3  # Conversion efficiency
gamma = 0.1  # Predator death rate
tenma = 0.1
f = 0.2
g = 0.1

x0 =20 # Initial prey population
y10 = 5  # Initial population of predator 1
y20 =10  # Initial population of predator 2
y0 = [x0, y10, y20]
print(t)
y = odeint(lotka_volterra, y0, t, args=(alpha, beta, delta, gamma, tenma, f, g))
g=(y[:,0])
g1= (y[:,1])
g2 = (y[:,2])

plt.figure()
plt.plot(t, g, 'r-', label='Prey (Rabbits)')
plt.plot(t,g1, 'b-', label='Predators (Wolves)')
plt.plot(t,g2, 'y-', label='Predators (Foxes)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend(loc = 'best')
plt.show()



