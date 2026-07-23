print("Hola mundo")

# Aprendiendo a comentar. Es ignora en la ejecución del programa.
# Sirve para dejar acotaciones en el código, explicaciones o recordatorios para el que lee.

""" 
Tambien podemos comentar usando la triple comilla. 
Es clave para comentarios largos, o para escribir documentación.

"""

# ---------------------------------------------------------------------
# Se usa este tipo de comentario para separar en secciones el código. Sirve para organizarlo y hacerlo más legible.
# ---------------------------------------------------------------------


# ---------------------------------------------------------------------
# SINTAXIS DE PYTHON - Reglas que se deben seguir al escribir el código para que sea válido.
# ---------------------------------------------------------------------

""" 
Indentación: sangría al comienzo de las líneas para indicar bloques de código.

Variables: contenedores que almacenan datos que pueden cambiar durante la ejecución del programa.
Cada variable tiene un nombre único y un valor asociado. Se pueden usar para almacenar números, texto, listas, etc.
Para nombrar las variables, se deben seguir ciertas reglas:
- El nombre debe comenzar con una letra (a-z, A-Z) o un guion bajo (_).
- El nombre puede contener letras, números y guiones bajos, pero NO puede iniciar con números ni se pueden utilizar espacios o caracteres especiales.
- El nombre no puede ser una palabra reservada de Python (como if, for, while, etc.).

Tipos de datos 
- Números: enteros (int) y decimales (float).
- Cadenas de texto: secuencias de caracteres (str).
- Booleanos: valores de verdad (True o False).

Castear: convertir un valor de un tipo de dato a otro. 
Por ejemplo, si x = 5 (es int), entonces y = str(x) convierte el número 5 a la cadena de texto "5".

"""

# Definimos una variable de tipo string
texto = "Hola mundo" #Va entre comillas

# Variable de tipo entero
numero = 23

# Variable de tipo float
numero_decimal = 3.14

# Numeros complejos
numero_complejo = 2 + 3j

# Variables de tipo SECUENCIA
# Una lista es ordenada y mutable, lo que significa que se pueden modificar sus elementos después de haber sido creada.
lista = [1, 2, 3, 4, 5]

# La tupla es ordenada, pero inmutable.
tupla = (1, 2, 3) # Tupla de números enteros

# Secuencia inmutable de números
rango = range(1, 10) # Rango de números del 1 al 9

# Variable de MAPEO
# Un diccionario es una colección de pares clave-valor, donde cada clave es única y se utiliza para acceder a su valor correspondiente.
diccionario = {
    "nombre": "Juan", 
    "edad": 30, 
    "ciudad": "Buenos Aires"
}

# Variables de CONJUNTO
# Set, conjunto: colección no ordenada de elementos únicos. No permite duplicados.
conjunto = {1, 2, 3, 4, 5}

# Frozenset: conjunto inmutable, no permite modificar sus elementos después de haber sido creado.
conjunto_inmutable = frozenset({1, 2, 3, 4, 5}) 

# Variable nula
nulo = None


# ---------------------------------------------------------------------
# CASTEO
# ---------------------------------------------------------------------

# Definimos:
txt1 = "Texto"
txt2 = "123"
txt3 = "Texto123"

nro1 = 10
nro2 = 3.14
nro3 = 2 + 3j

print(type(txt1)) # <class 'str'>
print(type(txt2)) # <class 'str'>
print(type(txt3)) # <class 'str'>
print(type(nro1)) # <class 'int'>
print(type(nro2)) # <class 'float'>
print(type(nro3)) # <class 'complex'>

# Casteo de str a int

var_casteada = int(txt2)
print(type(var_casteada)) # <class 'int'>

# Casteo de int a str

var_casteada2 = str(nro1)
print(type(var_casteada2)) # <class 'str'>