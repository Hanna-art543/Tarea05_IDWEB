print("Este es un programa iterativo, para salir coloque 0.")

while True:
    n = int(input("Ingresa un número entero: "))
    if n == 0:
        break

    suma = 0

    if n >= 2:
        for i in range (2, n+ 1, 2):
            suma += i
        
        print(f"La suma total de los pares desde 1 hasta {n} es {suma}")
    else:
        print("El número es inválido.")
    
print("Programa finalizado")

#Otra forma
print("Este es un programa iterativo, para salir coloque 0.")

while True:
    n = int(input("Ingresa un número entero: "))
    if n == 0:
        break

    suma = 0

    if n >= 2:
        for i in range(1, n+1):
            if i % 2 == 0:
                suma += i
        
        print(f"La suma total de los pares desde 1 hasta {n} es {suma}")
    else:
        print("El número es inválido.")
    
print("Programa finalizado")