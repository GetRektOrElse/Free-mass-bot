import pyautogui as gui

while 1:
    x, y = gui.position()
    print('({}, {})'.format(x, y))
