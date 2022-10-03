from p5 import *
import random

points = [[200,10],[10,390],[390,390]]
x = 200
y = 200

def setup():
    size(400, 400)
    background(220)
    text('Chaos Game', 10, 20)
    # no_loop()

def draw():
    global x
    global y
    i = 0
    while i < 10:
        target = points[random.randint(0, 2)]
        x = x - (x - target[0]) / 2
        y = y - (y - target[1]) / 2
        point(x, y)
        i+=1

if __name__ == '__main__':
    run()