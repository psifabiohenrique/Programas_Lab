import pyperclip


def calcular_NSeq(string):
    dados_brutos = string.split()
    conjunto = set(dados_brutos)
    try:
        pyperclip.copy(len(conjunto))
        return 'Copiado'
    except:
        return 'Falha'
