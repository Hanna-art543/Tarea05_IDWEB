def es_primo (num):
    if num <= 1:
        return False
    
    for i in range (2, int(num ** 0.5) + 1):
        if num % i == 0 :
            return False
        
    return True

print("Este programa verificará si es un número primo, para salir ingrese 0.")

while True:
    num = int(input("Ingrese el número:"))

    if num == 0:
        break

    if es_primo(num):
        print(f"El número {num} es primo.")
    else:
        print(f"El número {num} no es primo.")

print("Fin del programa.")