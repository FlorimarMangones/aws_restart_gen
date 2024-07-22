""" Tipo de dato primitivo
Booleanos bools
Valor de True o False
"""

almuerzo = True
descanso = False

print(f"La variable almuerzo tiene el valor {almuerzo} y es de tipo {type(almuerzo)}")

"""
Tipos de datos compuestos

Colecciones

"""


#### LISTA

"""
Es una colección ordenada de valores

* Se define con [] y separa sus elementos con ,
* Los elementos pueden ser de cualquier tipo de dato
print(f"La variable almuerzo tiene el valor {almuerzo} y es de tipo {type(almuerzo)}")

Tipos de datos compuestos
Colecciones
"""

#### LISTA

"""
Es una colección ordenada de valores

* Se define con [] y separa sus elementos con ,
* Los elementos pueden ser de cualquier tipo de dato
personas = ["Anahi", "David", "Ariel", 34, True, False]

* Mantiene un orden (Vale la pena aclarar)
"""

personas = ["Anahi", "David", "Ariel"]
numeros = [100, 95, 82]

myFruitList = ["apple", "banana", "cherry"]


print(f"La lista de frutas es {myFruitList}")
print(f"El tipo de dato es {type(myFruitList)}")


# Si quiero imprimir un elemento (banana) debo hacerlo por su índice
print(f"El segundo elemento es {myFruitList[1]}")

# Un error típico es intentar acceder a un índice que no existe
#print(myFruitList[5])
# IndexError: list index out of range


# Puedo cambiar el valor de los elementos
# Quiero cambiar banana por coco (indice 1)
myFruitList[1] = "coco"