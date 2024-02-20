import os
import pygame as pg

keybindings = {
    #when user presses YES
    "action": pg.K_y,
    #Mario Actions
    "jump":pg.K_j,
    "right":pg.K_RIGHT,
    "left":pg.K_LEFT,
    "down": pg.K_DOWN,

}

#Controls the game
#Controls the main loop
#the event loops
class control(object)