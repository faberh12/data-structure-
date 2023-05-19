class SLL:

    class Node:
        def __init__(self,value):
            self.value=value
            self.next=None

    def __init__(self):
        self.head=None
        self.tail=None
        self.length =0
    
    def show_list(self):
        array_with_nodes_value=list()
        current_node=self.head
        while(current_node != None):
            array_with_nodes_value.append(current_node.value)
            current_node=current_node.next
        #print(f'Los valores de los nodos de la SLL son:\n {array_with_nodes_value}')
        return array_with_nodes_value
        
    #1. Agregar un elemento al principio de la lista simplemente enlazada.
    def create_node_sll_unshift(self,value):
        new_node=self.Node(value)
        if self.head == None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length +=1
    
    #2. Agregar un elemento al final de la lista simplemente enlazada.
    def create_node_sll_ends(self,value):
        new_node=self.Node(value)
        if self.head == None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length +=1

    #3. Eliminar el primer elemento de la lista simplemente enlazada.
    def shift_node_sll(self):
        if self.length == 0:
            print('>> Lista vacia no hay nodos por eliminar <<')
        elif self.length == 1:
            self.head =None
            self.tail=None
            self.length-=1
        else:
            remove_node=self.head
            print(remove_node.value)
            self.head=remove_node.next
            self.length-=1

    #4. Eliminar el último elemento de la lista simplemente enlazada.
    def delete_node_sll_pop(self):
        if self.length == 0:
            print('>> Lista vacia no ha nodos por eliminar <<')
        elif self.length == 1:
            self.head = None
            self.tail=None
            self.length-=1
        else:
            current_node=self.head
            new_tail=current_node
            while current_node.next != None:
                new_tail=current_node
                current_node= current_node.next
            self.tail=new_tail
            self.tail.next=None
            self.length-=1
    
    #5. Obtener el tamaño de la lista simplemente enlazada
    def lenght_sll(self):
        return self.length
        #print(f'El tamaño de la SLL es: {self.length}')
    
    #6. Buscar un elemento en la lista simplemente enlazada y devolver su posición. 
    def get_node_index(self,value):
        if self.length == 0:
            print('>> Lista vacia no hay elementos<<')
        elif self.head.value == value:
            return print("1")
        elif self.tail.value == value:
            return print(self.length)
        else:
            current_node =self.head
            node_counter=1
            while(self.length > node_counter):
                if current_node.value == value:
                    return print(node_counter)   
                current_node=current_node.next
                node_counter+=1
            print('El valor no se encuentra en la lista')


    #Consultar nodo
    def get_node(self,index):
        if index<1 or index >self.length:
            return None
        elif index ==1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node =self.head
            node_counter=1
            while(index != node_counter):
                current_node=current_node.next
                node_counter+=1
            return current_node
    
    #7. Devolver el elemento en una determinada posición de la lista simplemente enlazada
    def get_node_value(self,index):
        if index<1 or index >self.length:
            print('No se encontro')
        elif index ==1:
            print(self.head.value) 
        elif index == self.length:
            print(self.tail.value) 
        else:
            current_node =self.head
            node_counter=1
            while(index != node_counter):
                current_node=current_node.next
                node_counter+=1
            print(current_node.value)
    
    #8. Invertir la lista simplemente enlazada
    def reverse_sll(self):
        if self.length == 2:
            self.head=self.tail
            self.tail=self.head
        if self.length>2:
            previus_node=None
            next_node=None
            current_node=self.head
            while current_node:
                next_node=current_node.next
                current_node.next=previus_node
                previus_node=current_node
                current_node=next_node
            self.head=previus_node
                
    #9. Eliminar todos los elementos de la lista simplemente enlazada.
    def delete_all_sll(self):
        self.head =None
        self.tail=None
        self.length=0

    #10. Ordenar los elementos de la lista simplemente enlazada.
    def order_sll(self):
        array_with_nodes_value=list()
        current_node=self.head
        while(current_node != None):
            array_with_nodes_value.append(current_node.value)
            current_node=current_node.next

        array_with_nodes_value.sort()
        
        node_counter=0
        current_node_two=self.head
        while(current_node_two != None):
            current_node_two.value=array_with_nodes_value[node_counter]
            node_counter+=1
            current_node_two=current_node_two.next
            
        

    #11.Eliminar un elemento en una posición determinada de la lista simplemente enlazada
    def remove_node(self,index):
        if index== 1:
            self.shift_node_sll()
        elif index==self.length:
            self.delete_node_sll_pop()
        else:
            remove_node_sll=self.get_node(index)
            if remove_node_sll!=None:
                previous_node=self.get_node(index -1)
                print(self.get_node(index).value)
                previous_node.next=remove_node_sll.next
                remove_node_sll.next=None
            else:
                print("          >> No se encontro el nodo  <<")
    
    #12. Insertar un elemento en una posición determinada de la lista simplemente enlazada. 
    def create_node_sll(self,index,value):
        if self.length==0:
            self.head=new_node
        elif index== 1:
            self.create_node_sll_unshift(value)
        elif index==self.length:
            self.create_node_sll_ends(value)
        else:
            current_node=self.head
            current_node_two=self.head
            new_node=self.Node(value)
            node_counter=1
            node_counter_two=1
            while current_node!=None:
                if node_counter==index:
                    new_node.next=current_node
                    break
                else:
                    node_counter +=1
                    current_node=current_node.next
            while current_node_two != None:
                if node_counter_two==index-1:
                    current_node_two.next=new_node
                    current_node_two=new_node
                    break
                else:
                    current_node_two=current_node_two.next
                    node_counter_two +=1
            self.length+=1
    
    #Insertar un elemento ingresado por el usuario. 
    def create_node_sll_user(self):
        index=int(input("ingrese la poscion en la que va el valor"))
        value=input("Ingrese el valor que desea añadir")
        if self.length==0:
            self.head=new_node
        elif index== 1:
            self.create_node_sll_unshift(value)
        elif index==self.length:
            self.create_node_sll_ends(value)
        else:
            current_node=self.head
            current_node_two=self.head
            new_node=self.Node(value)
            node_counter=1
            node_counter_two=1
            while current_node!=None:
                if node_counter==index:
                    new_node.next=current_node
                    break
                else:
                    node_counter +=1
                    current_node=current_node.next
            while current_node_two != None:
                if node_counter_two==index-1:
                    current_node_two.next=new_node
                    current_node_two=new_node
                    break
                else:
                    current_node_two=current_node_two.next
                    node_counter_two +=1
            self.length+=1


    #13. Actualizar el valor de un elemento en una posición determinada de la lista simplemente enlazada
    def update_node_value(self,index,new_value):
        search_node=self.get_node(index)
        if search_node != None:
            print(f'Actalizando el valor del nodo ...\n           >>{search_node.value} << a >> {new_value}')
            search_node.value=new_value
        else:
            print("   >>No se encontro el nodo") 
    
    #14. Comprobar si la lista simplemente enlazada está vacía.
    def empy_sll(self):
        if self.length == 0:
            print('>> Lista vacia no hay elementos<<')
        else:
            print(f"La lista tiene {self.length} elementos")


    #16 eliminar por valor 
    def eliminar_por_valor(self,value):
        if self.head ==None:
            print('La lista esta vacia') 
        elif self.head.value==value:
            self.shift_node_sll()
        elif self.tail.value == value:
            self.delete_node_sll_pop()
        else:
            count=1
            current_node=self.head
            while current_node != None:
                if current_node.value==value:
                    previous_node = self.get_node(count -1)
                    previous_node.next=current_node.next
                    current_node.next=None
                current_node=current_node.next
                count+=1
            self.length-=1

#Metodo que elimina duplicados y deja uno de cada uno
    def eliminar_duplicates(self):
        if self.head is None:
            return
        current_node=self.head
        values=set()
        while current_node is not None:
            if current_node.value in values:
                self.eliminar_por_valor(current_node.value)
            values.add(current_node.value)
            current_node=current_node.next
        print(values)
    
#metodo que une los duplicados
    def unir_duplicados(self):
        count=1
        if self.head is None:
            return
        current_node=self.head
        values=set()
        for item in self.show_list():
            if item in values:                
                self.create_node_sll(count,item)
                self.eliminar_por_valor(item)
            values.add(item)
            count+=1


