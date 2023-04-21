from random import sample
from colorama import Fore, init
init()

class sortAlgorithms:
    def __init__(self):
        self.number_list = range(100)
        self.list_burble_sort = sample(self.number_list, 8)
        self.list_select_sort = sample(self.number_list, 8)
        self.list_insert_sort = sample(self.number_list, 8)
        self.list_merge_sort = sample(self.number_list, 8)
        self.list_quick_sort = sample(self.number_list, 8)
        self.list_radix_sort = sample(self.number_list, 8)

    #Ordenamienti burbuja:
    def burble_sort_function(self):
        #Comparacion por pares, iniciamos comparando los 2 primeros elemetos de la lista
        print(Fore.CYAN + "-------------------------------------------" + Fore.RESET)
        print(Fore.GREEN + "Ordenamiento Burbuja"    + Fore.RESET)
        #Crear un contador para conocer la cantidad de elementos de la lista
        count_item_list = 0
        #Recorremos la lista self.list_burble_sort
        for i in self.list_burble_sort:
            #al contador de elementos, cada vez que visitemos una posicion le sumamos 1
            count_item_list += 1
        print(self.list_burble_sort)
        #Recorremos la lista e imprimimos su contenido en cada iteracion
        print("Primer for cantador -1: ", count_item_list-1)
        for j in range(count_item_list-1):
            print(Fore.RED + str(j) + Fore.RESET)
            for k in range(count_item_list-j-1):
                print(Fore.BLUE + str(k) + '' + str(k+1) + Fore.RESET)
                #Comparamos el valor de la posicion actual con el valor de siguiente posicion
                if self.list_burble_sort[k] > self.list_burble_sort[k+1]:
                    #Transportacion de valores
                    self.list_burble_sort[k], self.list_burble_sort[k+1] = self.list_burble_sort[k+1], self.list_burble_sort[k]
        print(self.list_burble_sort)

    def burble_sort_function_refactor(self):
        change_position = True
        while change_position:
            change_position = False
            for i in range(len(self.list_burble_sort)-1):
                if self.list_burble_sort[i] > self.list_burble_sort[i+1]:
                    self.list_burble_sort[i], self.list_burble_sort[i+1] = self.list_burble_sort[i+1], self.list_burble_sort[i]
                    change_position = True
        print(self.list_burble_sort)

    def select_sort_function(self):
        print(Fore.CYAN + "-------------------------------------------" + Fore.RESET)
        print(Fore.GREEN + "Ordenamiento Seleccion"    + Fore.RESET)
        count_item_list = 0
        #Inicializamos el contador
        for i in self.list_select_sort:
            count_item_list += 1
        print(self.list_select_sort)    

        #recorremos la lista y generamos la comparacion de valores entre posiciones
        for i in range(count_item_list):
            min = i
            print(Fore.RED + str(i) + Fore.RESET)
            for j in range(i+1, count_item_list):
                print(Fore.BLUE + str(j) + Fore.RESET)  
                #Comparacion de valores
                print('Comparacion: ' + Fore.BLUE + str(self.list_select_sort[min]) + '-' + str(self.list_select_sort[j]) + Fore.RESET)
                if self.list_select_sort[min] > self.list_select_sort[j]:
                    min = j
            #Generamos el intercambio
            self.list_select_sort[i], self.list_select_sort[min] = self.list_select_sort[min], self.list_select_sort[i]
            print(self.list_select_sort)
        print(self.list_select_sort)

    def insert_sort_function(self):
        print(Fore.CYAN + "-------------------------------------------" + Fore.RESET)
        print(Fore.GREEN + "Ordenamiento Insercion"    + Fore.RESET)
        print(self.insert_sort_function)
        #Separamos la lista en dos partes(puede o no estar) ordenados
        for i in range(1, len(self.list_insert_sort)):
            item_visited = self.list_insert_sort[i]
            #Visitamos la posicion anterior a la actual
            j = i - 1
            #Todos los elementos de valor mayor pasan adelante
            while j >= 0 and self.list_insert_sort[j] > item_visited:
                print(Fore.CYAN + str(self.list_insert_sort[j]) + Fore.RESET + " > " +  str(item_visited))
                self.list_insert_sort[j + 1] = self.list_insert_sort[j]
                j -= 1
                print("valor posicion j while" + str(self.list_insert_sort[j]))
            #Transposicion
            self.list_insert_sort[j + 1] = item_visited
        print(self.list_insert_sort)

    def merge_sort_function(self):
        print(Fore.CYAN + "-------------------------------------------" + Fore.RESET)
        print(Fore.GREEN + "Ordenamiento Merge"    + Fore.RESET)
        tamano_de_lista = len(self.list_merge_sort) - 1

        for posicion_actual in range(0, self.list_merge_sort):
            posicion_menor = posicion_actual
            nombre_menor = self.list_merge_sort[posicion_menor]

        for posicion_buscar in range(posicion_actual, tamano_de_lista):
            nombre_buscar = self.list_merge_sort[posicion_buscar + 1]

            if nombre_menor > nombre_buscar:
                mnombre_menor = nombre_buscar
                posicion_menor = posicion_buscar + 1

        if posicion_menor != posicion_actual:
            nombre_menor = self.list_merge_sort[posicion_menor]
            self.list_merge_sort[posicion_menor] = self.list_merge_sort[posicion_actual]
            self.list_merge_sort[posicion_actual] = nombre_menor
            print(self.list_merge_sort)