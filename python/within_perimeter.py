import sys,csv
from math import *

def futureGPSposition(d,lat,lng,heading):
    radiusEarthKm = 6371
    radiusEarthM = radiusEarthKm * 1000
    bearing = radians(heading)

    newlat = degrees((d/radiusEarthM) * cos(bearing)) + lat
    newlng = degrees((d/(radiusEarthM*sin(radians(newlat)))) * sin(bearing)) + lng
    return newlat,newlng

def simpleWithin(coordinates,lat,lng):
    #print "Checking if",lat,",",lng,"is within perimeter"
    lat = degrees(lat)
    lng = degrees(lng)
    j = len(coordinates)-1
    pointStatus = False
    for i in xrange(0,len(coordinates)):
        lati = degrees(float(coordinates[i][0]))
        latj = degrees(float(coordinates[j][0]))
        lngi = degrees(float(coordinates[i][1]))
        lngj = degrees(float(coordinates[j][1]))

        if (lngi < lng and lngj >= lng) or (lngj < lng and lngi >= lng):
            if lati + (lng - lngi) / (lngj - lngi) * (latj - lati) < lat:
                pointStatus = not(pointStatus)
        j = i
    return pointStatus
