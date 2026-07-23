a = "Hola"
b = "Mundo"

c = a + " " + b

#print(c)

# Sólo podemos concatenar variables del mismo tipo.

cadena = "Este curso va a durar {1} horas y tendrá {0} clases"
horas = 10
clases = 5

#print(cadena.format(horas, clases))

texto = 'La mejor serie que vi en mi vida es "Friends"'
#print(texto)

# Usando la barra invertida (\) podemos incluir caracteres especiales en una cadena de texto.

texto = "La mejor serie que vi en mi vida es \"Friends\""
#print(texto)

# Para hacer un salto de linea, usamos \n.
# Para hacer una tabulación, usamos \t.
# Para hacer backspace, usamos \b.

texto = "este texto es minuscula."
#print(texto.capitalize())

# La funcion count se usa para contar cuantas veces aparece un caracter o una secuencia de caracteres en un string.