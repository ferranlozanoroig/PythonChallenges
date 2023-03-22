# Escribir un programa que pida al usuario dos números
# y muestre por pantalla su división. Si el divisor es
# cero el programa debe mostrar un error.
import sys

numUser1 = int(input("Escribe un número:"))
numUser2 = int(input("Escribe otro número:"))

if numUser2 == 0:
    sys.exit("Error. El divisor no puede ser 0")

resultado = numUser1 / numUser2
print("La división entre los dos números es:", resultado)



