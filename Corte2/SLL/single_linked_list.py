class SingleLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    """Por fuera de la clase nodo"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def show_list(self):
        # 1. Declarar una array(lista) vacío que contendra los valores de los nodos de SLL
        # array_with_nodes_value = []
        array_with_nodes_value = list()
        current_node = self.head
        # Mientras el nodo actual que estoy visitando sea diferente de None
        while (current_node != None):
            # Añado al final de la listael valor extraido del nodo
            array_with_nodes_value.append(current_node.value)
            # Visito el próximo nodo antes de salir del while
            # Incrementamos en 1 el valor del nodo visitado
            # current_node += 1 NO SIRVE PARA PASAR AL SIGUIENTE NODO DE UNA SLL
            # Pasamos del nodo actual al siguiente nodo mediante el puntero
            current_node = current_node.next
        # Imprimimos la lista
        print(
            f'Los valores de los nodos de la SLL son:\n{array_with_nodes_value}')

    def create_node_sll_ends(self, value):
        # Creamos una variable que va a tener la estructura de un nodo
        new_node = self.Node(value)
        # Validar si la SLL tiene nodos o no
        if self.head == None:
            # Al nuevo nodo se convierte en la cabeza y cola de la lista
            self.head = new_node
            self.trail = new_node
        else:
            # Si en está condición, es porque ya existe al menos un nodo
            # 1. Debemos relacionar al nuevo nodo con la cola de la lista
            # 2. Convertir al nuevo nodo en la cola de la lista
            self.trail.next = new_node
            self.trail = new_node
        # Incrementamos en 1 el tamaño de la lista
        self.length += 1

    def create_node_sll_unshift(self, value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.trail = new_node
        else:
            # 1. Debemos relacionar al nuevo nodo con la cola de la lista
            # 2. Convertir al nuevo nodo en la cola de la lista
            new_node.next = self.head
            self.tail = new_node
        # Incrementamos en 1 el tamaño de la lista
        self.length += 1

    def delete_node_sll_pop(self):
        # 1. Validar si la lista está vacía
        # 2. Validar si la lista tiene un único nodo
        # 3. Si tiene más de un nodo eliminar el nodo que es la cola de lista
        # 4. Asignar al nodo anterior como la nueva cola de la lista
        if self.head == 0:
            print('>> Lista vacía no hay nodos por eliminar <<')
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            # 1. Recorrer la lista para identificar la cola
            current_node = self.head
            """ Nueva linea """
            new_tail = current_node
            # 2. Validar mediante el enlace del nodo actual que haya un nodo
            while current_node.next != None:
                # 3. Convertimos en la cola de la lista el nodo que actualmente visitamos
                new_tail = current_node
                # 4. Pasamos al siguiente nodo antes de salir del while
                current_node = current_node.next
            # 5. Actualizamos la cola de la lista
            self.tail = new_tail
            self.tail.next = None
            # 6. Restamos en 1 el tamaño de la lista
            self.length -= 1

    """ Eliminar nodo al inicio de la lista """

    def shift_node_sll(self):
        print(self.length)
        if self.length == 0:
            print('>> Lista vacía no hay nodos por elimina <<')
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            remove_node = self.head
            print(f'El valor del nodo a eliminar es: {remove_node.value} ')
            self.head = remove_node.next
            self.length -= 1

    def get_node(self, index):
        if index < 1 or index > self.length:
            return None
        elif index == 1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            node_counter = 1
            while (index != node_counter):
                current_node = current_node.next
                node_counter += 1
                return current_node

    def get_node_value(self, index):
        if index < 1 or index > self.length:
            print('No se encontro')
        elif index == 1:
            print(self.head.value)
        elif index == self.length:
            print(self.tail.value)
        else:
            current_node = self.head
            node_counter = 1
            while (index != node_counter):
                current_node = current_node.next
                node_counter += 1
            print(current_node.value)

    def update_node_value(self, index, new_value):
        search_node = self.get_node(index)
        if search_node != None:
            # Encontro el nodo y se puede actualizar
            print(
                'Actualizando el valor del nodo...\n {search_node.value} por {new_value}')
            search_node.value = new_value
        else:
            # No encuentra el nodo
            print('     >> No se encontro el nodo <<')

    def remove_node(self, index):
        if index == 1:
            self.shift_node_sll()
        elif index == self.length:
            self.delete_node_sll_pop()
        else:
            remove_node_sll = self.get_node(index)
            if remove_node_sll != None:
                previous_node = self.get_node(index - 1)
                print(self.get_node(index).value)
                previous_node.next = remove_node_sll.next
                remove_node_sll.next = None
            else:
                print('     >> No se encontro el nodo <<')

    # 5 Obtener el tamaño de la lista simplemente enlazada.
    def list_size_node(self):
        contador = 0
        current = self.head
        while current != None:
            current = current.next
            contador += 1
        return contador

    # 6 Buscar un elemento en la lista simplemente enlazada y devolver su posición.
    def seek_posicion(self, valor):
        if valor == self.head.value:
            return print('1')
        elif valor == self.tail.value:
            return print(self.length)
        else:
            current_node = self.head
            node_counter = 1
            while (valor != current_node.value):
                print(current_node.value)
                current_node = current_node.next
            return print(node_counter)

    # 8 Invertir la lista simplemente enlazada
    def invest_list(self):
        previous = None
        current_node = self.head
        while current_node != None:
            next = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = next
        self.head = previous

    # 9 Eliminar todos los elementos de la lista simplemente enlazada
    def remove_node_list(self):
        while self.head != None:
            remove_node = self.head
            self.head = remove_node.next
            self.length -= 1

    # 10 Ordenar los elementos de la lista
    def order_list(self):
        array_whith_nodes_value = list()
        new_list = list()
        current_node = self.head
        while (current_node != None):
            array_whith_nodes_value.append(current_node.value)
            current_node = current_node.next
        new_list = array_whith_nodes_value
        new_list.sort()
        return print(new_list)

    # 12 Insertar un elemento en una posicion
    def insert_node(self, index, value):
        new_node = self.Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            previous_node = self.head
            for i in range(index-1):
                previous_node = previous_node.next
                if previous_node is None:
                    raise IndexError("Index out of range")
                new_node.next = previous_node.next
                previous_node.next = new_node
        
    # 14 Comprobar si la lista esta vacia
    def check_if_it_is_empty(self):
        if self.head == None:
            return (print('La lista esta vacia'))
        else:
            return (print('La lista tiene elementos'))
