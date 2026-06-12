### Tuples ###

# Definición — dos formas de crear una tupla vacía
my_tuple = tuple()  # usando el constructor tuple()
my_other_tuple = () # forma más corta

# Las tuplas son como listas pero inmutables — no se pueden modificar una vez creadas
my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))  # → <class 'tuple'>

# Acceso a elementos — igual que listas y strings, por índice
print(my_tuple[0])   # primer elemento → 35
print(my_tuple[-1])  # último elemento → "Brais"
# print(my_tuple[4])  # IndexError — el índice 4 no existe (hay 5 elementos, índices 0-4... espera, sí existe)
# print(my_tuple[-6]) # IndexError — no existe índice -6, solo hay 5 elementos

print(my_tuple.count("Brais"))   # cuenta cuántas veces aparece "Brais" → 2
print(my_tuple.index("Moure"))   # devuelve el índice de la primera aparición de "Moure" → 3
print(my_tuple.index("Brais"))   # devuelve el índice de la primera aparición de "Brais" → 2

# my_tuple[1] = 1.80  # Error — las tuplas son inmutables, no se pueden modificar

# Concatenación — + une dos tuplas en una nueva
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas — slicing igual que en listas y strings
print(my_sum_tuple[3:6])  # elementos del índice 3 al 5

# Tupla mutable con conversión a lista
# Si necesitas modificar una tupla, la conviertes a lista, la modificas y la vuelves a convertir

my_tuple = list(my_tuple)   # convierte la tupla a lista → ya es modificable
print(type(my_tuple))       # → <class 'list'>

my_tuple[4] = "MoureDev"    # modifica el elemento en índice 4
my_tuple.insert(1, "Azul")  # inserta "Azul" en el índice 1
my_tuple = tuple(my_tuple)  # vuelve a convertir a tupla → ya es inmutable de nuevo
print(my_tuple)
print(type(my_tuple))  # → <class 'tuple'>

# Eliminación

# del my_tuple[2]  # TypeError — no puedes eliminar un elemento de una tupla
del my_tuple        # del sin índice elimina la variable entera de la memoria
# print(my_tuple)  # NameError — la variable ya no existe   