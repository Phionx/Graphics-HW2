#!/usr/bin/env python
from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if (x0 > x1) or ((x0 == x1) and (y1 > y0)):
        x = x0
        y = y0
        x0 = x1
        y0 = y1
        x1 = x
        y1 = y
        

    x = x0
    y = y0
    A = y1-y0
    B = -x1+x0
    
    
    if (y1 - y0)*(x1 - x0) > 0:
        if (y1 - y0) >= (x1 - x0):
            d = A + 2*B
            while (x <  x1):
                plot(screen, color, x + 250,y + 250)
                if (d < 0 ):
                    x+=1
                    d+=2*A
                y+=1
                d+=2*B
            print "Octant II\n"
        else:
            d = 2*A + B
            while (x <  x1):
                plot(screen, color, x + 250,y + 250)
                if (d > 0 ):
                    y+=1
                    d+=2*B
                x+=1
                d+=2*A
            print "Octant I\n"
    else:
        if (y1 - y0) <= -1*(x1 - x0):
            d = A-2*B
            while (x <  x1) or (y != y1):
                plot(screen, color, x + 250,y + 250)
                if (d > 0 ):
                    x+=1
                    d+=2*A
                y-=1
                d-=2*B
            print "Octant VII\n"
        else:
            d = 2*A - B
            while (x <  x1):
                plot(screen, color, x + 250,y + 250)
                if (d < 0 ):
                    y-=1
                    d-=2*B
                x+=1
                d+=2*A
            print "Octant VIII\n"


