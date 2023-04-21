'''
List methods
Date: 27/01/23

'''
class ListMethods:
    #1. Metodo inicializador de la clase
    def __init__(self):
        #Definimos una lista vacia
        self.pets = []
        self.vehicles = list()

    #2. Metodo para añadir elementos en la lista
    def add_list_elements(self):
        #['dog', 'cat']
        self.pets.append("dog")
        self.pets.append("cat")
        print(self.pets)

    #3. Metodo que solicita valores al usuario
    def input_data_vehicles_list(self):
        # Variables locales: vehicles_number, vehicle_type
        vehicles_number = int(input("¿Cuantos vehiculos tiene?"))
        #recorrer una lista
        for vehicle_item in range(vehicles_number):
            vehicle_type = input("Tipo de vehiculo: ")
            #Añadimos el vehiculo a la lista
            self.vehicles.append(vehicle_type)
        #Imprimir toda la lista
        print(self.vehicles)
        #Imprimir todos los elementos de la lista
        print(self.vehicles[-1]), print(self.vehicles[-2]), print(self.vehicles[-3])

    #4. Extraer subconjunto de una lista
    def show_collection_data_list(self):
        #Imprimir desde la posicion 2 hasta 3
        print(self.vehicles[2:4])   
        #Todos los elementos de la lista
        print(self.vehicles[:])
        #Elementos  desde un indice especifico: 2 [2, 3, ...]
        print(self.vehicles[2:])
        #Elementos hasta un indice especifico: 2 [0, 1, 2]
        print(self.vehicles[:2])
        #Acceder a los elementos de 2 en 2
        print(self.vehicles[::2])
        #Acceder a un SUBCONJUNTO de elementos de 2 en 2
        print(self.vehicles[1:5:2])

    #5. Iterar los elementos de una lista con for
    def iteration_list(self):
        for item in self.vehicles:
            print(item)
            #Validar si la lista contiene un valor especifico
        if "carro".capitalize() in self.vehicles:
            print("Si se encontro valor")
        else:
            print("No se encontro el valor")  

    #6. Añadir varios elementos al final de la lista
    def add_elements(self):
        self.vehicles.extend(["Avion", "tractomula", "otro medio"])
        print(self.vehicles)

    #7. Añadir un elemento en posicion especificada de la lista
    def add_specific_element(self):
        self.vehicles.insert(0, "Moto")
        print(self.vehicles)     

    #8. Eliminar ultimo elemento de la lista
    def remove_last_element(self):
        self.vehicles.pop()
        print(self.vehicles)

    #9. Eliminar elemento de posicion especifica
    def remove_specific_element(self):
        self.vehicles.pop(0)
        print(self.vehicles)

    #10. Eliminar todos los valores de la lista
    #def remove_element_by_name(self):
        #self.vehicles.clear()

    #11. Eliminar un valor especifico de la lista tractomula
    def remove_specific_element2(self):
        print(self.vehicles)
        self.vehicles.remove("tractomula".capitalize())
        print(self.vehicles)

    #12. E,liminar todas las coincidencias de valor en la lista
    def remove_all_match_elements(self):
        new_list = list(filter("tractomula".capitalize()).__ne__, self.vehicles)
        print(new_list)        