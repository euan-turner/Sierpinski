from pygame.math import Vector2
from shapely.geometry import Point

def createShape(n,cx,cy):
    intAngle = int(360/n)
    vec = Vector2(cx-100,cy-100)
    verts = []
    ##Repeat first vertex to make points circular
    for _ in range(0,n+1):
        p = Point((cx+vec.x,cy+vec.y))
        verts.append(p)
        vec.rotate_ip(intAngle)
    return verts
