### Operadores Aritméticos ###

# Operaciones con numeros enteros
print(3 + 4)   # Suma → 7
print(3 - 4)   # Resta → -1
print(3 * 4)   # Multiplicación → 12
print(3 / 4)   # División con decimales → 0.75
print(3 // 4)  # División entera — descarta los decimales → 0
print(3 % 4)   # Módulo — devuelve el resto de la división → 3
print(3 ** 4)  # Potencia — 3 elevado a 4 → 81
print(-3)      # Negativo → -3
print(+3)      # Positivo → 3
print(2 ** 3 + 5 * 4 - 10 / 2)  # Python respeta el orden matemático: primero ** y *, luego + y - → 23.0

# Operaciones con cadenas de texto
print("Hola " + "Python")  # + une dos strings → "Hola Python"
print("Hola " + str(5))    # hay que convertir el número a string con str() para poder concatenarlo

# Operaciones mixtas
print("Hola " * 3)          # * repite el string 3 veces → "Hola Hola Hola "
print("Hola " * (2 ** 3))   # 2**3 = 8, repite el string 8 veces

my_float = 2.5 * 2          # → 5.0
print("Hola " * int(my_float))  # int() convierte 5.0 a 5 para poder usarlo como repetidor

### Operadores de comparación ###
# Devuelven True o False

# Operaciones con enteros
print(3 == 4)  # Igualdad → False
print(3 != 4)  # Desigualdad → True
print(3 > 4)   # Mayor que → False
print(3 < 4)   # Menor que → True
print(3 >= 4)  # Mayor o igual que → False
print(3 <= 4)  # Menor o igual que → True

# Operaciones con cadenas de texto
# Python compara strings letra por letra según su valor ASCII
print("Hola" > "Python")   # "H" (72) < "P" (80) → False
print("Hola" < "Python")   # → True
print("aaaa" >= "abaa")    # compara letra por letra: "a"=="a", luego "a" < "b" → False
print(len("aaaa") >= len("abaa"))  # compara longitudes: 4 >= 4 → True
print("Hola" <= "Python")  # → True
print("Hola" == "Hola")    # → True
print("Hola" != "Python")  # → True

### Operadores lógicos ###
# and → True solo si ambos son True
# or  → True si al menos uno es True
# not → invierte el resultado

print(3 > 4 and "Hola" > "Python")  # False and False → False
print(3 > 4 or "Hola" > "Python")   # False or False → False
print(3 < 4 and "Hola" < "Python")  # True and True → True
print(3 < 4 or "Hola" > "Python")   # True or False → True (con or basta uno)
print(3 < 4 or ("Hola" > "Python" and 4 == 4))  # True or (False and True) → True
print(not (3 > 4))  # not False → True