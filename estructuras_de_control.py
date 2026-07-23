# ---------------------------------------------------------------------------------------------
# ESTRUCTURAS DE CONTROL
# ---------------------------------------------------------------------------------------------

# Es un bloque de codigo que permite controlar el flujo de ejecucion de un programa.
# Determinan que instrucciones se ejecutaran y en que orden, basandose en condiciones especificas.
# Tenemos:
# > Estructuras de decision/condicionales: ejecutan un bloque de codigo si se cumple una condicion. De lo contrario, se ejecuta otro bloque.
# > Bucles: ejecutan un blque de codigo repetidamente mientras se cumpla una condicion o hasta que se vuelva falsa. 
# > Estructuras de control de excepciones: permiten manejar errores o situaciones excepcionales que pueden ocurrir durante la ejecucion del programa.

# Condicionales
# if, elif, else

# Condicionales ternarias
# condicion_if_true if condicion else condicion_if_false

# Ejemplo:
edad = 18
condicion = "Mayor de edad" if edad >= 18 else "Menor de edad"
#print(condicion) 

# Bucles
# while, for

# Manejo de excepciones
# try ___ except TipoDeExcepcion as nombre_variable ___ finally ____

# Palabras clave para control de flujo
# break: termina el bucle actual y sale de el.
# continue: salta a la siguiente iteracion del bucle, omitiendo el codigo restante en la iteracion actual.
# pass: es una instruccion vacia que se utiliza como marcador de posicion en el codigo.


# ----------------------------------------------------------------------------------------------
# Estructuras de control: Condicionales
# ----------------------------------------------------------------------------------------------

"""
x = 10

if x > 0:
    print("x es un numero positivo")
elif x < 0:
    print("x es un numero negativo")
else:
    print("x es cero")


visa = True
pasaporte = True

if pasaporte and visa:
    print("Puedes viajar")
elif pasaporte and not visa:
    print("Necesitas una visa para viajar")
else:
    print("No puedes viajar")


edad = 67

if edad < 18 or edad > 50:
    if edad < 18:
        print("No tienes edad suficiente para ingresar al boliche")
    else:
        print("Su edad se excede de la permitida por el establecimiento")
elif edad >= 18 and edad <= 50:
    print("Puedes ingresar al boliche")
"""

# ----------------------------------------------------------------------------------------------
# Estructuras de control: Bucles
# ----------------------------------------------------------------------------------------------

contador = 0
limite = 5
sumatoria = 0

while contador <= limite :
    sumatoria += contador
    contador += 1

#print("La sumatoria de los numeros hasta", limite, "es:", sumatoria)

"""
for i in range(0, 9, 2):
    if i == 2:
        print("Pasamos por el 2")
    else:
        print("No es el 2, es el", i)

"""

# ----------------------------------------------------------------------------------------------
# Estructuras de control: Manejo de errores
# ----------------------------------------------------------------------------------------------

# try, except, finally

# Manejo de la division por cero
a = 10
b = 0

"""
try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Error: Division por cero")
finally:
    c = 0

"""

# Este tipo de estructura permite que sigas corriendo los bloques de codigo aunque se tope con un error. 

# ----------------------------------------------------------------------------------------------
# Estructuras de control: Palabras clave de control de flujo
# ----------------------------------------------------------------------------------------------

# break: sale del bucle y no se sigue ejecutando el codigo.
# continue: salta una parte del bucle y sigue con la proxima ejecucion del bloque

contador = 0

"""
while contador < 5:
    print(contador)
    contador += 1
    if contador == 3:
        continue

edad = 18

if edad > 18:
    print("Puede ingresar")
elif edad == 18:
    pass # No hace nada pero nos permite avanzar con el codigo sin que se rompa la estructura.
else:
    print("No puedes ingresar")

"""