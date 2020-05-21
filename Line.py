import random

class Line:

    def __init__(self, width, height, numBlocks, blockHeight, colour):
        self.numBlocks = numBlocks
        self.topLeftX = 0
        self.topLeftY = height - 2*blockHeight
        self.lineWidth = numBlocks*blockHeight
        self.dir = 1
        self.speed = 1000
        self.colour = colour

    def updateLevel(self, numFall, blockHeight, colour):
        self.numBlocks = self.numBlocks - numFall
        self.speed -= 100
        if self.speed < 150:
            self.speed = 150
        self.lineWidth = self.numBlocks*blockHeight
        self.topLeftX = 0
        self.topLeftY -= blockHeight
        if colour == 'random':
            rand1 = random.randint(0,255)
            rand2 = random.randint(0,255)
            rand3 = random.randint(0,255)
            self.colour = (rand1, rand2, rand3)