#!/usr/bin/env python

"""Draws a Levy flight using a Pareto distribution (started with PyGame stars.py example)"""

import random, math, pygame
from pygame.locals import *

#constants
WINSIZE = [800, 800]
WINCENTER = [400, 400]
DMAX = 240
# Pareto shape parameter
ALPHA = 1.5

def pareto():
    mode = 1.0
    return mode * pow(1.0 - random.random(), -1.0 / ALPHA) 

def next_point(prev):
    "choose next destination"
    angle = random.uniform(0,(2*math.pi))
#    angle = random.normalvariate(0,1.8)
#    distance = 2 * random.paretovariate(ALPHA)
    distance = 2 * pareto()
#    distance = 2 * random.weibullvariate(1.0, 0.9)
    # cap distance at DMAX
    if distance > DMAX:
        distance = DMAX
    point = [(math.sin(angle) * distance)+prev[0], (math.cos(angle) * distance)+prev[1]]
    return point

def main():
    random.seed()
    clock = pygame.time.Clock()
    #initialize and prepare screen
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('Levy Flight')
    white = 255, 240, 200
    black = 20, 20, 40
    screen.fill(black)

    done = False
    p = WINCENTER[:]
    while not done:
        # add point
        q = next_point(p)
        # draw line
        pygame.draw.line(screen, white, p, q, 1)
        p = q
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = True
                break
            elif e.type == MOUSEBUTTONDOWN and e.button == 1:
                # start a new random walk on click
                p = list(e.pos)
                screen.fill(black)
                break
        # run up to 90 FPS
        clock.tick(90)

# if python says run, then we should run
if __name__ == '__main__':
    main()



