def calcular_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return media

numeros = [10, 20, 30, 40, 50]
media_numeros = calcular_media(numeros)
print("A média dos números é:", media_numeros)