def cheese_and_crackers(cheese_count, boxes_of_crackers):
   print(f"Tienes {cheese_count} quesos.")
   print(f"Tienes {boxes_of_crackers} cajas de crackers.")
   print("Es suficiente.\n")

print("Cantidad de números:")
cheese_and_crackers(20, 30)

print("O usar variables para la función.")
amount_cheese = 10
amount_crackers = 50

cheese_and_crackers(amount_cheese, amount_crackers)

print("Realizar aritmética para las variables de función.")
cheese_and_crackers(10 + 20, 5 + 4)

print("Se puede combinar.")
cheese_and_crackers(amount_cheese + 20, amount_crackers + 4)

