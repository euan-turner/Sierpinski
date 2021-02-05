from funcs import createShape
from shapely.geometry import Point, Polygon
import pygame,random

##Colours
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
red = (255,0,0)

window = pygame.display.set_mode((700,700))
window.fill(white)
pygame.display.flip()

sides = 4

verts = createShape(sides,window.get_width()/2,window.get_height()/2)
poly = Polygon(verts)
restricted = Polygon([(350,300),(400,350),(350,400),(300,350)])

for vert in verts:
    pygame.draw.circle(window,black,(int(vert.x),int(vert.y)),5,0)

pygame.draw.polygon(window,yellow,[(int(i.x),int(i.y)) for i in verts],0)
pygame.draw.polygon(window,red,[(int(i[0]),int(i[1])) for i in restricted.exterior.coords])
pygame.display.flip()

##Select starting point
valid = False
while not valid:
    point = Point((random.randint(200,500),random.randint(200,500)))
    if poly.contains(point) and (not restricted.contains(point)):
        valid = True


lastVertex = None
cont = True
while cont:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cont = False
            continue
    
    vertex = random.choice(verts[0:len(verts)-1])
    

    midpoint = Point((int((point.x+vertex.x)/2), int((point.y+vertex.y)/2)))
    if restricted.contains(midpoint):
        continue
    pygame.draw.circle(window,black,(int(midpoint.x),int(midpoint.y)),1,0)
    point = midpoint
    lastVertex = vertex
    pygame.display.flip()
