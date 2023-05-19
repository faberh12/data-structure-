import pygame
class jugador:
    
    def __init__(self, screen,  x, y,mensajeX,mensajeY):
        self.list = []
        self.x = x
        self.y = y
        #Carta
        self.width=71
        self.height=109
        self.puntuacion = 0
        self.plantado = False
        self.perdio=False
        self.mensajeX=mensajeX
        self.mensajeY=mensajeY



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

    def puntuacionJugador(self):
        suma =0
        for carta in self.list:
            numero =self.obtenerNumeroCarta(carta)
            if numero == 'a':
                numero=11
            suma += numero
        self.puntuacion=suma
    
    def dibujarCartas(self,screen,carta,x,y):
        screen=screen
        imagenCarta = pygame.image.load(carta)
        imagenCarta = pygame.transform.scale(imagenCarta, (self.width, self.height))
        screen.blit(imagenCarta, (x, y))

    def mostrarCarta(self,screen):
        screen=screen
        for j, carta in enumerate(self.list):
                x = self.x + j * (40)
                y = self.y  
                self.dibujarCartas(screen,carta, x, y)


    