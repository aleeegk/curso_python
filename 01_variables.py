### Variables ###

# Variable de tipo string (texto)
my_string_variable = "My String variable"
print(my_string_variable)

# Variable de tipo int (número entero)
my_int_variable = 5
print(my_int_variable)

# Convertimos el int a string con str()
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))  # type() muestra el tipo de la variable → <class 'str'>

# Variable de tipo bool (verdadero o falso)
my_bool_variable = False
print(my_bool_variable)

# Concatenación — print acepta varias variables separadas por comas
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# len() devuelve la cantidad de caracteres del string
print(len(my_string_variable))

# Varias variables en una sola línea — posible pero úsalo con cuidado, puede ser difícil de leer
name, surname, alias, age = "Alejandro", "Ferreira", "Ale", 14
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# input() para pedir datos al usuario — siempre devuelve un string
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')

print(name)
print(age)

# Python permite reasignar una variable a cualquier tipo — name era string y ahora es int
name = 35
age = "Brais"
print(name)
print(age)

# Python permite indicar el tipo esperado con : pero NO lo fuerza
# address empieza como str pero se reasigna a bool, int y float sin error
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))  # → <class 'float'> porque el último valor asignado es 1.2