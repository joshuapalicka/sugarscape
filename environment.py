'''
Created on 2010-04-18

@author: rv
'''
from math import sqrt
from itertools import product
import random


class Environment:
    '''
    classdocs
    '''

    def __init__(self, size):
        '''
        Constructor
        '''
        (width, height) = size
        self.gridWidth = width
        self.gridHeight = height
        self.grid = [[[0, 0, 0, 0, None] for __ in range(width)] for __ in
                     range(  # was sugar, capacity, agent. now sugar, spice, sugar capacity, spice capacity, agent
                         height)]  # indexed by: [i][j][0] = sugar capacity (amt currently stored), [i][j][1] = spice capacity (amt currently stored), [i][j][2] = maxSugarCapacity, [i][j][3] = maxSpiceCapacity, [i][j][4] = agent

    def setCapacity(self, location, value, sugar=True):
        if sugar:
            (i, j) = location
            self.grid[i][j][0] = value
        else:
            (i, j) = location
            self.grid[i][j][1] = value

    def getCapacity(self, location, sugar=True):
        if sugar:
            (i, j) = location
            return int(self.grid[i][j][0])
        else:
            (i, j) = location
            return int(self.grid[i][j][1])

    def decCapacity(self, location, value, sugar=True):
        (i, j) = location
        if sugar:
            self.grid[i][j][0] = max(0, self.grid[i][j][2] - value)
        else:
            self.grid[i][j][1] = max(0, self.grid[i][j][3] - value)

    def addSugarSite(self, location, maxCapacity):
        # calculate radial dispersion of capacity from maxCapacity to 0
        (si, sj, r) = location
        distance = lambda di, dj: sqrt(di * di + dj * dj)
        D = distance(max(si, self.gridWidth - si), max(sj, self.gridHeight - sj)) * (r / float(self.gridWidth))
        for i, j in product(range(self.gridWidth), range(self.gridHeight)):
            c = min(1 + maxCapacity * (1 - distance(si - i, sj - j) / D), maxCapacity)
            if c > self.grid[i][j][2]:
                self.grid[i][j][2] = c

    def addSpiceSite(self, location, maxCapacity):
        # calculate radial dispersion of capacity from maxCapacity to 0
        (si, sj, r) = location
        distance = lambda di, dj: sqrt(di * di + dj * dj)
        D = distance(max(si, self.gridWidth - si), max(sj, self.gridHeight - sj)) * (r / float(self.gridWidth))
        for i, j in product(range(self.gridWidth), range(self.gridHeight)):
            c = min(1 + maxCapacity * (1 - distance(si - i, sj - j) / D), maxCapacity)
            if c > self.grid[i][j][3]:
                self.grid[i][j][3] = c

    def grow(self, alpha, sugar=True):
        # grow to maxCapacity with alpha 
        for i, j in product(range(self.gridWidth), range(self.gridHeight)):
            if sugar:
                self.grid[i][j][0] = min(self.grid[i][j][0] + alpha, self.grid[i][j][2])
            else:
                self.grid[i][j][0] = min(self.grid[i][j][0] + alpha, self.grid[i][j][2])  # if spice, grow both
                self.grid[i][j][1] = min(self.grid[i][j][1] + alpha, self.grid[i][j][3])

    def growRegion(self, region, alpha, sugar=True):
        # grow  region to maxCapacity with alpha
        (imin, jmin, imax, jmax) = region
        imin = max(imin, 0)
        jmin = max(jmin, 0)
        imax = min(imax + 1, self.gridWidth)
        jmax = min(jmax + 1, self.gridHeight)
        for j in range(jmin, jmax):
            for i in range(imin, imax):
                if sugar:
                    self.grid[i][j][0] = min(self.grid[i][j][0] + alpha, self.grid[i][j][2])
                else:
                    self.grid[i][j][1] = min(self.grid[i][j][1] + alpha, self.grid[i][j][3]) # TODO: make similar to grow?

    def setAgent(self, location, agent):
        (i, j) = location
        self.grid[i][j][4] = agent

    def getAgent(self, location):
        (i, j) = location
        return self.grid[i][j][4]

    def isLocationValid(self, location):
        (i, j) = location
        return 0 <= i < self.gridWidth and 0 <= j < self.gridHeight

    def isLocationFree(self, location):
        (i, j) = location
        return self.grid[i][j][4] is None

    def getRandomFreeLocation(self, location):
        # build a list of free locations i.e. where env.getAgent(x,y) == None
        # we don't use a global list and we re-build the list each time 
        # because init a new agent is much less frequent than updating agent's position (that would require append / remove to the global list)
        (xmin, xmax, ymin, ymax) = location
        freeLocations = [(i, j) for i, j in product(range(xmin, xmax), range(ymin, ymax)) if not self.grid[i][j][2]]
        # return random free location if exist
        if len(freeLocations) > 0:
            return freeLocations[random.randint(0, len(freeLocations) - 1)]
        return None
