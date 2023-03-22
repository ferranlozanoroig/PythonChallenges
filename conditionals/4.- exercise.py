# Escribir un programa que pida al usuario un número
# entero y muestre por pantalla si es par o impar.

numUsuario = int(input("Escriba un número: "))

if numUsuario % 2 == 0:
    print("El número", numUsuario, "es par")
else:
    print("El número", numUsuario, "es impar")