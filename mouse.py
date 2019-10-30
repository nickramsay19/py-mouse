from pynput.mouse import Button, Controller
import random
import time

mouse = Controller()

# Read pointer position
#print('The current pointer position is {0}'.format(
    #mouse.position))

# Set pointer position
#mouse.position = (10, 20)
#print('Now we have moved it to {0}'.format(
    #mouse.position))

# Move pointer relative to current position
#mouse.move(5, -5)

# Press and release
#mouse.press(Button.left)
#mouse.release(Button.left)

# Double click; this is different from pressing and releasing
# twice on Mac OSX
#mouse.click(Button.left, 2)

# Scroll two steps down
#mouse.scroll(0, 2)

annoyance_factor = 1 # between 0 and 1

click = True
ot = int(round(time.time() * 1000))
lt = 0

while True:

    # scroll 
    #if random.randint(0, 5000) == 0:
        #mouse.scroll(0, random.randint(0, 10) - 5)

    # click


    #if a % 5000 == 0:
        #if b == 0:
            #mouse.press(Button.left)
            #b = 1
        #else:
            #mouse.release(Button.left)
            #b = 0

    t = int(round(time.time() * 1000)) - ot

    if t % 750 == 0 and t != lt:
        mouse.press(Button.left)
        mouse.release(Button.left)
            

        click = not click
        print(t)
        
    lt = t

    #print(int(round(time.time() * 1000)) - ot)
    

    # move the mouse
    #x, y = 0, 0

    #if random.randint(0, 90) == 0:
        #x = random.randint(0, 4) - 2
    #if random.randint(0, 90) == 0:
        #y = random.randint(0, 4) - 2

    #mouse.move(x, y)