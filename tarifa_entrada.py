print("TARIFA DE ENTRADA AL PARQUE")

edad = int(input("Ingresa la edad de la persona: "))

if edad < 0:
    print("La edad no puede ser negativa.")
elif edad < 12:
    print("Costo de entrada: $50")
elif edad <= 17:
    print("Costo de entrada: $80")
else:
    print("Costo de entrada: $120")
