from math import cos,sin

def create_rectangle(lat,lon,height,width):
    edges = []
    edges.append( lat+height/2 * 90/100000000 )
