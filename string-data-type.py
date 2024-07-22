nombre = "Flor la mas bonita"
apellido = "XDXD"

nombre_completo = nombre +" "+ apellido #Es concatenacion

print("El nombre es:", nombre_completo)

### Funcion de entrada por teclado
# input()
#frena el probgrama y espera que el usuario ingrese algo por teclado
#por defecto el valor que se recibe es de tipo string 
#ojo string solo concatena no hace operaciones aritmeticas

nombre = input("ingresa el nombre: ")
aprellido = input("Ingresa tu apellido: ")

nombre_completo = nombre + " " + apellido

print(f"Hola, tu nombre es: {nombre_completo}")

## CONVERSION DE TIPOS DE VARIABLE 
# CASTING O CASTEO

# Puedo covertir un string a int a float por ejemplo

variable = "2"
numero_convertido = int(variable)

print(f"La variable era de tipo {type(variable)} y ahora es {type(numero_convertido)}")

"""
conversiones 
int()
float()
complex()
str()
"""

#Voy a sumar dos numeros
#SI NO CONVIERTO LO QUE RECIBO EN INPUT SERA STRING OJOJJOOOOOOO

""" AL Colocar un input estoy haciendo que el ususrio sea quien le de un valor
ejemplo num = "2"
para el input seria como
num = "(lo que ingresa el usuario)"
"""

num = input("Ingresa un numero: ")
num2 = input("Ingresa otro numero:")

#AL SER STRING SE CONCATENARAN (UNEN)
""" Otra forma de hacerlo es:

num = input("Ingresa un numero: ")
num int(num_entrada)
"""

resultado = num + num2

print(f"La suma de {num} y {num2} es {resultado}")

num = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero:"))

#AL SER STRING SE CONCATENARAN (UNEN)

resultado = num + num2

print(f"La suma de {num} y {num2} es {resultado}")

