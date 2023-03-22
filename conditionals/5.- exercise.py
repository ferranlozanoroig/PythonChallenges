# Para tributar un determinado impuesto se debe ser mayor
# de 16 años y tener unos ingresos iguales o superiores a
# 1000 € mensuales. Escribir un programa que pregunte al
# usuario su edad y sus ingresos mensuales y muestre por
# pantalla si el usuario tiene que tributar o no.

userAge = int(input("¿Cúal es su edad? "))
userRevenue = float(input("¿Cúal es su ingreso mensual? "))

if userAge > 16 and userRevenue >= 1000:
    print("Debes tributar a hacienda")
else:
    print("No debes tributar")