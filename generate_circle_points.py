#!/usr/bin/env python
from math import *

def vincenty_direct(init_bearing,distance,lat,lon):
    '''
        Vincenty Direct Formula
        @init_bearing = initial bearing
        @distance = distance from point
        @lat = current latitude
        @lon = current longitude

        returns latitude,longitude,final bearing
    '''
    angleRadHeading = radians(init_bearing)
    lat0 = radians(lat) #Current lat point converted to radians
    lon0 = radians(lon) #Current long point converted to radians

    a = 6378388
    b = 6356911.946
    f = 1.0/297.0

    sina1 = sin(angleRadHeading)
    cosa1 = cos(angleRadHeading)

    tanU1 = (1-f) * tan(lat0)
    cosU1 = 1.0 / sqrt((1+tanU1*tanU1))
    sinU1 = tanU1 * cosU1

    sigma1 = atan2(tanU1,cosa1)
    sina = cosU1 * sina1
    cosSqa = 1 - sina*sina
    uSq = cosSqa * (a*a-b*b)/(b*b)
    A = 1 + uSq/16384*(4096+uSq*(-768+uSq*(320-175*uSq)))
    B = uSq/1024 * (256+uSq*(-128+uSq*(74-47*uSq)))

    cos2sigmaM = 0.0
    sinsigma = 0.0
    cossigma = 0.0
    delta_sigma = 0.0

    sigma = distance / (b*A)
    sigma_transpose = 0.0
    iterations = 0
    value = True
    while value:
        cos2sigmaM = cos(2*sigma1+sigma)
        sinsigma = sin(sigma)
        cossigma = cos(sigma)
        delta_sigma = B*sinsigma*(cos2sigmaM+B/4*(cossigma*(-1+2*cos2sigmaM*cos2sigmaM)-B/6*cos2sigmaM*(-3+4*sinsigma*sinsigma)*(-3+4*cos2sigmaM*cos2sigmaM)))
        sigma_transpose = sigma
        sigma = distance / (b*A) + delta_sigma
        if fabs(sigma-sigma_transpose) > 1e-12 and ++iterations<200:
            value = False
    if iterations>=200:
        raise Exception("Formula failed to converge")

    x = sinU1*sinsigma - cosU1*cossigma*cosa1
    lat2 = atan2(sinU1*cossigma + cosU1*sinsigma*cosa1,(1-f)*sqrt(sina*sina+x*x))
    delta = atan2(sinsigma*sina1,cosU1*cossigma - sinU1*sinsigma*cosa1)

    C = f/16.0*cosSqa*(4+f*(4-3*cosSqa))
    L = delta - (1-C) * f * sina * (sigma + C*sina*(cos2sigmaM+C*cossigma*(-1+2*cos2sigmaM*cos2sigmaM)))
    lon2 = (lon0+L+3*pi)%(2*pi) - pi#normalise to -180...+180

    a2 = atan2(sina,-x)
    a2 = (a2+2*pi)%(2*pi)#normalise to 0...360

    return degrees(lat2),degrees(lon2),degrees(a2)

def generate_circle_points(radius,starting_degree,step,lat,lng):
    '''
        generates gps points around a center
        with a given radius and a step difference between
        each coordinate
    '''
    points = []
    angle = starting_degree
    full_circle = 0
    running=False
    while not running:
        points.append(vincenty_direct(angle,radius,lat,lng))
        if (full_circle > 360):
            running = True
        else:
            angle += step
            full_circle += step
    return points

def generate_spiral_path(lat,lng,max_distance,distance_step,bearing_step):
    '''
        Given a gps coorindate, the max distance from the center
        the difference between each distance step
        and the difference in angle between each step

        the function will return a list of points and bearings
        from the center in a spiral pattern
    '''
    distance = distance_step
    bearing = bearing_step
    points = []
    while distance < max_distance:
        points.append(vincenty_direct(bearing,distance,lat,lng))
        bearing += bearing_step
        if(bearing>360): bearing -= 360
        distance += distance_step
    return points

def generate_square_points(radius,lat,lng,angles):
    points = []
    for angle in angles:
        n_lat,n_lng,n_bearing = vincenty_direct(angle,radius,lat,lng)
        points.append((n_lat,n_lng))
    return points

def generate_hexagon_points(radius):
    return generate_circle_points(radius,0.0,60.0,53.307296,-6.232311)

if __name__=='__main__':
    print "uses degrees not radians for step"
    circle = generate_circle_points(15.0,0.0,60.0,53.307296,-6.232311)
    print "points generated"
    for (a,b,c) in circle: print "%s,%s"%(a,b)

    print "Also does squares"
    square = generate_square_points(15,53.307296,-6.232311,[45,135,225,315])
    print square
    for s in square: print s[0],",",s[1]
