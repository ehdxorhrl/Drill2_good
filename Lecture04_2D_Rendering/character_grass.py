import math

from pico2d import *

open_canvas()

# fill here
grass=load_image('grass.png')
character=load_image('character.png')
x=0
y=90

def run_rectagle():
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(400, 90)
    delay(1)
    print("rectagle")
    pass

def run_circle():
    print("circle")
    pass

while (True):
    run_rectagle()
    run_circle()
    break


close_canvas()
