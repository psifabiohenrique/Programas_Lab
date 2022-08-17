import PySimpleGUI as sg
from ValorU import calcular_valorU
from Recorrencia import calcular_recorrencia
from N_Seq import calcular_NSeq


user_data = ''
sg.theme('DarkAmber')

layout = [
    [sg.Push(), sg.Text('Valor U'), sg.Push()],
    [sg.Text('Cole a frequência relativa aqui'), sg.InputText(key='Input_ValorU')],
    [sg.Button('Calcular', key='Calc_valorU'), sg.Checkbox('Virgula?', key='Virgula_valorU')],
    [sg.HorizontalSeparator()],
    [sg.Push(), sg.Text('Tempo de Recorrência'), sg.Push()],
    [sg.Text('Cole todas as sequências aqui'), sg.InputText(key='Input_Recorrencia')],
    [sg.Button('Calcular', key='Calc_recorrencia'), sg.Checkbox('Virgula?', key='Virgula_recorrencia')],
    [sg.HorizontalSeparator()],
    [sg.Push(), sg.Text('Nº Sequências Diferentes'), sg.Push()],
    [sg.Text('Cole todas as sequências aqui'), sg.InputText(key='Input_Nseq')],
    [sg.Button('Calcular', key='Calc_Nseq')]
]

window = sg.Window('Calculos de Variabilidade', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    match event:
        case 'Calc_valorU':
            user_data = values['Input_ValorU']
            sg.popup_ok(calcular_valorU(user_data, values['Virgula_valorU']))
        case 'Calc_recorrencia':
            user_data = values['Input_Recorrencia']
            sg.popup_ok(calcular_recorrencia(user_data, values['Virgula_recorrencia']))
        case 'Calc_Nseq':
            user_data = values['Input_Nseq']
            sg.popup_ok(calcular_NSeq(user_data))

window.close()
