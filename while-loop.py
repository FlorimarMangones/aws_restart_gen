import random


print("Tengo el agrado de informarte que has sido seleccionado!🥇")
print("Para continuar debes adivinar 🧙 un numero")

number = random.randint(1,10)

print(number)

Escorrecto = False #Variable booleano

#Hola sino saluda no sigue el juego

while Escorrecto != True:
    guess = int(input("Ingresa un numero"))

if guess == number:
    Escorrecto = True
else:
    print("perdiste tu casa")