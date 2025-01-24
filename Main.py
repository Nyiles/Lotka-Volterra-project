# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:18:04 2024

@author: nicny
"""

import pygame
import random
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

"""
Welcome to a predator prey game which uses differential equations to predict the growth 
rate of both 2 selected predators and a selected prey. We can then continously integrate the differential
to find the overall population of a selected species. 
"""
# initializing the game and creating the screen of the game, which we can manipulate into a board later
pygame.init()

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# all the helpful color codes used throughout the game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
grey = (128,128,128)
green = (0,100,0)
brown = (165,42,42)
orange = (255,165,0)
# printing the intital lists which will hold all of the species
# also creating the starting positions for all of the species
orgposx = []
orgposy = []
orgposwovx = []
orgposwovy = []
orgposfoxx = []
orgposfoxy = []

existing = set(zip(orgposx,orgposy))
"""
while (len(orgposwovx ) <10):
    

    rand1 = random.randint(0, 15)*50
    rand2 = random.randint(0, 15)*50
    newpos = (rand1,rand2)
    
    if newpos not in existing:
        orgposwovx.append(rand1)
        orgposwovy.append(rand2)
        existing.add(newpos)

while (len(orgposbearx ) <2):

    rand1 = random.randint(0, 15)*50
    rand2 = random.randint(0, 15)*50
    newpos = (rand1,rand2)
    
    if newpos not in existing:
        orgposbearx.append(rand1)
        orgposbeary.append(rand2)
        existing.add(newpos)
"""      

num = random.randint(5, 80)
randfirst = []
randsecond = []
for i in range (0,num):
    randfirst.append(random.randint(0, 15)*50)
    randsecond.append(random.randint(0, 15)*50)
print(randfirst)
print(randsecond)
def draw_grass():
    for i in range (len(randfirst)):
        pygame.draw.line(screen, green,(randfirst[i],randsecond[i]), (randfirst[i],randsecond[i]-10),3 )
        pygame.draw.line(screen, green,(randfirst[i],randsecond[i]), (randfirst[i]-10,randsecond[i]-15),3 )
        pygame.draw.line(screen, green,(randfirst[i],randsecond[i]), (randfirst[i]+10,randsecond[i]-10),3 )
        

    
def draw_fox(t):
    for i in range(t):
        rand1 = random.randint(0, 15)*50
        rand2 = random.randint(0, 15)*50
        orgposfoxx.append(rand1)
        orgposfoxy.append(rand2)
    for i in range(t):
        pygame.draw.arc(screen, orange, (orgposfoxx[i]+5, orgposfoxy[i]+10, 32,18), np.pi, np.pi*2, 5)
        pygame.draw.ellipse(screen,orange,(orgposfoxx[i]+6, orgposfoxy[i]+20,10,10))
        pygame.draw.ellipse(screen,orange,(orgposfoxx[i]+26, orgposfoxy[i]+20,10,10))
        pygame.draw.ellipse(screen,orange,(orgposfoxx[i]+33, orgposfoxy[i]+14,10,7))
        pygame.draw.arc(screen, WHITE, (orgposfoxx[i], orgposfoxy[i]+20, 8,16), np.pi/2,3*np.pi/2,5)
        pygame.draw.line(screen, orange, (orgposfoxx[i]+10,orgposfoxy[i]+25), (orgposfoxx[i]+10,orgposfoxy[i]+40),4)
        pygame.draw.line(screen, orange, (orgposfoxx[i]+30,orgposfoxy[i]+25), (orgposfoxx[i]+30,orgposfoxy[i]+40),4)    
        
# designing of the bunnies
def draw_bunnies(t):
    
    for i in range(t):
        rand1 = random.randint(0, 15)*50
        rand2 = random.randint(0, 15)*50
        orgposx.append(rand1)
        orgposy.append(rand2)

    for i in range(t):
        pygame.draw.arc(screen, WHITE, (orgposx[i]+10, orgposy[i]+23, 30,25), 0, 3.14, 8)

        pygame.draw.ellipse(screen,WHITE,(orgposx[i]+12, orgposy[i]+32,12,6))
        pygame.draw.ellipse(screen,WHITE,(orgposx[i]+25, orgposy[i]+20,20,10))
        pygame.draw.arc(screen, WHITE, (orgposx[i]+10, orgposy[i]+10, 30,25), 0, np.pi/3, 3)
        pygame.draw.ellipse(screen,WHITE,(orgposx[i]+6, orgposy[i]+20,10,10))
        pygame.draw.ellipse(screen,BLACK,(orgposx[i]+36, orgposy[i]+22,4,4))
# designing of the wolves
def draw_wolves(t):
    for i in range(t):
        rand1 = random.randint(0, 15)*50
        rand2 = random.randint(0, 15)*50
        orgposwovx.append(rand1)
        orgposwovy.append(rand2)
        
    for i in range(t):
        pygame.draw.arc(screen, grey, (orgposwovx[i]+5, orgposwovy[i]+10, 32,18), np.pi, np.pi*2, 5)
        pygame.draw.ellipse(screen,grey,(orgposwovx[i]+6, orgposwovy[i]+20,10,10))
        pygame.draw.ellipse(screen,grey,(orgposwovx[i]+26, orgposwovy[i]+20,10,10))
        pygame.draw.ellipse(screen,grey,(orgposwovx[i]+33, orgposwovy[i]+14,10,7))
        pygame.draw.arc(screen, grey, (orgposwovx[i], orgposwovy[i]+20, 8,16), np.pi/2,3*np.pi/2,5)
        pygame.draw.line(screen, grey, (orgposwovx[i]+10,orgposwovy[i]+25), (orgposwovx[i]+10,orgposwovy[i]+40),4)
        pygame.draw.line(screen, grey, (orgposwovx[i]+30,orgposwovy[i]+25), (orgposwovx[i]+30,orgposwovy[i]+40),4)    
# makeing the board a 256 tiled chess-style board
# making the board tiled, with a different shade of green
# each tile is 50 long and 50 wide
def draw_board():
    for i in range (16):
        for j in range(16):
            if ((i+j) % 2 == 0):
                c = "dark green"
            else :
                c = "light green"
            pygame.draw.rect(screen,c,(i*50,j*50,48,48))
   

def collisions():
                
                orgposx.pop(0)
                orgposy.pop(0)
            
                return  
            
def collisions1():
                
                orgposwovx.pop(0)
                orgposwovy.pop(0)
            
                return 

def collisions2():
                
                orgposfoxx.pop(0)
                orgposfoxy.pop(0)
            
                return 

def comp(y, t, alpha, beta, delta, gamma, tenma, f, g):
    x, y1, y2 = y
    dxdt =  alpha * x - beta * x * (y1) - tenma * x * (y2)
    dy1dt = delta * beta * x * y1 - gamma * y1
    dy2dt = delta * beta * x * y2 - gamma * y2
    return [dxdt, dy1dt, dy2dt]



def lotka_volterra(y, t, alpha, beta, delta, gamma, tenma, f, g):
    x, y1, y2 = y
    dxdt =  alpha * x - beta * x * (y1) - tenma * x * (y2)
    dy1dt = delta * beta * x * y1 - gamma * y1
    dy2dt = delta * tenma * x * y2 - gamma * y2
    return [dxdt, dy1dt, dy2dt]

# whenever the growth rates spews out a negative, one of the wolves naturally dies

    

# Define parameters
alpha = 0.1  # Prey birth rate
beta = 0.05  # Predation rate
delta = 0.1  # Conversion efficiency
gamma = 0.1  # Predator death rate
tenma = 0.02 # predation rate for predator 2
f = 0.02 # conversion rate for predator 2
g = 0.1 # # death rate for predator 2
x0 =10  # Initial prey population
y10 = 10  # Initial population of predator  1
y20 = 2  # intiial population of predator 2
y0 = [x0, y10, y20]
run = True
count = 0
num =0
num1= 0
t = np.linspace(0,500,501)
clock = pygame.time.Clock()
countbun = []
countwolf = []
while run:
    screen.fill('brown')
    y = odeint(lotka_volterra, y0, t, args=(alpha, beta, delta, gamma, tenma, f, g))
    g=(y[:,0])
    g1= (y[:,1])
    g2 = (y[:,2])
    
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        elif event.type == pygame.KEYDOWN:
            count += 1
            
                 
    clock.tick(5)
    draw_board()
  
    draw_bunnies(math.ceil(g[count]))
    draw_wolves(math.ceil(g1[count]))
    
    draw_fox(math.ceil(g2[count]))
    collisions()
    collisions1()
    collisions2()
    draw_grass()
    pygame.display.flip()
    

pygame.quit()
#%%
t = np.linspace(0, 400, 1000)

# Solve the ODEs
y = odeint(comp, [10,10,2], t, args=(alpha, beta, delta, gamma, tenma, f, g))
g = y[:,0]
g1 = y[:,1]
g2 = y[:,2]
fig= plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot([], [], 'k-', label='Prey (Rabbits)')
line2, = ax.plot([], [], 'r-', label='Predator (Wolves)')
line3, = ax.plot([], [], 'b-', label='Predator (Foxes)')

ax.legend(loc='best')
ax.set_xlim(0,max(t))
ax.set_ylim(0,1.1*max(g))
ax.set_xlabel('Time')
ax.set_ylabel('Population')
plt.show()
def update(i):

    line1.set_data(t[:i],g[:i])
    line2.set_data(t[:i],g1[:i])
    line3.set_data(t[:i],g2[:i])
    
    
    
ani = FuncAnimation(fig, update, frames=len(t), interval =20, repeat_delay = 300)


