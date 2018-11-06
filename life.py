#!/usr/bin/env python3
""" conway's game of life """

import sys
import time
import curses

def init(width, height, seed):
    """ initialize universe """
    universe = [[]]*width
    for x in range(0, height):
        universe[x] = [False]*width
    for coord in seed:
        universe[coord[0]][coord[1]] = True
    return universe

def tick():
    """ advance one generation """
    nextgen = init(len(universe), len(universe[0]), [])
    for x in range(0, len(universe)):
        for y in range(0, len(universe[x])):
            cellstate = universe[x][y]
            nbcount = getnbcount([x, y])
            if cellstate:
                if nbcount < 2: nextgen[x][y] = False
                elif nbcount > 3: nextgen[x][y] = False
                else: nextgen[x][y] = True
            else:
                if nbcount == 3: nextgen[x][y] = True
    return nextgen

def simulate(window):
    """ simulate universe - wrapped funct for curses"""
    global universe
    for generation in range(1, generations):
        window.clear()
        window.addstr('Generation ' + str(generation) + '\n')
        for x in universe:
            line = ''
            for y in x:
                if y: line += '*'
                else: line += '.'
            line += '\n'
            window.addstr(line)
        window.refresh()
        time.sleep(1)
        universe = tick()

def getnbcount(cell):
    """ get count of living neighbors for cell """
    nbcount = 0
    x = cell[0]
    y = cell[1]
    nbcells = [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]
    for nbcell in nbcells:
        nbx = nbcell[0]
        nby = nbcell[1]
        if nbx < 0 or nby < 0: continue
        elif nbx >= width or nby >= height: continue
        if universe[nbx][nby]:
            nbcount += 1
    return nbcount

# global vars for initialization
# ToDo: get these from user (argparse ..)
width = 10
height = 10
generations = 20

# example seeds
glider = [[0,1],[1,2],[2,0],[2,1],[2,2]]
blinker = [[1,0], [1,1], [1,2]]
toad = [[1,1], [1,2], [1,3], [2,0], [2,1], [2,2]]

# main
universe = init(width, height, glider)
curses.wrapper(simulate)
