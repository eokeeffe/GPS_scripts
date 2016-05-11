#!/usr/bin/env python

from pylab import *

L=30.#length of a side
s=.52#the width of each path
dt=1.326# the time to make a turn
vf=1.607#walking speed
t=0#the time - it goes up

N=round(L/(2*s)+0.5) # how many sqaure

print "Number of sqaures",N

while N>0:
    t=t+(4*L)/vf + 4*dt
    L=L-2*s
    N=N-1
print "Time in seconds to complete:",t
