""" 

---CALCULADORA AUTOMATICA DE 2 NUMERO

Vamos a solicitar al usuario 2 numeros
y a realizar todas las operaciones posibles (+,-,*,/,//,%,**) 
mostrando el resultado de una forma clara

"""

num = int(input("Ingresa un numero:"))
num2 = int(input("Ingresa otro numero:"))
resultado1 = num + num2
resultado2 = num - num2
resultado3 = num * num2
resultado4 = num / num2
resultado5 = num // num2
resultado6 = num % num2
resultado7 = num ** num2

print(f"La suma de {num} y {num2} es {resultado1}")
print(f"La resta de {num} y {num2} es {resultado2}")
print(f"La multiplicacion de {num} y {num2} es {resultado3}")
print(f"La division inexacta de {num} y {num2} es {resultado4}")
print(f"La division exacta de {num} y {num2} es {resultado5}")
print(f"Es el % de {num} y {num2} es {resultado6}")
print(f"La potencia de {num} y {num2} es {resultado7}")