import pgzrun
import time
import random
speed = 3
WIDTH = 800
HEIGHT = 800

player = Actor('trent.png')


def draw():
 screen.clear()
 player.draw()
 
 def move_player(player):
if keyboard.left:
  player.x -= 1
elif keyboard.right:
  player.x += 1

def update():
  move_player()
  draw()

pgzrun.go()
