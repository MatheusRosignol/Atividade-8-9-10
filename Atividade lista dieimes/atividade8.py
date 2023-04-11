def ler_temperatura():
    temperatura = float(input("Digite a temperatura em graus Celsius: "))
    return temperatura

def calcular_fahrenheit(celsius):
    fahrenheit = (9 * celsius + 160) / 5
    return fahrenheit

def mostrar_resultado(fahrenheit):
    print("A temperatura em graus Fahrenheit é:", fahrenheit)

# programa principal
celsius = ler_temperatura()
fahrenheit = calcular_fahrenheit(celsius)
mostrar_resultado(fahrenheit)