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
    target = points[random.randint(0, 2)]
    x = x - (x - target[0]) / 2
    y = y - (y - target[1]) / 2
    point(x, y)

if __name__ == '__main__':
    run()
""""
JAVASCRIPT PORT TO PYTHON


// Chaos Game

console.log("Chaos Game");

let points = [{
    x: 200,
    y: 0
}, {
    x: 0,
    y: 400
}, {
    x: 400,
    y: 400
}];
let x = 200;
let y = 200;

function setup() {
    createCanvas(400, 400);
    background(220);
    text('Chaos Game', 10, 20);
}

function draw() {
    let target = random(points);
    x = x - (x - target.x) / 2;
    y = y - (y - target.y) / 2;
    point(x, y);
}
"""