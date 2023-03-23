# Escribir un programa que pregunte al usuario su edad y muestre por
# pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("¿Cuál es su edad? "))

for i in range(edad):
    print(str(i+1))