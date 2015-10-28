from __future__ import division

def find_intersection(p0,p1,p2,p3):
    x1=p1[0]-p0[0]
    y1=p1[1]-p0[1]
    x2=p3[0]-p2[0]
    y2=p3[1]-p2[1]
    
    denom = x1*y2-x2*y1
    
    if denom==0: return None#collinear
    denom_is_positive=denom>0
    
    x3=p0[0]-p2[0]
    y3=p0[1]-p2[1]
    
    s_numer = x1*y3-y1*x3
    
    if (s_numer<0)==denom_is_positive: return None#no collision
    
    t_numer = x2*y3-y2*x3
    
    if (t_numer<0)==denom_is_positive: return None#no collision
    
    if (s_numer>denom)==denom_is_positive or (t_numer>denom)==denom_is_positive: return None#no collision
    
    #collision detected
    
    t=t_numer/denom
    
    intersection_point = [p0[0]+(t*x1),p0[1]+(t*y3)]
    return intersection_point

# Create input data.
# black lines
line_segments = [[(1,4), (4,4)], [(2,3), (5,3)], [(3,2), (6,2)], [(6.5, 1), (7,1)], [(7.5, 0), (8.5,0)]]
# red lines
test_segments = [[(4.5,0), (4.5,4.5)], [(6.25, 0), (6.25, 4.5)]]

# Check all lines for intersections
intersections = set()
for test_segment in test_segments:
    for line_segment in line_segments:
        p0, p1 = test_segment[0], test_segment[1]
        p2, p3 = line_segment[0], line_segment[1]
        result = find_intersection(p0, p1, p2, p3)
        if result is not None:
            intersections.add(tuple(result))

print intersections
