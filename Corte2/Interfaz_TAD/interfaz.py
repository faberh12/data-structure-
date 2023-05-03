import pygame, sys
import webbrowser
from pygame.locals import *
from sll import SingleLinkedList
from ComboBox import ComboBox
inst=SingleLinkedList()
class main:
    def __init__(self):
        pygame.init()
        self.window_size=(1280,720)
        self.window= pygame.display.set_mode(self.window_size)
        self.gray_color=(211,211,211)
        self.white_color=(255,255,255)
        self.black_color=(0,0,0)
        self.font=pygame.font.SysFont('Times New Roman',16)
        self.dragon1 = pygame.image.load("imgs/dragon1.jpg")
        self.dragon2 = pygame.image.load("imgs/dragon2.jpg")
        self.dragon3 = pygame.image.load("imgs/dragon3.jpg")
        self.dragon4 = pygame.image.load("imgs/dragon4.jpg")
        self.dragon5 = pygame.image.load("imgs/dragon5.jpg")
        self.dragon6 = pygame.image.load("imgs/dragon6.jpg")
        self.uam_image = pygame.image.load("imgs/UAM.png")
        self.github_image = pygame.image.load("imgs/github.png")
        self.options_image = pygame.image.load("imgs/menu.png")
        self.arbol_image = pygame.image.load("imgs/arbol.png")
        self.nodo_image= pygame.image.load("imgs/nodo.png")
        self.combo_functions_rect= pygame.Rect(351,185,242,37)
        self.combo= ComboBox(self.window,['Añadir al inicio','Añadir al final','Eliminar al inicio','Eliminar al final','Invertir la lista', 'Eliminar todos los elementos','Eliminar por posicion','Añadir por posicion','Actualizar valor'],self.combo_functions_rect,self.black_color,'Times New Roman',16,20,self.white_color,self.white_color,40,' ')
        self.combo_selected= False
        self.combo_pos_rect= pygame.Rect(862,185,50,37)
        self.combo_pos= ComboBox(self.window,['1','2','3','4','5','6','7','8'],self.combo_pos_rect,self.black_color,'Times New Roman',16,20,self.white_color,self.white_color,40,' ')
        self.combo_pos_selected= False
        self.initial_window = True
        self.click_button= False
        self.rect_aux= None
        self.node_aux= None
        self.github_rect= pygame.Rect(850,665,38,36)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 
                if self.initial_window:
                    self.initial()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.mouse_pos= pygame.mouse.get_pos()
                        self.click_on_head()
                else:
                    self.draw_sll_window()
                    self.combo.draw()
                    self.combo_pos.draw()
            pygame.display.flip()    
            
    def rectGroup(self):
        self.black_rect = pygame.Rect(209,265,105,150)
        self.captain_rect = pygame.Rect(407,265,98,155)
        self.hulk_rect = pygame.Rect(515,265,110,155)
        self.ironman_rect = pygame.Rect(603,265,254,155)                 
        self.ojo_rect = pygame.Rect(802,265,116,150)
        self.panther_rect = pygame.Rect(919,265,101,155) 
    
    def text(self):
        pygame.display.set_caption('INTERFAZ TAD 1SEM')
        self.font.set_bold(True)
        sll_text= self.font.render('Single Linked List', True, self.black_color)
        self.font.set_bold(False)
        status_text= self.font.render('Estado de la lista: ', True,self.black_color)
        copyright_text= self.font.render('Desarrollado por : Fabian Hernandez Castaño',True,self.black_color)
        copyright_2_text= self.font.render('@ I SEM -2023',True,self.black_color)
        sll_option= self.font.render('SLL',True,self.black_color)
        dll_option= self.font.render('DLL',True,self.black_color)
        pyc_option= self.font.render('PILAS Y COLAS',True,self.black_color)
        arbol_option= self.font.render('ÁRBOL',True,self.black_color)
        grafo_option= self.font.render('GRAFO',True,self.black_color)
        self.window.blit(sll_option,(89,30))
        self.window.blit(dll_option,(312,30))
        self.window.blit(pyc_option,(540,30))
        self.window.blit(arbol_option,(874,30))
        self.window.blit(grafo_option,(1134,30))
        self.window.blit(sll_text,(154,133))
        self.window.blit(status_text,(154,423))
        self.window.blit(copyright_text,(485,661))
        self.window.blit(copyright_2_text,(569,683))
        self.window.blit(self.options_image,(40,27))
        self.window.blit(self.options_image,(254,27))
        self.window.blit(self.options_image,(485,27))
        self.window.blit(self.arbol_image,(822,27))
        self.window.blit(self.options_image,(1082,27))
        
        
    def draw_dll_window(self):
        self.window.fill(self.gray_color)
        self.top_rect=pygame.draw.rect(self.window,self.white_color,(0,0,1280,87),0,0)
        self.bottom_rect= pygame.draw.rect(self.window, self.white_color,(0,649,1280,71),0,0)
        self.list_rect= pygame.draw.rect(self.window,self.white_color,(154,460,1020,159),0,20)
        self.black_intital_rect = pygame.Rect(418,271,114,135)
        self.captain_rect_initial = pygame.Rect(608,271,114,135)
        self.hulk_rect_initial = pygame.Rect(798,271,114,135)  
        self.text()
        init_text= self.font.render('PARA INICIAR DEBES SELECCINAR UNA IMAGEN QUE SERA LA CABEZA DE LA LISTA',True, self.black_color)
        self.window.blit(init_text,(341,220))
        self.window.blit(self.dragon1, (418,271))
        self.window.blit(self.dragon2,(608,271))
        self.window.blit(self.dragon3,(798,271))
        self.window.blit(self.uam_image,(1188,658))
        self.window.blit(self.github_image,(850,665))       
    
    def draw_sll_window(self):
        self.window.fill(self.gray_color)
        self.top_rect=pygame.draw.rect(self.window,self.white_color,(0,0,1280,87),0,0)
        self.bottom_rect= pygame.draw.rect(self.window, self.white_color,(0,649,1280,71),0,0)
        self.list_rect= pygame.draw.rect(self.window,self.white_color,(154,460,1044,159),0,20)
        self.button_rect= pygame.draw.rect(self.window,self.black_color,(959,185,129,38),0,20)
        self.text()
        agree_text= self.font.render('Aceptar', True,self.white_color)
        methods_text= self.font.render('Seleccione un método: ',True,self.black_color)
        pos_text= self.font.render('Seleccione una posición: ',True,self.black_color)
        pygame.draw.rect(self.window,self.black_color,self.combo_functions_rect,0,20)
        pygame.draw.rect(self.window,self.black_color,self.combo_pos_rect,0,20)
        self.window.blit(methods_text,(154,192))
        self.window.blit(pos_text,(666,192))
        self.window.blit(agree_text,(990,192))
        self.window.blit(self.dragon1, (209,265))
        self.window.blit(self.dragon2,(345,265))
        self.window.blit(self.dragon3,(465,265))
        self.window.blit(self.dragon4,(590,265))
        self.window.blit(self.dragon5,(780,265))
        self.window.blit(self.dragon6,(910,265))
        self.window.blit(self.uam_image,(818,658))
        self.window.blit(self.github_image,(910,665)) 
        self.rectGroup()
        self.visual_list() 
        self.select_image()
        
    
    def initial(self):
        self.window.fill(self.white_color)
        self.top_rect=pygame.draw.rect(self.window,self.white_color,(0,0,1280,87),0,0)
        self.bottom_rect= pygame.draw.rect(self.window, self.white_color,(0,649,1280,71),0,0)
        self.list_rect= pygame.draw.rect(self.window,self.white_color,(154,460,1020,159),0,20)
        self.dragon1_intital_rect = pygame.Rect(418,271,114,135)
        self.dragon2_rect_initial = pygame.Rect(608,271,114,135)
        self.dragon3_rect_initial = pygame.Rect(798,271,114,135)  
        self.text()
        init_text= self.font.render('PARA INICIAR DEBES SELECCINAR UNA IMAGEN QUE SERA LA CABEZA DE LA LISTA',True, self.black_color)
        self.window.blit(init_text,(341,220))
        self.window.blit(self.dragon1, (418,271))
        self.window.blit(self.dragon2,(608,271))
        self.window.blit(self.dragon3,(798,271))
        self.window.blit(self.uam_image,(1188,658))
        self.window.blit(self.github_image,(850,665))
        
    
    def click_on_head(self):
        mouse_pos= pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.dragon1_intital_rect.collidepoint(mouse_pos):
                inst.create_node_sll_unshift('Dragon1')
                inst.show_list()
                self.initial_window = False
            elif self.dragon2_rect_initial.collidepoint(mouse_pos):
                inst.create_node_sll_unshift('Dragon2')
                inst.show_list()
                self.initial_window = False
            elif self.dragon3_rect_initial.collidepoint(mouse_pos):
                inst.create_node_sll_unshift('Dragon3')
                inst.show_list()
                self.initial_window = False

    def visual_list(self):
        gap=0
        for i in range(1,inst.length+1):
            if inst.get_node_value(i)== 'Dragon1':
                self.window.blit(self.dragon1, (164+gap,472))
            elif inst.get_node_value(i) == 'Dragon2':
                self.window.blit(self.dragon2,(164+gap,472))
            elif inst.get_node_value(i) == 'Dragon3':
                self.window.blit(self.dragon3,(164+gap,472))
            elif inst.get_node_value(i) == 'Dragon4':
                self.window.blit(self.dragon4,(164+gap,472))
            elif inst.get_node_value(i) == 'Dragon5':
                self.window.blit(self.dragon5,(164+gap,472))
            elif inst.get_node_value(i) == 'Dragon6':
                self.window.blit(self.dragon6,(164+gap,472))    
            gap+=130



    def select_image(self):
        if pygame.mouse.get_pressed()[0]:
            if self.black_rect.collidepoint(pygame.mouse.get_pos()):
                self.node_aux= 'Dragon1'
                print('Nodo seleccionado')
            elif self.captain_rect.collidepoint(pygame.mouse.get_pos()):
                self.node_aux= 'Dragon2'
                print('Nodo seleccionado')
            elif self.hulk_rect.collidepoint(pygame.mouse.get_pos()):
                self.node_aux= 'Dragon3'
                print('Nodo seleccionado')
            elif self.ironman_rect.collidepoint(pygame.mouse.get_pos()):
                self.node_aux= 'Dragon4'
                print('Nodo seleccionado')
            elif self.ojo_rect.collidepoint(pygame.mouse.get_pos()):
                self.node_aux= 'Dragon5'
                print('Nodo seleccionado')
            elif self.panther_rect.collidepoint(pygame.mouse.get_pos()):
                self.node_aux= 'Dragon6'
                print('Nodo seleccionado')
            if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                print('click en el boton')
                if self.combo.getIndex()== 1:
                    if self.node_aux is not None:                        
                        inst.create_node_sll_unshift(self.node_aux)
                        self.node_aux=None
                        inst.show_list()
                if self.combo.getIndex()== 2:
                    if self.node_aux is not None:
                        inst.create_node_sll_ends(self.node_aux)
                        self.node_aux=None
                        inst.show_list()
                if self.combo.getIndex()== 3:
                    inst.shift_node_sll()
                    self.node_aux=None
                    inst.show_list()
                if self.combo.getIndex()== 4:
                    inst.delete_node_sll_pop()
                    self.node_aux=None
                    inst.show_list()
                if self.combo.getIndex()== 5:
                    inst.reverse()
                    self.node_aux=None
                    inst.show_list()
                if self.combo.getIndex()==6:
                    inst.remove_node_list()
                    self.node_aux=None
                    inst.show_list()
                if self.combo.getIndex()==7:
                    inst.remove_node_index(self.combo_pos.getIndex())
                    self.node_aux=None
                    inst.show_list()
                if self.combo.getIndex()==8:
                    if self.node_aux is not None:
                        inst.insert_on_index(self.combo_pos.getIndex(),self.node_aux)
                        self.node_aux=None
                        inst.show_list()
                if self.combo.getIndex()==9:
                    if self.node_aux is not None:
                        inst.update_node_value(self.combo_pos.getIndex(),self.node_aux)
                        self.node_aux=None
                        inst.show_list()