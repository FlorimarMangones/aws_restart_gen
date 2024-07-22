""" Escribe un programa que pida al usuario su nombre y su edad , y luego imprima un mensaje diciendo cuantos anos tendra el usuario en  anos."""

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
resultado = edad + 5
print(f"Tu edad en 5 años será:{resultado}")

""" Crea una lista con los nombre de 5 frutas y muestra el tercer elemento de la lista"""

miListadeFrutas = ["manzana", "cambur", "patilla", "melon", "durazno"]
print(f"La lista de frutas es {miListadeFrutas}")
print(f"El tercer elemento es {miListadeFrutas[3]}")

"""Escribe un programa que pida al usuario un numero entero y determine si es par o impar"""

numero_entero = int(input("Ingresa un numero entero: "))

if numero_entero % 2 == 0:
    print(f"{numero_entero} es un número par.")
else:
    print(f"{numero_entero} es un número impar.")