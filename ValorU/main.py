import PySimpleGUI as sg
from ValorU import calcular_valorU


user_data = ''
sg.theme('DarkAmber')

layout = [
    [sg.Text('Cole a frequência relativa'), sg.InputText(key='Input_user')],
    [sg.Button('Calcular', key='Calcular')]
]

window = sg.Window('Valor U', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == 'Calcular':
        user_data = values['Input_user']
        calcular_valorU(user_data)



window.close()
