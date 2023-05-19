from combo_box import ComboBox
from single_linked_list import SLL
from menu import Menu
from botonoes_seleccion import Boton
import pygame
import sys
import webbrowser
from blackjack import blackjack

class MegaInterfaz:
    def __init__(self):
        #Lista rectangulos
        self.inst_sll = SLL()
        self.rectangulo=list()
        pygame.init()
        self.BLACK   = (0  , 0  ,   0)
        self.WHITE   = (255, 255, 255)
        self.GREEN   = (134, 181, 129)
        self.RED     = (255, 0  ,   0)
        self.BLUE    = (0  , 0  , 255)
        self.GRAY    = (170, 170, 170)
        self.LIGHT_BLUE = (161, 163, 212)
        #Crera pantallas
        self.screen=pygame.display.set_mode((1200,700))
        #Nombre a la pestaña
        pygame.display.set_caption("Mega Menu")
        #self.colorPantalla=(230,230,230)
        self.colorRect=(230,230,230)
        #Imagenes
        self.goku = Boton('1',(430,185,100,100),"imagenes/goku.png")
        self.goku2 = Boton('2',(550,185,100,100),"imagenes/goku2.png")
        self.goku3 = Boton('3',(670,185,100,100),"imagenes/goku3.png")
        self.goku4 = Boton('4',(930,380,100,100),"imagenes/goku4.png")
        self.goku5 = Boton('5',(160,380,100,100),"imagenes/goku5.png")
        self.goku6 = Boton('6',(270,380,100,100),"imagenes/goku6.png")
        self.goku7 = Boton('7',(380,380,100,100),"imagenes/goku7.png")
        self.goku8 = Boton('8',(490,380,100,100),"imagenes/goku8.png")
        self.goku9 = Boton('9',(600,380,100,100),"imagenes/goku9.png")
        self.goku10 = Boton('10',(710,380,100,100),"imagenes/goku10.png")
        self.goku11 = Boton('11',(820,380,100,100),"imagenes/goku11.png")
        self.list_button = [self.goku,self.goku2,self.goku3,self.goku4,self.goku5,self.goku6,self.goku7,self.goku8,self.goku9,self.goku10, self.goku11]
        
        self.git_rect = pygame.Rect(885, 646, 52, 54)
        self.gitHub=pygame.image.load("imagenes/logo.png")
        self.gitHub=pygame.transform.scale(self.gitHub,(52,54))
        self.git_bool = False
        self.limit_superate=False

        #combobox metodo
        self.combo_rect = pygame.Rect(370, 300, 250, 20)
        self.combo = ComboBox(self.screen, ["Agregar al inicio", "Agregar al final", "Eliminar primero", "Eliminar ultimo", "Invertirla","Eliminar todo","Eliminar con posición","Insertar con posición","Actualizar valor","Eliminar duplicados","unir duplicados"], self.combo_rect, self.GRAY, "Arial", 15, 5, self.WHITE, self.WHITE, 25, "Seleccione una opción")
        self.button = pygame.Rect(504, 333, 191, 39)
        self.click_button = False
        #ombobox dos
        self.combo_dos_rect = pygame.Rect(815, 300, 250, 25)
        self.combo_dos = ComboBox(self.screen, ["1", "2", "3", "4", "5"], self.combo_dos_rect, self.GRAY, "Arial", 17, 5, self.WHITE, self.WHITE, 40, "Seleccione una opción")
        self.main_menu = Menu(self.screen, {"SLL": "imagenes/list-outline.png","BlackJack": "imagenes/list-outline.png", "Grafos": "imagenes/circle-nodes-solid.png"}, self.BLUE, 50, "Times New Roman", 22, self.WHITE)
        
        self.imagenSeleccionada = None
        self.blackjack = blackjack(self.screen)


    def corre_juego(self):
        #Para que no se cierre la ventana y corra continuamente
        while True:
            for event in pygame.event.get():
                #Reaccion a eventos especificos
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos=pygame.mouse.get_pos()
                    for item in self.list_button:
                        item.quitar_seleccion_otros()
                        if item.mouse_encima(mouse_pos):
                            item.select_button(mouse_pos)
                            self.imagenSeleccionada = item.imagen
                    
                    if self.clickOnButton(mouse_pos):
                        metodo=self.combo.getIndex()
                        posicion=self.combo_dos.getIndex()
                        if metodo==1:
                            if self.inst_sll.lenght_sll()<7:
                                self.inst_sll.create_node_sll_unshift(self.imagenSeleccionada)
                            else:
                                self.limit_superate=True
                        elif metodo ==2:
                            if self.inst_sll.lenght_sll()<7:
                                self.inst_sll.create_node_sll_ends(self.imagenSeleccionada)
                            else:
                                self.limit_superate=True
                        elif metodo==3:
                            self.inst_sll.shift_node_sll()
                        elif metodo==4:
                            self.inst_sll.delete_node_sll_pop()
                            self.limit_superate=False
                        elif metodo == 5:
                            self.inst_sll.reverse_sll()
                        elif metodo == 6:
                            self.inst_sll.delete_all_sll()
                            self.limit_superate=False
                        elif metodo==7:
                            self.inst_sll.remove_node(posicion)
                            self.limit_superate=False
                        elif metodo==8:
                            if self.inst_sll.lenght_sll()<7:
                                self.inst_sll.create_node_sll(posicion,self.imagenSeleccionada)
                            else:
                                self.limit_superate=True
                        elif metodo==9:
                            self.inst_sll.update_node_value(posicion,self.imagenSeleccionada)
                        elif metodo==10:
                            self.inst_sll.eliminar_duplicates()
                            self.limit_superate=False
                        elif metodo==11:
                            self.inst_sll.unir_duplicados()
                            print('')
            self.screen.fill(self.BLACK)
            #Rectangulos interfaz
            #Rectangulo grande
            pygame.draw.rect(self.screen,self.colorRect,(20,70,1160,550))
            pygame.draw.rect(self.screen,self.colorRect,(0,645,1200,55))
            #Menu 
            if(self.main_menu.getSelectedOption() == 0):
                #Mostrar lista
                pygame.draw.rect(self.screen,self.WHITE,(50,490,1100,100))
                #Dibujar lista
                list_sll=self.inst_sll.show_list()
                count=0
                y_pos=490
                x_pos=0
                for item in list_sll:
                    x_pos+=100
                    self.screen.blit(item,(x_pos,y_pos))
                    count+=1
                self.mostrarSLL()
                self.click_git()
                if self.limit_superate:
                    self.mensaje_limite()
            elif(self.main_menu.getSelectedOption() == 1):
                self.click_git()
                self.mostrarBlackJack()
            elif(self.main_menu.getSelectedOption() == 2):
                pygame.draw.rect(self.screen, (250, 10, 20), (0, 40, self.screen.get_width(), self.screen.get_height() - 40))
            self.main_menu.draw()

            #Actualizar pantalla
            pygame.display.flip()
        

    def click_git(self):
        if self.git_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not self.git_bool:
                self.git_bool = True
                webbrowser.open("https:github.com/faberh12/data-structure-/tree/main/Corte2")
        if not pygame.mouse.get_pressed()[0]:
            self.git_bool = False

    def texto(self,tamaño,texto,color,cords):
        Fuente = pygame.font.SysFont("Arial",tamaño)
        texto = Fuente.render(texto,0,color)
        self.screen.blit(texto,(cords[0],cords[1]))

    def mostrarSLL(self): 
        #Texto
        self.texto(20,"DESARROLADO POR: Fabian Hernández Castaño",self.BLACK,(450,650))
        self.texto(20,"SINGLE LINKED LIST",self.BLACK,(70,100))
        self.texto(18,"PARA INICIAR DEBES SELECCIONAR AL MENOS UNA IMAGEN QUE SERÁ LA CABEZA DE LA LISTA",self.BLACK,(250,150))
        self.texto(18,"Selecciona un método",self.BLACK,(190,300))
        self.texto(18,"Selecciona la posición",self.BLACK,(620,300))
        #Dibujar botones
        for item in self.list_button:
            item.draw_button(self.screen)
        #Imagen git
        self.screen.blit(self.gitHub,(885,646))
        #Combo box
        pygame.draw.rect(self.screen, self.BLACK, self.combo_rect, 0, 5)
        self.drawButton("Aceptar", self.BLACK, self.button, 0, 16, 22, True, self.WHITE, "Consolas")
        pygame.draw.rect(self.screen, self.BLACK, self.combo_dos_rect, 0, 5)
        self.combo_dos.draw()
        self.combo.draw()
    
    def mostrarBlackJack(self):
        #Imagenes
        self.fondo=pygame.image.load("imagenesC/fondo.png")
        self.fondo=pygame.transform.scale(self.fondo,(1160,550))
        self.screen.blit(self.fondo,(20,70))
        self.crupier=pygame.image.load("imagenesC/crupier.png")
        self.crupier=pygame.transform.scale(self.crupier,(300,200))
        self.screen.blit(self.crupier,(450,155))
        self.screen.blit(self.gitHub,(885,646))
        self.blackjack.botones(self.screen)
        #Texto
        self.texto(20,"DESARROLADO POR: Fabian Hernandez Castaño",self.BLACK,(450,650))
        self.texto(16,"Para iniciar el juego debes dar click en el boton Empezar: ",self.WHITE,(108,108))
        self.texto(18,"Para reiniciar da click en Repetir: ",self.WHITE,(715,108))
        self.texto(18,"Jugador 1 ",self.WHITE,(208,332))
        self.texto(18,"Jugador 2 ",self.WHITE,(556,381))
        self.texto(18,"Jugador 3 ",self.WHITE,(906,332))

        self.blackjack.correr(self.screen)




    def drawButton(self, text, button_color, background_rect, border, border_radius, text_size, text_bold, text_color, text_font):
        pygame.draw.rect(self.screen, button_color, background_rect, border, border_radius)
        font = pygame.font.SysFont("Arial", text_size, text_bold)
        render_text = font.render(text, True, text_color, None)
        self.screen.blit(render_text, (background_rect.x + (background_rect.width - render_text.get_width())/2, background_rect.y + (background_rect.height - render_text.get_height())/2))

    def clickOnButton(self,mouse_pos):
        if self.button.collidepoint(mouse_pos):
            return True
        else:
            return False
        
    #mensaje de limite superado
    def mensaje_limite(self):
        return self.texto(40,"Limite de elementos superado",self.BLACK,(400,95))