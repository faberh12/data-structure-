'''
Data type:list practice
Date: 25/01/23
'''

# 1. Declarar la clase
class ListPractice:
    #2. crear funcion inicializadora de la clase
    def __init__(self):
        self.student_name = "Juan"
        self.courses_list = ["POO", "TAD"]

    #3. Funcion customizada
    def show_info_list(self):
        # Imprimir rl contenido de la lista courses_list
        print(self.courses_list)  
        # Cantidad de elementos que tiene la lista
        print(len(self.courses_list))  

    #4. Funcion que solicita al usuario ingresar informacion
    def input_data_courses(self):
        #1. Declaramos una variable a nivel del metodo
        print('Ingrese la siguiente informacion: ')
        self.student_name = input('Nombre: ')
        # Solicitud de numero entero
        courses_number = int(input('Cantidad asignaturas: '))
        # Validamos si el courses_number es menor wue el tamaño actual de la lista
        if courses_number <= len(self.courses_list):
            print('>> Error: Cursos a inscribir es menor que 2 <<')
        else:
            print('cantidad de asignaturas mayor a 2')        
        # Solicitar nombre de las asignaturas al usuario
        for course in range(len(self.courses_list), courses_number):    
            course_name = input('Nombre asignatura: ')
        #Añadimos nuevoelemento al final de la lista
        if course_name == self.courses_list[0] or course_name == self.courses_list[1]:
            print('son iguales')
        else:
            self.courses_list.append(course_name)       
        # Imprimir contenido de la lista 
        print(self.courses_list)     