from single_linked_list import SingleLinkedList
inst_sll = SingleLinkedList()

# Ingresamos como parametro el valor del nodo

""" Métodos para añadir nodo """
inst_sll.create_node_sll_ends('Batman')
inst_sll.create_node_sll_ends('Robin')
inst_sll.create_node_sll_ends('Gatuela')
inst_sll.create_node_sll_ends('Deadpool')
inst_sll.create_node_sll_ends('Wolverine')
inst_sll.create_node_sll_unshift('Hulk')
# | Hulk | Batman | Robin | Wolverine
inst_sll.show_list()

""" Métodos de eliminar """
print('-------------------------------------------')
print('        >> Eliminar último nodo <<')
inst_sll.delete_node_sll_pop()
inst_sll.show_list()

# | Hulk | Batman | Robin |

print('-------------------------------------------')
print('\n        >> Eliminar primer nodo <<')
inst_sll.shift_node_sll()
inst_sll.show_list()
# | Batman | Robin |

print('-------------------------------------------')
print('\n        >> Consultar valor de nodo <<')
inst_sll.get_node_value(1)
inst_sll.get_node_value(2)

print('-------------------------------------------')
print('\n        >> Actualizar valor de nodo <<')
inst_sll.update_node_value(1, "Linterna verde")
inst_sll.show_list()

print('-------------------------------------------')
print('\n        >> Eliminar nodo especifico <<')
inst_sll.remove_node(3)
inst_sll.show_list()

""" Métodos busqueda en la lista """
print('-------------------------------------------')
print('\n        >> Obtener tamaño de la lista <<')
print(inst_sll.list_size_node())
inst_sll.show_list()

print('-------------------------------------------')
print('\n        >> Buscar un elemento de la lista <<')
print(inst_sll.seek_posicion('Gatuela'))
inst_sll.show_list()

print('-------------------------------------------')
print('\n        >> Invertir elementos de la lista <<')
inst_sll.invest_list()
inst_sll.show_list()

print('---------------------------------------------------')
print('\n     >> Ordenar todos los elementos de la lista <<')
print(inst_sll.order_list())

print('---------------------------------------------------')
print('\n     >> Insertar un elemento en una posicion <<')
inst_sll.insert_node(2, 'Deadpool')
inst_sll.show_list()

print('---------------------------------------------------')
print('\n     >> Comprobar si la lista esta vacia <<')
inst_sll.check_if_it_is_empty()

print('---------------------------------------------------')
print('\n     >> Eliminar todos los elementos de la lista <<')
inst_sll.remove_node_list()
inst_sll.show_list()
inst_sll.check_if_it_is_empty()