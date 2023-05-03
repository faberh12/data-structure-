import pygame
import sys
from menu import Menu
from interfaz import main
pygame.init()

class TAD:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("TAD 1SEM")
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (134, 181, 129)
        self.RED = (255, 0,   0)
        self.BLUE = (0, 0, 255)
        self.GRAY = (170, 170, 170)
        self.LIGHT_BLUE = (161, 163, 212)
        self.main_menu = Menu(self.screen, {"SLL": "imgs/list-outline.png", "DLL": "imgs/list-outline.png", "Pilas y colas": "imgs/list-outline.png", "Árboles": "imgs/tree-solid.png", "Grafos": "imgs/circle-nodes-solid.png"}, self.GREEN, 100, "Arial", 22, self.BLACK)
        

    def run(self):
        while True:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
            self.screen.fill(self.WHITE)
            if(self.main_menu.getSelectedOption() == 0):
                pygame.draw.rect(self.screen, (200, 200, 200), (0, 40, self.screen.get_width(), self.screen.get_height() - 40))
            elif(self.main_menu.getSelectedOption() == 1):
                pygame.draw.rect(self.screen, (250, 10, 20), (0, 40, self.screen.get_width(), self.screen.get_height() - 40))
            self.main_menu.draw()
            pygame.display.flip()

if __name__ == "__main__":
    inst_main = main()
    inst_main.run()