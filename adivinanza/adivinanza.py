import random

numero_secreto = random.randint(1, 101)
adivinado = False
intentos = 0
intentos_max = 7

print("¡Bienvenido al juego de adivinanza!")

while not adivinado and intentos < intentos_max:
    numero = int(input("Introduzca un número del 1 al 100: "))

    if numero == numero_secreto:
        print("¡Felicidades! Has adivinado el número secreto.")
        adivinado = True
    
    elif numero < numero_secreto:
        print("El número secreto es mayor al ingresado. Intenta de nuevo.")
    
    else:
        print("El número secreto es menor al ingresado. Intenta de nuevo.")

    intentos += 1

    if intentos == intentos_max and not adivinado:
        print(f"Lo siento, has alcanzado el número máximo de intentos. El número secreto era {numero_secreto}.")

    
# Se podría hacer también con un if y un break con al condición de intentos_max.