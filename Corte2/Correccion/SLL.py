class Sll:
    class node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.length = 0

        def __init__(self):
            self.head = None
            self.tail = None
            self.length = 0

    def show_list(self):
        array_with_node = list()
        current_node = self.head
        while(current_node != None):
            array_with_node.append(current_node.value)
            current_node = current_node.next
        print(f'Los valores del nodo son:\n {array_with_node}')

    def create_node_end(self, value):
        #Variable con la estructura del node
        new_node = self.Node(value)

        #Validar si tiene nodos
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def multiplicate_list(self):
        array_with_node = list()
        current_node = self.head
        while(current_node != None):
            array_with_node.append(current_node.value * 2)
            current_node = current_node.next
        print(array_with_node)