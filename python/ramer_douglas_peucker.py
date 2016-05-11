import math
from __future__ import division

def DouglasPeucker(Pointlist,epsilon=math.eps):
    if len(Pointlist) < 2: return Pointlist
    dmax = 0.0
    index = 0
    end = len(Pointlist)
    ResultList = []
    
    for i in xrange(2,end-1):
        d = shortestDistanceToSegment(Pointlist[i],Line(Pointlist[1],Pointlist[end]))
        if d > dmax:
            index = i
            dmax = d
     #If max distance is greater than epsilon, recursively simplify
     if dmax > epsilon:
        #recursive call
        recResults1 = DouglasPeucker(Pointlist[1:index],epsilon)
        recResults2 = DouglasPeucker(Pointlist[index:end],epsilon)
        
        ResultList
     else:
        ResultList = [Pointlist[1],Pointlist[end]]
     # return the result
     return ResultList

def shortestDistanceToSegment():
    #
