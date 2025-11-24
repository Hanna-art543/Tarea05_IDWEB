print("A continuación se verá la clasificación de edades.")
edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Edad inválida, no puede ser menor de 0.")
elif 0 <= edad <= 12:
    print("Es un niño.")
elif 13 <= edad <= 17:
    print("Es un adolescente.")
elif 18 <= edad <= 60:
    print("Es un adulto.")
else:
    print("Es un adulto mayor.")
