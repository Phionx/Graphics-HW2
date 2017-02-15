#!/usr/bin/env python
from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

display(screen)
draw_line(10, 10, 200, 200, screen, color)
save_extension(screen, 'img.png')
