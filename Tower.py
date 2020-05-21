from Row import Row

class Tower:

    def __init__(self, width, height, numBlocks, blockHeight, colour):
        self.topLeftX = (width - numBlocks*blockHeight)/2
        self.topLeftY = height-blockHeight
        bottomRow = Row(self.topLeftX, self.topLeftY, numBlocks)
        self.currLevel = 1
        self.towerLevels = {self.currLevel: bottomRow}
        self.colour = colour

    def addRow(self, newTopLeftX, newTopLeftY, numBlocksToAdd):
        self.topLeftX = newTopLeftX
        self.topLeftY = newTopLeftY
        self.currLevel += 1
        self.towerLevels[self.currLevel] = Row(newTopLeftX, newTopLeftY, numBlocksToAdd)
        


    