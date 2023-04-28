class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    #Insertar un nodo en el arbol
    def insert(self, root, node):
        #Si no existe raiz en el arbol
        if root is None:
            root = node
        else:
            if root.value > node.value:
                if root.left_node is None:
                    root.left_node = node
                else:
                    self.insert(root.left_node, node)
            else:
                if root.right_node is None:
                    root.right_node = node
                else:
                    self.insert(root.right_node, node)

    def print_tree(self, root):
        if root is not None:
            self.print_tree(root.left_node)
            print(root.value)
            self.print_tree(root.right_node)