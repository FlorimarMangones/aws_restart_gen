print("hola mundo flor1")
# Un comentario de una sola linea
# ESTOSE INGNORA ES UN COMENTARIO
"""
UN COMENTARIO MULTILINEA
"""
### Tipos de datos en python

# int enteror integer
## un numero natural que puede estar entre -n a n
## Debemos almacenarlo en una variable
""" La variable es la representacipon de un valor 
el nombre de un identificador
NO puedo llamar a una variable incumpliendo

* NO puede iniciar con un numero
* NO puede tener caracteres especiales
* NO puede contener espacios
* NO puede ser una palabra reservada (for, while, or, try, except...)

SI PUEDO:

* Utilizar numeros en medio o al final: variable2
* Utilizar guion bajo: varible_total
* Solo llamarse guion bajo: _
* Diferenciar entre mayusculas y minusculas: A a B b

"""
# Python intuye el tipo de dato
# Para nombrar una variable debo asignar un valor asi>
# identificador = valor

num = 2
num2 = 10
num_entero = 5
n = 10

# veamos el tipo de dato con type()

print(num)
print(type(num)) # <class 'int'>

resultado = num + num2
print(resultado)

# Forma practica de imprimir con variables
# Uso del f-string
# uico una f antes de las comillas
# dentro puedo imprimir el valor de las variables entre llaves {}

print(f"Hola, sume el valor {num} y el valor {num2} dando {resultado}")

### float : numeros decimales
### se separa el entero del decimal con punto

num = 4.5
num2 = 3.2

resultdo = num *num2

print(f"Hola, sume el valor {num} y el valor {num2} dando {resultado}")
print(f"El tipo de dato de {num} es {type(num)}")

### complex : Complejo o imaginario
### se representa con una j al final del numero
### Vienen del problema de raiz de menos1

num = 4j
num2 = 3j

resultdo = num - num2

print(f"Hola, sume el valor {num} y el valor {num2} dando {resultado}")
print(f"El tipo de dato de {num} es {type(num)}")



### Ejemplos de operaciones

num = 10

num2 = 5

suma = num + num2
resta = num - num2
mult = num * num2
division = num / num2 # Esto resultará en un float

# Hacer una división entera (omitiendo los decimales) con //
# NO aproxima, sólo elimina el decimal
division_entera = num // num2

print(division_entera)
# Residuo
# Se realizara una división, pero el resultado fuera lo que sobró
# de la división entera

modulo = num % 2

print(f"modulo: {num}  % 2 es {modulo}")

##Exponente: elevado **

elevado = 3**2
print(f"3 elevado a la 2 es {elevado}")