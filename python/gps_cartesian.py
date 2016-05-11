#!/usr/bin/env python
# Script for converting latitude,longitude to cartesian coordinates
# and back

from math import *

def toCartesian(lat,lon):
    lat,lon = map(radians,[lat,lon])
    R = 6467
    x = R * cos(lat)*cos(lon)
    y = R * cos(lat)*sin(lon)
    z = R * sin(lat)
    
    return x,y,z

def toSpherical(x,y,z):
    r = sqrt((x**2)+(y**2)+(z**2))
    lat = degrees(asin(z/r))
    lon = degrees(atan2(y,x))
    return lat,lon

lat = 53.3077
lon = -6.233015
print lat,lon
x,y,z = toCartesian(lat,lon)
print x,y,z
lat2,lon2 = toSpherical(x,y,z)
print lat2,lon2
