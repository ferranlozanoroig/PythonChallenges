# Escribir un programa que almacene la cadena de caracteres
# contraseña en una variable, pregunte al usuario por la contraseña
# e imprima por pantalla si la contraseña introducida por el usuario
# coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

variablePassword = "contraseña"
datoUsuario = input("¿Cúal es su contraseña?")

if variablePassword == datoUsuario.lower():
    print("La contraseña coinicde")
else:
    print("La contraseña no coincide")