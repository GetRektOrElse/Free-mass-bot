from math import sin, cos, tan, asin, acos, atan, pi
import pyautogui as gui

def coords(center, radius, angle):
    offset = (round(radius * sin(angle), 3), -round(radius * cos(angle), 3))
    return tuple(a + b for a, b in zip(center, offset))

def rotate(center, radius, seconds, points):
    unit_angle = 2 * pi / points
    for i in range(points):
        gui.moveTo(*coords(center, radius, i * unit_angle), seconds/points)

gui.keyDown('w')
for i in range(15):
    rotate([i/2 for i in gui.size()], 400, 0, 20)
gui.keyUp('w')
