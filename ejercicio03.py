import math

radio = float(input("Ingrese el radio: "))

area = math.pi * (radio ** 2)

perimetro = 2 * math.pi * radio

print("Perímetro del círculo: {:.2f}".format(perimetro))
print("Área del circulo: {:.2f}".format(area))