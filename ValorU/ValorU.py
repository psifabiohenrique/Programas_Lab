import pyperclip
import math


def calcular_valorU(string):
    dados_brutos = string.split()
    dados = []
    for i in dados_brutos:
        dados.append(float(i))
    lista = []
    dividir = math.log2(len(dados)) // math.log2(2)
    acumulador = 0

    for i in dados:
        if i != 0:
            log_item = math.log2(float(i))
            log_2 = math.log2(2)
            lista.append((i * (log_item / log_2)) / dividir)
        else:
            lista.append(0)

    for i in lista:
        acumulador += i
    valor_u = acumulador * -1

    try:
        pyperclip.copy(valor_u)
        return 'Copiado'
    except:
        return 'Falha'

