### Strings ###

# Strings con comillas dobles y simples (ambas funcionan igual)
my_string = "Mi String"
my_other_string = 'Mi otro String'

# len() devuelve la cantidad de caracteres del string
print(len(my_string))
print(len(my_other_string))

# + concatena (une) dos strings
print(my_string + " " + my_other_string)

# \n es un salto de línea
my_new_line_string = "Este es un String \ncon salto de línea"
print(my_new_line_string)

# \t es una tabulación (espacio largo)
my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

# \\ escapa el backslash, haciendo que \t y \n se impriman literalmente
my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo — 4 formas de meter variables dentro de un print

name, surname, age = "Alejandro", "Ferreira", 14

# .format() — los {} se reemplazan en orden por los valores del .format()
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))

# % — estilo antiguo: %s es string, %d es número entero
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))

# Concatenación — une strings con +, los números hay que convertirlos con str()
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))

# f-string — la forma más moderna y legible, variables directamente entre {}
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres — asigna cada letra a una variable distinta
language = "python"
a, b, c, d, e, f = language
print(a)  # → p
print(b)  # → y

# División (slicing) — corta el string con [inicio:fin]
language_slice = language[1:3]  # del índice 1 al 2 (el 3 no se incluye) → "yt"
print(language_slice)

language_slice = language[1:]  # desde el índice 1 hasta el final → "ython"
print(language_slice)

language_slice = language[-2]  # índice -2 cuenta desde el final → "o"
print(language_slice)

language_slice = language[0:6:2]  # de 0 a 6 saltando de 2 en 2 → "pto"
print(language_slice)

# Reverse — [::-1] recorre el string al revés
reversed_language = language[::-1]  # → "nohtyp"
print(reversed_language)

# Funciones / métodos de strings
print(language.capitalize()) # Primera letra mayúscula, resto minúsculas → "Python"
print(language.upper())      # Todo mayúsculas → "PYTHON"
print(language.lower())      # Todo minúsculas → "python"
print(language.count("t"))   # Cuenta cuántas veces aparece "t" → 1
print("1".isnumeric())       # Comprueba si es un número → True
print(language.isnumeric())  # "python" no es número → False
print(language.upper().isupper())  # Convierte a mayúsculas y comprueba si todo es mayúscula → True
print(language.startswith("py"))   # Comprueba si empieza por "py" → True
print("Py" == "py")  # False — Python distingue mayúsculas de minúsculas