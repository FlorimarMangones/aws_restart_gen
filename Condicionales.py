### CONDICIONALES
## if / else
"""

edad = int(input("Ingresa tu edad: "))
if edad >=18:
    print("eres mayor de edad")
elif edad >= 65:
    print("eres una persona de la 3era edad")
else:
    print("no eres mayor de edad")
    
    
  ## ESCRIBE UN PROGRAMA QUE PIDA AL USUARIO SU EDAD Y DETERMINE SI PUEDE VOTAR (MAYOR O IGUAL A 18 ANOS)
    
edad = int(input("Ingresa tu edad: "))
if edad >=18:
    print("puedes votar")
else:
    print("no puedes votar")
    
    ## Crea un programa que pida al usuario una temperatura en grados celsious y determine si esta en estado solido, liquido
    ### o gaseoso (usando los puntos de congelacion y ebullicion del agua)
    
    # Solicita la temperatura 
temp = float(input("Introduce la temperatura en grados Celsius: "))

# Estado del agua
if temp <= 0:
    estado = "sólido"
elif 0 < temp < 100:
    estado = "líquido"
else:
    estado = "gaseoso"
print(f"A {temp} grados Celsius, el agua está en estado {estado}.")

### Pedir un numero entero y determinar si es positivo, negativo o cero

num = int(input("Escribe un numero: "))
if num > 0:
    print(f"El número {num} es positivo.")
elif num <0:
    print(f"El número {num} es negativo.")
else:
    print("El número es cero.")
"""
"""
mascota = "perro"
color = "marron"
if mascota =="perro" or color == "cafe":
    print("tu mascota es perro")
else:
    print("No conozco tu mascota")
    """
    
#ESCRIBE UN PROGRAMA QUE PIDA AL USUARIO DOS NUMEROS Y VERIFIQUE SON POSITIVOS
"""
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
if num1 >0 and num2 >0:
    print(f"Ambos numeros {num1} {num2} son positivos. ")
else:
    print(f"error")
"""
"""
edad = int(input("Ingrese tu edad: "))
Id = input("Indique con una S si tiene identificacion o con un N sino tiene identificacion: ")
if Id.upper() == "S":
    print("Tienes identificación.")
elif Id.upper() == "N":
    print("No tienes identificación.")
else:
    print("Entrada inválida. Por favor, indica con una S o una N.")
"""
#ESCRIBE UN PROGRAMA QUE VERIFIQUE SI UNA PERSONA ES APTA PARA VOTAR. LA PERSONA DEBE SER MAYOR DE 18 A;OS Y DEBE TENER UNA IDENTIFICACION VALIDA

### INVENTAR UN CORTO EJERCICIO DE LOGICA CON LA SENTENCIA CONDICIONAL OR. 

mascota = "perro"
color = "marron"
if mascota =="perro" or color == "cafe":
    print("tu mascota es perro")
else:
    print("No conozco tu mascota")