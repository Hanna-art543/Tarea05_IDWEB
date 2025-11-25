print("Este programa calculará la suma de todos lo números pares desde 1 hasta n.")
n = int(input("Ingrese n: "))

suma = 0

if n >= 2:
    for i in range (2, n+ 1, 2):
        suma += i
    
    print(f"La suma total de los pares desde 1 hasta {n} es {suma}")
else:
    print("El número es inválido.")

