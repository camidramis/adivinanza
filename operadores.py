# ---------------------------------------------------------------------------------------------
# Operadores en Python
# ---------------------------------------------------------------------------------------------

# Son simbolos o conjuntos de simbolos que realizan una operacion espefifica en uno o mas operandos.
# Hay distintos tipos de operadores: aritmeticos, de comparacion, logicos, de asignacion, entre otros.

# ---------------------------------------------------------------------------------------------
# Operadores Aritmeticos
# ---------------------------------------------------------------------------------------------

# Algunos incluyen: 
# + la suma
# - la resta
# * la multiplicacion
# / la division > devuelve un numero decimal
# // la division entera > devuelve un numero entero
# % el modulo > devuelve el resto de una division
# ** la potencia

# ---------------------------------------------------------------------------------------------
# Operadores de Asignacion
# ---------------------------------------------------------------------------------------------

# = asignacion
# += suma y asignacion
# -= resta y asignacion
# *= multiplicacion y asignacion
# /= division y asignacion > devuelve un decimal.

# ---------------------------------------------------------------------------------------------
# Operadores de Comparacion
# ---------------------------------------------------------------------------------------------

# == igual a
# != diferente a
# ! negacion
# >, <
# >=, <=


# ---------------------------------------------------------------------------------------------
# Operadores Logicos
# ---------------------------------------------------------------------------------------------

# Devuelven un valor booleano (True o False) dependiendo de la evaluacion de las condiciones.
# and: ambas condiciones se deben cumplir
# or: si se cumple al menos una de las condiciones
# not: lo opuesto a lo que se afirme, se puede usar en lugar de !=

x = 15
booleano = x > 10 and x < 20
#print(booleano) # True

y = 5
booleano2 = y > 10 or y < 20
#print(booleano2) # True

z = 0
booleano3 = z >= 0 and z!= 0
#print(booleano3) # False


# ---------------------------------------------------------------------------------------------
# Operadores de identidad
# ---------------------------------------------------------------------------------------------

# is
# is not

a = "Hola"
b = "Hola"
booleano = a is b
#print(booleano)


# ---------------------------------------------------------------------------------------------
# Operadores de peretenencia
# ---------------------------------------------------------------------------------------------

# in
# not in

texto = "En este texto van tecnologias: Python, Java, R, Django"

#print('Django' in texto)
#print('C++' in texto)

# Hay que tener en cuenta que son busquedas case sensitive. 
# Hay que limpiar el texto con las funciones como strip o lower para evitar errores de coincidencia.