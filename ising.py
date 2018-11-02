# Project 2 - Ferromagnetism
#

import math                          # importing math
import random                        # importing random
import numpy as np                   # importing numpy
import matplotlib.pyplot as plt      # importing plots
import matplotlib.animation as animation  # importing animations

# creating a 50x50 grid of numbers between -1 and 1
grid = np.random.uniform(-1, 1, (50,50))
# changing the floats to intergers
grid[grid > 0] = 1
grid[grid < 0] = -1
# wrapping the grid at the boundaries 
grid = np.pad(grid, (1,1), 'wrap')

# calculating H(sigma)
h = 0                           # setting h to be 0
for c in range(50):             # for loop for rows
    for v in range(50):         # nested for loop for columns
        centre = grid[c,v]      # assigning the working term to a variable
        en = (centre*grid[c+1, v]) + (centre*grid[c-1,v]) + (centre*grid[c,v+1]) + (centre*grid[c,v-1])
        h=+en                   # adding each iteration of en to h
hsig = h/2                      # dividing h to account for repeated calculations
#print(hsig)

# calculating H(sigma)' when a random electron is flipped 
def spin():
    for c in range(1):
        random.randint(0,51)    # choosing a random row
    for v in range(1):
        random.randint(0,51)    # choosing a random column
    grid[c,v] = grid[c,v]*-1    # flipping the sign of the random electron
    h = 0                       # setting h to 0
    for b in range(50):         # for loop for rows
        for n in range(50):     # nested for loop for columns
            centre = grid[b,n]  # setting the working item to a variable
            en = (centre*grid[b+1, n]) + (centre*grid[b-1,n]) + (centre*grid[b,n+1]) + (centre*grid[b,n-1])
            h=+en               # adding each iteration of en to h
    hsig = h/2                  # dividing h by 2 to account for the repeated calculations
    return hsig                 # returning H(sigma)'
print(spin())                   # running the function spin()

# choosing which H(sigma) to take as energy
def roll():
    s = spin()                  # securing the value from spin()
    if s < hsig:                # if H(sigma)' is smaller than H(sigma)
        return s                # keep H(sigma)' as the energy
    else:                       # if H(sigma) is smaller than H(sigma)'
	Prob = np.exp((-1*s + hsig)/T)  # calculating the probability H(sigma) will be taken as energy
        return Prob             #returning the probability
T = 5                           #test temperature
print(roll())                   #running the function roll()
