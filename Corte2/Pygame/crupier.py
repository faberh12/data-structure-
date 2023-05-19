import pygame
class crupier:
    
    def __init__(self, screen,  x, y):
        self.list = []
        self.x = x
        self.y = y
        self.puntuacion = 0
        #Carta
        self.width=71
        self.height=109

    def añadirCarta(self, carta):
        numero =self.obtenerNumeroCarta(carta)
        if numero == 'a':
            if self.puntuacion <=10:
                self.puntuacion +=11
                self.list.append(carta)
            elif self.puntuacion >10:
                self.puntuacion +=1
                self.list.append(carta)
        else:
            self.puntuacion+=numero
            self.list.append(carta)
    
    def obtenerNumeroCarta(self,carta):
        nombre_archivo = carta.split('/')[-1].split('.')[0]
        numero_str = nombre_archivo.split('-')[0]
        if numero_str.isdigit():
            numero = int(numero_str)
        else:
            if numero_str.lower() == 'a':
                numero = 'a'
            elif numero_str.lower() in ('j', 'q', 'k'):
                numero = int(10)
            else:
                numero = 0 
        return numero
    
    def dibujarCartas(self,screen,carta,x,y):
        screen=screen
        imagenCarta = pygame.image.load(carta)
        imagenCarta = pygame.transform.scale(imagenCarta, (self.width, self.height))
        screen.blit(imagenCarta, (x, y))

    def mostrarCarta(self,screen):
        screen=screen
        for j in range(len(self.list) - 1):
            carta = self.list[j]
            x = 714 + j * 40
            y = 178 
            self.dibujarCartas(screen,carta, x, y) 
            self.dibujarCartas(screen,"imagenesC/cartaDosCrupier.png", 798, 178)

    def mostrarCartasFinales(self,screen):
        screen=screen
        for j, carta in enumerate(self.list):
                x = 714 + j * 40
                y = 178   
                self.dibujarCartas(screen,carta, x, y)
    