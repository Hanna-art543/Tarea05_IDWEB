def contar_vocales(texto):
    resultado = {
        "total": 0,
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }

    texto = texto.lower()

    for letra in texto:
        if letra in "aeiou":
            resultado["total"] += 1
            resultado[letra] +=1
    
    return resultado

textoIngresado = input("Ingrese un texto:")
print(contar_vocales(textoIngresado))