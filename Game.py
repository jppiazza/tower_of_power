import pygame
from Line import Line
from Tower import Tower
from time import sleep

pygame.init()

width = 600
height = 500
flashSpeed = 100

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tower of Power')

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
aqua = (0, 255, 255)
black = (0, 0, 0)

class Game:

    def __init__(self, blocks, blockHeight):
        self.blocks = blocks
        self.blockHeight = blockHeight
        self.gameOver = False
        self.flashNum = 6
        self.gameStarted = False

    def play(self):

        line = Line(width, height, self.blocks, self.blockHeight, green)
        tower = Tower(width, height, self.blocks, self.blockHeight, blue)
        i = 0

        while True:
            i += 1

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    if event.key == pygame.K_SPACE:
                        self.gameStarted = True
                        self.calcFallingBlocks(line, tower)

            screen.fill(white)

            # draw the tower
            for key in tower.towerLevels.keys():
                pygame.draw.rect(screen, tower.colour, [tower.towerLevels[key].x, tower.towerLevels[key].y, tower.towerLevels[key].numBlocks*self.blockHeight, self.blockHeight])

            if line.topLeftY < 0:
                self.gameOver = True
                self.finishGame('winner')

            # Move the block from side to side
            if i % line.speed == 0 and not self.gameOver:
                if self.gameStarted == False:
                    text = pygame.font.SysFont("comicsansms", 25)
                    textSurface = text.render("Press space bar to stop the block.", True, black)
                    textRect = textSurface.get_rect()
                    textRect.center = (width/2, height/8)
                    screen.blit(textSurface, textRect)
                pygame.draw.rect(screen, line.colour, [line.topLeftX, line.topLeftY, line.lineWidth, self.blockHeight])
                pygame.display.update()
                if ((line.topLeftX + line.lineWidth >= width or line.dir == -1) and line.topLeftX > 0):
                    line.topLeftX -= self.blockHeight
                    line.dir = -1
                elif (line.topLeftX <= 0 or line.dir == 1):
                    line.topLeftX += self.blockHeight
                    line.dir = 1

            # Lost the game
            if i % flashSpeed == 0 and self.gameOver:
                if self.flashNum == 0:
                    self.finishGame('gameover')
                else:
                    if self.flashNum % 2 == 0:
                        pygame.draw.rect(screen, line.colour, [line.topLeftX- line.dir*self.blockHeight, line.topLeftY, line.lineWidth, self.blockHeight])
                    self.flashNum -= 1    
                    pygame.display.update()
                    sleep(0.15)

    def calcFallingBlocks(self, line, tower):
        diff = line.topLeftX - line.dir*self.blockHeight - tower.topLeftX
        mod = abs(diff)/self.blockHeight
        
        if mod >= line.numBlocks:
            self.gameOver = True
            return

        if diff < 0:
            newTopLeftX = line.topLeftX + (mod-line.dir)*self.blockHeight 
        else:
            newTopLeftX = line.topLeftX - line.dir*self.blockHeight    
        
        tower.addRow(newTopLeftX, line.topLeftY, line.numBlocks - mod)
        line.updateLevel(mod, self.blockHeight, 'random')

    def finishGame(self, status):
        text = pygame.font.SysFont("comicsansms", 25)
        if status == 'winner':
            writing = "You Win! Press p to play again. Press q to quit."
        else:
            writing = "Game over. Press p to play again. Press q to quit."
        textSurface = text.render(writing, True, black)
        textRect = textSurface.get_rect()
        textRect.center = (width/2, height/8)
        screen.blit(textSurface, textRect)
                   
        while self.gameOver:   

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                    if event.key == pygame.K_p:
                        main()
            pygame.display.update()

def main():
    newGame = Game(4, 50)
    newGame.play()

if __name__ == '__main__':
    main()