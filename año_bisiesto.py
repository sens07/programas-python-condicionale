print("AÑO BISIESTO")

anio = int(input("Ingresa un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año", anio, "es bisiesto.")
elif anio > 0:
    print("El año", anio, "no es bisiesto.")
else:
    print("Ingresa un año válido.")
