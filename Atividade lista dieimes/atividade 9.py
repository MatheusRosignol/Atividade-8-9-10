def ler_valores():
    tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
    velocidade = float(input("Digite a velocidade média durante a viagem (em km/h): "))
    return tempo, velocidade

def calcular_distancia(tempo, velocidade):
    distancia = tempo * velocidade
    return distancia

def calcular_litros(distancia):
    litros = distancia / 12
    return litros

def apresentar_resultado(tempo, velocidade, distancia, litros):
    print("Velocidade média: {:.2f} km/h".format(velocidade))
    print("Tempo gasto na viagem: {:.2f} horas".format(tempo))
    print("Distância percorrida: {:.2f} km".format(distancia))
    print("Litros de combustível utilizados: {:.2f} litros".format(litros))

# programa principal
tempo, velocidade = ler_valores()
distancia = calcular_distancia(tempo, velocidade)
litros = calcular_litros(distancia)
apresentar_resultado(tempo, velocidade, distancia, litros)