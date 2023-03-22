# Los tramos impositivos para la declaración de la renta
# en un determinado país son los siguientes:

gains = float(input("¿Cuál es su renta anual? "))

if gains < 10000:
    tipo = 5
elif gains <= 20000:
    tipo = 15
elif gains <= 35000:
    tipo = 20
elif gains <= 60000:
    tipo = 30
else:
    tipo = 45

print("Debes pagar", gains * tipo / 100, "€")