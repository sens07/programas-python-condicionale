print("CLASIFICACIÓN DE TRIÁNGULOS")

lado1 = float(input("Ingresa la longitud del primer lado: "))
lado2 = float(input("Ingresa la longitud del segundo lado: "))
lado3 = float(input("Ingresa la longitud del tercer lado: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Los lados deben ser mayores que cero.")
elif lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print("Las longitudes ingresadas no forman un triángulo.")
elif lado1 == lado2 and lado2 == lado3:
    print("El triángulo es equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")
