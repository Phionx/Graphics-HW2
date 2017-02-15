#!/usr/bin/env python
from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x0 = x0+250
    y0 = y0+250
    x1 = x1+250
    y1 = y1+250

    x = x0
    y = y0
    A = y1-y0
    B = -x1+x0

    if (y1 - y0)*(x1 - x0) > 0:
        if(y1 - y0)/(x1 - x0) >= 1:
            d = A + 2*B
            while (x <  x1):
                plot(screen, color, x,y)
                if (d < 0 ):
                    x+=1
                    d+=2*A
                y+=1
                d+=2*B
        else:
            d = 2*A + B
            while (x <  x1):
                plot(x,y)
                if (d > 0 ):
                    y+=1
                    d+=2*B
                x+=1
                d+=2*A
    else:
        if(y1 - y0)/(x1 - x0) <= -1:
            d = A-2*B
            while (x <  x1):
                plot(x,y)
                if (d > 0 ):
                    x+=1
                    d+=2*A
                y-=1
                d-=2*B
        else:
            d = 2*A - B
            while (x <  x1):
                plot(x,y)
                if (d < 0 ):
                    y-=1
                    d-=2*B
                x+=1
                d+=2*A


