def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("Cálculo del MCD usando el algoritmo de Euclides.")
print("Ingrese 0 en ambos valores para salir.\n")

while True:
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))

    if a == 0 and b == 0:
        break

    resultado = mcd(a, b)
    print(f"El MCD de {a} y {b} es: {resultado}\n")

print("Programa finalizado.")
