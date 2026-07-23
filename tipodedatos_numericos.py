import random

# -------------------------------------------------------------------------------------
# Tipos de datos númericos
# -------------------------------------------------------------------------------------

# Existen:
x = 1 # Entero (int)
y = 3.14 # Decimal (float)
z = 2 + 3j # Complejo (complex)

#Los tres tipos de datos aceptan números negativos.

# print(type(x)) # <class 'int'>
# print(type(y)) # <class 'float'>
# print(type(z)) # <class 'complex'>

x = 2

y = float(x)

# print(y)
# print(type(y)) # <class 'float'>

x = 3.14

y = int(x)

# print(y)
# print(type(y))

# Esto tipo de casteo de float a int, elimina la parte decimal del numero definido, quedando solo la parte entera.


# ------------------------------------------------------------------------------------------
# Rangos de aleatoreidad
# ------------------------------------------------------------------------------------------

x = random.randrange(1, 10) # No incluye el 10. Va del 1 al 9
# print(x)

x = random.random()
# print(x) # Imprime un número decimal aleatorio entre 0.0 y 1.0. De tipo Float

x = random.randint(1, 10) # Incluye el 10. Va del 1 al 10
# print(x) # Imprime un número entero aleatorio entre 1 y 10
