"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas
a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
y en función de su respuesta le muestre un menú con los ingredientes disponibles
para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el
tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la
pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

print("Bienvenido a la pizzería Bella Napoli, por favor elija la pizza de su preferencia:" "\n"
      "1) Pizza vegetariana" "\n" "2) Pizza no vegetariana")
tipoPizza = int(input("Introduce el número de la pizza que quieras: "))

if tipoPizza == 1:
    print("Sólo puedes elegir un ingrediente de la pizza vegetariana:" "\n"
          "1) Pimiento" "\n" "2) Tofu")
    ingredienteVeg = str(input("Introduce el ingrediente que desees: "))
    print("Su pizza es vegetariana de tomate, mozzarella y ", end="")
    if ingredienteVeg == 1:
        print("pimiento")
    else:
        print("tofu")
else:
    print("Sólo puedes elegir un ingrediente de la pizza no vegetariana:" "\n"
          "1) Peperoni" "\n" "2) Jamón" "\n" "3) Salmón")
    ingredienteNoVeg = str(input("Introduce el ingrediente que desees: "))
    print("Su pizza es no vegetariana de tomate, mozzarella y ", end="")
    if ingredienteNoVeg == 1:
        print("peperoni")
    elif ingredienteNoVeg == 2:
        print("jamón")
    else:
        print("salmón")
