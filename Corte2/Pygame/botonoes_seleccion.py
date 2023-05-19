import pygame

class Boton:
    def __init__(self,id,cords,nombreImagen):
        self.id=id
        self.cords=cords
        self.imagen=pygame.image.load(nombreImagen)
        self.imagen=pygame.transform.scale(self.imagen,(100,100))
        self.WHITE   = (255, 255, 255)
        self.GRAY=(200, 200, 200)
        self.selected=False

    def draw_button(self,screen):
        if not self.selected:
            pygame.draw.rect(screen,self.WHITE,self.cords)
        else:
            pygame.draw.rect(screen,self.GRAY,self.cords)
        screen.blit(self.imagen,(self.cords[0],self.cords[1]))


    def select_button(self,mouse_pos):
        x_mouse=mouse_pos[0]
        y_mouse=mouse_pos[1]
        if x_mouse>=self.cords[0] and y_mouse>=self.cords[1] and x_mouse<=self.cords[0]+self.cords[2] and y_mouse<=self.cords[1]+self.cords[3]:
            if self.selected:
                self.selected=False
            else:
                self.selected=True

    def esta_seleccionado(self):
        return self.selected
    
    def quitar_seleccion_otros(self):
        self.selected=False

    def mouse_encima(self,mouse_pos):
        x_mouse=mouse_pos[0]
        y_mouse=mouse_pos[1]
        if x_mouse>=self.cords[0] and y_mouse>=self.cords[1] and x_mouse<=self.cords[0]+self.cords[2] and y_mouse<=self.cords[1]+self.cords[3]:
            return True
        else:
            return False