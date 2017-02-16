#!/usr/bin/env python
from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

display(screen)

draw_line(0, 0, 250, 0, screen, color)
draw_line(0, 0, 250, 125, screen, color)
draw_line(0, 0, 250, 250, screen, color)
draw_line(0, 0, 125, 250, screen, color)
draw_line(0, 0, 0, 250, screen, color)
draw_line(0, 0, -125, 250, screen, color)
draw_line(0, 0, -250, 250, screen, color)
draw_line(0, 0, -250, 125, screen, color)
draw_line(0, 0, -250, 0, screen, color)
draw_line(0, 0, -250, -125, screen, color)
draw_line(0, 0, -250, -250, screen, color)
draw_line(0, 0, -125, -250, screen, color)
draw_line(0, 0, 0, -250, screen, color)
draw_line(0, 0, 125, -250, screen, color)
draw_line(0, 0, 250, -250, screen, color)
draw_line(0, 0, 250, -125, screen, color)

for i in range(-50,50):
    draw_line(i*5, 0, 0, -i*5, screen, color) 
    draw_line(-i*5, 0, 0, i*5, screen, [255,0,0]) 
    draw_line(0, 0, -i*5, i*5, screen, [0,0,255]) 
    draw_line(0, 0, i*5, -i*5, screen, [255,0,255]) 
    draw_line(i*5, 0,  -i*5, 0, screen, color) 
    draw_line(-i*5, 0, i*5, 0 ,screen, [255,0,0]) 
    draw_line(0, -i*5, 0, i*5, screen, [0,0,255]) 
    draw_line(0, i*5, 0, -i*5, screen, [255,0,255]) 
    draw_line(0, i*5, -i*5, 0, screen, color) 
    draw_line(0, -i*5, i*5, 0, screen, [255,0,0]) 
save_extension(screen, 'img.png')
