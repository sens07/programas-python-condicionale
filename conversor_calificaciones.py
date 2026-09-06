print("CONVERSOR DE CALIFICACIONES")

calificacion = float(input("Ingresa una calificación de 0 a 100: "))

if calificacion < 0 or calificacion > 100:
    print("La calificación debe estar entre 0 y 100.")
elif calificacion >= 90:
    print("Calificación: A")
elif calificacion >= 80:
    print("Calificación: B")
elif calificacion >= 70:
    print("Calificación: C")
elif calificacion >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")
