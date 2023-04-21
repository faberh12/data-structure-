class TupleList:
    def __init__(self):
        self.countries_list = []
        self.country_name = ""
        self.population = 0
        self.continent = ""

    # Funcion que solicita al usuario nro de paises a crear 
    def total_countries(self):
        print("Ingrese la siguiente informacion")  
        print("=========================================== ")
        while True:
            try:
                number_countries = int(input("Cantidad a añadir: "))
                for country in range(number_countries):
                    self.country_name = input("  Pais >> ")
                    while True:
                        try:
                            self.population = int(input("  Poblacion >> "))
                            self.continent = input("  Continente >> ")  
                        print("-------------------")
                        #Añadimos una tupla a la lista append((valores de la tupla))
                        self.countries_list.append(self.country_name, self.population, self.continent)
                        except ValueError:
                        print(">> Se esperaba un numero >>")  
                print(self.countries_list)
            except ValueError:
        print(">> Error en el tipo de dato suministrado <<")     