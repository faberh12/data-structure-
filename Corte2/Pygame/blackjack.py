import random
import pygame
from crupier import crupier
from jugador import jugador

class blackjack:

    def __init__(self, screen):
        self.screen = screen
        #Colores
        self.BLACK   = (0  , 0  ,   0)
        self.WHITE   = (255, 255, 255)
        self.GREEN   = (134, 181, 129)
        self.RED     = (255, 0  ,   0)
        self.BLUE    = (0  , 0  , 255)
        self.GRAY    = (170, 170, 170)
        self.BROWN = (161, 130, 98)
        #Cartas
        self.imagesCartas = ["imagenesC/9V2.JPG", "imagenesC/2.JPG", "imagenesC/2V2.JPG", "imagenesC/3.JPG",
                             "imagenesC/3V2.JPG", "imagenesC/4V2.JPG", "imagenesC/5.JPG", "imagenesC/6.JPG",
                             "imagenesC/7.JPG", "imagenesC/7V2.JPG", "imagenesC/7V3.JPG", "imagenesC/8.JPG",
                             "imagenesC/9.JPG", "imagenesC/10.JPG", "imagenesC/J.JPG", "imagenesC/J2.JPG",
                             "imagenesC/K.JPG", "imagenesC/K3.JPG", "imagenesC/Q2.JPG",
                             "imagenesC/cartaDosCrupier.PNG"]
        self.baraja = []
        self.cartas_iniciales= True
        self.jugador_1 = jugador(self.screen, 137, 360,170,280)
        self.jugador_2 = jugador(self.screen, 485, 416,515,340)
        self.jugador_3 = jugador(self.screen, 833, 362,850,290)
        self.jugadores = [self.jugador_1, self.jugador_2, self.jugador_3]
        self.crupier = crupier(self.screen, 300,300)
        #Botones
        self.btnEmpezar=pygame.Rect(465,102,143,34)
        self.btnPlantarUno=pygame.Rect(223,486,143,34)
        self.btnPlantarDos=pygame.Rect(537,542,143,34)
        self.btnPlantarTres=pygame.Rect(834,486,143,34)
        self.btnPedir=pygame.Rect(488,311,227,34)
        self.btnRepetir=pygame.Rect(932,102,143,34)
        #Turno
        self.turno=1
        #Booleanas
        self.presionarEmpezar=False
        self.presionarRepetir=False
        self.final=False
        self.mensajes=True
        self.turnoC=True
        self.verificar=False
        self.inicio=False
        self.pedir=False
        self.plantar1=False
        self.plantar2=False
        self.plantar3=False

    def dioClickBoton(self,btn,boolClick):     
        if btn.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not boolClick and not self.verificar:
                self.verificar=True
                boolClick=True
                return True
        if not pygame.mouse.get_pressed()[0]:
            self.verificar=False
            boolClick=False
            return False

    def correr(self,screen):
        self.screen=screen
        if self.dioClickBoton(self.btnEmpezar,self.presionarEmpezar):
            self.llenarBaraja()
            self.repartirCartasIniciales()
            self.inicio=True
        if self.inicio:
            self.turnoJugador()
            self.mostrarMensajes()
        if self.dioClickBoton(self.btnRepetir,self.presionarRepetir):
            self.reset()
        self.dibujarCartas(screen)
        
        

    def llenarBaraja(self):
        random.shuffle(self.imagesCartas)
        self.baraja.extend(self.imagesCartas)   # Agrega las imágenes mezcladas a la baraja

    def repartirCartasIniciales(self):
        while self.cartas_iniciales:
            self.jugador_1.añadirCarta(self.baraja.pop())
            self.jugador_2.añadirCarta(self.baraja.pop())
            self.jugador_3.añadirCarta(self.baraja.pop())
            self.jugador_1.añadirCarta(self.baraja.pop())
            self.jugador_2.añadirCarta(self.baraja.pop())
            self.jugador_3.añadirCarta(self.baraja.pop())
            self.crupier.añadirCarta(self.baraja.pop())
            self.cartas_iniciales = False

    def dibujarCartas(self,screen):
        for jugador in self.jugadores:
            jugador.mostrarCarta(screen)
        if not self.final:
            self.crupier.mostrarCarta(screen)

    def dibujoBotones(self, screen,text, button_color,background_rect, border, border_radius, text_size, text_bold, text_color):
        screen=screen
        pygame.draw.rect(self.screen, button_color, background_rect, border, border_radius)
        font = pygame.font.SysFont("Times New Roman", text_size, text_bold)
        render_text = font.render(text, True, text_color, None)
        self.screen.blit(render_text, (background_rect.x + (background_rect.width - render_text.get_width())/2, background_rect.y + (background_rect.height - render_text.get_height())/2))

    def botones(self,screen):
        screen=screen
        #Botones
        self.dibujoBotones(screen,"EMPEZAR", self.RED, self.btnEmpezar,0, 16, 18, True, self.BLACK)
        self.dibujoBotones(screen,"PLANTARME", self.RED, self.btnPlantarUno,0, 16, 18, True, self.BLACK)
        self.dibujoBotones(screen,"PLANTARME", self.RED, self.btnPlantarDos,0, 16, 18, True, self.BLACK)
        self.dibujoBotones(screen,"PLANTARME", self.RED, self.btnPlantarTres,0, 16, 18, True, self.BLACK)
        self.dibujoBotones(screen,"PEDIR CARTAS", self.RED, self.btnPedir,0, 16, 18, True, self.BLACK)
        self.dibujoBotones(screen,"REPETIR", self.RED, self.btnRepetir,0, 16, 18, True, self.BLACK)


    def turnoJugador(self):
        if self.turno==1:
            if self.dioClickBoton(self.btnPedir,self.pedir) and not self.jugador_1.perdio:
                    self.jugador_1.añadirCarta(self.baraja.pop())
                    print(self.jugador_1.puntuacion)
                    if self.jugador_1.puntuacion > 21:
                        self.turno +=1
                        self.jugador_1.perdio=True
            elif self.dioClickBoton(self.btnPlantarUno,self.plantar1) or self.jugador_1.perdio:
                self.turno+=1
        
        if self.turno==2:
            if self.dioClickBoton(self.btnPedir,self.pedir) and not self.jugador_2.perdio:
                    self.jugador_2.añadirCarta(self.baraja.pop())
                    print(self.jugador_2.puntuacion)
                    if self.jugador_2.puntuacion > 21:
                        self.turno +=1
                        self.jugador_2.perdio=True
            elif self.dioClickBoton(self.btnPlantarDos,self.plantar2) or self.jugador_2.perdio:
                self.turno+=1

        if self.turno==3:
            if self.dioClickBoton(self.btnPedir,self.pedir) and not self.jugador_3.perdio:
                    self.jugador_3.añadirCarta(self.baraja.pop())
                    print(self.jugador_3.puntuacion)
                    if self.jugador_3.puntuacion > 21:
                        self.turno +=1
                        self.jugador_3.perdio=True
            elif self.dioClickBoton(self.btnPlantarTres,self.plantar3) or self.jugador_3.perdio:
                self.turno+=1

        if self.turno==4:
            self.final=True
            if self.crupier.puntuacion <=16:
                self.crupier.añadirCarta(self.baraja.pop())
            self.crupier.mostrarCartasFinales(self.screen)
            self.mensajeFinal()
                
        
    def texto(self,tamaño,texto,color,cords):
        miFuente=pygame.font.SysFont("Times New Roman",tamaño)
        texto=miFuente.render(texto,0,color)
        self.screen.blit(texto,(cords[0],cords[1]))
        

    def mostrarMensajes(self):
        if self.mensajes:
            if self.jugador_1.perdio is True:
                self.texto(20,"Te pasaste de los 21",self.WHITE,(179,310))
            elif self.jugador_1.puntuacion==21:
                self.texto(20,"Blackjack",self.GREEN,(179,297))

            if self.jugador_2.perdio:
                self.texto(20,"Te pasaste de los 21",self.WHITE,(520,360))
            elif  self.jugador_2.puntuacion==21:
                self.texto(20,"Blackjack",self.GREEN,(520,354))

            if self.jugador_3.perdio:
                self.texto(20,"Te pasaste de los 21",self.WHITE,(880,305))
            elif self.jugador_3.puntuacion==21:
                self.texto(20,"Blackjack",self.GREEN,(880,305))
            
    def mensajeFinal(self):
        for jugador in (self.jugadores):
            if jugador.puntuacion>self.crupier.puntuacion and jugador.puntuacion<21 :
                self.texto(20,"Superaste la puntuacion del crupier",self.GREEN,(jugador.mensajeX,jugador.mensajeY))
            elif jugador.puntuacion <self.crupier.puntuacion:
                self.texto(20,"Crupier gano",self.BLUE,(jugador.mensajeX,jugador.mensajeY))
            elif jugador.puntuacion == self.crupier.puntuacion :
                self.texto(20,"Empatas con el crupier" ,self.BLUE,(jugador.mensajeX,jugador.mensajeY))
            elif jugador.puntuacion <=21 and self.crupier.puntuacion>21 :
                self.texto(20,"Crupier pierde contigo",self.GREEN,(jugador.mensajeX,jugador.mensajeY))


    def reset(self):
            self.__init__(self.screen)