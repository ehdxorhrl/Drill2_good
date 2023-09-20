import math

from pico2d import *

open_canvas()

# fill here
grass=load_image('grass.png')
character=load_image('character.png')

x=0
y=90

def render_all(_x,_y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(_x, _y)
    delay(0.02)


def run_rectagle():
    print("rectagle")

    global x
    global y
    
    #bottom->right
    for x in range(50,750+10,10):
        render_all(x,y)

    for y in range(90,550+10,10):
        render_all(x,y)

    for x in range(750,50-10,-10):
        render_all(x,y)

def run_circle():
    cx,cy,r=400,300,200
    for deg in range(0,360,5):
        x=cx+r*math.cos(deg/360*2*math.pi)
        y=cy+r*math.sin(deg/360*2*math.pi)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.02)

while (True):
    run_rectagle()
    #run_circle()
    break


close_canvas()
