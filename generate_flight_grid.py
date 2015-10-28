#!/usr/bin/env python
from generate_circle_points import *
from within_perimeter import *
import numpy as np
import math

def creategrid(min_lon, max_lon, min_lat, max_lat, cell_size, mesh=False):
    '''
        Output grid within geobounds and specifice cell size
        cell_size_deg should be in decimal degrees
    '''
    # dense grid
    N = cell_size
    x = np.linspace(min_lat, max_lat, N)
    y = np.linspace(min_lon, max_lon, N)
    x, y = np.meshgrid(x, y)
    xgs, ygs = x.flatten(), y.flatten()
    return xgs,ygs

def pointToArray(points):
    '''
        split input points to longitude and latitude arrays

    '''
    # find x,y of map projection grid.
    lons=[]
    lats=[]
    for point in points:
        lons.append(point[1])
        lats.append(point[0])
    return lats,lons

if __name__=='__main__':
    perimeter = [(53.307655,-6.232907),
    (53.307098,-6.233088),
    (53.306938,-6.231717),
    (53.307496,-6.231533)]
    lats,lons = pointToArray(perimeter)
    #print lats,lons
    max_lng = max(lons)
    min_lng = min(lons)
    max_lat = max(lats)
    min_lat = min(lats)
    print min_lng,max_lng
    print min_lat,max_lat
    grid_lats,grid_lons = creategrid(min_lng,max_lng,min_lat,max_lat,5)
    #print grid_lons
    a = np.delete(grid_lons, 0)
    a = np.delete(grid_lons, 0)
    a = np.delete(grid_lats, 0)
    a = np.delete(grid_lats, 0)
    grid = np.vstack([grid_lats,grid_lons]).T
    #for i in xrange(len(grid_lons)): print "%.5f,%.5f"%(grid_lats[i],grid_lons[i])
    for point in grid:
        print "%.5f,%.5f"%(point[0],point[1])
