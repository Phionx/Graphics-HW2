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
save_extension(screen, 'img.png')
