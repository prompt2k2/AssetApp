from turtle import *
from random import randint, random

while True:
    up()
    goto(randint(-400,400), randint(-400,400))
    down()
    R = random()
    B = random()
    G = random()
    
    color(R, B, G)
    dot(randint(20,80))