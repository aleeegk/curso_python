### Lists ###

# Definición — dos formas de crear una lista vacía
my_list = list()  # usando el constructor list()
my_other_list = []  # forma más común y corta

print(len(my_list))  # → 0, la lista está vacía

# Listas con valores — pueden contener cualquier tipo de dato
my_list = [35, 24, 62, 52, 30, 30, 17]  # lista de enteros

print(my_list)
print(len(my_list))  # → 7 elementos

my_other_list = [35, 1.77, "Brais", "Moure"]  # lista mixta: int, float, strings

print(type(my_list))        # → <class 'list'>
print(type(my_other_list))  # → <class 'list'>

# Acceso a elementos — igual que slicing en strings, empieza en índice 0
print(my_other_list[0])   # primer elemento → 35
print(my_other_list[1])   # segundo elemento → 1.77
print(my_other_list[-1])  # último elemento → "Moure"
print(my_other_list[-4])  # cuarto desde el final → 35
print(my_list.count(30))  # cuenta cuántas veces aparece 30 → 2
# print(my_other_list[4])  # IndexError — no existe índice 4, solo hay 4 elementos (0-3)
# print(my_other_list[-5]) # IndexError — tampoco existe índice -5

# Desempaquetado — asigna cada elemento a una variable (tienen que coincidir en cantidad)
age, height, name, surname = my_other_list
print(name)  # → "Brais"

# Desempaquetado manual accediendo por índice
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)  # → 35

# Concatenación — + une dos listas en una nueva
print(my_list + my_other_list)
# print(my_list - my_other_list)  # Error — no se puede restar listas

# Creación, inserción, actualización y eliminación

my_other_list.append("MoureDev")  # append() añade un elemento al final
print(my_other_list)

my_other_list.insert(1, "Rojo")  # insert(índice, valor) inserta en una posición concreta
print(my_other_list)

my_other_list[1] = "Azul"  # actualiza el elemento en el índice 1
print(my_other_list)

my_other_list.remove("Azul")  # remove() elimina la primera aparición del valor
print(my_other_list)

my_list.remove(30)  # elimina el primer 30 que encuentra (había dos)
print(my_list)

print(my_list.pop())   # pop() sin argumento elimina y devuelve el último elemento
print(my_list)

my_pop_element = my_list.pop(2)  # pop(índice) elimina y devuelve el elemento en ese índice
print(my_pop_element)
print(my_list)

del my_list[2]  # del elimina el elemento en el índice 2 sin devolver nada
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()  # copy() crea una copia independiente — si usaras = ambas apuntarían a la misma lista

my_list.clear()       # vacía la lista completamente
print(my_list)        # → []
print(my_new_list)    # la copia no se ve afectada

my_new_list.reverse()  # invierte el orden de los elementos
print(my_new_list)

my_new_list.sort()  # ordena los elementos de menor a mayor
print(my_new_list)

# Sublistas — slicing igual que en strings
print(my_new_list[1:3])  # elementos del índice 1 al 2 (el 3 no se incluye)

# Cambio de tipo — Python permite reasignar una variable a cualquier tipo
my_list = "Hola Python"  # my_list era una lista y ahora es un string
print(my_list)
print(type(my_list))  # → <class 'str'>