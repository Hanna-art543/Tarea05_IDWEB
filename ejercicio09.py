def invertir_cadena(texto):
    texto_invertido = ""

    for i in range(len(texto) - 1, -1, -1):
        texto_invertido += texto[i]

    return texto_invertido

cadena = input("Ingrese una frase o texto: ")
invertir = invertir_cadena(cadena)

print("La cadena invertida es:", invertir)


#Otra forma
def invertir_cadena(texto):
    return texto[::-1]

cadena = input("Ingrese una frase o texto: ")
invertida = invertir_cadena(cadena)

print("La cadena invertida es:", invertida)
