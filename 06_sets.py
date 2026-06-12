### Sets ###

# Definición — dos formas de crear un set
my_set = set()  # set vacío usando el constructor
my_other_set = {}  # ojo — esto NO es un set vacío, es un diccionario vacío

print(type(my_set))        # → <class 'set'>
print(type(my_other_set))  # → <class 'dict'> — por eso hay que usar set() para crear uno vacío

my_other_set = {"Brais", "Moure", 35}  # al añadir elementos ya lo reconoce como set
print(type(my_other_set))  # → <class 'set'>

print(len(my_other_set))   # → 3 elementos

# Inserción — add() añade un elemento al set
my_other_set.add("MoureDev")

print(my_other_set)  # el orden puede variar — los sets no guardan orden

my_other_set.add("MoureDev")  # los sets no admiten duplicados — simplemente lo ignora

print(my_other_set)  # sigue teniendo los mismos elementos

# Búsqueda — in comprueba si un elemento existe en el set
print("Moure" in my_other_set)   # → True
print("Mouri" in my_other_set)   # → False

# Eliminación
my_other_set.remove("Moure")  # remove() elimina el elemento — da error si no existe
print(my_other_set)

my_other_set.clear()          # clear() vacía el set
print(len(my_other_set))      # → 0

del my_other_set               # del elimina la variable de la memoria
# print(my_other_set)          # NameError — la variable ya no existe

# Transformación — puedes convertir un set a lista para poder acceder por índice
my_set = {"Brais", "Moure", 35}
my_list = list(my_set)   # los sets no tienen índices, las listas sí
print(my_list)
print(my_list[0])        # ahora sí puedes acceder por índice

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

# union() combina dos sets en uno nuevo sin duplicados
my_new_set = my_set.union(my_other_set)

# puedes encadenar varios union() seguidos — añade JavaScript y C# al resultado
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))

# difference() devuelve los elementos que están en my_new_set pero NO en my_set
print(my_new_set.difference(my_set))  # → {'Kotlin', 'Swift', 'Python'}