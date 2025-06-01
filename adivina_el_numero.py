import random 

numero_aleatorio = random.randint(1, 10)

print("Bienvenido al juego de adivinar el numero")

intento = int(input("Adivina el numero entre 1 y 10: "))

while intento != numero_aleatorio:
    print("Demasiado pequeño")
    intento = int(input("Intenta de nuevo: "))

print("¡Correcto! El numero era", numero_aleatorio)
