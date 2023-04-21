'''
    name: Fabian Hernandez Castaño
    Date: 06/02/23

'''
from colorama import Fore,init
init()

class Superhero:
    #1. Metodo inicializador de la clase
    def __init__(self):
        #Definimos una lidta vacia
        self.Marvel = []
        self.DC = list()
        self.super_name = ""
        self.super_powers = []
        self.super_creator = []
        self.menu_option = 0

    def initialitation_menu(self):
        #Tipos datos de ejemplo
        self.Marvel.append(("Spider-man", ["Lanzar telarañas", "Acrobata"], ["Stan Lee", "Steve Ditko"]))
        self.Marvel.append(("Thor", ["Volar", "Electricidad"],["Stan lee", "Larry lieber"]))
        self.Marvel.append(("Iron man", ["Volar","Lanzar cohetes"], ["Stan Lee"]))
        self.DC.append(("Robin", ["Hacker", "Acrobata"], ["Bob Kane", "Bill Finger"]))
        self.DC.append(("Linterna verde", ["Crear cosas", "volar"], ["Martin Nodel", "Gil kane"]))
        self.DC.append(("Shazam", ["Super fuerza, Lanzar rayos"], ["Avery Li-Chung Wang"]))
        while True:
            try:
                self.menu_option = int(input(Fore.BLUE + '1.Agregar superheroe\n2.Ver poderes\n3.Eliminar superheroe\n4.Superheroe mayor cantidad de superpoderes\n5.Superheroe menor cantidad de superpoderes\n6.Unir lista DC y lista Marvel\n7.Salir\nIngrese una opcion: ' + Fore.RESET))
                if self.menu_option < 1 or self.menu_option  > 7:
                     print('Opcion incorrecta')
                elif self.menu_option == 1:
                         self.add_superhero()

                elif self.menu_option == 2:
                         self.nombre_superhero_powers()

                elif self.menu_option == 3:
                         self.delete_superhero()

                elif self.menu_option == 4:
                         self.mayor_powers()

                elif self.menu_option == 5:
                         self.menor_powers()

                elif self.menu_option == 6:
                         self.unir_lists()
                
                else:
                    print('Salio del programa con exito')
                    break
            except ValueError:
                 print('Error, Error, Error')            
    

    #4. Metodo para agregar el superheroe
    def add_superhero(self):
        while True:
            try:
                print(" Ingrese la información: ")
                superhero_world = int(input("Mundo al que pertenecen los superhores: \n[1] DC\n[2] Marvel\n[3] Salir\n"))
                if superhero_world == 1 or superhero_world == 2:
                    num_superheroes = int(input("Cantidad de superheroes: "))
                    for superheroe in range(num_superheroes):
                        print(f" >>> {superheroe + 1} <<< ")
                        self.super_name = str(input("Nombre del superheroe: "))
                        # title(): Pone las primeras letras de cada palabra en mayúscula
                        # split(): Separa las palabras
                        self.super_powers = input("Poderes:  (separados por una coma)\n").title().split(", ")
                        
                        # si solo es un elemento devolver un string
                        if len(self.super_powers) == 1:
                            self.super_powers = self.super_powers[0]

                        self.super_creator = input("Creadores: (separados por coma)\n").title().split(", ")
                        if len(self.super_creator) == 1:
                            self.super_creator = self.super_creator[0]
                        
                        # Agregar a la lista, dependiendo si es de DC o Marvel
                        if superhero_world == 1:
                            self.DC.append((self.super_name, self.super_powers, self.super_creator))
                        elif superhero_world == 2:
                            self.Marvel.append((self.super_name, self.super_powers, self.super_creator))
                else:
                    break
            except ValueError:
                print(" ¡Error!: debe ingresar un número")
    #5. Metodo que solicita el nombre del superheroe y si lo encuentra devuelve los superpoderes
    def nombre_superhero_powers(self):
        super = False
        self.super_name = input("Ingrese el nombre del superheroe: ")
        aux_list = self.Marvel + self.DC
        for superhero in aux_list:
            if self.super_name in superhero:
                # Imprime la lista de poderes
                super = True
                print(f"Poderes: {superhero[1]}")
        
        if not super:
            print("No pudimos encontrar ese superheroe")
            selection = input("¿Desea añadir un nuevo superheroe?\n[1] S\n[2] N\n")
            if selection == '1':
                self.add_superhero()


    #6. metodo que solcita el nombre del superheroe y elimina toda la informacion
    def delete_superhero(self):
        self.super_name = input("Ingrese el nombre del superheroe: ")
        for superhero in self.Marvel:
            if self.super_name == superhero[0]:
                print(f"Se elimino {self.superheroe_name} de la lista de superheroes Marvel")
                self.Marvel.remove(superhero)

        for superhero in self.DC:
            if self.super_name == superhero[0]:
                print(f"Se elimino {self.superheroe_name} de la lista de superheroes DC")
                self.DC.remove(superhero)
        
    #7. Metodo que devuelve el nombre del superheroe que tiene mas superpoderes
    def mayor_powers(self):
        mayor = 0
        aux_list = self.Marvel + self.DC
        for superhero in aux_list:
            # Valida si es una lista o un String
            if type(superhero[1]) == str:
                longitud = 0
            else:
                longitud = len(superhero[1])

            if longitud > mayor:
                mayor = len(superhero[1])
                name = superhero[0]
        print(f"El nombre del superhéroe con más poderes es: {name}")
    #8. Metodo que devuelve el nombre del superheroe que tiene menos superpoderes
    def menor_powers(self):
        least = 100
        aux_list = self.Marvel + self.DC
        for superhero in aux_list:
            # Valida si es una lista o un String
            if type(superhero[1]) == str:
                menor = 1
            else:
                menor = len(superhero[1])

            if menor < least:
                least = len(superhero[1])
                name = superhero[0]
        print(f"El nombre del superhéroe con menos poderes es: {name}")
    #9. Metodo que une las dos listas
    def unir_lists(self):
        unir_list = self.Marvel + self.DC
        print(" >>> Lista unida xd <<<")
        print(unir_list)