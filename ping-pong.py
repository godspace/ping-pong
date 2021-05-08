from pygame import *

W = 800
H = 400
window = display.set_mode((W,H))
clock = time.Clock()

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
           game = False 
    window.fill((50,150,50))
    display.update()
    clock.tick(24)