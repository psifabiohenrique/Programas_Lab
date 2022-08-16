import pyperclip


def calcular_recorrencia(string):
    dados_brutos = string.split()
    universo = ['1111', '1112', '1121', '1122', '1211', '1212', '1221', '1222', '2222', '2221', '2212', '2211', '2122', '2121', '2112', '2111']

    valores = []

    for uni in universo:
        contador = 0
        primeira = True
        for seq in dados_brutos:
            if not primeira:
                if uni == seq:
                    valores.append(contador)
                    contador = 0
                else:
                    contador += 1
            if primeira:
                if uni == seq:
                    primeira = False
                    contador = 0
        primeira = True
    resultado = str(sum(valores) / len(valores))

    try:
        pyperclip.copy(resultado.replace('.', ','))
        return 'Copiado'
    except:
        return 'Falha'